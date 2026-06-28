from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import subprocess
import sys


@dataclass(frozen=True)
class Failure:
    check_id: str
    detail: str


@dataclass(frozen=True)
class Owner:
    path: str
    heading: str = ""


@dataclass(frozen=True)
class OwnerRow:
    path: str
    rule_id: str
    owner_cell: str


@dataclass(frozen=True)
class ReferenceRecord:
    path: str
    identifier: str


@dataclass(frozen=True)
class ChangelogSection:
    heading: str
    body: str


REPO_ROOT = Path(__file__).resolve().parents[4]
FAILURES: list[Failure] = []

CHECK_IDS = [
    "paths.required-files",
    "graph.references",
    "graph.owner-headings",
    "graph.template-routes",
    "router.required-routes",
    "router.route-budget",
    "release.route",
    "discoverability.safety",
    "phrases.duplicated-policy",
    "phrases.duplicate-blocks",
    "placeholders.current-surfaces",
    "tracking.work-items",
    "scenarios.golden-traversal",
    "release.identity",
    "release.notes",
    "release.changelog-schema",
    "release.package-boundary",
    "release.template-context",
]

CANONICAL_REFERENCES = [
    ".agents/skills/dev-doc-harness/references/policy-architecture.md",
    ".agents/skills/dev-doc-harness/references/artifact-contract.md",
    ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md",
    ".agents/skills/dev-doc-harness/references/subagent-model-policy.md",
    ".agents/skills/dev-doc-harness/references/durable-planning-quality.md",
    ".agents/skills/dev-doc-harness/references/release-policy.md",
    ".agents/skills/dev-doc-harness/references/context-and-quality-gates.md",
    ".agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md",
    ".agents/skills/dev-doc-harness/references/subagent-role-examples.md",
]

TEMPLATE_FILES = [
    ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
    ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
    ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
    ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
    ".agents/skills/dev-doc-harness/assets/templates/plan-amendment.md",
    ".agents/skills/dev-doc-harness/assets/templates/variance-log.md",
]

CURRENT_SURFACE_FILES = [
    "AGENTS.md",
    "README.md",
    ".agents/skills/dev-doc-harness/SKILL.md",
    ".agents/skills/dev-doc-harness/scripts/test_harness_policy.py",
    "docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md",
    "docs/work-items/2026-06-05-refactor-as-code/snapshots/test-cases.snapshot.md",
    "docs/work-items/2026-06-05-refactor-as-code/deltas/testing-guide.delta.md",
    "docs/work-items/2026-06-05-refactor-as-code/deltas/operator-manual.delta.md",
    "docs/work-items/2026-06-05-refactor-as-code/deltas/architecture-summary.delta.md",
    "docs/work-items/2026-06-07-followup-hardening/snapshots/architecture.snapshot.md",
    "docs/work-items/2026-06-07-followup-hardening/snapshots/test-cases.snapshot.md",
    "docs/work-items/2026-06-07-followup-hardening/deltas/testing-guide.delta.md",
    "docs/work-items/2026-06-07-followup-hardening/deltas/operator-manual.delta.md",
    "docs/work-items/2026-06-07-followup-hardening/deltas/architecture-summary.delta.md",
] + CANONICAL_REFERENCES + TEMPLATE_FILES

REQUIRED_FILES = [
    "AGENTS.md",
    "README.md",
    "CHANGELOG.md",
    ".agents/skills/dev-doc-harness/SKILL.md",
    ".agents/skills/dev-doc-harness/VERSION",
    ".agents/skills/dev-doc-harness/scripts/test_harness_policy.py",
    ".agents/skills/dev-doc-harness/references/policy-architecture.md",
    ".agents/skills/dev-doc-harness/references/artifact-contract.md",
    ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md",
    ".agents/skills/dev-doc-harness/references/subagent-model-policy.md",
    ".agents/skills/dev-doc-harness/references/durable-planning-quality.md",
    ".agents/skills/dev-doc-harness/references/release-policy.md",
    ".agents/skills/dev-doc-harness/docs/releases/0.3.0.md",
    ".agents/skills/dev-doc-harness/references/context-and-quality-gates.md",
    ".agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md",
    ".agents/skills/dev-doc-harness/references/subagent-role-examples.md",
    ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
    ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
    ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
    ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
    ".agents/skills/dev-doc-harness/assets/templates/plan-amendment.md",
    ".agents/skills/dev-doc-harness/assets/templates/variance-log.md",
    "docs/work-items/2026-06-05-refactor-as-code/snapshots/test-cases.snapshot.md",
    "docs/work-items/2026-06-05-refactor-as-code/deltas/testing-guide.delta.md",
    "docs/work-items/2026-06-05-refactor-as-code/deltas/operator-manual.delta.md",
    "docs/work-items/2026-06-05-refactor-as-code/deltas/architecture-summary.delta.md",
    "docs/work-items/2026-06-07-followup-hardening/snapshots/test-cases.snapshot.md",
    "docs/work-items/2026-06-07-followup-hardening/snapshots/architecture.snapshot.md",
    "docs/work-items/2026-06-07-followup-hardening/deltas/testing-guide.delta.md",
    "docs/work-items/2026-06-07-followup-hardening/deltas/operator-manual.delta.md",
    "docs/work-items/2026-06-07-followup-hardening/deltas/architecture-summary.delta.md",
    "docs/work-items/2026-06-07-release-versioning/snapshots/test-cases.snapshot.md",
]


