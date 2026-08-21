from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import sys


@dataclass(frozen=True)
class FragmentEntry:
    path: Path
    ordinal: int
    heading: str
    release_target: str
    package_impact: str
    legacy: bool
    body: str


REPO_ROOT = Path(__file__).resolve().parents[4]
FRAGMENT_GLOB = "docs/work-items/*/changelog/*.md"
LEGACY_METADATA_PATTERNS = {
    "Release target": re.compile(r"^Release target:\s+`([^`]+)`\s*$", flags=re.MULTILINE),
    "Package impact": re.compile(r"^Package impact:\s+`([^`]+)`\s*$", flags=re.MULTILINE),
    "Release-note": re.compile(r"^Release-note:\s+`([^`]+)`\s*$", flags=re.MULTILINE),
}
COMPACT_METADATA_PATTERN = re.compile(r"^Meta --\s+`([^`]+)`\s*:\s*`([^`]+)`\s*$", flags=re.MULTILINE)
VALID_PACKAGE_IMPACT = {"distributable", "repository-only"}
LEGACY_PACKAGE_IMPACT = VALID_PACKAGE_IMPACT | {"planning-only"}
VALID_RELEASE_NOTE = {"include", "source-only", "omit"}
# Accept a bare heading or the schema's paired Markdown code-span form.
CHANGELOG_HEADING = r"(?:\d{4}-\d{2}-\d{2}[^\n`]+|`\d{4}-\d{2}-\d{2}[^\n`]+`)"


