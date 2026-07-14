from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile


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
CURRENT_DEVELOPMENT_MARKER = "0.6+"
RELEASE_NOTE_VERSIONS = ["0.4.0", "0.5.0", "0.6.0"]
LATEST_RELEASE_NOTE_VERSION = RELEASE_NOTE_VERSIONS[-1]

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
    "templates.assembly",
    "placeholders.current-surfaces",
    "tracking.work-items",
    "scenarios.golden-traversal",
    "release.identity",
    "release.notes",
    "release.changelog-schema",
    "release.package-boundary",
    "release.template-context",
    "changelog.fragments",
    "architecture.decisions",
    "artifact-style.guidance",
    "plain-language.policy",
    "models.selection-dimensions",
    "execution.thread-start",
    "lifecycle.transition-targets",
    "quality.commitment-verification",
    "templates.commitment-verification",
    "compat.current-historical",
]

CANONICAL_REFERENCES = [
    ".agents/skills/dev-doc-harness/references/policy-architecture.md",
    ".agents/skills/dev-doc-harness/references/naming-conventions.md",
    ".agents/skills/dev-doc-harness/references/artifact-contract.md",
    ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md",
    ".agents/skills/dev-doc-harness/references/subagent-model-policy.md",
    ".agents/skills/dev-doc-harness/references/durable-planning-quality.md",
    ".agents/skills/dev-doc-harness/references/artifact-style.md",
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
    ".agents/skills/dev-doc-harness/assets/templates/architecture-snapshot.md",
    ".agents/skills/dev-doc-harness/assets/templates/plan-amendment.md",
    ".agents/skills/dev-doc-harness/assets/templates/variance-log.md",
]

PRIMARY_TEMPLATE_FILES = [
    ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
    ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
    ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
    ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
]

PLAN_TEMPLATE_FILES = [
    ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
    ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
]