def join_repo_path(path: str) -> Path:
    return REPO_ROOT / path


def add_failure(check_id: str, detail: str) -> None:
    FAILURES.append(Failure(check_id, detail))


def read_repo_text(path: str) -> str:
    full_path = join_repo_path(path)
    if not full_path.exists():
        add_failure("paths.required-files", f"Missing file before read: {path}")
        return ""
    return full_path.read_text(encoding="utf-8")


def write_check_result(check_id: str) -> None:
    failures = [failure for failure in FAILURES if failure.check_id == check_id]
    if not failures:
        print(f"PASS {check_id}")
        return
    for failure in failures:
        print(f"FAIL {check_id}: {failure.detail}")


def to_repo_relative_path(full_path: Path) -> str:
    try:
        relative = full_path.resolve().relative_to(REPO_ROOT)
    except ValueError:
        relative = full_path
    return relative.as_posix()


def assert_path_exists(check_id: str, path: str) -> None:
    if not join_repo_path(path).exists():
        add_failure(check_id, f"Missing path: {path}")


def assert_path_absent(check_id: str, path: str) -> None:
    if join_repo_path(path).exists():
        add_failure(check_id, f"Unexpected path exists: {path}")


def assert_text_contains(check_id: str, path: str, pattern: str, label: str | None = None) -> None:
    text = read_repo_text(path)
    if not re.search(pattern, text, flags=re.IGNORECASE):
        add_failure(check_id, f"Missing {label or pattern} in {path}")


def assert_text_not_contains(check_id: str, path: str, pattern: str, label: str | None = None) -> None:
    text = read_repo_text(path)
    if re.search(pattern, text):
        add_failure(check_id, f"Unexpected {label or pattern} in {path}")


def get_concrete_ids(text: str) -> list[str]:
    matches = re.findall(r"\b(?:module|rule|schema|scenario|metric):[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?", text)
    return sorted(set(matches))


def add_owner(owners: dict[str, dict[str, list[Owner]]], kind: str, identifier: str, path: str, heading: str = "") -> None:
    owners[kind].setdefault(identifier, []).append(Owner(path, heading))


def get_owner_graph() -> tuple[dict[str, dict[str, list[Owner]]], list[OwnerRow]]:
    owners: dict[str, dict[str, list[Owner]]] = {
        "module": {},
        "rule": {},
        "schema": {},
        "scenario": {},
        "metric": {},
    }
    owner_rows: list[OwnerRow] = []

    for path in CANONICAL_REFERENCES:
        text = read_repo_text(path)
        for match in re.finditer(r"(?:Module:|owns)\s+`(module:[a-z0-9][a-z0-9.-]*)`", text):
            add_owner(owners, "module", match.group(1), path)

        for line in re.split(r"\r?\n", text):
            row_match = re.match(r"^\|\s*`(rule:[a-z0-9][a-z0-9.-]*)`\s*\|\s*(.+?)\s*\|", line)
            if row_match:
                rule_id = row_match.group(1)
                owner_cell = row_match.group(2)
                add_owner(owners, "rule", rule_id, path, owner_cell)
                owner_rows.append(OwnerRow(path, rule_id, owner_cell))

    for path in TEMPLATE_FILES:
        text = read_repo_text(path)
        for match in re.finditer(r"Schema:\s+`(schema:[a-z0-9][a-z0-9.-]*)`", text):
            add_owner(owners, "schema", match.group(1), path)

    scenario_metric_owner_files = [
        "docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md",
        "docs/work-items/2026-06-05-refactor-as-code/snapshots/test-cases.snapshot.md",
        "docs/work-items/2026-06-07-followup-hardening/snapshots/architecture.snapshot.md",
        "docs/work-items/2026-06-07-followup-hardening/snapshots/test-cases.snapshot.md",
        "docs/work-items/2026-06-07-release-versioning/snapshots/test-cases.snapshot.md",
    ]
    for path in scenario_metric_owner_files:
        text = read_repo_text(path)
        for identifier in get_concrete_ids(text):
            if identifier.startswith("scenario:"):
                add_owner(owners, "scenario", identifier, path)
            elif identifier.startswith("metric:"):
                add_owner(owners, "metric", identifier, path)

    return owners, owner_rows