def repo_display_path(path: Path, repo_root: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def parse_fragment(path: Path, repo_root: Path) -> tuple[list[FragmentEntry], list[str]]:
    errors: list[str] = []
    entries: list[FragmentEntry] = []
    display_path = repo_display_path(path, repo_root)
    text = normalize_newlines(path.read_text(encoding="utf-8")).strip()
    headings = list(re.finditer(rf"^(#{{2,3}})\s+({CHANGELOG_HEADING})\s*$", text, flags=re.MULTILINE))
    if not headings:
        errors.append(f"{display_path}: expected at least one changelog entry heading, found 0")
        return entries, errors

    for index, heading_match in enumerate(headings, start=1):
        next_start = headings[index].start() if index < len(headings) else len(text)
        entry_text = text[heading_match.start() : next_start].strip()
        heading = heading_match.group(2).strip()
        context = f"{display_path}: entry {index} `{heading}`"
        entry_errors: list[str] = []
        body_without_heading = entry_text[heading_match.end() - heading_match.start() :].strip()
        compact_matches = list(COMPACT_METADATA_PATTERN.finditer(body_without_heading))
        legacy_matches = {
            field: list(pattern.finditer(body_without_heading)) for field, pattern in LEGACY_METADATA_PATTERNS.items()
        }
        legacy = not compact_matches
        if compact_matches:
            if len(compact_matches) != 1:
                entry_errors.append(f"{context}: expected exactly one Meta field, found {len(compact_matches)}")
            elif any(legacy_matches.values()):
                entry_errors.append(f"{context}: mixed compact and legacy metadata is not allowed")
            else:
                release_target, package_impact = compact_matches[0].groups()
                if not release_target.strip():
                    entry_errors.append(f"{context}: Meta release target must not be blank")
                if package_impact not in VALID_PACKAGE_IMPACT:
                    entry_errors.append(f"{context}: invalid Meta package impact `{package_impact}`")
                body_without_metadata = COMPACT_METADATA_PATTERN.sub("", body_without_heading).strip()
        else:
            values: dict[str, str] = {}
            for field, matches in legacy_matches.items():
                if len(matches) != 1:
                    entry_errors.append(f"{context}: expected exactly one legacy {field} field, found {len(matches)}")
                else:
                    values[field] = matches[0].group(1)
            if not entry_errors:
                release_target = values["Release target"]
                package_impact = values["Package impact"]
                release_note = values["Release-note"]
                if not release_target.strip():
                    entry_errors.append(f"{context}: Release target must not be blank")
                if package_impact not in LEGACY_PACKAGE_IMPACT:
                    entry_errors.append(f"{context}: invalid legacy Package impact value `{package_impact}`")
                if release_note not in VALID_RELEASE_NOTE:
                    entry_errors.append(f"{context}: invalid legacy Release-note value `{release_note}`")
                body_without_metadata = body_without_heading
                for pattern in LEGACY_METADATA_PATTERNS.values():
                    body_without_metadata = pattern.sub("", body_without_metadata)
                body_without_metadata = body_without_metadata.strip()

        if entry_errors:
            errors.extend(entry_errors)
            continue

        entries.append(
            FragmentEntry(
                path=path,
                ordinal=index,
                heading=heading,
                release_target=release_target,
                package_impact=package_impact,
                legacy=legacy,
                body=(
                    f"### {heading}\n\nMeta -- `{release_target}` : `{package_impact}`\n\n"
                    f"{body_without_metadata}\n"
                ),
            )
        )
    return entries, errors


def discover_fragments(repo_root: Path) -> tuple[list[FragmentEntry], list[str]]:
    entries: list[FragmentEntry] = []
    errors: list[str] = []
    for path in sorted(repo_root.glob(FRAGMENT_GLOB)):
        fragment_entries, entry_errors = parse_fragment(path, repo_root)
        errors.extend(entry_errors)
        entries.extend(fragment_entries)
    return entries, errors


def duplicate_heading_errors(entries: list[FragmentEntry], repo_root: Path) -> list[str]:
    by_heading: dict[str, list[FragmentEntry]] = {}
    for entry in entries:
        by_heading.setdefault(entry.heading, []).append(entry)

    errors: list[str] = []
    for heading, duplicates in sorted(by_heading.items()):
        if len(duplicates) <= 1:
            continue
        paths = ", ".join(
            f"{repo_display_path(entry.path, repo_root)} (entry {entry.ordinal}: `{entry.heading}`)"
            for entry in duplicates
        )
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


def migrate_root_changelog(changelog_text: str) -> str:
    entry_pattern = re.compile(
        rf"^(#{{2,3}}\s+{CHANGELOG_HEADING})\s*\n(?P<body>.*?)(?=^##\s+|^###\s+{CHANGELOG_HEADING}\s*$|\Z)",
        flags=re.MULTILINE | re.DOTALL,
    )
    result: list[str] = []
    cursor = 0
    for match in entry_pattern.finditer(changelog_text):
        result.append(changelog_text[cursor : match.start()])
        body = match.group("body").strip()
        compact_matches = list(COMPACT_METADATA_PATTERN.finditer(body))
        legacy_matches = {field: list(pattern.finditer(body)) for field, pattern in LEGACY_METADATA_PATTERNS.items()}
        if compact_matches:
            release_target, package_impact = compact_matches[0].groups()
            body_without_metadata = COMPACT_METADATA_PATTERN.sub("", body).strip()
        elif all(len(matches) == 1 for matches in legacy_matches.values()):
            release_target = legacy_matches["Release target"][0].group(1)
            package_impact = legacy_matches["Package impact"][0].group(1)
            body_without_metadata = body
            for pattern in LEGACY_METADATA_PATTERNS.values():
                body_without_metadata = pattern.sub("", body_without_metadata)
            body_without_metadata = body_without_metadata.strip()
        else:
            result.append(match.group(0))
            cursor = match.end()
            continue
        if package_impact != "planning-only":
            result.append(
                f"{match.group(1)}\n\nMeta -- `{release_target}` : `{package_impact}`\n\n{body_without_metadata}\n"
            )
        cursor = match.end()
    result.append(changelog_text[cursor:])
    migrated = re.sub(r"\n{3,}", "\n\n", "".join(result))
    return re.sub(
        rf"(?<!\n)\n(?=^###\s+{CHANGELOG_HEADING}\s*$)",
        "\n\n",
        migrated,
        flags=re.MULTILINE,
    ).rstrip() + "\n"


def consolidate(repo_root: Path, check: bool, lint: bool, migrate_root: bool) -> int:
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
    if lint:
        return 0

    changelog_path = repo_root / "CHANGELOG.md"
    if not changelog_path.exists():
        print("CHANGELOG.md: missing root changelog", file=sys.stderr)
        return 1

    changelog_text = normalize_newlines(changelog_path.read_text(encoding="utf-8"))
    if migrate_root:
        migrated_text = migrate_root_changelog(changelog_text)
        if migrated_text == changelog_text:
            print("Root changelog is already migrated.")
            return 0
        changelog_path.write_text(migrated_text, encoding="utf-8", newline="\n")
        print("Migrated root CHANGELOG.md to compact metadata.")
        return 0
    existing_headings = get_root_headings(changelog_text)
    missing_entries = [
        entry
        for entry in entries
        if entry.release_target == "unreleased"
        and entry.package_impact in VALID_PACKAGE_IMPACT
        and entry.heading not in existing_headings
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
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Validate root changelog completeness without modifying it.")
    mode.add_argument("--lint", action="store_true", help="Validate fragment grammar and duplicate headings only.")
    mode.add_argument("--migrate-root", action="store_true", help="Remove root planning-only entries and compact root metadata.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=REPO_ROOT,
        help="Repository root to inspect. Defaults to the script's containing repository.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    return consolidate(args.repo_root.resolve(), args.check, args.lint, args.migrate_root)


if __name__ == "__main__":
    sys.exit(main())
