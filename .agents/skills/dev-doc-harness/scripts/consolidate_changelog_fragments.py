from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import sys


@dataclass(frozen=True)
class FragmentEntry:
    path: Path
    heading: str
    release_target: str
    package_impact: str
    release_note: str
    body: str


REPO_ROOT = Path(__file__).resolve().parents[4]
FRAGMENT_GLOB = "docs/work-items/*/changelog/*.md"
METADATA_PATTERNS = {
    "Release target": re.compile(r"^Release target:\s+`([^`]+)`\s*$", flags=re.MULTILINE),
    "Package impact": re.compile(r"^Package impact:\s+`([^`]+)`\s*$", flags=re.MULTILINE),
    "Release-note": re.compile(r"^Release-note:\s+`([^`]+)`\s*$", flags=re.MULTILINE),
}
VALID_PACKAGE_IMPACT = {"distributable", "repository-only", "planning-only"}
VALID_RELEASE_NOTE = {"include", "source-only", "omit"}
CHANGELOG_HEADING = r"\d{4}-\d{2}-\d{2}[^\n]+"


def repo_display_path(path: Path, repo_root: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def parse_fragment(path: Path, repo_root: Path) -> tuple[FragmentEntry | None, list[str]]:
    errors: list[str] = []
    display_path = repo_display_path(path, repo_root)
    text = normalize_newlines(path.read_text(encoding="utf-8")).strip()
    headings = list(re.finditer(rf"^(#{{2,3}})\s+({CHANGELOG_HEADING})\s*$", text, flags=re.MULTILINE))
    if len(headings) != 1:
        errors.append(f"{display_path}: expected exactly one changelog entry heading, found {len(headings)}")
        return None, errors

    values: dict[str, str] = {}
    for field, pattern in METADATA_PATTERNS.items():
        matches = list(pattern.finditer(text))
        if len(matches) != 1:
            errors.append(f"{display_path}: expected exactly one {field} field, found {len(matches)}")
        else:
            values[field] = matches[0].group(1)

    if errors:
        return None, errors

    release_target = values["Release target"]
    package_impact = values["Package impact"]
    release_note = values["Release-note"]

    if not release_target.strip():
        errors.append(f"{display_path}: Release target must not be blank")
    if package_impact not in VALID_PACKAGE_IMPACT:
        errors.append(f"{display_path}: invalid Package impact value `{package_impact}`")
    if release_note not in VALID_RELEASE_NOTE:
        errors.append(f"{display_path}: invalid Release-note value `{release_note}`")
    if errors:
        return None, errors

    heading = headings[0].group(2).strip()
    body_without_heading = text[headings[0].end() :].strip()
    entry_body = f"### {heading}\n\n{body_without_heading}\n"
    return (
        FragmentEntry(
            path=path,
            heading=heading,
            release_target=release_target,
            package_impact=package_impact,
            release_note=release_note,
            body=entry_body,
        ),
        [],
    )


def discover_fragments(repo_root: Path) -> tuple[list[FragmentEntry], list[str]]:
    entries: list[FragmentEntry] = []
    errors: list[str] = []
    for path in sorted(repo_root.glob(FRAGMENT_GLOB)):
        entry, entry_errors = parse_fragment(path, repo_root)
        errors.extend(entry_errors)
        if entry is not None:
            entries.append(entry)
    return entries, errors


def duplicate_heading_errors(entries: list[FragmentEntry], repo_root: Path) -> list[str]:
    by_heading: dict[str, list[FragmentEntry]] = {}
    for entry in entries:
        by_heading.setdefault(entry.heading, []).append(entry)

    errors: list[str] = []
    for heading, duplicates in sorted(by_heading.items()):
        if len(duplicates) <= 1:
            continue
        paths = ", ".join(repo_display_path(entry.path, repo_root) for entry in duplicates)
        errors.append(f"Duplicate changelog fragment heading `{heading}` in: {paths}")
    return errors


def get_root_headings(changelog_text: str) -> set[str]:
    return {
        match.group(1).strip()
        for match in re.finditer(rf"^#{{2,3}}\s+({CHANGELOG_HEADING})\s*$", changelog_text, flags=re.MULTILINE)
    }


def find_unreleased_insertion(changelog_text: str) -> tuple[int | None, list[str]]:
    match = re.search(r"^## Unreleased\s*$", changelog_text, flags=re.MULTILINE)
    if not match:
        return None, ["CHANGELOG.md: missing `## Unreleased` section"]
    return match.end(), []


def build_updated_changelog(changelog_text: str, missing_entries: list[FragmentEntry]) -> tuple[str, list[str]]:
    insertion_index, errors = find_unreleased_insertion(changelog_text)
    if insertion_index is None:
        return changelog_text, errors

    ordered_entries = sorted(missing_entries, key=lambda entry: entry.heading, reverse=True)
    insertion = "\n\n".join(entry.body.strip() for entry in ordered_entries).strip()
    before = changelog_text[:insertion_index].rstrip()
    after = changelog_text[insertion_index:].lstrip()
    if after:
        updated = f"{before}\n\n{insertion}\n\n{after}"
    else:
        updated = f"{before}\n\n{insertion}\n"
    return updated, []


def consolidate(repo_root: Path, check: bool) -> int:
    changelog_path = repo_root / "CHANGELOG.md"
    if not changelog_path.exists():
        print("CHANGELOG.md: missing root changelog", file=sys.stderr)
        return 1

    entries, errors = discover_fragments(repo_root)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    duplicate_errors = duplicate_heading_errors(entries, repo_root)
    if duplicate_errors:
        for error in duplicate_errors:
            print(error, file=sys.stderr)
        return 1

    changelog_text = normalize_newlines(changelog_path.read_text(encoding="utf-8"))
    existing_headings = get_root_headings(changelog_text)
    missing_entries = [
        entry
        for entry in entries
        if entry.release_target == "unreleased" and entry.heading not in existing_headings
    ]

    if check:
        for entry in missing_entries:
            print(
                f"Missing from CHANGELOG.md: {entry.heading} ({repo_display_path(entry.path, repo_root)})",
                file=sys.stderr,
            )
        return 1 if missing_entries else 0

    if not missing_entries:
        print("No missing unreleased changelog fragments.")
        return 0

    updated_text, update_errors = build_updated_changelog(changelog_text, missing_entries)
    if update_errors:
        for error in update_errors:
            print(error, file=sys.stderr)
        return 1

    changelog_path.write_text(updated_text, encoding="utf-8", newline="\n")
    print(f"Inserted {len(missing_entries)} changelog fragment(s) into CHANGELOG.md.")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate and consolidate work-item changelog fragments.")
    parser.add_argument("--check", action="store_true", help="Validate without modifying CHANGELOG.md.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=REPO_ROOT,
        help="Repository root to inspect. Defaults to the script's containing repository.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    return consolidate(args.repo_root.resolve(), args.check)


if __name__ == "__main__":
    sys.exit(main())