def get_reference_records() -> list[ReferenceRecord]:
    records: list[ReferenceRecord] = []
    for path in CURRENT_SURFACE_FILES:
        text = read_repo_text(path)
        for identifier in get_concrete_ids(text):
            records.append(ReferenceRecord(path, identifier))
    return records


def get_owner_table_heading_names(owner_cell: str) -> list[str]:
    return [f"## {match.group(1).strip()}" for match in re.finditer(r"##\s*([^`|]+?)(?:\s+and\s+|$)", owner_cell)]


def assert_graph_references(owners: dict[str, dict[str, list[Owner]]], references: list[ReferenceRecord]) -> None:
    for record in references:
        if re.search(r"/snapshots/test-cases\.snapshot\.md$", record.path) and re.search("^rule" + r":test\.", record.identifier):
            continue
        kind = record.identifier.split(":", 1)[0]
        if kind in owners and record.identifier not in owners[kind]:
            add_failure("graph.references", f"Dangling {kind} reference '{record.identifier}' in {record.path}")

    for kind in ("module", "rule", "schema"):
        for identifier, owner_entries in owners[kind].items():
            paths = sorted({entry.path for entry in owner_entries})
            if len(paths) > 1:
                add_failure("graph.references", f"Duplicate {kind} owner for '{identifier}': {', '.join(paths)}")


def assert_owner_headings(owner_rows: list[OwnerRow]) -> None:
    for row in owner_rows:
        text = read_repo_text(row.path)
        for heading in get_owner_table_heading_names(row.owner_cell):
            if not re.search(rf"^{re.escape(heading)}\s*$", text, flags=re.MULTILINE):
                add_failure("graph.owner-headings", f"Owner heading '{heading}' for {row.rule_id} is missing in {row.path}")


def get_policy_references(path: str) -> list[str]:
    text = read_repo_text(path)
    line = next((line for line in re.split(r"\r?\n", text) if re.search(r"^Policy references:", line)), "")
    return get_concrete_ids(line) if line else []


def assert_template_routes() -> None:
    operation_requirements = {
        "small-medium": ["module:lifecycle", "module:quality", "module:models"],
        "large-anchor": ["module:lifecycle", "module:quality", "module:models"],
        "phase-plan": ["module:lifecycle", "module:quality", "module:models"],
        "amendment": ["module:lifecycle", "module:freeze-gate"],
    }
    operation_templates = {
        "small-medium": [
            ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
            ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
        ],
        "large-anchor": [".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md"],
        "phase-plan": [".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md"],
        "amendment": [".agents/skills/dev-doc-harness/assets/templates/plan-amendment.md"],
    }

    for operation, requirements in operation_requirements.items():
        combined: set[str] = set()
        for template in operation_templates[operation]:
            combined.update(get_policy_references(template))
        for required in requirements:
            if required not in combined:
                add_failure("graph.template-routes", f"Template set for '{operation}' is missing policy reference '{required}'")


def assert_route_contains(operation: str, required_patterns: list[str], check_id: str = "router.required-routes") -> None:
    path = ".agents/skills/dev-doc-harness/SKILL.md"
    text = read_repo_text(path)
    route_line = next((line for line in re.split(r"\r?\n", text) if re.search(re.escape(operation), line)), "")
    if not route_line:
        add_failure(check_id, f"Missing operation route: {operation}")
        return
    for pattern in required_patterns:
        if not re.search(pattern, route_line):
            add_failure(check_id, f"Route '{operation}' is missing target pattern: {pattern}")


def assert_route_budgets() -> None:
    text = read_repo_text(".agents/skills/dev-doc-harness/SKILL.md")
    budgets = {
        "Classify work size": 1,
        "Draft or review small/medium specs and plans": 3,
        "Draft or review large anchor specs": 3,
        "Draft or review phase plans": 3,
        "Freeze planning packages": 4,
        "Execute approved work and record variance": 4,
        "Use or review sub-agent strategy": 2,
        "Evidence-heavy review or reports": 1,
        "Release, package, or team adoption work": 1,
        "Validate current harness surfaces": 2,
        "Update templates or router guidance": 3,
        "Superpowers or spec-kit compatibility": 3,
    }

    lines = re.split(r"\r?\n", text)
    for operation, budget in budgets.items():
        route_line = next((line for line in lines if re.search(rf"^\|\s*{re.escape(operation)}\s*\|", line)), "")
        if not route_line:
            add_failure("router.route-budget", f"Missing route for budget check: {operation}")
            continue
        raw_cells = route_line.split("|")
        if len(raw_cells) < 5:
            add_failure("router.route-budget", f"Malformed route row for budget check: {operation}")
            continue
        cells = [cell.strip() for cell in raw_cells[1:-1]]
        if len(cells) < 2:
            add_failure("router.route-budget", f"Malformed route row for budget check: {operation}")
            continue
        required_cell = cells[1]
        module_count = len(set(re.findall(r"module:[a-z0-9][a-z0-9.-]*", required_cell)))
        if module_count > budget:
            add_failure("router.route-budget", f"Route '{operation}' requires {module_count} modules, budget is {budget}")