ASSEMBLY_MANIFEST_FILES = [
    ".agents/skills/dev-doc-harness/assets/templates/assemblies/small-medium-work-item-spec.json",
    ".agents/skills/dev-doc-harness/assets/templates/assemblies/small-medium-work-item-plan.json",
    ".agents/skills/dev-doc-harness/assets/templates/assemblies/large-phased-work-item-spec.json",
    ".agents/skills/dev-doc-harness/assets/templates/assemblies/large-phased-work-item-phase-plan.json",
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

PLAIN_LANGUAGE_RULE_ID = "rule" + ":style.plain-language"
PLAIN_LANGUAGE_PROMPT = (
    "Use `must` for binding Statements and `should` for advisory prose; "
    f"see `{PLAIN_LANGUAGE_RULE_ID}`."
)
PLAIN_LANGUAGE_CANONICAL_EXCEPTION = (
    "Do not use `shall` in author-facing current guidance or newly created durable artifacts."
)
PLAIN_LANGUAGE_FIXTURE_PATH = ".agents/skills/dev-doc-harness/scripts/fixtures/plain-language.md"
PLAIN_LANGUAGE_ACTIVE_MARKDOWN_PATHS = [
    "AGENTS.md",
    ".agents/skills/dev-doc-harness/SKILL.md",
    *CANONICAL_REFERENCES,
    *TEMPLATE_FILES,
]

REQUIRED_FILES = [
    "AGENTS.md",
    "README.md",
    "CHANGELOG.md",
    ".agents/skills/dev-doc-harness/SKILL.md",
    ".agents/skills/dev-doc-harness/VERSION",
    ".agents/skills/dev-doc-harness/scripts/test_harness_policy.py",
    ".agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py",
    ".agents/skills/dev-doc-harness/references/policy-architecture.md",
    ".agents/skills/dev-doc-harness/references/naming-conventions.md",
    ".agents/skills/dev-doc-harness/references/artifact-contract.md",
    ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md",
    ".agents/skills/dev-doc-harness/references/subagent-model-policy.md",
    ".agents/skills/dev-doc-harness/references/durable-planning-quality.md",
    ".agents/skills/dev-doc-harness/references/artifact-style.md",
    ".agents/skills/dev-doc-harness/references/release-policy.md",
    *[f".agents/skills/dev-doc-harness/docs/releases/{version}.md" for version in RELEASE_NOTE_VERSIONS],
    ".agents/skills/dev-doc-harness/scripts/assemble_templates.py",
    ".agents/skills/dev-doc-harness/assets/templates/blocks",
    ".agents/skills/dev-doc-harness/assets/templates/assemblies",
    *ASSEMBLY_MANIFEST_FILES,
    ".agents/skills/dev-doc-harness/references/context-and-quality-gates.md",
    ".agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md",
    ".agents/skills/dev-doc-harness/references/subagent-role-examples.md",
    ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
    ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
    ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
    ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
    ".agents/skills/dev-doc-harness/assets/templates/architecture-snapshot.md",
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


def normalize_prose(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def assert_normalized_text_contains(check_id: str, path: str, phrase: str, label: str | None = None) -> None:
    if normalize_prose(phrase) not in normalize_prose(read_repo_text(path)):
        add_failure(check_id, f"Missing {label or phrase} in {path}")


def assert_text_not_contains(check_id: str, path: str, pattern: str, label: str | None = None) -> None:
    text = read_repo_text(path)
    if re.search(pattern, text):
        add_failure(check_id, f"Unexpected {label or pattern} in {path}")


def get_plain_language_active_markdown_paths() -> list[str]:
    paths = set(PLAIN_LANGUAGE_ACTIVE_MARKDOWN_PATHS)
    blocks_root = join_repo_path(".agents/skills/dev-doc-harness/assets/templates/blocks")
    if blocks_root.exists():
        paths.update(to_repo_relative_path(path) for path in blocks_root.glob("*.md"))
    return sorted(paths)


def find_unapproved_plain_language_modals(path: str, text: str) -> list[str]:
    if path not in get_plain_language_active_markdown_paths():
        return []

    failures: list[str] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not re.search(r"(?i)\bshall\b", line):
            continue
        if (
            path == ".agents/skills/dev-doc-harness/references/artifact-style.md"
            and line.strip() == PLAIN_LANGUAGE_CANONICAL_EXCEPTION
        ):
            continue
        failures.append(f"{path}:{line_number}: prohibited modal outside the canonical definition")
    return failures


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
        "large-anchor": ["module:lifecycle", "module:quality", "module:models", "module:artifact-style"],
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


def assert_route_requires(operation: str, required_patterns: list[str], check_id: str) -> None:
    path = ".agents/skills/dev-doc-harness/SKILL.md"
    text = read_repo_text(path)
    route_line = next((line for line in re.split(r"\r?\n", text) if re.search(rf"^\|\s*{re.escape(operation)}\s*\|", line)), "")
    if not route_line:
        add_failure(check_id, f"Missing operation route: {operation}")
        return
    cells = [cell.strip() for cell in route_line.split("|")[1:-1]]
    required_cell = cells[1] if len(cells) > 1 else ""
    for pattern in required_patterns:
        if not re.search(pattern, required_cell):
            add_failure(check_id, f"Route '{operation}' is missing required target pattern: {pattern}")


def assert_route_budgets() -> None:
    text = read_repo_text(".agents/skills/dev-doc-harness/SKILL.md")
    budgets = {
        "Classify work size": 1,
        "Draft or review small/medium specs and plans": 4,
        "Draft or review large anchor specs": 4,
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

    shared_assembly_blocks = {
        paragraph
        for _, paragraph in get_normalized_paragraphs(
            ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.common.handoff.md"
        )
    }
    shared_generated_targets = set(PRIMARY_TEMPLATE_FILES)
    seen: dict[str, str] = {}
    for target in targets:
        for _, paragraph_text in get_normalized_paragraphs(target):
            if paragraph_text in seen and seen[paragraph_text] != target:
                is_intentional_generated_copy = (
                    paragraph_text in shared_assembly_blocks
                    and seen[paragraph_text] in shared_generated_targets
                    and target in shared_generated_targets
                )
                if not is_intentional_generated_copy:
                    add_failure("phrases.duplicate-blocks", f"Duplicate broad policy block in {seen[paragraph_text]} and {target}")
            else:
                seen.setdefault(paragraph_text, target)


def assert_template_assembly() -> None:
    check_id = "templates.assembly"
    script_path = ".agents/skills/dev-doc-harness/scripts/assemble_templates.py"
    block_name_pattern = re.compile(
        r"^(?:spec|plan)\.\d{3}\.(?:common|small|large|phase)\.[a-z0-9]+(?:-[a-z0-9]+)*\.md$"
    )
    allowed_scopes = {"common", "small", "large", "phase"}
    expected_outputs = set(PRIMARY_TEMPLATE_FILES)
    declared_outputs: set[str] = set()

    blocks_root = join_repo_path(".agents/skills/dev-doc-harness/assets/templates/blocks")
    expected_handoff_blocks = [
        ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.085.small.handoff.md",
        ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.085.large.handoff.md",
        ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.common.handoff.md",
    ]
    for path in expected_handoff_blocks:
        assert_path_exists(check_id, path)
    for path in [
        ".agents/skills/dev-doc-harness/assets/templates/blocks/handoff.085.common.combined-small-spec.md",
        ".agents/skills/dev-doc-harness/assets/templates/blocks/handoff.085.common.execution-thread.md",
        ".agents/skills/dev-doc-harness/assets/templates/blocks/handoff.085.common.large-anchor-spec.md",
    ]:
        assert_path_absent(check_id, path)
    if blocks_root.exists():
        for block_path in sorted(blocks_root.glob("*.md")):
            name = block_path.name
            if not block_name_pattern.match(name):
                add_failure(check_id, f"Block filename does not follow the spec/plan grammar: {name}")
                continue
            scope = name.split(".")[2]
            if scope not in allowed_scopes:
                add_failure(check_id, f"Block filename has unsupported scope '{scope}': {name}")

    assembly_root = join_repo_path(".agents/skills/dev-doc-harness/assets/templates/assemblies")
    expected_manifest_set = {Path(path).name for path in ASSEMBLY_MANIFEST_FILES}
    if assembly_root.exists():
        discovered_manifest_set = {path.name for path in assembly_root.glob("*.json")}
        for manifest_name in sorted(discovered_manifest_set - expected_manifest_set):
            add_failure(check_id, f"Unexpected assembly manifest: {manifest_name}")
        for manifest_name in sorted(expected_manifest_set - discovered_manifest_set):
            add_failure(check_id, f"Expected assembly manifest was not discovered: {manifest_name}")

    for manifest in ASSEMBLY_MANIFEST_FILES:
        manifest_path = join_repo_path(manifest)
        if not manifest_path.exists():
            add_failure(check_id, f"Missing assembly manifest: {manifest}")
            continue
        try:
            data = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            add_failure(check_id, f"Manifest is not valid JSON: {manifest}: {exc}")
            continue

        output = data.get("output")
        blocks = data.get("blocks")
        if not isinstance(output, str) or output not in expected_outputs:
            add_failure(check_id, f"Manifest {manifest} has unexpected output: {output!r}")
        else:
            declared_outputs.add(output)
        if not isinstance(blocks, list) or not blocks:
            add_failure(check_id, f"Manifest {manifest} must have a non-empty blocks list")
            continue
        def assembly_order(block: str) -> tuple[int, str]:
            name = Path(block).name
            match = block_name_pattern.match(name)
            return (int(name.split(".")[1]), name) if match else (999, name)

        if blocks != sorted(blocks, key=assembly_order):
            add_failure(check_id, f"Manifest {manifest} blocks should sort in assembly order")
        for block in blocks:
            if not isinstance(block, str):
                add_failure(check_id, f"Manifest {manifest} contains a non-string block entry: {block!r}")
                continue
            if not block.startswith("blocks/") or "/" in block.removeprefix("blocks/"):
                add_failure(check_id, f"Manifest {manifest} block path must be under blocks/: {block}")
                continue
            block_name = Path(block).name
            if not block_name_pattern.match(block_name):
                add_failure(check_id, f"Manifest {manifest} references badly named block: {block}")
            if not join_repo_path(f".agents/skills/dev-doc-harness/assets/templates/{block}").exists():
                add_failure(check_id, f"Manifest {manifest} references missing block: {block}")

    missing_outputs = expected_outputs - declared_outputs
    for output in sorted(missing_outputs):
        add_failure(check_id, f"No assembly manifest declares output: {output}")

    unresolved_include_pattern = re.compile(r"(\{\{|\{%[^\n]*include|<!--\s*include|blocks/)", re.IGNORECASE)
    for template in PRIMARY_TEMPLATE_FILES:
        text = read_repo_text(template)
        if not text.startswith("<!-- Generated by assemble_templates.py"):
            add_failure(check_id, f"{template} must start with the generated-source note")
        if unresolved_include_pattern.search(text):
            add_failure(check_id, f"{template} contains unresolved include or source-block syntax")

    commitment_header_pattern = re.compile(
        r"\|\s*Specification Commitment\s*\|\s*Disposition\s*\|\s*Implementation Tasks\s*\|"
    )
    verification_header_pattern = re.compile(
        r"\|\s*Verification Criterion\s*\|\s*Plan Checks\s*\|\s*Expected evidence stage\s*\|"
    )
    for template in PLAN_TEMPLATE_FILES:
        text = read_repo_text(template)
        task_plan_match = re.search(r"^## Implementation Tasks\s*(?P<body>.*?)(?=^##\s+|\Z)", text, flags=re.MULTILINE | re.DOTALL)
        checks_match = re.search(r"^## Plan Checks\s*(?P<body>.*?)(?=^##\s+|\Z)", text, flags=re.MULTILINE | re.DOTALL)
        commitment_match = re.search(r"^## Commitment-Disposition Mapping\s*(?P<body>.*?)(?=^##\s+|\Z)", text, flags=re.MULTILINE | re.DOTALL)
        verification_match = re.search(r"^## Verification-Execution Mapping\s*(?P<body>.*?)(?=^##\s+|\Z)", text, flags=re.MULTILINE | re.DOTALL)

        if not task_plan_match:
            add_failure(check_id, f"{template} is missing ## Implementation Tasks")
        else:
            task_plan = task_plan_match.group("body")
            for label in ["Dependencies:", "Implementation:", "Exit criteria:"]:
                if label not in task_plan:
                    add_failure(check_id, f"{template} task section is missing field label: {label}")
            if not re.search(r"^### `TASK-\d{3}` Implementation Task —", task_plan, re.MULTILINE):
                add_failure(check_id, f"{template} is missing a full-name TASK heading")

        if not checks_match:
            add_failure(check_id, f"{template} is missing ## Plan Checks")
        else:
            for label in ["Covers:", "Procedure:", "Expected result:", "Evidence record:", "Stage or environment:"]:
                if label not in checks_match.group("body"):
                    add_failure(check_id, f"{template} Plan Checks are missing field label: {label}")
        if not commitment_match or not commitment_header_pattern.search(commitment_match.group("body")):
            add_failure(check_id, f"{template} is missing the commitment-disposition mapping header")
        if not verification_match or not verification_header_pattern.search(verification_match.group("body")):
            add_failure(check_id, f"{template} is missing the verification-execution mapping header")

    if join_repo_path(script_path).exists():
        result = subprocess.run(
            [sys.executable, str(join_repo_path(script_path)), "--check"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            detail = (result.stdout + result.stderr).strip() or f"{script_path} --check failed"
            add_failure(check_id, detail)
    else:
        add_failure(check_id, f"Missing assembly script: {script_path}")


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
    if not re.search(rf"\A{re.escape(CURRENT_DEVELOPMENT_MARKER)}\r?\n?\Z", version_text):
        add_failure(check_id, f"{version_path} must contain exactly {CURRENT_DEVELOPMENT_MARKER} plus an optional trailing newline")
        return
    for version in RELEASE_NOTE_VERSIONS:
        assert_path_exists(check_id, f".agents/skills/dev-doc-harness/docs/releases/{version}.md")


def assert_release_notes() -> None:
    check_id = "release.notes"
    release_notes_path = f".agents/skills/dev-doc-harness/docs/releases/{LATEST_RELEASE_NOTE_VERSION}.md"
    release_notes = read_repo_text(release_notes_path)
    changelog = read_repo_text("CHANGELOG.md")
    required_headings = [
        f"# Dev Doc Harness {LATEST_RELEASE_NOTE_VERSION}",
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

    source_entries = re.findall(r"`(2026-[^`]+)`", source_match.group("body"))
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
            r"^###?\s+(?P<heading>2026-[^\r\n]+)\r?\n(?P<body>.*?)(?=^###?\s+|\Z)",
            text,
            flags=re.MULTILINE | re.DOTALL,
        )
        if re.search(r"^Release target:\s+`", match.group("body"), flags=re.MULTILINE)
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
        elif not re.search(r"^(?:unreleased|0\.\d+\.\d+|0\.\d+\+)$", release_target_lines[0].group(1)):
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
    release_notes = f".agents/skills/dev-doc-harness/docs/releases/{LATEST_RELEASE_NOTE_VERSION}.md"

    assert_text_contains(check_id, release_policy, r"distributable harness package is root `AGENTS\.md` plus `\.agents/`", "release policy package boundary")
    assert_text_contains(check_id, release_notes, r"distributable package is root `AGENTS\.md` plus `\.agents/`", "release notes package boundary")
    assert_text_contains(check_id, "README.md", r"copyable distributable package is\s+the root `AGENTS\.md` file plus the\s+`\.agents/` folder", "README package boundary")
    assert_text_contains(check_id, release_policy, r"Do not copy this repository's `docs/work-items/`", "release policy work-item exclusion")
    assert_text_contains(check_id, "README.md", r"(?i)do not copy this repository's\s+`docs/work-items/` folder", "README work-item exclusion")
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


def run_consolidation_fixture(args: list[str], repo_root: Path) -> subprocess.CompletedProcess[str]:
    script_path = join_repo_path(".agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py")
    return subprocess.run(
        [sys.executable, str(script_path), "--repo-root", str(repo_root), *args],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
    )


def write_fixture_file(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def assert_changelog_fragment_contract() -> None:
    check_id = "changelog.fragments"
    script_path = ".agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py"
    lifecycle = ".agents/skills/dev-doc-harness/references/artifact-contract.md"
    freeze = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"
    naming = ".agents/skills/dev-doc-harness/references/naming-conventions.md"
    release_policy = ".agents/skills/dev-doc-harness/references/release-policy.md"
    release_process = "docs/release-branch-process.md"
    operator_docs = ["README.md", ".agents/skills/dev-doc-harness/docs/operator-note.md"]
    hook = ".githooks/pre-commit"

    assert_text_contains(check_id, lifecycle, r"docs/work-items/<work-id>/changelog/\*\.md", "lifecycle fragment location")
    assert_text_contains(check_id, lifecycle, r"root `CHANGELOG\.md` remains the consolidated publication view", "root changelog publication view")
    assert_text_contains(check_id, freeze, r"approved planning artifacts.+changelog source fragment", "freeze stages fragment")
    assert_text_contains(check_id, naming, r"<changelog-fragment-path>", "fragment path derived pattern")
    assert_text_contains(check_id, release_policy, r"Dev Doc Harness distribution release", "harness distribution release scope")
    assert_text_contains(check_id, release_policy, r"after fragment consolidation", "root source after consolidation")
    assert_text_contains(check_id, release_process, r"consolidate_changelog_fragments\.py --check", "release process consolidation check")
    assert_text_contains(check_id, release_process, r"consolidate_changelog_fragments\.py --lint", "release process lint")
    assert_text_contains(check_id, release_process, r"before renaming `## Unreleased`", "release process ordering")
    assert_text_contains(check_id, lifecycle, r"multiple independently valid, newest-first entries", "lifecycle multi-entry grammar")
    assert_text_contains(check_id, naming, r"multiple independently valid, newest-first entries", "naming multi-entry grammar")
    assert_text_contains(check_id, hook, r"set -eu", "hook strict shell mode")
    assert_text_contains(check_id, hook, r"consolidate_changelog_fragments\.py --lint", "hook lint gate")
    assert_text_not_contains(check_id, hook, r"consolidate_changelog_fragments\.py --check", "hook root completeness gate")

    for phrase, label in [
        ("The copyable distributable package is the root `AGENTS.md` file plus the `.agents/` folder.", "README package boundary"),
        ("Do not copy this repository's `docs/work-items/` folder.", "README work-item exclusion"),
        ("you can roll back by reverting that dedicated update.", "README rollback guidance"),
    ]:
        assert_normalized_text_contains(check_id, "README.md", phrase, label)

    for path in operator_docs:
        assert_text_contains(check_id, path, r"project-owned checkpoint", f"{path} operator checkpoint")
        assert_text_contains(check_id, path, r"product/application release", f"{path} downstream release boundary")

    for template in PRIMARY_TEMPLATE_FILES:
        assert_text_contains(check_id, template, r"docs/work-items/<work-id>/changelog/\*\.md", f"{template} fragment matrix guidance")
        assert_text_contains(check_id, template, r"consolidat", f"{template} consolidation guidance")

    if not join_repo_path(script_path).exists():
        add_failure(check_id, f"Missing consolidation script: {script_path}")
        return

    with tempfile.TemporaryDirectory() as temp_dir:
        repo_root = Path(temp_dir)
        changelog = repo_root / "CHANGELOG.md"
        write_fixture_file(
            changelog,
            "# Changelog\n\n## Unreleased\n\n## 0.5.0 - 2026-06-01\n\n### Changed\n\n- Previous release.\n",
        )
        valid_fragment = repo_root / "docs/work-items/2027-01-02_example/changelog/implementation.md"
        valid_entry = (
            "### 2027-01-02_example -- add newer fixture entry\n\n"
            "Release target: `unreleased`\n"
            "Package impact: `repository-only`\n"
            "Release-note: `source-only`\n\n"
            "#### Added\n\n"
            "- Added a newer fixture entry.\n\n"
            "### 2027-01-02_example -- add fixture entry\n\n"
            "Release target: `unreleased`\n"
            "Package impact: `repository-only`\n"
            "Release-note: `source-only`\n\n"
            "#### Added\n\n"
            "- Added a fixture entry.\n"
        )
        write_fixture_file(valid_fragment, valid_entry)

        lint_result = run_consolidation_fixture(["--lint"], repo_root)
        if lint_result.returncode != 0:
            add_failure(check_id, f"--lint should accept valid entries before consolidation: {(lint_result.stdout + lint_result.stderr).strip()}")

        missing_check = run_consolidation_fixture(["--check"], repo_root)
        if missing_check.returncode == 0:
            add_failure(check_id, "--check should fail when a valid fragment is missing from CHANGELOG.md")
        elif any(
            heading not in (missing_check.stdout + missing_check.stderr)
            for heading in [
                "2027-01-02_example -- add newer fixture entry",
                "2027-01-02_example -- add fixture entry",
            ]
        ):
            add_failure(check_id, "--check failure should name each missing fragment heading")
        if "add fixture entry" in changelog.read_text(encoding="utf-8"):
            add_failure(check_id, "--check modified CHANGELOG.md")

        write_result = run_consolidation_fixture([], repo_root)
        if write_result.returncode != 0:
            add_failure(check_id, f"write consolidation failed: {(write_result.stdout + write_result.stderr).strip()}")
        consolidated = changelog.read_text(encoding="utf-8")
        for heading in [
            "### 2027-01-02_example -- add newer fixture entry",
            "### 2027-01-02_example -- add fixture entry",
        ]:
            if consolidated.count(heading) != 1:
                add_failure(check_id, "write consolidation should insert each valid fragment exactly once")
        if "## 0.5.0 - 2026-06-01" not in consolidated:
            add_failure(check_id, "write consolidation should preserve historical release sections")

        duplicate_result = run_consolidation_fixture([], repo_root)
        if duplicate_result.returncode != 0:
            add_failure(check_id, f"duplicate consolidation failed: {(duplicate_result.stdout + duplicate_result.stderr).strip()}")
        duplicate_text = changelog.read_text(encoding="utf-8")
        for heading in [
            "### 2027-01-02_example -- add newer fixture entry",
            "### 2027-01-02_example -- add fixture entry",
        ]:
            if duplicate_text.count(heading) != 1:
                add_failure(check_id, "rerunning consolidation should not duplicate an existing heading")

        final_check = run_consolidation_fixture(["--check"], repo_root)
        if final_check.returncode != 0:
            add_failure(check_id, f"--check should pass after consolidation: {(final_check.stdout + final_check.stderr).strip()}")

    with tempfile.TemporaryDirectory() as temp_dir:
        repo_root = Path(temp_dir)
        write_fixture_file(repo_root / "CHANGELOG.md", "# Changelog\n\n## Unreleased\n")
        invalid_fragment = repo_root / "docs/work-items/2026-07-09_bad/changelog/implementation.md"
        write_fixture_file(
            invalid_fragment,
            "### 2026-07-09_bad -- valid first entry\n\n"
            "Release target: `unreleased`\n"
            "Package impact: `repository-only`\n"
            "Release-note: `source-only`\n\n"
            "#### Changed\n\n"
            "- Valid first entry.\n\n"
            "### 2026-07-09_bad -- malformed second entry\n\n"
            "Release target: `unreleased`\n"
            "Release target: `unreleased`\n"
            "Package impact: `repository-only`\n\n"
            "#### Changed\n\n"
            "- Missing release note metadata.\n",
        )
        invalid_result = run_consolidation_fixture(["--lint"], repo_root)
        invalid_output = invalid_result.stdout + invalid_result.stderr
        if invalid_result.returncode == 0:
            add_failure(check_id, "malformed fragment should make --check fail")
        for expected in ["docs/work-items/2026-07-09_bad/changelog/implementation.md", "malformed second entry", "Release target", "Release-note"]:
            if expected not in invalid_output:
                add_failure(check_id, f"malformed fragment output should mention {expected}")

    with tempfile.TemporaryDirectory() as temp_dir:
        repo_root = Path(temp_dir)
        write_fixture_file(repo_root / "CHANGELOG.md", "# Changelog\n\n## Unreleased\n")
        write_fixture_file(
            repo_root / "docs/work-items/2026-07-09_duplicate/changelog/implementation.md",
            "### 2026-07-09_duplicate -- shared heading\n\n"
            "Release target: `unreleased`\n"
            "Package impact: `repository-only`\n"
            "Release-note: `source-only`\n\n"
            "#### Changed\n\n"
            "- First duplicate fixture.\n\n"
            "### 2026-07-09_duplicate -- shared heading\n\n"
                "Release target: `unreleased`\n"
                "Package impact: `repository-only`\n"
                "Release-note: `source-only`\n\n"
                "#### Changed\n\n"
                "- Second duplicate fixture.\n",
        )
        duplicate_result = run_consolidation_fixture(["--lint"], repo_root)
        duplicate_output = duplicate_result.stdout + duplicate_result.stderr
        if duplicate_result.returncode == 0:
            add_failure(check_id, "duplicate fragment headings should make --check fail")
        for expected in ["Duplicate changelog fragment heading", "implementation.md", "entry 1", "entry 2", "shared heading"]:
            if expected not in duplicate_output:
                add_failure(check_id, f"duplicate fragment output should mention {expected}")

    with tempfile.TemporaryDirectory() as temp_dir:
        repo_root = Path(temp_dir)
        write_fixture_file(repo_root / "CHANGELOG.md", "# Changelog\n\n## Unreleased\n")
        write_fixture_file(
            repo_root / "docs/work-items/2026-07-09_downstream/changelog/release-target.md",
            "### 2026-07-09_downstream -- accept downstream release target\n\n"
            "Release target: `1.2.3`\n"
            "Package impact: `repository-only`\n"
            "Release-note: `source-only`\n\n"
            "#### Changed\n\n"
            "- Accepted a downstream release target value.\n",
        )
        downstream_result = run_consolidation_fixture(["--check"], repo_root)
        if downstream_result.returncode != 0:
            add_failure(
                check_id,
                f"non-harness release target values should validate: {(downstream_result.stdout + downstream_result.stderr).strip()}",
            )

    with tempfile.TemporaryDirectory() as temp_dir:
        repo_root = Path(temp_dir)
        write_fixture_file(
            repo_root / "docs/work-items/2026-07-09_lint-only/changelog/implementation.md",
            "### 2026-07-09_lint-only -- accept without root changelog\n\n"
            "Release target: `unreleased`\n"
            "Package impact: `repository-only`\n"
            "Release-note: `source-only`\n\n"
            "#### Changed\n\n"
            "- Lint does not require root completeness.\n",
        )
        lint_result = run_consolidation_fixture(["--lint"], repo_root)
        if lint_result.returncode != 0:
            add_failure(check_id, f"--lint should not require CHANGELOG.md: {(lint_result.stdout + lint_result.stderr).strip()}")


def assert_work_item_architecture_decisions() -> None:
    check_id = "architecture.decisions"
    lifecycle = ".agents/skills/dev-doc-harness/references/artifact-contract.md"
    quality = ".agents/skills/dev-doc-harness/references/durable-planning-quality.md"
    router = ".agents/skills/dev-doc-harness/SKILL.md"
    snapshot_template = ".agents/skills/dev-doc-harness/assets/templates/architecture-snapshot.md"
    operator_docs = ["README.md", ".agents/skills/dev-doc-harness/docs/operator-note.md"]
    spec_templates = [
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
    ]
    plan_templates = [
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
    ]

    assert_text_contains(check_id, lifecycle, "rule" + r":lifecycle[.]work-item-architecture-decisions", "lifecycle architecture rule owner")
    assert_text_contains(check_id, lifecycle, r"## Work-item architecture decisions", "lifecycle architecture rule heading")
    assert_text_contains(check_id, lifecycle, r"required, not applicable, or deferred", "architecture snapshot matrix states")
    assert_text_contains(check_id, lifecycle, r"plans? and phase plans?.+consume", "plans consume architecture")
    assert_text_contains(check_id, lifecycle, r"ARCHITECTURE\.md.+future work", "future durable architecture docs boundary")

    assert_text_contains(check_id, quality, r"architectural decisions", "quality architecture preservation")
    assert_text_contains(check_id, quality, r"silently reinterpret", "quality prevents silent reinterpretation")
    assert_text_contains(check_id, router, r"architecture snapshot", "router architecture snapshot discoverability")

    for path in operator_docs:
        assert_text_contains(check_id, path, r"work-item architecture", "operator work-item architecture guidance")
        assert_text_contains(check_id, path, r"ARCHITECTURE\.md.+future work", "operator durable architecture boundary")

    for path in spec_templates:
        assert_text_contains(check_id, path, r"## Architecture Decisions", "spec architecture section")
        assert_text_contains(check_id, path, r"drivers", "spec architecture drivers prompt")
        assert_text_contains(check_id, path, r"rejected alternatives", "spec architecture alternatives prompt")
        assert_text_contains(check_id, path, r"architecture snapshot", "spec architecture snapshot prompt")

    for path in plan_templates:
        assert_text_contains(check_id, path, r"architecture.+input", "plan architecture input prompt")
        assert_text_contains(check_id, path, r"architecture snapshot", "plan architecture snapshot reference")
        assert_text_contains(check_id, path, r"amendment", "plan architecture amendment path")
        assert_text_contains(check_id, path, r"reinterpret", "plan architecture reinterpretation guard")

    assert_text_contains(check_id, snapshot_template, r"Schema:\s+`" + "schema" + r":snapshot[.]architecture`", "architecture snapshot schema")
    for pattern, label in [
        (r"## Decision Ledger", "decision ledger section"),
        (r"DEC-001", "decision ID example"),
        (r"Source spec sections", "source spec trace"),
        (r"## Decision Drivers", "decision drivers section"),
        (r"## Constraints", "constraints section"),
        (r"Selected approach", "selected approach field"),
        (r"Affected boundaries", "affected boundaries field"),
        (r"Rejected alternatives", "rejected alternatives field"),
        (r"Validation cues", "validation cues field"),
        (r"ARCHITECTURE\.md.+future work", "future durable docs boundary"),
    ]:
        assert_text_contains(check_id, snapshot_template, pattern, label)

    disallowed_architecture_workflow = r"(?i)(create|update|maintain|require)\s+`?ARCHITECTURE\.md`?"
    for path in [lifecycle, router, *operator_docs, *spec_templates, *plan_templates, snapshot_template]:
        assert_text_not_contains(check_id, path, disallowed_architecture_workflow, "active ARCHITECTURE.md workflow")


def assert_artifact_style_guidance() -> None:
    check_id = "artifact-style.guidance"
    style = ".agents/skills/dev-doc-harness/references/artifact-style.md"
    architecture = ".agents/skills/dev-doc-harness/references/policy-architecture.md"
    quality = ".agents/skills/dev-doc-harness/references/durable-planning-quality.md"
    router = ".agents/skills/dev-doc-harness/SKILL.md"
    role_examples = ".agents/skills/dev-doc-harness/references/subagent-role-examples.md"
    template_paths = [
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
        ".agents/skills/dev-doc-harness/assets/templates/architecture-snapshot.md",
        ".agents/skills/dev-doc-harness/assets/templates/plan-amendment.md",
        ".agents/skills/dev-doc-harness/assets/templates/variance-log.md",
    ]

    assert_text_contains(check_id, style, r"Module:\s+`module:artifact-style`", "artifact-style module declaration")
    for rule_id in [
        "rule:style.final-artifact-content",
        "rule:style.scannable-structure",
        "rule:style.placeholder-control",
        "rule:style.trace-density",
        "rule:style.template-prompts",
    ]:
        assert_text_contains(check_id, style, re.escape(rule_id), f"{rule_id} owner")

    assert_text_contains(check_id, architecture, r"module:artifact-style", "module catalog entry")
    assert_text_contains(check_id, architecture, r"large anchor specs", "large anchor routing condition")
    assert_text_contains(check_id, architecture, r"hard-to-scan", "hard-to-scan routing condition")
    assert_text_contains(check_id, quality, r"Baseline artifact readability", "baseline readability section")
    assert_text_contains(check_id, quality, "rule" + r":evidence[.]preservation", "quality evidence cross-reference")
    assert_text_contains(check_id, router, r"Draft or review large anchor specs.+module:artifact-style", "large route style requirement")
    assert_route_requires(
        "Draft or review small/medium specs and plans",
        ["module:artifact-style"],
        check_id,
    )
    assert_text_not_contains(check_id, role_examples, r"standard-review", "non-canonical model policy")

    for path in template_paths:
        assert_text_contains(check_id, path, r"final artifact|Final artifact|Superseded by: None|DEC-001|AMD-001|VAR-001", "template final-state or trace cue")

    for path in [
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
    ]:
        assert_text_contains(check_id, path, r"unresolved required decisions", "readiness unresolved-decision check")

    assert_text_contains(check_id, ".agents/skills/dev-doc-harness/assets/templates/architecture-snapshot.md", r"DEC-001", "architecture decision ID")
    assert_text_contains(check_id, ".agents/skills/dev-doc-harness/assets/templates/plan-amendment.md", r"AMD-001", "amendment ID")
    assert_text_contains(check_id, ".agents/skills/dev-doc-harness/assets/templates/variance-log.md", r"VAR-001", "variance ID")


def assert_plain_language_policy() -> None:
    check_id = "plain-language.policy"
    style = ".agents/skills/dev-doc-harness/references/artifact-style.md"
    router = ".agents/skills/dev-doc-harness/SKILL.md"
    prompt_paths = [
        ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.030.common.commitments-verification.md",
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
    ]
    small_medium_source_blocks = [
        ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.010.small.header.md",
        ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.010.small.header-inputs.md",
    ]

    assert_text_contains(check_id, style, re.escape(PLAIN_LANGUAGE_RULE_ID), "plain-language rule owner")
    assert_text_contains(check_id, style, r"must.+binding.+should.+guidance", "canonical must/should rule")
    if read_repo_text(style).count(PLAIN_LANGUAGE_CANONICAL_EXCEPTION) != 1:
        add_failure(check_id, "canonical definition-only exception must appear exactly once")
    assert_route_requires(
        "Draft or review small/medium specs and plans",
        ["module:artifact-style"],
        check_id,
    )
    for path in prompt_paths:
        assert_text_contains(check_id, path, re.escape(PLAIN_LANGUAGE_PROMPT), "plain-language prompt")
    for path in small_medium_source_blocks:
        assert_text_contains(check_id, path, r"module:artifact-style", "required small/medium style module")
        assert_text_contains(check_id, path, r"must load `module:artifact-style`", "mandatory small/medium style cue")

    if not find_unapproved_plain_language_modals("AGENTS.md", "A current authoring rule shall fail."):
        add_failure(check_id, "synthetic active-surface occurrence did not fail")
    for path, text in [
        (style, PLAIN_LANGUAGE_CANONICAL_EXCEPTION),
        ("docs/work-items/frozen/spec_example.md", "Historical text shall remain unchanged."),
        ("LICENSE", "Legal text shall remain unchanged."),
        (PLAIN_LANGUAGE_FIXTURE_PATH, "Validator fixture shall remain outside the Markdown scan."),
    ]:
        if find_unapproved_plain_language_modals(path, text):
            add_failure(check_id, f"controlled exclusion was scanned: {path}")

    if PLAIN_LANGUAGE_FIXTURE_PATH in get_plain_language_active_markdown_paths():
        add_failure(check_id, "plain-language fixture path is inside the active Markdown scan")

    for path in get_plain_language_active_markdown_paths():
        for failure in find_unapproved_plain_language_modals(path, read_repo_text(path)):
            add_failure(check_id, failure)


def assert_model_selection_dimensions() -> None:
    check_id = "models.selection-dimensions"
    models = ".agents/skills/dev-doc-harness/references/subagent-model-policy.md"
    role_examples = ".agents/skills/dev-doc-harness/references/subagent-role-examples.md"
    readme = "README.md"

    for rule_id in [
        "rule:models.selection-dimensions",
        "rule:models.orchestration-mode",
        "rule:models.execution-continuity",
    ]:
        assert_text_contains(check_id, models, re.escape(rule_id), f"{rule_id} owner")

    for label in [
        "Model generation",
        "Capability tier",
        "Reasoning effort",
        "Orchestration mode",
        "Resolved profile",
        "Availability/fallback",
        "Execution continuity",
        "Context visibility",
        "Artifact rehydration required",
    ]:
        assert_text_contains(check_id, models, re.escape(label), f"selection field '{label}'")

    for tier in ["flagship", "balanced", "fast/economy"]:
        assert_text_contains(check_id, models, re.escape(tier), f"vendor-neutral tier '{tier}'")
    for mapping in ["GPT-5.6", "Sol", "Terra", "Luna"]:
        assert_text_contains(check_id, models, re.escape(mapping), f"current provider mapping '{mapping}'")

    assert_text_contains(check_id, models, r"[Uu]ltra.+platform[- ]managed.+multi-agent|platform[- ]managed.+multi-agent.+[Uu]ltra", "ultra orchestration classification")
    assert_text_contains(check_id, models, r"does not (?:automatically )?provide.+task partitioning", "platform orchestration limitation")
    assert_text_contains(check_id, models, r"enterprise-default.+(?:assess|consider).+(?:platform multi-agent|ultra)", "enterprise platform-orchestration assessment")
    assert_text_contains(check_id, models, r"economy-default.+Terra medium.+suggested baseline", "economy baseline policy")

    assert_text_contains(
        check_id,
        models,
        r"Terra medium.+suggested baseline.+substantial bounded work.+explicit outputs and validation",
        "calibrated Terra-medium bounded-work baseline",
    )
    assert_text_contains(check_id, models, r"Terra high.+effort escalation", "effort escalation classification")
    assert_text_contains(check_id, models, r"Sol medium.+tier escalation", "tier escalation classification")
    assert_text_contains(check_id, models, r"Sol high.+exceptional.+written reason", "exceptional Sol-high escalation")
    assert_text_contains(check_id, models, r"residual uncertainty|new variance", "late escalation justification")
    assert_text_contains(check_id, models, r"de-escalat.+bounded", "bounded-work de-escalation")
    assert_text_contains(
        check_id,
        models,
        r"missing product input.+undecided requirement.+plan contradiction.+(?:variance|approval)",
        "missing-decision approval boundary",
    )

    for path in [models, role_examples]:
        assert_text_contains(check_id, path, r"independent sub-agent reviewer.+default", "independent sub-agent reviewer default")
        assert_text_contains(check_id, path, r"curated artifacts", "independent reviewer context")
        assert_text_contains(check_id, path, r"separate task or thread.+operator-managed fallback", "manual review-isolation fallback")
        assert_text_contains(check_id, path, r"(?:one|single) named lens", "independent reviewer lens")
        assert_text_contains(check_id, path, r"evidence-backed", "evidence-backed finding requirement")
        assert_text_contains(check_id, path, r"severity", "evidence-backed finding severity")
        assert_text_contains(check_id, path, r"reproduction or validation path", "finding validation path")
        assert_text_contains(check_id, path, r"orchestration thread.+(?:owns|retains).+integration", "orchestration-owned integration")

    for layer in ["recommendation", "harness authorization", "runtime permission", "platform availability"]:
        assert_text_contains(check_id, models, re.escape(layer), f"authorization layer '{layer}'")
    assert_text_contains(check_id, models, r"approved fallback", "approved fallback behavior")
    assert_text_contains(check_id, models, r"de-facto orchestration mode", "de-facto orchestration reporting")
    assert_text_contains(check_id, models, r"unplanned.+(?:ultra|platform multi-agent).+(?:fresh confirmation|confirmation)", "unplanned orchestration confirmation")

    strategy_templates = [
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
    ]
    for path in strategy_templates:
        for label in ["Model generation", "Capability tier", "Reasoning effort", "Orchestration mode", "Resolved profile", "Availability/fallback"]:
            assert_text_contains(check_id, path, re.escape(label), f"template selection field '{label}'")
        assert_text_not_contains(check_id, path, r"Model class/profile:", "conflated per-role model class/profile field")

    strategy_source_blocks = [
        ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.040.common.model-strategy.md",
        ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.060.large.phase-decomposition-model.md",
    ]
    for path in strategy_source_blocks:
        assert_text_contains(check_id, path, r"suggested baseline", "strategy prompt baseline cue")
        assert_text_contains(check_id, path, r"effort.*tier|tier.*effort", "strategy prompt effort-tier cue")
        assert_text_contains(check_id, path, r"residual uncertainty or variance", "strategy prompt late-escalation cue")
        assert_text_contains(check_id, path, r"module:models", "strategy prompt canonical-policy route")

    assert_text_not_contains(check_id, models, r"\| Model class/profile \|", "conflated canonical example column")

    for path in [role_examples, readme]:
        assert_text_contains(check_id, path, r"Capability tier", "capability-tier guidance")
        assert_text_contains(check_id, path, r"Orchestration mode", "orchestration-mode guidance")
        assert_text_contains(check_id, path, r"ultra", "ultra guidance")
        assert_text_contains(check_id, path, r"execution-thread-start", "execution startup route")


def assert_execution_thread_start() -> None:
    check_id = "execution.thread-start"
    models = ".agents/skills/dev-doc-harness/references/subagent-model-policy.md"
    execution = ".agents/skills/dev-doc-harness/references/context-and-quality-gates.md"
    freeze = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"
    architecture = ".agents/skills/dev-doc-harness/references/policy-architecture.md"
    router = ".agents/skills/dev-doc-harness/SKILL.md"

    assert_text_contains(check_id, execution, re.escape("rule:execution-quality.execution-thread-start"), "execution-thread-start owner")
    assert_text_contains(check_id, execution, r"applicable instructions.+frozen artifacts", "instruction and artifact load order")
    assert_text_contains(check_id, execution, r"avoid.+rediscover", "rediscovery avoidance")
    assert_text_contains(check_id, execution, r"named task|first activity", "named starting activity")
    assert_text_contains(check_id, execution, r"variance", "variance stop route")

    assert_text_contains(check_id, models, r"new task with curated-artifact handoff", "new-task transition preference")
    assert_text_contains(check_id, models, r"(?:exact|precise).+remaining context.+not exposed|not exposed.+(?:exact|precise).+remaining context", "no unexposed context estimate")
    assert_text_contains(check_id, models, r"same-task.+re(?:-|)read.+frozen|same-task.+rehydrat", "same-task artifact rehydration")

    for path in PRIMARY_TEMPLATE_FILES:
        assert_text_contains(check_id, path, r"## Next-task handoff", "next-task handoff section")
        assert_text_contains(check_id, path, r"Exact authoritative artifacts:.+approved spec, plan or phase plan", "actual frozen boundary inputs")
        for label in [
            "Execution continuity",
            "Context visibility",
            "Artifact rehydration required",
            "First activity",
            "Variance stop condition",
        ]:
            assert_text_contains(check_id, path, re.escape(label), f"handoff field '{label}'")
        assert_text_contains(check_id, path, re.escape("rule:execution-quality.execution-thread-start"), "startup rule reference")

    for label in ["capability tier", "reasoning effort", "orchestration mode", "fallback", "execution continuity", "context visibility", "artifact rehydration"]:
        assert_text_contains(check_id, freeze, re.escape(label), f"freeze confirmation '{label}'")
    assert_text_contains(check_id, architecture, r"execution-thread-start", "architecture owner route")
    assert_text_contains(check_id, router, r"execution-thread-start", "router discoverability")


def assert_lifecycle_transition_targets() -> None:
    check_id = "lifecycle.transition-targets"
    lifecycle = ".agents/skills/dev-doc-harness/references/artifact-contract.md"
    freeze = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"
    models = ".agents/skills/dev-doc-harness/references/subagent-model-policy.md"

    assert_text_contains(check_id, lifecycle, re.escape("rule" + ":lifecycle.planning-shape"), "planning-shape rule owner")
    assert_text_contains(check_id, lifecycle, r"## Small/medium planning shape", "planning-shape owner heading")
    assert_text_contains(check_id, lifecycle, r"small/medium.+spec and plan.+(?:together|combined)", "combined small/medium default")
    assert_text_contains(check_id, lifecycle, r"spec-only freeze.+explicit.+(?:reason|exception)", "staged small/medium exception")
    assert_text_contains(check_id, lifecycle, r"large/phased.+phase-plan drafting", "large-anchor phase-plan route")

    for label in ["Planning shape", "Frozen package", "Next activity"]:
        assert_text_contains(check_id, freeze, re.escape(label), f"freeze field '{label}'")
    assert_text_contains(check_id, freeze, r"explicit.+approval.+creat.+task|approval.+specifically.+creat.+task", "task-creation approval")
    assert_text_contains(check_id, freeze, r"exact supported.+(?:model|configuration)|supported.+recorded.+settings", "exact supported configuration")
    assert_text_contains(check_id, freeze, r"manual.+copy-ready handoff|copy-ready handoff.+manual", "visible manual fallback")
    assert_text_contains(check_id, freeze, r"(?:do not|without).+silently substitut", "no configuration substitution")
    assert_text_contains(check_id, freeze, r"same task.+(?:separate|current-task|current task)", "separate same-task route")
    assert_text_contains(check_id, models, r"actual frozen.+(?:boundary|package)|frozen.+boundary", "continuity uses actual frozen boundary")
    assert_text_contains(check_id, models, r"documented next activity|named next activity", "continuity uses documented next activity")

    for path in PRIMARY_TEMPLATE_FILES:
        for label in ["Planning shape", "Frozen package", "Next activity"]:
            assert_text_contains(check_id, path, re.escape(label), f"{path} field '{label}'")

    small_spec = ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md"
    large_spec = ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md"
    for path in PLAN_TEMPLATE_FILES:
        assert_text_contains(check_id, path, r"approval.+creat.+task|creat.+task.+approval", f"{path} creation approval")
        assert_text_contains(check_id, path, r"manual.+copy-ready handoff|copy-ready handoff.+manual", f"{path} manual fallback")
        assert_text_contains(check_id, path, r"exact supported.+(?:model|configuration)|supported.+recorded.+settings", f"{path} exact configuration")
    assert_text_contains(check_id, small_spec, r"combined small/medium", "small spec combined planning shape")
    assert_text_contains(check_id, small_spec, r"does not.+(?:independent|plan-drafting).+handoff|no independent.+handoff", "small spec no independent plan handoff")
    assert_text_contains(check_id, large_spec, r"phase-plan drafting", "large anchor next activity")


CURRENT_SPEC_SCHEMA_PATHS = [
    ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.030.common.commitments-verification.md",
    ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
    ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
]

CURRENT_PLAN_SCHEMA_PATHS = [
    ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
    ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
]

CURRENT_COMMITMENT_VOCABULARY_PATHS = sorted(set(
    CANONICAL_REFERENCES
    + TEMPLATE_FILES
    + [
        ".agents/skills/dev-doc-harness/SKILL.md",
        ".agents/skills/dev-doc-harness/assets/templates/architecture-snapshot.md",
        ".agents/skills/dev-doc-harness/assets/templates/plan-amendment.md",
        ".agents/skills/dev-doc-harness/assets/templates/variance-log.md",
        ".agents/skills/dev-doc-harness/docs/operator-note.md",
        "README.md",
    ]
))


def validate_commitment_spec_fixture(text: str) -> list[str]:
    errors: list[str] = []
    spec_matches = list(re.finditer(r"^### `(?P<id>SPEC-\d{3})` Specification Commitment — .+$", text, re.MULTILINE))
    ver_matches = list(re.finditer(r"^(?P<level>#{3,4}) `(?P<id>VER-\d{3})` Verification Criterion — .+$", text, re.MULTILINE))
    spec_ids = [match.group("id") for match in spec_matches]
    ver_defs = [match.group("id") for match in ver_matches]
    if not spec_ids:
        errors.append("missing exact Specification Commitment heading")
    if len(spec_ids) != len(set(spec_ids)):
        errors.append("duplicate Specification Commitment ID")
    if len(ver_defs) != len(set(ver_defs)):
        errors.append("duplicate Verification Criterion ID")
    entity_matches = sorted([*spec_matches, *ver_matches], key=lambda match: match.start())
    next_start = {match.start(): (entity_matches[index + 1].start() if index + 1 < len(entity_matches) else len(text)) for index, match in enumerate(entity_matches)}
    for match in spec_matches:
        block = text[match.end():next_start[match.start()]]
        for field in ("Kind:", "Intent:", "Statement:"):
            if field not in block:
                errors.append(f"{match.group('id')} missing commitment field {field}")
    cross_start = text.find("## Cross-cutting Verification Criteria")
    for match in ver_matches:
        block = text[match.end():next_start[match.start()]]
        for field in ("Covers:", "Criterion:", "Expected evidence:"):
            if field not in block:
                errors.append(f"{match.group('id')} missing criterion field {field}")
        covers = set(re.findall(r"`(SPEC-\d{3})`", block.partition("Criterion:")[0]))
        if not covers:
            errors.append(f"{match.group('id')} has empty Covers")
        invalid_targets = sorted(covers - set(spec_ids))
        if invalid_targets:
            errors.append(f"{match.group('id')} invalid Covers target: {', '.join(invalid_targets)}")
        is_cross = cross_start >= 0 and match.start() > cross_start
        if is_cross and (match.group("level") != "###" or len(covers) < 2):
            errors.append(f"cross-cutting {match.group('id')} must be level three and cover at least two commitments")
        if not is_cross and (match.group("level") != "####" or len(covers) != 1):
            errors.append(f"local {match.group('id')} must be level four and cover exactly one commitment")
        if not is_cross:
            preceding_specs = [spec for spec in spec_matches if spec.start() < match.start()]
            adjacent_spec = preceding_specs[-1].group("id") if preceding_specs else None
            if covers != {adjacent_spec}:
                errors.append(f"local {match.group('id')} must be adjacent to its covered commitment")
    return errors


def validate_commitment_plan_fixture(text: str) -> list[str]:
    errors: list[str] = []
    required_sections = [
        "## Commitment-Disposition Mapping",
        "## Verification-Execution Mapping",
        "## Implementation Tasks",
        "## Plan Checks",
    ]
    for section in required_sections:
        if section not in text:
            errors.append(f"missing plan section {section}")
    task_ids = re.findall(r"^### `(TASK-\d{3})` Implementation Task — .+$", text, re.MULTILINE)
    check_ids = re.findall(r"^### `(CHECK-\d{3})` Plan Check — .+$", text, re.MULTILINE)
    task_matches = list(re.finditer(r"^### `(TASK-\d{3})` Implementation Task — .+$", text, re.MULTILINE))
    check_matches = list(re.finditer(r"^### `(CHECK-\d{3})` Plan Check — .+$", text, re.MULTILINE))
    if not task_ids:
        errors.append("missing exact Implementation Task heading")
    if not check_ids:
        errors.append("missing exact Plan Check heading")
    if len(task_ids) != len(set(task_ids)):
        errors.append("duplicate Implementation Task ID")
    if len(check_ids) != len(set(check_ids)):
        errors.append("duplicate Plan Check ID")
    entity_matches = sorted([*task_matches, *check_matches], key=lambda match: match.start())
    next_start = {match.start(): (entity_matches[index + 1].start() if index + 1 < len(entity_matches) else len(text)) for index, match in enumerate(entity_matches)}
    for match in task_matches:
        block = text[match.end():next_start[match.start()]]
        for field in ("Dependencies:", "Implementation:", "Exit criteria:"):
            if field not in block:
                errors.append(f"{match.group(1)} missing Implementation Task field {field}")
    for match in check_matches:
        block = text[match.end():next_start[match.start()]]
        for field in ("Covers:", "Procedure:", "Expected result:", "Evidence record:", "Stage or environment:"):
            if field not in block:
                errors.append(f"{match.group(1)} missing Plan Check field {field}")
        if not re.search(r"`VER-\d{3}`", block.partition("Procedure:")[0]):
            errors.append(f"{match.group(1)} has no Verification Criterion coverage")
    if "| Specification Commitment | Disposition |" not in text:
        errors.append("missing commitment-disposition table header")
    if "| Verification Criterion | Plan Checks | Expected evidence stage |" not in text:
        errors.append("missing verification-execution table header")
    commitment_section = text.partition("## Commitment-Disposition Mapping")[2].partition("## Verification-Execution Mapping")[0]
    verification_section = text.partition("## Verification-Execution Mapping")[2].partition("## Implementation Tasks")[0]
    mapped_specs = set(re.findall(r"\|\s*`(SPEC-\d{3})`", commitment_section))
    mapped_vers = set(re.findall(r"\|\s*`(VER-\d{3})`", verification_section))
    mapped_checks = set(re.findall(r"`(CHECK-\d{3})`", verification_section))
    if task_ids and not mapped_specs:
        errors.append("commitment-disposition mapping has no rows")
    if check_ids and not mapped_vers:
        errors.append("verification-execution mapping has no rows")
    invalid_mapped_checks = sorted(mapped_checks - set(check_ids))
    if invalid_mapped_checks:
        errors.append(f"verification mapping targets missing Plan Check: {', '.join(invalid_mapped_checks)}")
    orphan_checks = sorted(set(check_ids) - mapped_checks)
    if orphan_checks:
        errors.append(f"orphan Plan Check: {', '.join(orphan_checks)}")
    for match in check_matches:
        block = text[match.end():next_start[match.start()]]
        covered = set(re.findall(r"`(VER-\d{3})`", block.partition("Procedure:")[0]))
        invalid_vers = sorted(covered - mapped_vers)
        if invalid_vers:
            errors.append(f"{match.group(1)} invalid Verification Criterion target: {', '.join(invalid_vers)}")
    return errors


def assert_commitment_verification_quality() -> None:
    check_id = "quality.commitment-verification"
    quality = ".agents/skills/dev-doc-harness/references/durable-planning-quality.md"
    style = ".agents/skills/dev-doc-harness/references/artifact-style.md"
    for rule_id in [
        "rule:quality.specification-commitments",
        "rule:quality.verification-criteria",
        "rule:quality.plan-checks",
        "rule:quality.asymmetric-plan-coverage",
        "rule:quality.conformance-status",
    ]:
        assert_text_contains(check_id, quality, re.escape(rule_id), f"{rule_id} owner")
    for rule_id in [
        "rule:style.full-name-entity-headings",
        "rule:style.verification-criterion-placement",
        "rule:style.asymmetric-traceability",
    ]:
        assert_text_contains(check_id, style, re.escape(rule_id), f"{rule_id} owner")


def assert_commitment_verification_templates() -> None:
    check_id = "templates.commitment-verification"
    positive_spec = """### `SPEC-001` Specification Commitment — One\nKind: `Constraint`\nIntent: `Establish`\nStatement:\n1. One.\n#### `VER-001` Verification Criterion — One\nCovers:\n1. `SPEC-001`.\nCriterion:\n1. One.\nExpected evidence:\n1. One.\n### `SPEC-002` Specification Commitment — Two\nKind: `Deliverable`\nIntent: `Change`\nStatement:\n1. Two.\n## Cross-cutting Verification Criteria\n### `VER-002` Verification Criterion — Both\nCovers:\n1. `SPEC-001`.\n2. `SPEC-002`.\nCriterion:\n1. Both.\nExpected evidence:\n1. Both.\n"""
    positive_plan = """## Commitment-Disposition Mapping\n| Specification Commitment | Disposition | Implementation Tasks |\n|---|---|---|\n| `SPEC-001` | Implement | `TASK-001` |\n## Verification-Execution Mapping\n| Verification Criterion | Plan Checks | Expected evidence stage |\n|---|---|---|\n| `VER-001` | `CHECK-001` | Final |\n## Implementation Tasks\n### `TASK-001` Implementation Task — Change\nDependencies:\n1. None.\nImplementation:\n1. Change.\nExit criteria:\n1. Done.\n## Plan Checks\n### `CHECK-001` Plan Check — Verify\nCovers:\n1. `VER-001`.\nProcedure:\n1. Run.\nExpected result:\n1. Pass.\nEvidence record:\n1. Record.\nStage or environment:\n1. Final.\n"""
    if errors := validate_commitment_spec_fixture(positive_spec):
        add_failure(check_id, f"positive spec fixture failed: {errors}")
    if errors := validate_commitment_plan_fixture(positive_plan):
        add_failure(check_id, f"positive plan fixture failed: {errors}")
    negative_specs = [
        positive_spec.replace(" Specification Commitment", ""),
        positive_spec.replace("Kind:", "Legacy kind:"),
        positive_spec.replace("1. `SPEC-001`.", "1. `SPEC-999`.", 1),
        positive_spec.replace("### `VER-002`", "#### `VER-002`"),
        positive_spec.replace("SPEC-002", "SPEC-001", 1),
        positive_spec.replace("1. `SPEC-001`.\nCriterion:", "1. `SPEC-002`.\nCriterion:", 1),
    ]
    if any(not validate_commitment_spec_fixture(fixture) for fixture in negative_specs):
        add_failure(check_id, "a declared negative spec fixture passed")
    negative_plans = [
        positive_plan.replace("## Commitment-Disposition Mapping", "## Spec Traceability"),
        positive_plan.replace("### `TASK-001` Implementation Task", "### `T-001`"),
        positive_plan.replace("Evidence record:\n1. Record.\n", ""),
        positive_plan.replace("| `SPEC-001` | Implement | `TASK-001` |\n", ""),
        positive_plan.replace("| `VER-001` | `CHECK-001` | Final |\n", ""),
        positive_plan.replace("`CHECK-001` | Final", "`CHECK-999` | Final"),
        positive_plan.replace("| `VER-001` | `CHECK-001` | Final |", "| `VER-001` | None | Final |"),
        positive_plan.replace("1. `VER-001`.\nProcedure:", "1. `VER-999`.\nProcedure:"),
        positive_plan.replace(
            "## Plan Checks",
            "### `TASK-001` Implementation Task — Duplicate\nDependencies:\n1. None.\nImplementation:\n1. Duplicate.\nExit criteria:\n1. Done.\n## Plan Checks",
        ),
    ]
    if any(not validate_commitment_plan_fixture(fixture) for fixture in negative_plans):
        add_failure(check_id, "a declared negative plan fixture passed")
    for path in CURRENT_SPEC_SCHEMA_PATHS:
        assert_path_exists(check_id, path)
        if join_repo_path(path).exists():
            for error in validate_commitment_spec_fixture(read_repo_text(path)):
                add_failure(check_id, f"{path}: {error}")
    for path in CURRENT_PLAN_SCHEMA_PATHS:
        assert_path_exists(check_id, path)
        if join_repo_path(path).exists():
            for error in validate_commitment_plan_fixture(read_repo_text(path)):
                add_failure(check_id, f"{path}: {error}")
    traceability_block = ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.020.common.traceability-approach-surfaces.md"
    task_block = ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.050.common.task-plan.md"
    for section in ["## Commitment-Disposition Mapping", "## Verification-Execution Mapping"]:
        assert_text_contains(check_id, traceability_block, re.escape(section), f"traceability block section {section}")
    for pattern, label in [
        (r"## Implementation Tasks", "implementation tasks section"),
        (r"### `TASK-001` Implementation Task", "full-name task heading"),
        (r"## Plan Checks", "plan checks section"),
        (r"### `CHECK-001` Plan Check", "full-name check heading"),
    ]:
        assert_text_contains(check_id, task_block, pattern, label)
    architecture_template = ".agents/skills/dev-doc-harness/assets/templates/architecture-snapshot.md"
    assert_text_contains(check_id, architecture_template, r"### `DEC-001` Architecture Decision —", "full-name Architecture Decision heading")
    assert_text_contains(check_id, architecture_template, r"Source spec sections:", "Architecture Decision source mapping")


def assert_current_historical_compatibility() -> None:
    check_id = "compat.current-historical"
    legacy_entity_heading = r"(?m)^#{2,4}\s+(?:`?(?:REQ|AC|T|V)-\d{3}`?|Requirements$|Acceptance Criteria$|Task Plan$|Validation Plan$)"
    for path in CURRENT_COMMITMENT_VOCABULARY_PATHS:
        if join_repo_path(path).exists():
            assert_text_not_contains(check_id, path, legacy_entity_heading, "legacy current entity heading")
    historical_paths = [
        "docs/work-items/2026-07-11_model-selection-dimensions/spec_model-selection-dimensions.md",
        "docs/work-items/2026-07-11_model-selection-dimensions/plan_model-selection-dimensions.md",
    ]
    historical_text = ""
    for path in historical_paths:
        assert_path_exists(check_id, path)
        if join_repo_path(path).exists():
            historical_text += read_repo_text(path)
    for entity_id in ["REQ-001", "AC-001", "T-001", "V-001"]:
        if entity_id not in historical_text:
            add_failure(check_id, f"historical fixture is missing {entity_id}")
    if validate_commitment_spec_fixture(historical_text) == [] or validate_commitment_plan_fixture(historical_text) == []:
        add_failure(check_id, "historical fixture was incorrectly accepted as current schema")


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
        {"path": ".agents/skills/dev-doc-harness/references/naming-conventions.md", "pattern": "rule:naming.work-item-paths", "label": "naming convention owner"},
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

    assert_template_assembly()
    write_check_result("templates.assembly")

    placeholder_targets = [
        "AGENTS.md",
        "README.md",
        ".agents/skills/dev-doc-harness/SKILL.md",
        ".agents/skills/dev-doc-harness/references/policy-architecture.md",
        ".agents/skills/dev-doc-harness/references/naming-conventions.md",
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
            {"path": ".agents/skills/dev-doc-harness/references/artifact-contract.md", "pattern": "<amendment-filename>", "label": "amendment path"},
            {"path": ".agents/skills/dev-doc-harness/references/naming-conventions.md", "pattern": "plan_amendment-NNN", "label": "amendment filename grammar"},
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
            {"path": "AGENTS.md", "pattern": "already exists and contains previous documentation packages", "label": "root continuity gate"},
            {"path": "README.md", "pattern": r"already exists and\s+contains previous documentation packages", "label": "README continuity gate"},
            {"path": ".agents/skills/dev-doc-harness/SKILL.md", "pattern": "already exists and contains previous documentation packages", "label": "router continuity gate"},
            {"path": ".agents/skills/dev-doc-harness/docs/operator-note.md", "pattern": "already exists and contains previous documentation packages", "label": "operator-note continuity gate"},
            {"path": ".agents/skills/dev-doc-harness/references/artifact-contract.md", "pattern": "Do not create or seed", "label": "canonical anti-bootstrap rule"},
            {"path": ".agents/skills/dev-doc-harness/references/artifact-contract.md", "pattern": "minimal pointer stubs", "label": "canonical pointer-only rule"},
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

    assert_changelog_fragment_contract()
    write_check_result("changelog.fragments")

    assert_work_item_architecture_decisions()
    write_check_result("architecture.decisions")

    assert_artifact_style_guidance()
    write_check_result("artifact-style.guidance")

    assert_plain_language_policy()
    write_check_result("plain-language.policy")

    assert_model_selection_dimensions()
    write_check_result("models.selection-dimensions")

    assert_execution_thread_start()
    write_check_result("execution.thread-start")

    assert_lifecycle_transition_targets()
    write_check_result("lifecycle.transition-targets")

    assert_commitment_verification_quality()
    write_check_result("quality.commitment-verification")

    assert_commitment_verification_templates()
    write_check_result("templates.commitment-verification")

    assert_current_historical_compatibility()
    write_check_result("compat.current-historical")


def main() -> int:
    run_checks()
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