def assert_scenario_evidence(scenario_id: str, evidence: list[dict[str, str]]) -> None:
    for item in evidence:
        assert_text_contains(
            "scenarios.golden-traversal",
            item["path"],
            item["pattern"],
            f"{scenario_id} evidence '{item['label']}'",
        )


def get_normalized_paragraphs(path: str) -> list[tuple[str, str]]:
    text = read_repo_text(path)
    paragraphs: list[str] = []
    current: list[str] = []
    in_fence = False
    for line in re.split(r"\r?\n", text):
        if re.search(r"^\s*```", line):
            in_fence = not in_fence
            continue
        if (
            in_fence
            or re.search(r"^\s*\|", line)
            or re.search(r"^\s*#", line)
            or re.search(r"^\s*[-*]\s", line)
            or re.search(r"^\s*\d+\.", line)
        ):
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        if not line.strip():
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        current.append(line.strip())
    if current:
        paragraphs.append(" ".join(current))

    normalized: list[tuple[str, str]] = []
    for paragraph in paragraphs:
        words = re.findall(r"[a-z0-9]+", paragraph.lower())
        if len(words) >= 55:
            normalized.append((path, " ".join(words)))
    return normalized


def assert_duplicate_blocks() -> None:
    targets = [
        "AGENTS.md",
        "README.md",
        ".agents/skills/dev-doc-harness/SKILL.md",
    ] + CANONICAL_REFERENCES + TEMPLATE_FILES

    seen: dict[str, str] = {}
    for target in targets:
        for _, paragraph_text in get_normalized_paragraphs(target):
            if paragraph_text in seen and seen[paragraph_text] != target:
                add_failure("phrases.duplicate-blocks", f"Duplicate broad policy block in {seen[paragraph_text]} and {target}")
            else:
                seen.setdefault(paragraph_text, target)


def run_git(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", "-C", str(REPO_ROOT), *args], capture_output=True, text=True, check=False)


def assert_work_item_tracking() -> None:
    assert_path_absent("tracking.work-items", "docs/work-items/AGENTS.md")

    ignored = run_git(["check-ignore", "-v", "docs/work-items/2026-06-07-followup-hardening/spec-followup-hardening.md"])
    if ignored.returncode == 0 and ignored.stdout.strip():
        add_failure("tracking.work-items", f"Work-item docs are still ignored: {ignored.stdout.strip()}")

    work_items_root = join_repo_path("docs/work-items")
    markdown_files = sorted(to_repo_relative_path(path) for path in work_items_root.rglob("*.md"))
    tracked_result = run_git(["ls-files", "docs/work-items"])
    tracked = set(tracked_result.stdout.splitlines())
    for path in markdown_files:
        if path not in tracked:
            add_failure("tracking.work-items", f"Untracked work-item Markdown artifact: {path}")


def assert_release_identity() -> None:
    check_id = "release.identity"
    version_path = ".agents/skills/dev-doc-harness/VERSION"
    version_text = read_repo_text(version_path)
    if not re.search(r"\A0\.3\.0\r?\n?\Z", version_text):
        add_failure(check_id, f"{version_path} must contain exactly 0.3.0 plus an optional trailing newline")
        return
    version = version_text.rstrip("\r\n")
    assert_path_exists(check_id, f".agents/skills/dev-doc-harness/docs/releases/{version}.md")


def assert_release_notes() -> None:
    check_id = "release.notes"
    release_notes_path = ".agents/skills/dev-doc-harness/docs/releases/0.3.0.md"
    release_notes = read_repo_text(release_notes_path)
    changelog = read_repo_text("CHANGELOG.md")
    required_headings = [
        "# Dev Doc Harness 0.3.0",
        "## Release",
        "## Package Contents",
        "## Added",
        "## Changed",
        "## Compatibility",
        "## Team Adoption",
        "## Rollback",
        "## Source Changelog Entries",
    ]

    for heading in required_headings:
        if not re.search(rf"^{re.escape(heading)}\s*$", release_notes, flags=re.MULTILINE):
            add_failure(check_id, f"Missing release-note heading '{heading}'")

    source_match = re.search(r"^## Source Changelog Entries\s*(?P<body>.*?)(?=^##\s+|\Z)", release_notes, flags=re.MULTILINE | re.DOTALL)
    if not source_match:
        add_failure(check_id, "Missing Source Changelog Entries section body")
        return

    source_entries = re.findall(r"`(2026-06-07-release-versioning: [^`]+)`", source_match.group("body"))
    if not source_entries:
        add_failure(check_id, "No source changelog entries listed in release notes")

    for entry in source_entries:
        if not re.search(rf"^###?\s+{re.escape(entry)}\s*$", changelog, flags=re.MULTILINE):
            add_failure(check_id, f"Release-note source entry is missing from CHANGELOG.md: {entry}")


def get_changelog_sections() -> list[ChangelogSection]:
    text = read_repo_text("CHANGELOG.md")
    return [
        ChangelogSection(match.group("heading").strip(), match.group("body"))
        for match in re.finditer(
            r"^###?\s+(?P<heading>2026-06-07-release-versioning:[^\r\n]+)\r?\n(?P<body>.*?)(?=^###?\s+|\Z)",
            text,
            flags=re.MULTILINE | re.DOTALL,
        )
    ]


def assert_release_changelog_schema() -> None:
    check_id = "release.changelog-schema"
    sections = get_changelog_sections()
    if not sections:
        add_failure(check_id, "No current release-versioning changelog entries found")
        return

    for section in sections:
        release_target_lines = list(re.finditer(r"^Release target:\s+`([^`]+)`\s*$", section.body, flags=re.MULTILINE))
        package_impact_lines = list(re.finditer(r"^Package impact:\s+`([^`]+)`\s*$", section.body, flags=re.MULTILINE))
        release_note_lines = list(re.finditer(r"^Release-note:\s+`([^`]+)`\s*$", section.body, flags=re.MULTILINE))

        if len(release_target_lines) != 1:
            add_failure(check_id, f"{section.heading} must contain exactly one Release target field")
        elif release_target_lines[0].group(1) != "0.3.0":
            add_failure(check_id, f"{section.heading} has invalid Release target '{release_target_lines[0].group(1)}'")

        if len(package_impact_lines) != 1:
            add_failure(check_id, f"{section.heading} must contain exactly one Package impact field")
        elif package_impact_lines[0].group(1) not in ("distributable", "repository-only", "planning-only"):
            add_failure(check_id, f"{section.heading} has invalid Package impact '{package_impact_lines[0].group(1)}'")

        if len(release_note_lines) != 1:
            add_failure(check_id, f"{section.heading} must contain exactly one Release-note field")
        elif release_note_lines[0].group(1) not in ("include", "source-only", "omit"):
            add_failure(check_id, f"{section.heading} has invalid Release-note '{release_note_lines[0].group(1)}'")


def assert_release_package_boundary() -> None:
    check_id = "release.package-boundary"
    release_policy = ".agents/skills/dev-doc-harness/references/release-policy.md"
    release_notes = ".agents/skills/dev-doc-harness/docs/releases/0.3.0.md"

    assert_text_contains(check_id, release_policy, r"distributable harness package is root `AGENTS\.md` plus `\.agents/`", "release policy package boundary")
    assert_text_contains(check_id, release_notes, r"distributable package is root `AGENTS\.md` plus `\.agents/`", "release notes package boundary")
    assert_text_contains(check_id, "README.md", r"copyable distributable package is\s+the root `AGENTS\.md` file plus the `\.agents/` folder", "README package boundary")
    assert_text_contains(check_id, release_policy, r"Do not copy this repository's `docs/work-items/`", "release policy work-item exclusion")
    assert_text_contains(check_id, "README.md", r"Do not copy this repository's `docs/work-items/` folder", "README work-item exclusion")
    assert_text_contains(check_id, release_policy, r"(?i)rollback.+revert", "release policy rollback")
    assert_text_contains(check_id, release_notes, r"(?i)revert.+dedicated harness update", "release notes rollback")
    assert_text_contains(check_id, "README.md", r"(?i)roll back by reverting", "README rollback")


def assert_release_template_context() -> None:
    check_id = "release.template-context"
    field_literal = "Harness release: `<version or unknown>`"
    field_pattern = rf"^{re.escape(field_literal)}\s*$"
    for template in TEMPLATE_FILES:
        text = read_repo_text(template)
        count = len(re.findall(field_pattern, text, flags=re.MULTILINE))
        if count != 1:
            add_failure(check_id, f"{template} must contain exactly one Harness release field; found {count}")


def assert_release_scenarios() -> None:
    check_id = "release.notes"
    snapshot_path = "docs/work-items/2026-06-07-release-versioning/snapshots/test-cases.snapshot.md"
    scenario_ids = [
        "scenario:release.package-identity",
        "scenario:release.release-notes-source",
        "scenario:release.changelog-schema",
        "scenario:release.package-boundary",
        "scenario:release.template-context",
        "scenario:release.team-adoption-rollback",
    ]
    for scenario_id in scenario_ids:
        assert_text_contains(check_id, snapshot_path, re.escape(scenario_id), f"{scenario_id} snapshot row")


def run_checks() -> None:
    for path in REQUIRED_FILES:
        assert_path_exists("paths.required-files", path)
    write_check_result("paths.required-files")

    owners, owner_rows = get_owner_graph()
    references = get_reference_records()
    assert_graph_references(owners, references)
    write_check_result("graph.references")

    assert_owner_headings(owner_rows)
    write_check_result("graph.owner-headings")

    assert_template_routes()
    write_check_result("graph.template-routes")

    assert_route_contains("Classify work size", ["module:lifecycle", "rule:lifecycle.work-sizing"])
    assert_route_contains("Draft or review small/medium specs and plans", ["module:lifecycle", "module:quality", "module:models"])
    assert_route_contains("Draft or review large anchor specs", ["module:lifecycle", "module:quality", "module:models"])
    assert_route_contains("Draft or review phase plans", ["module:quality", "module:lifecycle", "module:models"])
    assert_route_contains("Freeze planning packages", ["module:freeze-gate", "module:lifecycle"])
    assert_route_contains("Execute approved work and record variance", ["module:lifecycle", "module:execution-quality"])
    assert_route_contains("Use or review sub-agent strategy", ["module:models", "rule:models.strategy-required"])
    assert_route_contains("Evidence-heavy review or reports", ["module:evidence"])
    assert_route_contains("Release, package, or team adoption work", ["module:release"])
    assert_route_contains("Update templates or router guidance", ["module:architecture"])
    assert_route_contains("Superpowers or spec-kit compatibility", ["module:lifecycle"])
    write_check_result("router.required-routes")

    assert_route_budgets()
    write_check_result("router.route-budget")

    assert_route_contains("Release, package, or team adoption work", ["module:release"], "release.route")
    write_check_result("release.route")

    discoverability = [
        {"path": ".agents/skills/dev-doc-harness/SKILL.md", "pattern": "Classify work size", "label": "work sizing"},
        {"path": ".agents/skills/dev-doc-harness/SKILL.md", "pattern": "Planning Artifact Freeze Gate", "label": "planning freeze gates"},
        {"path": ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md", "pattern": "stop before implementation", "label": "stop before implementation"},
        {"path": ".agents/skills/dev-doc-harness/references/artifact-contract.md", "pattern": "Immutable snapshots", "label": "immutable snapshots"},
        {"path": ".agents/skills/dev-doc-harness/references/artifact-contract.md", "pattern": "Variance policy", "label": "variance and amendments"},
        {"path": ".agents/skills/dev-doc-harness/references/artifact-contract.md", "pattern": r"CHANGELOG.md.+before commits", "label": "changelog before commit"},
        {"path": ".agents/skills/dev-doc-harness/references/artifact-contract.md", "pattern": "Documentation artifact matrix", "label": "documentation matrix"},
        {"path": "AGENTS.md", "pattern": "single repository-local selection point", "label": "active repository model policy"},
        {"path": ".agents/skills/dev-doc-harness/SKILL.md", "pattern": "Superpowers compatibility", "label": "Superpowers compatibility"},
        {"path": ".agents/skills/dev-doc-harness/references/policy-architecture.md", "pattern": "Historical artifacts are tracked documentation", "label": "historical artifact handling"},
    ]
    for topic in discoverability:
        assert_text_contains("discoverability.safety", topic["path"], topic["pattern"], topic["label"])
    write_check_result("discoverability.safety")

    duplicate_phrase_targets = [
        "AGENTS.md",
        "README.md",
        ".agents/skills/dev-doc-harness/SKILL.md",
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
        ".agents/skills/dev-doc-harness/assets/templates/plan-amendment.md",
        ".agents/skills/dev-doc-harness/assets/templates/variance-log.md",
    ]
    disallowed_phrases = [
        "Fresh confirmation is still required",
        r"Long-running .*more than 3 total sub-agents",
        "Context strategy must say how",
        "Before approval, operator feedback edits this draft directly",
        r"When this .*ready for operator review, follow",
        r"After this .*approved, frozen, and followed",
        r"module:models.*when model or sub-agent strategy is assessed",
    ]
    for target in duplicate_phrase_targets:
        for phrase in disallowed_phrases:
            assert_text_not_contains("phrases.duplicated-policy", target, phrase, phrase)
    write_check_result("phrases.duplicated-policy")

    assert_duplicate_blocks()
    write_check_result("phrases.duplicate-blocks")

    placeholder_targets = [
        "AGENTS.md",
        "README.md",
        ".agents/skills/dev-doc-harness/SKILL.md",
        ".agents/skills/dev-doc-harness/references/policy-architecture.md",
        ".agents/skills/dev-doc-harness/references/artifact-contract.md",
        ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md",
        ".agents/skills/dev-doc-harness/references/subagent-model-policy.md",
        ".agents/skills/dev-doc-harness/references/durable-planning-quality.md",
        ".agents/skills/dev-doc-harness/references/context-and-quality-gates.md",
        ".agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md",
        ".agents/skills/dev-doc-harness/scripts/test_harness_policy.py",
        "docs/work-items/2026-06-05-refactor-as-code/snapshots/test-cases.snapshot.md",
        "docs/work-items/2026-06-05-refactor-as-code/deltas/testing-guide.delta.md",
        "docs/work-items/2026-06-05-refactor-as-code/deltas/operator-manual.delta.md",
        "docs/work-items/2026-06-05-refactor-as-code/deltas/architecture-summary.delta.md",
        "docs/work-items/2026-06-07-followup-hardening/snapshots/test-cases.snapshot.md",
        "docs/work-items/2026-06-07-followup-hardening/snapshots/architecture.snapshot.md",
        "docs/work-items/2026-06-07-followup-hardening/deltas/testing-guide.delta.md",
        "docs/work-items/2026-06-07-followup-hardening/deltas/operator-manual.delta.md",
        "docs/work-items/2026-06-07-followup-hardening/deltas/architecture-summary.delta.md",
    ]
    placeholder_patterns = ["Status:[ ]Draft", "T[D]B", "T[O]DO", "R[e]place", "blank u[n]less", "unresolved d[e]cision"]
    for target in placeholder_targets:
        for pattern in placeholder_patterns:
            assert_text_not_contains("placeholders.current-surfaces", target, pattern, pattern)
    write_check_result("placeholders.current-surfaces")

    assert_work_item_tracking()
    write_check_result("tracking.work-items")

    scenario_snapshot = "docs/work-items/2026-06-05-refactor-as-code/snapshots/test-cases.snapshot.md"
    scenario_ids = [
        "scenario:work-size.very-small-skip",
        "scenario:planning.small-medium",
        "scenario:planning.large-anchor-freeze",
        "scenario:planning.phase-plan-freeze",
        "scenario:execution.post-freeze-authorization",
        "scenario:variance.high-impact-amendment",
        "scenario:models.sub-agent-authorization",
        "scenario:compat.superpowers",
        "scenario:history.historical-artifact-handling",
    ]
    for scenario_id in scenario_ids:
        assert_text_contains("scenarios.golden-traversal", scenario_snapshot, re.escape(scenario_id), f"{scenario_id} snapshot row")

    assert_scenario_evidence(
        "scenario:work-size.very-small-skip",
        [
            {"path": "AGENTS.md", "pattern": "Very small mechanical edits", "label": "root sizing summary"},
            {"path": ".agents/skills/dev-doc-harness/SKILL.md", "pattern": "Classify work size", "label": "router sizing route"},
            {"path": ".agents/skills/dev-doc-harness/references/artifact-contract.md", "pattern": "Small mechanical work may skip", "label": "lifecycle sizing rule"},
        ],
    )
    assert_scenario_evidence(
        "scenario:planning.small-medium",
        [
            {"path": ".agents/skills/dev-doc-harness/SKILL.md", "pattern": "Draft or review small/medium specs and plans", "label": "small medium route"},
            {"path": ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md", "pattern": "schema:spec.small-medium", "label": "small spec schema"},
            {"path": ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md", "pattern": "schema:plan.small-medium", "label": "small plan schema"},
        ],
    )
    assert_scenario_evidence(
        "scenario:planning.large-anchor-freeze",
        [
            {"path": ".agents/skills/dev-doc-harness/SKILL.md", "pattern": "Draft or review large anchor specs", "label": "large route"},
            {"path": ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md", "pattern": "schema:spec.large-phased", "label": "large spec schema"},
            {"path": ".agents/skills/dev-doc-harness/references/artifact-contract.md", "pattern": "rule:lifecycle.large-phase-orchestration", "label": "large phase orchestration rule owner"},
            {"path": ".agents/skills/dev-doc-harness/references/artifact-contract.md", "pattern": "Large or phased planning orchestration", "label": "large phase orchestration heading"},
            {"path": ".agents/skills/dev-doc-harness/SKILL.md", "pattern": "rule:lifecycle.large-phase-orchestration", "label": "large route orchestration rule"},
            {"path": ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md", "pattern": "rule:lifecycle.large-phase-orchestration", "label": "large spec orchestration rule"},
            {"path": ".agents/skills/dev-doc-harness/references/artifact-contract.md", "pattern": "anchor-spec-only", "label": "anchor spec only package"},
            {"path": ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md", "pattern": "combined planning", "label": "combined planning exception"},
            {"path": ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md", "pattern": "Approval freeze checkpoint", "label": "freeze owner"},
        ],
    )
    assert_scenario_evidence(
        "scenario:planning.phase-plan-freeze",
        [
            {"path": ".agents/skills/dev-doc-harness/SKILL.md", "pattern": "Draft or review phase plans", "label": "phase plan route"},
            {"path": ".agents/skills/dev-doc-harness/references/durable-planning-quality.md", "pattern": "rule:quality.phase-plan-fresh-thread", "label": "fresh thread rule"},
            {"path": ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md", "pattern": "schema:plan.phase", "label": "phase schema"},
            {"path": ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md", "pattern": "rule:lifecycle.large-phase-orchestration", "label": "phase plan orchestration rule"},
            {"path": ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md", "pattern": "phase-plan drafting resumes only after fresh operator instruction", "label": "post anchor phase planning authorization"},
            {"path": ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md", "pattern": "approved anchor spec", "label": "approved anchor input"},
            {"path": ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md", "pattern": "rule:freeze.approval-freeze", "label": "phase freeze owner"},
        ],
    )
    assert_scenario_evidence(
        "scenario:execution.post-freeze-authorization",
        [
            {"path": ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md", "pattern": "fresh operator response", "label": "fresh authorization"},
            {"path": ".agents/skills/dev-doc-harness/references/artifact-contract.md", "pattern": "rule:lifecycle.variance-policy", "label": "variance rule"},
            {"path": ".agents/skills/dev-doc-harness/references/context-and-quality-gates.md", "pattern": "Implementation stayed within scope", "label": "scope quality gate"},
            {"path": ".agents/skills/dev-doc-harness/references/artifact-contract.md", "pattern": r"CHANGELOG.md.+before commits", "label": "changelog expectation"},
        ],
    )
    assert_scenario_evidence(
        "scenario:variance.high-impact-amendment",
        [
            {"path": ".agents/skills/dev-doc-harness/references/artifact-contract.md", "pattern": "plan-amendment-NNN-short-title", "label": "amendment path"},
            {"path": ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md", "pattern": "Amendment freeze", "label": "amendment freeze"},
            {"path": ".agents/skills/dev-doc-harness/assets/templates/plan-amendment.md", "pattern": "schema:plan.amendment", "label": "amendment schema"},
        ],
    )
    assert_scenario_evidence(
        "scenario:models.sub-agent-authorization",
        [
            {"path": ".agents/skills/dev-doc-harness/references/subagent-model-policy.md", "pattern": "rule:models.approved-strategy-authorized", "label": "approved strategy rule"},
            {"path": ".agents/skills/dev-doc-harness/references/subagent-model-policy.md", "pattern": "rule:models.fresh-confirmation", "label": "fresh confirmation rule"},
            {"path": ".agents/skills/dev-doc-harness/references/subagent-model-policy.md", "pattern": "curated-artifact sub-agent", "label": "curated artifact phase planning"},
            {"path": ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md", "pattern": "Context strategy", "label": "small plan strategy table"},
            {"path": ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md", "pattern": "Context strategy", "label": "large spec strategy table"},
            {"path": ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md", "pattern": "Context strategy", "label": "phase plan strategy table"},
        ],
    )
    assert_scenario_evidence(
        "scenario:compat.superpowers",
        [
            {"path": "AGENTS.md", "pattern": "Superpowers", "label": "root compatibility"},
            {"path": ".agents/skills/dev-doc-harness/SKILL.md", "pattern": "Superpowers compatibility", "label": "router compatibility"},
            {"path": ".agents/skills/dev-doc-harness/references/artifact-contract.md", "pattern": "rule:lifecycle.superpowers-compatibility", "label": "lifecycle compatibility"},
        ],
    )
    assert_scenario_evidence(
        "scenario:history.historical-artifact-handling",
        [
            {"path": ".agents/skills/dev-doc-harness/references/artifact-contract.md", "pattern": "rule:lifecycle.immutable-snapshots", "label": "immutable rule"},
            {"path": ".agents/skills/dev-doc-harness/references/policy-architecture.md", "pattern": "Historical artifacts are tracked documentation", "label": "historical handling"},
            {"path": "docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md", "pattern": "scenario:history.historical-artifact-handling", "label": "source scenario"},
        ],
    )
    write_check_result("scenarios.golden-traversal")

    assert_release_identity()
    write_check_result("release.identity")

    assert_release_notes()
    assert_release_scenarios()
    write_check_result("release.notes")

    assert_release_changelog_schema()
    write_check_result("release.changelog-schema")

    assert_release_package_boundary()
    write_check_result("release.package-boundary")

    assert_release_template_context()
    write_check_result("release.template-context")


def main() -> int:
    run_checks()
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
