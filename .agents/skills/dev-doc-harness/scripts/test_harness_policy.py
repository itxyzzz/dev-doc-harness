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
CURRENT_DEVELOPMENT_MARKER = "0.9+"
RELEASE_NOTE_VERSIONS = ["0.4.0", "0.5.0", "0.6.0", "0.7.0", "0.8.0", "0.9.0"]
LATEST_RELEASE_NOTE_VERSION = RELEASE_NOTE_VERSIONS[-1]

CHECK_IDS = [
    "paths.required-files",
    "graph.references",
    "graph.owner-headings",
    "graph.template-routes",
    "router.required-routes",
    "router.route-budget",
    "router.maintenance-architecture",
    "release.route",
    "discoverability.safety",
    "skill.openai-metadata",
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
    "documentation.assessment",
    "architecture.decisions",
    "artifact-style.guidance",
    "plain-language.policy",
    "models.selection-dimensions",
    "execution.thread-start",
    "lifecycle.transition-targets",
    "quality.commitment-verification",
    "templates.commitment-verification",
    "compat.current-historical",
    "scenarios.harness-simplification",
    "compat.superpowers-adapter-contract",
    "execution.method-fallbacks",
    "clarity.planning-template-contract",
    "presentation.next-stage-summary",
]

CANONICAL_REFERENCES = [
    ".agents/skills/dev-doc-harness/references/maintenance-architecture.md",
    ".agents/skills/dev-doc-harness/references/naming-conventions.md",
    ".agents/skills/dev-doc-harness/references/artifact-contract.md",
    ".agents/skills/dev-doc-harness/references/implementation-changelog.md",
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

PLAIN_LANGUAGE_RULE_ID = "rule" + ":quality.plain-language"
PLAIN_LANGUAGE_PROMPT = (
    "Use `must` for binding Statements and `should` for advisory prose; "
    f"see `{PLAIN_LANGUAGE_RULE_ID}`."
)
PLAIN_LANGUAGE_FIXTURE_PATH = ".agents/skills/dev-doc-harness/scripts/fixtures/plain-language.md"
PLAIN_LANGUAGE_ACTIVE_MARKDOWN_PATHS = [
    "AGENTS.md",
    ".agents/skills/dev-doc-harness/SKILL.md",
    *CANONICAL_REFERENCES,
    *TEMPLATE_FILES,
]
OPERATIONAL_ROUTER_SURFACES = [
    "AGENTS.md",
    "README.md",
    ".agents/skills/dev-doc-harness/SKILL.md",
    ".agents/skills/dev-doc-harness/docs/operator-note.md",
    *CANONICAL_REFERENCES,
]

REQUIRED_FILES = [
    "AGENTS.md",
    "README.md",
    "CHANGELOG.md",
    ".agents/skills/dev-doc-harness/SKILL.md",
    ".agents/skills/dev-doc-harness/VERSION",
    ".agents/skills/dev-doc-harness/agents/openai.yaml",
    ".agents/skills/dev-doc-harness/scripts/test_harness_policy.py",
    ".agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py",
    ".agents/skills/dev-doc-harness/references/maintenance-architecture.md",
    ".agents/skills/dev-doc-harness/references/naming-conventions.md",
    ".agents/skills/dev-doc-harness/references/artifact-contract.md",
    ".agents/skills/dev-doc-harness/references/implementation-changelog.md",
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


def read_markdown_h2_section(path: str, heading: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(heading)}\s*$\n(?P<body>.*?)(?=^## |\Z)",
        read_repo_text(path),
    )
    return match.group("body") if match else ""


def assert_agents_bootstrap_contract() -> None:
    check_id = "discoverability.safety"
    path = "AGENTS.md"
    semantic_anchors = [
        (r"repository development[\s\S]+very small mechanical edits[\s\S]+\.agents/skills/dev-doc-harness/SKILL\.md", "harness activation"),
        (r"very small mechanical edits[\s\S]+(?:skip|without) durable artifacts[\s\S]+module:lifecycle", "very-small-mechanical exception"),
        (r"selects?[\s\S]+`economy-default`", "active repository model policy"),
        (r"Superpowers[\s\S]+methodology[\s\S]+(?:harness|Dev Doc Harness)[\s\S]+artifact(?:-| )location[\s\S]+lifecycle", "Superpowers/harness ownership"),
        (r"docs/work-items/<work-id>", "canonical work-item location"),
        (r"combined small/medium[\s\S]+spec[\s\S]+plan", "combined small/medium planning"),
        (r"docs/superpowers[\s\S]+only when[\s\S]+already exists[\s\S]+previous documentation packages", "guarded legacy compatibility route"),
        (r"fresh start authorization[\s\S]+planned method", "execution-start routing"),
        (r"operator[\s\S]+(?:method|model)[\s\S]+reasoning[\s\S]+next-stage continuity[\s\S]+without an amendment", "operator runtime overrides"),
        (r"only when[\s\S]+maintain, package, or release[\s\S]+Dev Doc Harness distribution[\s\S]+source repository", "source-repository-only distribution maintenance"),
        (r"Do not use[\s\S]+downstream[\s\S]+releases", "downstream release exclusion"),
    ]
    for pattern, label in semantic_anchors:
        assert_text_contains(check_id, path, pattern, label)

    word_count = len(read_repo_text(path).split())
    if word_count > 360:
        add_failure(check_id, f"AGENTS.md has {word_count} words; maximum is 360")


def assert_skill_openai_metadata() -> None:
    check_id = "skill.openai-metadata"
    path = ".agents/skills/dev-doc-harness/agents/openai.yaml"
    expected = {
        "display_name": "Dev Doc Harness",
        "short_description": "Plan and govern repository development work",
        "default_prompt": "Use $dev-doc-harness to guide this repository development task through the appropriate planning, execution, and validation lifecycle.",
    }

    if not join_repo_path(path).exists():
        add_failure(check_id, f"Missing path: {path}")
        return

    lines = read_repo_text(path).splitlines()
    if not lines or lines[0] != "interface:":
        add_failure(check_id, f"Missing top-level interface mapping in {path}")
        return

    actual: dict[str, str] = {}
    for line in lines[1:]:
        match = re.fullmatch(r'  ([a-z_]+): "([^"\r\n]*)"', line)
        if not match:
            add_failure(check_id, f"Unexpected metadata syntax or top-level field in {path}: {line!r}")
            continue
        key, value = match.groups()
        if key in actual:
            add_failure(check_id, f"Duplicate interface field in {path}: {key}")
        actual[key] = value

    if set(actual) != set(expected):
        missing = sorted(set(expected) - set(actual))
        extra = sorted(set(actual) - set(expected))
        if missing:
            add_failure(check_id, f"Missing interface fields in {path}: {', '.join(missing)}")
        if extra:
            add_failure(check_id, f"Unrequested interface fields in {path}: {', '.join(extra)}")

    for key, value in expected.items():
        if actual.get(key) != value:
            add_failure(check_id, f"Unexpected {key} value in {path}")

    short_description = actual.get("short_description", "")
    if not 25 <= len(short_description) <= 64:
        add_failure(check_id, "short_description must be 25-64 characters")
    if "$dev-doc-harness" not in actual.get("default_prompt", ""):
        add_failure(check_id, "default_prompt must reference $dev-doc-harness")


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
    return [
        match.group("heading").strip()
        for match in re.finditer(
            r"(?<!`)(?P<fence>`+)(?P<heading>#{2,6}\s+.*?)(?P=fence)(?!`)",
            owner_cell,
        )
    ]


def assert_owner_heading_parser_contract() -> None:
    expected = ["### Nested owner", "#### Deep owner", "#### `Run in` (next-stage continuity)"]
    actual = get_owner_table_heading_names(
        "`### Nested owner` and `#### Deep owner` and ``#### `Run in` (next-stage continuity)``"
    )
    if actual != expected:
        add_failure(
            "graph.owner-headings",
            f"Owner-heading parser did not preserve nested heading levels: expected {expected}, got {actual}",
        )


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
        headings = get_owner_table_heading_names(row.owner_cell)
        if not headings:
            add_failure(
                "graph.owner-headings",
                f"Owner cell for {row.rule_id} does not declare a backticked Markdown heading in {row.path}",
            )
        for heading in headings:
            if not re.search(rf"^{re.escape(heading)}\s*$", text, flags=re.MULTILINE):
                add_failure("graph.owner-headings", f"Owner heading '{heading}' for {row.rule_id} is missing in {row.path}")


def get_policy_references(path: str) -> list[str]:
    text = read_repo_text(path)
    line = next((line for line in re.split(r"\r?\n", text) if re.search(r"^Policy references:", line)), "")
    return get_concrete_ids(line) if line else []


def assert_template_routes() -> None:
    operation_requirements = {
        "small-medium": ["module:lifecycle", "module:naming", "module:quality", "module:models"],
        "large-anchor": ["module:lifecycle", "module:naming", "module:quality", "module:models", "module:artifact-style"],
        "phase-plan": ["module:lifecycle", "module:naming", "module:quality", "module:models"],
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

    for template in PLAN_TEMPLATE_FILES:
        references = get_policy_references(template)
        if "module:freeze-gate" in references:
            add_failure("graph.template-routes", f"Draft plan template retains deferred policy reference 'module:freeze-gate': {template}")
        deferred_freeze_prefix = "rule:" + "freeze."
        if any(reference.startswith(deferred_freeze_prefix) for reference in references):
            add_failure("graph.template-routes", f"Draft plan template retains deferred freeze rule: {template}")


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
        "Draft or review large anchor specs": 5,
        "Draft or review phase plans": 4,
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


def get_operation_router_owners(surface_texts: dict[str, str]) -> list[str]:
    heading = r"(?m)^## Operation router\s*$"
    return sorted(path for path, text in surface_texts.items() if re.search(heading, text))


def assert_router_maintenance_architecture() -> None:
    check_id = "router.maintenance-architecture"
    router = ".agents/skills/dev-doc-harness/SKILL.md"
    maintenance = ".agents/skills/dev-doc-harness/references/maintenance-architecture.md"
    former_reference = ".agents/skills/dev-doc-harness/references/policy-architecture.md"

    assert_path_absent(check_id, former_reference)
    router_owners = get_operation_router_owners({path: read_repo_text(path) for path in OPERATIONAL_ROUTER_SURFACES})
    if router_owners != [router]:
        add_failure(check_id, f"SKILL.md must be the sole operational-router surface; found: {', '.join(router_owners) or 'none'}")

    duplicate_router_fixture = {
        router: "## Operation router\n",
        "README.md": "## Operation router\n",
    }
    if get_operation_router_owners(duplicate_router_fixture) != [router, "README.md"]:
        add_failure(check_id, "duplicate operational-router fixture was not detected")

    assert_text_not_contains(check_id, maintenance, r"(?m)^## Router Inputs\s*$", "duplicate router inputs heading")
    assert_text_not_contains(
        check_id,
        maintenance,
        re.escape("docs/work-items/2026-06-05-refactor-as-code"),
        "work-item snapshot provenance",
    )
    assert_text_not_contains(check_id, maintenance, re.escape("Reusable policy source?"), "retired taxonomy column")
    for removed_type in ["Artifact schema", "Operator-facing summary", "Historical snapshot"]:
        assert_text_not_contains(check_id, maintenance, re.escape(removed_type), f"retired content type {removed_type}")
    for retained_type in ["Normative policy", "Advisory guidance", "Example"]:
        assert_text_contains(check_id, maintenance, re.escape(retained_type), f"retained content type {retained_type}")


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
        for block_path in join_repo_path(".agents/skills/dev-doc-harness/assets/templates/blocks").glob("plan.*.common.*.md")
        for _, paragraph in get_normalized_paragraphs(to_repo_relative_path(block_path))
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
        ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.small.handoff.md",
        ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.phase.handoff.md",
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

    for template in PLAN_TEMPLATE_FILES:
        text = read_repo_text(template)
        for pattern, label in [
            (r"## Traceability approach", "traceability section"),
            (r"Use local links", "local-link default"),
            (r"Add a mapping only when", "benefit-based mapping"),
            (r"## Implementation tasks", "task section"),
            (r"### `TASK-001` `<short imperative title>`", "concise task heading"),
            (r"#### `CHECK-001` `<short title>`", "nested check heading"),
        ]:
            assert_text_contains(check_id, template, pattern, label)

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

    # Release-note files are frozen historical artifacts. They may retain source
    # headings for planning-only entries intentionally removed from the compact
    # root changelog; Git preserves the original source record.


def get_changelog_sections() -> list[ChangelogSection]:
    text = read_repo_text("CHANGELOG.md")
    return [
        ChangelogSection(match.group("heading").strip(), match.group("body"))
        for match in re.finditer(
            r"^###?\s+(?P<heading>2026-[^\r\n]+)\r?\n(?P<body>.*?)(?=^###?\s+|\Z)",
            text,
            flags=re.MULTILINE | re.DOTALL,
        )
        if re.search(r"^Meta --\s+`", match.group("body"), flags=re.MULTILINE)
    ]


def assert_release_changelog_schema() -> None:
    check_id = "release.changelog-schema"
    sections = get_changelog_sections()
    if not sections:
        add_failure(check_id, "No current release-versioning changelog entries found")
        return

    for section in sections:
        meta_lines = list(re.finditer(r"^Meta --\s+`([^`]+)`\s*:\s*`([^`]+)`\s*$", section.body, flags=re.MULTILINE))

        if len(meta_lines) != 1:
            add_failure(check_id, f"{section.heading} must contain exactly one compact Meta field")
            continue

        release_target, package_impact = meta_lines[0].groups()
        if not re.search(r"^(?:unreleased|0\.\d+\.\d+|0\.\d+\+)$", release_target):
            add_failure(check_id, f"{section.heading} has invalid Meta release target '{release_target}'")
        if package_impact not in ("distributable", "repository-only"):
            add_failure(check_id, f"{section.heading} has invalid Meta package impact '{package_impact}'")

    changelog = read_repo_text("CHANGELOG.md")
    if re.search(r"^Package impact:\s+`planning-only`\s*$", changelog, flags=re.MULTILINE):
        add_failure(check_id, "CHANGELOG.md must not retain planning-only entries")
    for legacy_field in ["Release target:", "Package impact:", "Release-note:"]:
        if legacy_field in changelog:
            add_failure(check_id, f"CHANGELOG.md must not retain legacy metadata field '{legacy_field}'")


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
    changelog_reference = ".agents/skills/dev-doc-harness/references/implementation-changelog.md"
    freeze = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"
    naming = ".agents/skills/dev-doc-harness/references/naming-conventions.md"
    release_policy = ".agents/skills/dev-doc-harness/references/release-policy.md"
    release_process = ".agents/skills/dev-doc-harness/docs/release-branch-process.md"
    operator_docs = ["README.md", ".agents/skills/dev-doc-harness/docs/operator-note.md"]
    hook = ".githooks/pre-commit"

    assert_text_contains(check_id, changelog_reference, r"docs/work-items/<work-id>/changelog/\*\.md", "implementation fragment location")
    assert_text_contains(check_id, changelog_reference, r"implementation-fragment\.md", "ordinary implementation fragment filename")
    assert_text_contains(check_id, changelog_reference, r"phase-NN-fragment\.md", "phase implementation fragment filename")
    assert_text_contains(check_id, changelog_reference, r"### `<date> <commit-subject>`", "fragment heading grammar")
    assert_text_contains(check_id, changelog_reference, r"The heading must be synchronized to its implementation commit subject", "fragment heading synchronization")
    assert_text_contains(check_id, changelog_reference, r"matching planned commit row and fragment heading", "commit synchronization")
    assert_text_contains(check_id, changelog_reference, r"Keep a Changelog", "changelog body convention")
    assert_text_contains(check_id, changelog_reference, r"## Compatibility and legacy support", "legacy guidance section")
    guidance_text = read_repo_text(changelog_reference)
    if guidance_text.find("## Compatibility and legacy support") < guidance_text.find("## Consolidation"):
        add_failure(check_id, "legacy guidance section must follow routine consolidation guidance")
    assert_text_contains(check_id, changelog_reference, r"Root `CHANGELOG\.md` is the curated release source", "root changelog publication view")
    assert_text_not_contains(check_id, freeze, r"changelog source fragment", "freeze planning fragment")
    assert_text_not_contains(check_id, lifecycle, r"^## Changelog$", "retired lifecycle changelog section")
    assert_text_not_contains(check_id, lifecycle, r"docs/work-items/<work-id>/changelog/", "lifecycle fragment path leak")
    assert_text_not_contains(check_id, lifecycle, r"implementation-fragment\.md", "lifecycle ordinary fragment filename leak")
    assert_text_not_contains(check_id, lifecycle, r"phase-(?:NN|01)-fragment\.md", "lifecycle phase fragment filename leak")
    assert_text_not_contains(check_id, naming, r"changelog-fragment-path", "retired fragment path derived pattern")
    assert_text_not_contains(check_id, naming, r"## Changelog entries", "retired changelog-entry section")
    assert_text_contains(check_id, release_policy, r"Dev Doc Harness distribution release", "harness distribution release scope")
    assert_text_contains(check_id, release_policy, r"after fragment consolidation", "root source after consolidation")
    assert_text_contains(check_id, release_process, r"consolidate_changelog_fragments\.py --check", "release process consolidation check")
    assert_text_contains(check_id, release_process, r"consolidate_changelog_fragments\.py --lint", "release process lint")
    assert_text_contains(check_id, release_process, r"before renaming `## Unreleased`", "release process ordering")
    assert_text_contains(check_id, changelog_reference, r"newest-first", "implementation fragment ordering")
    assert_text_contains(check_id, hook, r"set -eu", "hook strict shell mode")
    assert_text_contains(check_id, hook, r"consolidate_changelog_fragments\.py --lint", "implementation fragment lint gate")
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
        assert_text_contains(check_id, path, r"module:implementation-changelog", f"{path} implementation-stage handoff")
        assert_text_contains(check_id, path, r"consolidate_changelog_fragments\.py", f"{path} consolidation command")

    for template in [
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
    ]:
        assert_text_not_contains(check_id, template, r"changelog", f"{template} changelog procedure leak")
    for template in PLAN_TEMPLATE_FILES:
        handoffs = len(re.findall(r"Before an implementation commit, follow `module:implementation-changelog`", read_repo_text(template)))
        if handoffs != 1:
            add_failure(check_id, f"{template} must contain exactly one concise implementation-changelog handoff; found {handoffs}")

    for path in [lifecycle, freeze, ".agents/skills/dev-doc-harness/assets/templates/plan-amendment.md"]:
        assert_text_not_contains(check_id, path, r"matching changelog", f"{path} changelog synchronization leak")

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
        valid_fragment = repo_root / "docs/work-items/2027-01-02_example/changelog/implementation-fragment.md"
        valid_entry = (
            "### 2027-01-02_example -- add newer fixture entry\n\n"
            "Meta -- `unreleased` : `repository-only`\n\n"
            "#### Added\n\n"
            "- Added a newer fixture entry.\n\n"
            "### 2027-01-02_example -- add fixture entry\n\n"
            "Meta -- `unreleased` : `repository-only`\n\n"
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

    with tempfile.TemporaryDirectory() as temp_dir:
        repo_root = Path(temp_dir)
        changelog = repo_root / "CHANGELOG.md"
        write_fixture_file(
            changelog,
            "# Changelog\n\n## Unreleased\n\n"
            "### 2026-07-01 legacy delivery\n\n"
            "Release target: `unreleased`\nPackage impact: `repository-only`\nRelease-note: `source-only`\n\n"
            "#### Changed\n\n- Keep delivered work.\n\n"
            "### 2026-07-01 legacy plan\n\n"
            "Release target: `unreleased`\nPackage impact: `planning-only`\nRelease-note: `source-only`\n\n"
            "#### Added\n\n- Remove this planning record.\n",
        )
        first_migration = run_consolidation_fixture(["--migrate-root"], repo_root)
        if first_migration.returncode != 0:
            add_failure(check_id, f"root migration fixture failed: {(first_migration.stdout + first_migration.stderr).strip()}")
        migrated_once = changelog.read_bytes()
        if b"planning-only" in migrated_once or b"Release-note:" in migrated_once or b"Meta -- `unreleased` : `repository-only`" not in migrated_once:
            add_failure(check_id, "root migration should remove planning-only legacy entries and compact remaining metadata")
        second_migration = run_consolidation_fixture(["--migrate-root"], repo_root)
        if second_migration.returncode != 0 or changelog.read_bytes() != migrated_once:
            add_failure(check_id, "a second root migration should be byte-for-byte idempotent")

    with tempfile.TemporaryDirectory() as temp_dir:
        repo_root = Path(temp_dir)
        changelog = repo_root / "CHANGELOG.md"
        write_fixture_file(
            changelog,
            "# Changelog\n\n## Unreleased\n\n"
            "### 2026-07-02 later delivery\n\n"
            "Meta -- `unreleased` : `repository-only`\n\n"
            "#### Changed\n\n- Preserve later body.\n"
            "### 2026-07-01 earlier delivery\n\n"
            "Meta -- `unreleased` : `repository-only`\n\n"
            "#### Changed\n\n- Preserve earlier body.\n\n"
            "## 0.7.0 - 2026-07-01\n\n"
            "### 2026-07-01 released delivery\n\n"
            "Meta -- `0.7.0` : `distributable`\n\n"
            "#### Changed\n\n- Preserve release body.\n",
        )
        first_spacing_migration = run_consolidation_fixture(["--migrate-root"], repo_root)
        spaced_once = changelog.read_bytes()
        migrated_spacing = changelog.read_text(encoding="utf-8")
        if first_spacing_migration.returncode != 0 or "Preserve later body.\n\n### 2026-07-01 earlier delivery" not in migrated_spacing:
            add_failure(check_id, "root migration should leave one blank line between consecutive entry headings")
        if "## 0.7.0 - 2026-07-01" not in migrated_spacing or "Preserve release body." not in migrated_spacing:
            add_failure(check_id, "root migration should preserve release headings and bodies while normalizing spacing")
        second_spacing_migration = run_consolidation_fixture(["--migrate-root"], repo_root)
        if second_spacing_migration.returncode != 0 or changelog.read_bytes() != spaced_once:
            add_failure(check_id, "root spacing normalization should be byte-for-byte idempotent")

    with tempfile.TemporaryDirectory() as temp_dir:
        repo_root = Path(temp_dir)
        changelog = repo_root / "CHANGELOG.md"
        write_fixture_file(
            changelog,
            "# Changelog\n\n## Unreleased\n\n"
            "### 2026-07-01 legacy plan\n\n"
            "Release target: `unreleased`\nPackage impact: `planning-only`\nRelease-note: `source-only`\n\n"
            "#### Added\n\n- Remove this planning record.\n\n"
            "## 0.7.0 - 2026-07-01\n\n"
            "### 2026-07-01 legacy delivery\n\n"
            "Release target: `0.7.0`\nPackage impact: `distributable`\nRelease-note: `include`\n\n"
            "#### Changed\n\n- Preserve this release section.\n",
        )
        release_migration = run_consolidation_fixture(["--migrate-root"], repo_root)
        migrated_release = changelog.read_text(encoding="utf-8")
        if release_migration.returncode != 0 or "## 0.7.0 - 2026-07-01" not in migrated_release:
            add_failure(check_id, "root migration must preserve conventional release headings adjacent to removed planning-only entries")

    with tempfile.TemporaryDirectory() as temp_dir:
        repo_root = Path(temp_dir)
        write_fixture_file(repo_root / "CHANGELOG.md", "# Changelog\n\n## Unreleased\n")
        write_fixture_file(
            repo_root / "docs/work-items/2026-07-01_legacy/changelog/planning-approval.md",
            "### 2026-07-01 legacy plan\n\n"
            "Release target: `unreleased`\nPackage impact: `planning-only`\nRelease-note: `source-only`\n\n"
            "#### Added\n\n- Frozen planning record.\n",
        )
        legacy_lint = run_consolidation_fixture(["--lint"], repo_root)
        legacy_check = run_consolidation_fixture(["--check"], repo_root)
        if legacy_lint.returncode != 0 or legacy_check.returncode != 0:
            add_failure(check_id, "legacy planning-only fragments should lint but never require root consolidation")

    with tempfile.TemporaryDirectory() as temp_dir:
        repo_root = Path(temp_dir)
        write_fixture_file(repo_root / "CHANGELOG.md", "# Changelog\n\n## Unreleased\n")
        write_fixture_file(
            repo_root / "docs/work-items/2026-08-01_mixed/changelog/implementation-fragment.md",
            "### 2026-08-01 mixed metadata\n\n"
            "Meta -- `unreleased` : `repository-only`\n"
            "Release target: `unreleased`\nPackage impact: `repository-only`\nRelease-note: `source-only`\n\n"
            "#### Changed\n\n- Invalid mixed metadata.\n",
        )
        mixed_result = run_consolidation_fixture(["--lint"], repo_root)
        if mixed_result.returncode == 0 or "mixed compact and legacy metadata" not in (mixed_result.stdout + mixed_result.stderr):
            add_failure(check_id, "mixed compact and legacy fragment metadata must fail lint")


def assert_documentation_assessment_contract() -> None:
    check_id = "documentation.assessment"
    lifecycle = ".agents/skills/dev-doc-harness/references/artifact-contract.md"
    shared_block = ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.080.common.documentation-assessment.md"
    small_header = ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.010.small.header.md"
    large_header = ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.010.large.header.md"
    small_readiness = ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.090.small.readiness-approval.md"
    large_readiness = ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.090.large.readiness-approval.md"
    phase_tasks = ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.080.phase.documentation-tasks.md"
    expected_ids = [
        "DOC-TEST-CASE",
        "DOC-TEST-GUIDE",
        "DOC-OPS-GUIDE",
        "DOC-API-GUIDE",
        "DOC-ARCH-SUMMARY",
    ]

    assert_text_contains(check_id, lifecycle, r"rule:lifecycle.documentation-assessment", "assessment rule owner")
    assert_text_contains(check_id, lifecycle, r"## Documentation assessment", "assessment policy heading")
    retired_matrix = "Documentation artifact" + r"\s+" + "matrix"
    assert_text_not_contains(check_id, lifecycle, retired_matrix, "retired assessment matrix")
    lifecycle_text = read_repo_text(lifecycle)
    lifecycle_ids = re.findall(r"`(DOC-[A-Z-]+)`", lifecycle_text)
    if lifecycle_ids != expected_ids:
        add_failure(check_id, f"lifecycle assessment IDs must appear once in order; found {lifecycle_ids}")
    for status in ["Not required", "Required", "Deferred"]:
        assert_text_contains(check_id, lifecycle, re.escape(status), f"assessment status {status}")
    assert_text_contains(check_id, lifecycle, r"no changelog entry and no architecture-snapshot entry", "assessment exclusions")

    assert_text_contains(check_id, shared_block, r"## Documentation assessment", "shared assessment heading")
    block_text = read_repo_text(shared_block)
    block_ids = re.findall(r"^- `(DOC-[A-Z-]+)`:", block_text, flags=re.MULTILINE)
    if block_ids != expected_ids:
        add_failure(check_id, f"shared assessment bullets must appear once in order; found {block_ids}")
    for phrase, label in [
        ("Required — <output path>; Plan Task: TASK-NNN", "required output and task shape"),
        ("Deferred — owner: <owner>; resolution point: <event>", "deferred owner and resolution shape"),
    ]:
        if block_text.count(phrase) != 1:
            add_failure(check_id, f"shared assessment must define one {label}")
    if block_text.count("<status>") != len(expected_ids):
        add_failure(check_id, f"shared assessment must render {len(expected_ids)} status placeholders")
    assert_text_not_contains(check_id, shared_block, r"changelog", "shared assessment changelog row")
    assert_text_not_contains(check_id, shared_block, r"Architecture snapshot", "shared assessment architecture row")

    for path in [small_header, large_header]:
        assert_text_contains(check_id, path, r"rule:lifecycle.documentation-assessment", f"{path} assessment reference")
    for path in [small_readiness, large_readiness]:
        assert_text_contains(check_id, path, r"Documentation assessment covers every required decision", f"{path} generic assessment readiness")
        assert_text_not_contains(check_id, path, r"DOC-", f"{path} duplicated assessment IDs")
    assert_text_contains(check_id, phase_tasks, r"Consume the approved documentation assessment", "phase assessment handoff")
    assert_text_not_contains(check_id, phase_tasks, r"DOC-", "phase duplicated assessment IDs")
    assert_text_not_contains(check_id, phase_tasks, r"changelog", "phase changelog procedure")

    for path in [
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
    ]:
        assert_text_contains(check_id, path, r"## Documentation assessment", f"{path} assembled assessment")
        assert_text_not_contains(check_id, path, retired_matrix, f"{path} retired matrix")


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
        assert_text_contains(
            check_id,
            path,
            r"ARCHITECTURE\.md.+(?:future work|not covered by (?:the )?harness)",
            "operator durable architecture boundary",
        )

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
    architecture = ".agents/skills/dev-doc-harness/references/maintenance-architecture.md"
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
    assert_text_not_contains(check_id, role_examples, r"standard-review", "non-canonical model policy")

    for path in template_paths:
        assert_text_contains(check_id, path, r"final artifact|Final artifact|Superseded by: None|DEC-001|AMD-001|VAR-001", "template final-state or trace cue")

    for path in [
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
    ]:
        assert_text_contains(
            check_id,
            path,
            r"required decision|unresolved required decisions|unresolved implementation decision|No unresolved placeholders, plan-affecting decisions, missing sections, or ownerless deferrals remain\.",
            "readiness unresolved-decision check",
        )

    assert_text_contains(check_id, ".agents/skills/dev-doc-harness/assets/templates/architecture-snapshot.md", r"DEC-001", "architecture decision ID")
    assert_text_contains(check_id, ".agents/skills/dev-doc-harness/assets/templates/plan-amendment.md", r"AMD-001", "amendment ID")
    assert_text_contains(check_id, ".agents/skills/dev-doc-harness/assets/templates/variance-log.md", r"VAR-001", "variance ID")


def assert_plain_language_policy() -> None:
    check_id = "plain-language.policy"
    quality = ".agents/skills/dev-doc-harness/references/durable-planning-quality.md"
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

    assert_text_contains(check_id, quality, re.escape(PLAIN_LANGUAGE_RULE_ID), "plain-language rule owner")
    assert_text_contains(check_id, quality, r"must.+binding.+should.+guidance", "canonical must/should rule")
    route_line = next(
        (
            line
            for line in read_repo_text(router).splitlines()
            if line.startswith("| Draft or review small/medium specs and plans |")
        ),
        "",
    )
    route_cells = [cell.strip() for cell in route_line.split("|")[1:-1]]
    required_route = route_cells[1] if len(route_cells) > 1 else ""
    optional_route = route_cells[2] if len(route_cells) > 2 else ""
    if "module:artifact-style" in required_route:
        add_failure(check_id, "routine small/medium route requires module:artifact-style")
    if not re.search(r"module:artifact-style.+large or hard to scan", optional_route, flags=re.IGNORECASE):
        add_failure(check_id, "routine small/medium route lacks conditional artifact-style loading")
    for path in prompt_paths:
        assert_text_contains(check_id, path, re.escape(PLAIN_LANGUAGE_PROMPT), "plain-language prompt")
    for path in small_medium_source_blocks:
        policy_references = get_policy_references(path)
        if "module:artifact-style" in policy_references:
            add_failure(check_id, f"{path} requires module:artifact-style in policy references")
        assert_text_contains(check_id, path, r"module:quality", "quality readability route")
        assert_text_contains(check_id, path, r"large or hard to scan", "conditional artifact-style cue")

    if not find_unapproved_plain_language_modals("AGENTS.md", "A current authoring rule shall fail."):
        add_failure(check_id, "synthetic active-surface occurrence did not fail")
    for path, text in [
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

    model_selection = read_markdown_h2_section(models, "Model selection")
    for facet in ["Generation", "Capability tier", "Reasoning effort"]:
        if facet not in model_selection:
            add_failure(check_id, f"Model selection does not define the '{facet}' facet")
    assert_text_contains(
        check_id,
        models,
        r"Resolved profile.+concrete runtime mapping.+(?:three|Generation.+Capability tier.+Reasoning effort).+(?:not|isn't|is not).+(?:fourth|facet)",
        "resolved profile is an optional runtime mapping rather than a fourth facet",
    )

    current_diagnostics = read_markdown_h2_section(models, "Current-session diagnostics")
    for field in ["Resolved model profile", "Context visibility"]:
        if field not in current_diagnostics:
            add_failure(check_id, f"Current-session diagnostics omit '{field}'")
    for duplicated_field in ["Generation:", "Capability tier:", "Reasoning effort:", "Orchestration mode:"]:
        if duplicated_field in current_diagnostics:
            add_failure(check_id, f"Current-session diagnostics duplicate next-stage field '{duplicated_field}'")
    if not re.search(r"omit unless.+exposed and material", current_diagnostics, flags=re.IGNORECASE):
        add_failure(check_id, "Current-session diagnostics do not use the exposed-and-material omission rule")

    for rule_id in [
        "rule:models.selection-dimensions",
        "rule:models.orchestration-mode",
        "rule:models.next-stage-continuity",
    ]:
        assert_text_contains(check_id, models, re.escape(rule_id), f"{rule_id} owner")

    for label in [
        "Generation",
        "Capability tier",
        "Reasoning effort",
        "Orchestration mode",
        "Resolved profile",
        "Availability/fallback",
        "Next-stage continuity",
        "Context visibility",
        "Run in",
    ]:
        assert_text_contains(check_id, models, re.escape(label), f"selection field '{label}'")

    for tier in ["flagship", "balanced", "fast/economy"]:
        assert_text_contains(check_id, models, re.escape(tier), f"vendor-neutral tier '{tier}'")
    for mapping in ["GPT-5.6", "Sol", "Terra", "Luna"]:
        assert_text_contains(check_id, models, re.escape(mapping), f"current provider mapping '{mapping}'")

    assert_text_contains(check_id, models, r"[Uu]ltra.+platform[- ]managed.+multi-agent|platform[- ]managed.+multi-agent.+[Uu]ltra", "ultra orchestration classification")
    assert_text_contains(check_id, models, r"does not (?:automatically )?provide.+task partitioning", "platform orchestration limitation")
    assert_text_contains(check_id, models, r"enterprise-default.+(?:assess|consider).+(?:platform multi-agent|ultra)", "enterprise platform-orchestration assessment")
    assert_text_contains(check_id, models, r"economy-default.+balanced/medium.+Terra medium or equivalent", "economy baseline policy")

    assert_text_contains(
        check_id,
        models,
        r"balanced/medium.+Terra medium or equivalent.+suggested baseline.+substantial bounded work.+explicit outputs and validation",
        "calibrated balanced/medium bounded-work baseline",
    )
    assert_text_contains(check_id, models, r"balanced/high.+Terra high or equivalent.+effort escalation", "effort escalation classification")
    assert_text_contains(check_id, models, r"flagship/medium.+Sol medium or equivalent.+tier escalation", "tier escalation classification")
    assert_text_contains(check_id, models, r"flagship/high.+Sol high or equivalent.+exceptional.+written reason", "exceptional flagship/high escalation")
    assert_text_contains(check_id, models, r"residual uncertainty|new variance", "late escalation justification")
    assert_text_contains(check_id, models, r"de-escalat.+bounded", "bounded-work de-escalation")
    assert_text_contains(
        check_id,
        models,
        r"missing product input.+undecided requirement.+plan contradiction.+(?:variance|approval)",
        "missing-decision approval boundary",
    )

    assert_text_contains(check_id, models, r"rule:lifecycle.stage-boundaries", "lifecycle-owned stage boundary")
    assert_text_contains(check_id, models, r"planning method.+planning-review|planning-review.+planning method", "planning-stage method and review")
    assert_text_contains(check_id, models, r"execution method.+Plan Task.+final review|Plan Task.+final review.+execution method", "execution-stage method and review")
    assert_text_contains(check_id, models, r"spec drafting", "pre-spec assessment boundary")
    assert_text_contains(check_id, models, r"future work", "pre-spec mechanism future-work boundary")

    for path in [models, role_examples]:
        assert_text_contains(check_id, path, r"independent sub-agent reviewer.+default", "independent sub-agent reviewer default")
        assert_text_contains(check_id, path, r"curated artifacts", "independent reviewer context")
        assert_text_contains(check_id, path, r"separate task or thread.+operator-managed fallback", "manual review-isolation fallback")
        assert_text_contains(check_id, path, r"(?:one|single) named lens", "independent reviewer lens")
        assert_text_contains(check_id, path, r"evidence-backed", "evidence-backed finding requirement")
        assert_text_contains(check_id, path, r"severity", "evidence-backed finding severity")
        assert_text_contains(check_id, path, r"reproduction or validation path", "finding validation path")
        assert_text_contains(check_id, path, r"orchestration session.+(?:owns|retains).+integration", "orchestration-owned integration")

    assert_text_contains(check_id, models, r"plan's normal post-freeze", "approved strategy starts with plan authorization")
    assert_text_contains(check_id, models, r"outside that strategy", "out-of-strategy confirmation boundary")
    assert_text_contains(check_id, models, r"Platform rules may still require", "platform permission boundary")
    assert_text_contains(check_id, models, r"availability fallback", "approved fallback behavior")
    assert_text_contains(check_id, models, r"de-facto orchestration mode", "de-facto orchestration reporting")
    assert_text_contains(check_id, models, r"unplanned sub-agent.+stronger tier or effort.+broader write authority", "unplanned orchestration confirmation")
    assert_text_contains(
        check_id,
        models,
        r"tightly coupled.+same-file.+write-capable.+(?:do not|does not).+read-only reviewer",
        "read-only reviewer remains suitable for tightly coupled work",
    )
    assert_text_contains(
        check_id,
        models,
        r"high-blast-radius.+independent reviewer",
        "independent high-blast-radius final review",
    )
    assert_text_contains(
        check_id,
        models,
        r"orchestration session.+(?:not|isn't|is not).+independent review",
        "final integration is distinct from independent review",
    )

    strategy_templates = [
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
    ]
    for path in strategy_templates:
        for label in ["Current orchestration session", "Next-stage recommendation", "Method", "Orchestration mode", "Run in", "Review", "Generation", "Capability tier", "Reasoning"]:
            assert_text_contains(check_id, path, re.escape(label), f"template selection field '{label}'")
        assert_text_not_contains(check_id, path, r"Model class/profile:", "conflated per-role model class/profile field")

    large_strategy_source = ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.060.large.phase-decomposition-model.md"
    for path in [large_strategy_source]:
        assert_text_contains(check_id, path, r"Current orchestration session", "planning observations prompt")
        assert_text_contains(check_id, path, r"Next-stage recommendation", "next-stage selection prompt")
        assert_text_contains(check_id, path, r"upcoming-stage sub-agent assessment", "upcoming-stage assessment prompt")
        assert_text_contains(check_id, path, r"module:models", "strategy prompt canonical-policy route")

    plan_strategy_source = ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.055.common.model-strategy.md"
    assert_text_contains(check_id, plan_strategy_source, r"upcoming-stage sub-agent assessment", "plan sub-agent assessment prompt")
    for path in [plan_strategy_source, large_strategy_source]:
        assert_text_contains(check_id, path, r"Write authority", "sub-agent write-authority prompt")
        assert_text_contains(check_id, path, r"Concurrency", "sub-agent concurrency prompt")
    assert_text_not_contains(check_id, plan_strategy_source, r"Current planning Codex task", "duplicated plan current-task prompt")
    assert_text_not_contains(check_id, plan_strategy_source, r"Next-stage recommendation", "duplicated plan next-stage prompt")
    assert_text_contains(check_id, models, r"header metadata.+final handoff.+shared strategy", "plan-state placement guidance")
    for path in [
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
    ]:
        assert_text_contains(
            check_id,
            path,
            r"## Implementation tasks[\s\S]*## Model and Sub-agent Strategy[\s\S]*## Planned commits",
            "strategy appears after tasks and before planned commits",
        )

    assert_text_not_contains(check_id, models, r"\| Model class/profile \|", "conflated canonical example column")

    for path in [role_examples]:
        assert_text_contains(check_id, path, r"Capability tier", "capability-tier guidance")
        assert_text_contains(check_id, path, r"Orchestration mode", "orchestration-mode guidance")
        assert_text_contains(check_id, path, r"ultra", "ultra guidance")

    assert_normalized_text_contains(
        check_id,
        readme,
        "Model (generation, capability tier, and reasoning)",
        "plain-language model guidance",
    )
    assert_text_contains(
        check_id,
        readme,
        r"Orchestration \(Method, Orchestration mode, `Run in` the same orchestration session or a new one, and stage-appropriate Review\)",
        "plain-language orchestration guidance",
    )
    assert_normalized_text_contains(
        check_id,
        readme,
        "Orchestration mode",
        "plain-language orchestration-mode field",
    )
    assert_text_contains(check_id, readme, r"host-native execution", "host-portable execution fallback")
    assert_text_contains(check_id, readme, r"ultra", "ultra guidance")
    assert_text_contains(check_id, role_examples, r"execution-thread-start", "execution startup route")
    assert_normalized_text_contains(
        check_id,
        readme,
        "same-session switch rehydrates the frozen package before editing",
        "next-stage continuity guidance",
    )


def assert_execution_thread_start() -> None:
    check_id = "execution.thread-start"
    models = ".agents/skills/dev-doc-harness/references/subagent-model-policy.md"
    execution = ".agents/skills/dev-doc-harness/references/context-and-quality-gates.md"
    freeze = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"
    architecture = ".agents/skills/dev-doc-harness/references/maintenance-architecture.md"
    router = ".agents/skills/dev-doc-harness/SKILL.md"

    assert_text_contains(check_id, execution, re.escape("rule:execution-quality.execution-thread-start"), "execution-thread-start owner")
    assert_text_contains(check_id, execution, re.escape("rule:freeze.stop-before-implementation"), "post-freeze authorization owner")
    assert_text_contains(check_id, execution, re.escape("rule:models.selection-dimensions"), "runtime selection owner")
    assert_text_contains(check_id, execution, re.escape("rule:models.next-stage-continuity"), "next-stage continuity owner")
    assert_text_contains(check_id, execution, r"applicable instructions.+frozen artifacts", "instruction and artifact load order")
    assert_text_contains(check_id, execution, r"branch.+worktree.+approval state.+amendments.+variance.+(?:baseline|validation baseline)", "working-state and baseline verification")
    assert_text_contains(check_id, execution, r"avoid.+rediscover", "rediscovery avoidance")
    assert_text_contains(check_id, execution, r"documented next lifecycle stage", "named lifecycle stage")
    assert_text_contains(check_id, execution, r"variance", "variance stop route")

    assert_text_contains(check_id, models, r"new orchestration session", "new-session transition preference")
    assert_text_contains(check_id, models, r"numeric context thresholds.+remaining-context estimates.+predict compaction", "no unexposed context estimate")
    assert_text_contains(check_id, models, r"same-session route rereads the frozen package", "same-session artifact rehydration")

    small_plan = ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md"
    phase_plan = ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md"
    assert_text_contains(check_id, small_plan, r"## Implementation handoff", "small-plan handoff section")
    assert_text_contains(check_id, small_plan, r"Next lifecycle stage[\s\S]*Stage:[\s\S]*Frozen package", "small-plan compact handoff inputs")
    assert_text_contains(check_id, small_plan, re.escape("rule:execution-quality.execution-thread-start"), "small-plan startup rule reference")
    assert_text_contains(check_id, phase_plan, r"## Phase implementation handoff", "phase implementation handoff section")
    assert_text_contains(check_id, phase_plan, r"Phase execution startup", "phase execution startup")
    assert_text_contains(check_id, phase_plan, r"## Phase completion report", "phase completion report")
    assert_text_contains(check_id, phase_plan, re.escape("rule:execution-quality.execution-thread-start"), "phase startup rule reference")
    assert_text_not_contains(check_id, phase_plan, r"Post-phase transition", "retired post-phase transition")

    for label in ["Method", "Run in", "Review", "Generation", "Capability tier", "Reasoning", "Execution requirements and contingencies"]:
        assert_text_contains(check_id, freeze, re.escape(label), f"freeze confirmation '{label}'")
    assert_text_contains(check_id, freeze, re.escape("rule:execution-quality.execution-thread-start"), "consumer-side startup protocol")
    assert_text_contains(check_id, architecture, r"execution-thread-start", "architecture owner route")
    assert_text_contains(check_id, router, r"execution-thread-start", "router discoverability")


def assert_lifecycle_transition_targets() -> None:
    check_id = "lifecycle.transition-targets"
    lifecycle = ".agents/skills/dev-doc-harness/references/artifact-contract.md"
    freeze = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"
    models = ".agents/skills/dev-doc-harness/references/subagent-model-policy.md"

    assert_text_contains(check_id, lifecycle, re.escape("rule" + ":lifecycle.planning-shape"), "planning-shape rule owner")
    assert_text_contains(check_id, lifecycle, r"## Lifecycle stage boundaries", "lifecycle-stage owner heading")
    assert_text_contains(check_id, lifecycle, r"Work item folders[\s\S]+Lifecycle stage boundaries", "lifecycle stage boundaries follow work-item folders")
    assert_text_contains(check_id, lifecycle, r"small/medium.+spec and plan.+(?:together|combined)", "combined small/medium default")
    assert_text_contains(check_id, lifecycle, r"spec-only freeze.+explicit.+(?:reason|exception)", "staged small/medium exception")
    for stage, label in [
        ("plan drafting", "staged small/medium route"),
        ("plan execution", "combined small/medium route"),
        ("phase-plan drafting", "large-anchor route"),
        ("phase execution", "phase-plan route"),
        ("documented resumed stage", "amendment resumption route"),
    ]:
        assert_text_contains(check_id, lifecycle, re.escape(stage), label)

    for label in ["Planning shape", "Frozen package", "Next lifecycle stage"]:
        assert_text_contains(check_id, freeze, re.escape(label), f"freeze field '{label}'")
    assert_text_contains(check_id, freeze, r"explicit.+approval.+creat.+task|approval.+specifically.+creat.+task", "task-creation approval")
    assert_text_contains(check_id, freeze, r"exact supported.+(?:model|configuration)|supported.+recorded.+settings", "exact supported configuration")
    assert_text_contains(check_id, freeze, r"manual.+copy-ready handoff|copy-ready handoff.+manual", "visible manual fallback")
    assert_text_contains(check_id, freeze, r"(?:do not|without).+silently substitut", "no configuration substitution")
    assert_text_contains(check_id, freeze, r"`same orchestration session`[\s\S]+current-session authorization route separate", "separate same-session route")
    assert_text_contains(check_id, models, r"Run in`? accepts only `same orchestration session` or `new orchestration session`", "exclusive Run in values")
    assert_text_contains(check_id, models, r"actual frozen.+(?:boundary|package)|frozen.+boundary", "continuity uses actual frozen boundary")
    assert_text_contains(check_id, models, r"documented next lifecycle stage|named next lifecycle stage", "continuity uses documented lifecycle stage")

    retired_route_paths = [
        lifecycle,
        freeze,
        models,
        ".agents/skills/dev-doc-harness/references/context-and-quality-gates.md",
        ".agents/skills/dev-doc-harness/SKILL.md",
        *[to_repo_relative_path(path) for path in join_repo_path(".agents/skills/dev-doc-harness/assets/templates/blocks").glob("*.md")],
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
    ]
    retired_handoff_snapshot_pattern = r"(?i)\bhandoff[- ]snapshot\b"
    for path in retired_route_paths:
        assert_text_not_contains(check_id, path, retired_handoff_snapshot_pattern, "retired handoff-snapshot route")
        assert_text_not_contains(check_id, path, r"(?m)^#### Activity$", "retired Activity summary heading")
        assert_text_not_contains(check_id, path, r"First Plan Task", "retired task-level transition field")
    for legacy_route_fixture in [
        "approval commit or handoff snapshot",
        "<spec-filename or handoff snapshot>",
    ]:
        if not re.search(retired_handoff_snapshot_pattern, legacy_route_fixture):
            add_failure(check_id, f"retired-route fixture was not rejected: {legacy_route_fixture}")

    approval_freeze = read_markdown_h2_section(freeze, "Approval freeze checkpoint")
    post_freeze = read_markdown_h2_section(freeze, "Post-freeze transition routing")
    if not re.search(r"package[^\n]+frozen[\s\S]+same agent turn[\s\S]+Post-freeze transition routing", approval_freeze, flags=re.IGNORECASE):
        add_failure(check_id, "approval-freeze checklist does not contain freeze, stop, and routing mechanics")
    post_freeze_only = (
        r"fresh (?:explicit )?operator|operator response|authoriz(?:e|es|ed|ation) (?:implementation|execution|the action)|"
        r"runtime (?:selection|override)|operator override|independent review|Superpowers|execution-thread-start|"
        r"complete the approved plan|bare `?Confirm`?|same-orchestration-session route"
    )
    if re.search(post_freeze_only, approval_freeze, flags=re.IGNORECASE):
        add_failure(check_id, "approval-freeze checkpoint contains post-freeze routing details")
    if not re.search(r"fresh operator response[\s\S]+planned execution method[\s\S]+fresh explicit operator start", post_freeze, flags=re.IGNORECASE):
        add_failure(check_id, "post-freeze routing does not own authorization and runtime override handling")
    if not re.search(r"new orchestration session[\s\S]+default continuation[\s\S]+approval[\s\S]+create", post_freeze, flags=re.IGNORECASE):
        add_failure(check_id, "new-session route does not make approved agent task creation the default")
    if not re.search(r"manual[\s\S]+(?:unavailable|incompatible|operator)", post_freeze, flags=re.IGNORECASE):
        add_failure(check_id, "new-orchestration-session route does not limit manual creation to fallback or operator request")
    continuity_match = re.search(
        r"(?ms)^### Continuity rules\s*$\n(?P<body>.*?)(?=^### |^## |\Z)",
        post_freeze,
    )
    continuity_body = continuity_match.group("body") if continuity_match else ""
    if not continuity_match:
        add_failure(check_id, "post-freeze routing must contain a Continuity rules section")
    continuity_labels = re.findall(r"(?m)^#### `([^`]+)`\s*$", continuity_body)
    if continuity_labels != ["new orchestration session", "same orchestration session"]:
        add_failure(check_id, f"post-freeze routing must contain exactly the two canonical Run in branches; found {continuity_labels}")
    assert_text_contains(check_id, freeze, r"select and report.+(?:Git )?starting state", "explicit Git starting-state selection")
    assert_text_contains(check_id, freeze, r"`working-tree`", "detached managed-worktree source baseline")
    assert_text_contains(check_id, freeze, r"uncommitted (?:changes|paths)", "dirty working-tree disclosure")
    assert_text_contains(check_id, freeze, r"default branch.+prohibited|prohibited.+default branch", "no default-branch fallback")

    multiple_gates = read_markdown_h2_section(freeze, "Multiple gates for very large or phased work items")
    if not re.search(r"(?:normally|by default)[\s\S]+multiple freeze gates", multiple_gates, flags=re.IGNORECASE):
        add_failure(check_id, "large/phased route does not present multiple freeze gates as the default")

    small_spec = ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md"
    large_spec = ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md"
    assert_text_contains(check_id, small_spec, r"combined small/medium", "small spec combined planning shape")
    assert_text_contains(check_id, small_spec, r"Transition owner.*plan", "small spec plan-owned transition")
    assert_text_contains(check_id, large_spec, r"rolling", "large anchor rolling sequence")


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


def validate_commitment_plan_fixture(text: str) -> list[str]:
    errors: list[str] = []
    required_sections = ["## Implementation tasks"]
    for section in required_sections:
        if section not in text:
            errors.append(f"missing plan section {section}")
    implementation_section = re.search(r"^## Implementation tasks$", text, re.MULTILINE)
    section_start = implementation_section.end() if implementation_section else 0
    next_section = re.search(r"^## ", text[section_start:], re.MULTILINE)
    section_end = section_start + next_section.start() if next_section else len(text)
    task_matches = [
        match for match in re.finditer(r"^### `(TASK-\d{3})` .+$", text, re.MULTILINE)
        if section_start < match.start() < section_end
    ]
    all_check_matches = list(re.finditer(r"^#### `(CHECK-\d{3})` .+$", text, re.MULTILINE))
    check_matches = [match for match in all_check_matches if section_start < match.start() < section_end]
    task_ids = [match.group(1) for match in task_matches]
    check_ids = [match.group(1) for match in check_matches]
    if not task_ids:
        errors.append("missing exact Implementation Task heading")
    if not check_ids:
        errors.append("missing exact nested Plan Check heading")
    if len(task_ids) != len(set(task_ids)):
        errors.append("duplicate Implementation Task ID")
    if len(check_ids) != len(set(check_ids)):
        errors.append("duplicate Plan Check ID")
    if "## Plan checks" in text:
        errors.append("shared Plan Checks section is not allowed")
    if re.search(r"^### `(CHECK-\d{3})` .+$", text, re.MULTILINE):
        errors.append("Plan Checks must be nested in an Implementation Task")
    for match in all_check_matches:
        if match not in check_matches:
            errors.append(f"{match.group(1)} is outside the Implementation tasks section")
    entity_matches = sorted([*task_matches, *check_matches], key=lambda match: match.start())
    next_start = {match.start(): (entity_matches[index + 1].start() if index + 1 < len(entity_matches) else len(text)) for index, match in enumerate(entity_matches)}
    task_ranges = [
        (match.group(1), match.start(), task_matches[index + 1].start() if index + 1 < len(task_matches) else len(text))
        for index, match in enumerate(task_matches)
    ]
    for match in task_matches:
        block = text[match.end():next_start[match.start()]]
        for field in ("Dependencies:", "Implementation:", "Exit criteria:"):
            if field not in block:
                errors.append(f"{match.group(1)} missing Implementation Task field {field}")
    for match in check_matches:
        block = text[match.end():next_start[match.start()]]
        if not any(start < match.start() < end for _, start, end in task_ranges):
            errors.append(f"{match.group(1)} is not nested in an Implementation Task")
        for field in ("Covers:", "Method:", "Expected result:", "Evidence record:"):
            if field not in block:
                errors.append(f"{match.group(1)} missing Plan Check field {field}")
        if not re.search(r"`VER-\d{3}`", block.partition("Method:")[0]):
            errors.append(f"{match.group(1)} has no Verification Criterion coverage")
    return errors


def assert_commitment_verification_quality() -> None:
    check_id = "quality.commitment-verification"
    quality = ".agents/skills/dev-doc-harness/references/durable-planning-quality.md"
    execution_quality = ".agents/skills/dev-doc-harness/references/context-and-quality-gates.md"
    for rule_id in [
        "rule:quality.specification-commitments",
        "rule:quality.verification-criteria",
        "rule:quality.plan-tasks",
        "rule:quality.plan-checks",
        "rule:quality.asymmetric-plan-coverage",
        "rule:quality.conformance-status",
    ]:
        assert_text_contains(check_id, quality, re.escape(rule_id), f"{rule_id} owner")
    for pattern, label in [
        (r"all harness-managed durable specs and plans", "general durable-artifact scope"),
        (r"legalistic authority language and legalistic modal phrasing", "precise plain-language boundary"),
        (r"question material to the artifact.?s documented next activity", "material open-question boundary"),
        (
            r"Avoid legalistic authority language and legalistic modal phrasing.*?Say what to do and why only when the reason helps the reader act\. Prefer scannable sections, lists, and tables over dense prose\.\n\nEvery durable planning artifact should read as final artifact content",
            "preserved readability reordering",
        ),
        (r"A commitment conforms only when", "commitment conformance rule"),
        (r"operator-provided source materials", "durable source-preservation rule"),
        (r"## Plan quality bar", "general plan-quality section"),
        (r"## Additional phase-plan quality bar", "phase-only quality section"),
        (r"one orchestration session with its recorded bounded delegation", "phase execution-size boundary"),
        (r"## Spec quality bar[\s\S]*?### Specification Commitments[\s\S]*?### Verification Criteria[\s\S]*?## Plan quality bar", "spec entity hierarchy"),
        (r"## Plan quality bar[\s\S]*?### Plan Tasks[\s\S]*?### Plan Checks[\s\S]*?## Additional phase-plan quality bar", "plan entity hierarchy"),
        (r"A Plan Task is a bounded", "Plan Task definition"),
        (r"flat list of self-contained tasks", "flat task-body rule"),
        (r"nested in exactly one Plan Task", "task-bound check rule"),
        (r"explicit integration or verification task", "end-to-end parent-task rule"),
    ]:
        assert_text_contains(check_id, quality, pattern, label)
    assert_text_not_contains(check_id, quality, r"Verification Criteria and their Plan Checks within the tasks that run them", "ambiguous verification-in-task wording")
    assert_text_not_contains(check_id, quality, r"Record Plan Check evidence", "planning-time evidence record")
    for pattern, label in [
        (r"rule:execution-quality.conformance-evidence", "execution conformance-evidence owner"),
        (r"## Conformance evidence", "execution conformance-evidence section"),
        (r"During implementation, after a task-bound Plan Check runs", "implementation-time evidence timing"),
        (r"`met`, `not met`, `pending`, (?:or|and) `blocked`", "criterion conformance states"),
        (r"not a planning-time assertion", "planning/execution ownership boundary"),
    ]:
        assert_text_contains(check_id, execution_quality, pattern, label)

def assert_commitment_verification_templates() -> None:
    check_id = "templates.commitment-verification"
    spec_paths = CURRENT_SPEC_SCHEMA_PATHS
    plan_paths = CURRENT_PLAN_SCHEMA_PATHS
    for path in spec_paths:
        assert_text_contains(check_id, path, r"`SPEC-001`", "SPEC ID anchor")
        assert_text_contains(check_id, path, r"`VER-001`", "VER ID anchor")
        assert_text_contains(check_id, path, r"Expected evidence:", "Verification Criterion evidence prompt")
        assert_text_not_contains(check_id, path, r"(?m)^Kind:", "separate Kind field")
        assert_text_not_contains(check_id, path, r"(?m)^Intent:", "separate Intent field")
    for path in plan_paths:
        assert_text_contains(check_id, path, r"Use local links", "local-link traceability")
        assert_text_contains(check_id, path, r"Add a mapping only when", "benefit-based mapping")
        assert_text_contains(check_id, path, r"### `TASK-001` `<short imperative title>`", "TASK ID anchor")
        assert_text_contains(check_id, path, r"#### `CHECK-001` `<short title>`", "nested CHECK ID anchor")
        assert_text_contains(check_id, path, r"Evidence record:", "Plan Check evidence-record prompt")
        assert_text_not_contains(check_id, path, r"(?m)^## Plan checks$", "shared Plan Checks section")
        assert_text_not_contains(check_id, path, r"Related task\(s\):", "variable task relation")
        assert_text_not_contains(check_id, path, r"Commitment-Disposition Mapping", "mandatory commitment mapping")
        assert_text_not_contains(check_id, path, r"Verification-Execution Mapping", "mandatory verification mapping")

    phase_source = ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.030.phase.session-readiness.md"
    phase_template = ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md"
    assert_text_contains(check_id, phase_source, r"## Phase session readiness", "phase session-readiness heading")
    assert_normalized_text_contains(
        check_id,
        phase_source,
        "one orchestration session with its documented bounded delegation",
        "phase source execution-size boundary",
    )
    assert_text_contains(check_id, phase_source, r"amendment", "approved-anchor amendment path")
    assert_text_not_contains(check_id, phase_source, r"update the anchor spec before freeze", "retired approved-anchor edit path")
    assert_normalized_text_contains(
        check_id,
        phase_template,
        "one orchestration session with its documented bounded delegation",
        "phase template execution-size boundary",
    )
    assert_text_not_contains(check_id, plan_paths[0], r"one orchestration session with bounded delegation", "ordinary plan phase-only boundary")

    small_readiness = ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.090.small.readiness-completion-approval.md"
    phase_readiness = ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.090.phase.readiness-completion-approval.md"
    assert_text_contains(check_id, small_readiness, r"This plan document is self-sufficient", "small-plan fresh-session readiness")
    assert_text_contains(check_id, small_readiness, r"Plan Checks cover the full set of Verification Criteria", "small-plan verification coverage")
    assert_text_contains(check_id, small_readiness, r"Required documentation outputs are assigned to implementation tasks", "small-plan documentation assignment")
    assert_text_contains(check_id, small_readiness, r"deferred documentation items name an owner and resolution point", "small-plan documentation deferral")
    assert_text_not_contains(check_id, small_readiness, r"DOC-", "small-plan duplicated documentation IDs")
    assert_text_contains(check_id, phase_readiness, r"Required documentation outputs are assigned to this phase", "phase-plan documentation assignment")
    assert_text_contains(check_id, phase_readiness, r"deferred documentation items name an owner and resolution point", "phase-plan documentation deferral")
    assert_text_not_contains(check_id, phase_readiness, r"DOC-", "phase-plan duplicated documentation IDs")
    assert_text_contains(check_id, phase_readiness, r"Phase completion report", "phase completion-report readiness")
    assert_text_not_contains(check_id, phase_readiness, r"Post-phase transition", "retired phase post-transition readiness")

    task_bound_plan = """## Implementation tasks
### `TASK-001` Implement one change
Dependencies:
1. None.
Implementation:
1. Change one surface.
Exit criteria: Done.
#### `CHECK-001` Verify one criterion
Covers: `VER-001`.
Method: Run the focused validator.
Expected result: It passes.
Evidence record: Completion report.
"""
    if errors := validate_commitment_plan_fixture(task_bound_plan):
        add_failure(check_id, f"task-bound Plan Check fixture failed: {errors}")
    shared_check_plan = task_bound_plan.replace("#### `CHECK-001`", "## Plan checks\n### `CHECK-001`")
    after_section_check_plan = task_bound_plan.replace(
        "#### `CHECK-001` Verify one criterion\nCovers: `VER-001`.\nMethod: Run the focused validator.\nExpected result: It passes.\nEvidence record: Completion report.\n",
        "## Planned commits\n#### `CHECK-001` Verify one criterion\nCovers: `VER-001`.\nMethod: Run the focused validator.\nExpected result: It passes.\nEvidence record: Completion report.\n",
    )
    for fixture, label in [
        (task_bound_plan.replace("Covers: `VER-001`.\n", ""), "missing criterion coverage"),
        (task_bound_plan.replace("Evidence record: Completion report.\n", ""), "missing evidence record"),
        (shared_check_plan, "shared Plan Checks section"),
        (after_section_check_plan, "check outside the Implementation tasks section"),
    ]:
        if not validate_commitment_plan_fixture(fixture):
            add_failure(check_id, f"local-link Plan Check fixture with {label} passed")
    return


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
    if validate_commitment_plan_fixture(historical_text) == []:
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


def traceability_fixture_errors(text: str) -> list[str]:
    has_local_links = "Related: `SPEC-001` -> `TASK-001`; `VER-001` -> `CHECK-001`." in text
    has_mapping = "## Mapping" in text
    if not has_local_links and not has_mapping:
        return ["needs local links or a mapping"]
    if has_mapping and not re.search(r"Mapping benefit: `(coverage|handoff|deterministic validation)`", text):
        return ["mapping has no concrete benefit"]
    return []


def execution_fixture_errors(text: str) -> list[str]:
    required = ["Frozen package", "Fresh start instruction", "continue through planned tasks"]
    errors = [f"missing {item}" for item in required if item not in text]
    if "ask after each task" in text:
        errors.append("adds a per-task confirmation")
    return errors


def variance_fixture_route(text: str) -> str:
    if "same scope, outcome, and evidence purpose" in text:
        return "variance"
    if re.search(r"changes (?:the )?(?:outcome|architecture|API|data|security|privacy|compliance)|invalidates evidence", text):
        return "amendment"
    return "invalid"


def verification_criterion_fixture_errors(text: str) -> list[str]:
    if "Applicability: `Cross-phase`" in text and "Owning phase:" not in text:
        return ["cross-phase criterion has no owning phase"]
    return []


def multi_check_fixture_mode(text: str) -> str:
    if "All required: `Yes`" in text:
        return "all-required"
    if "Equivalent alternatives: `Yes`" in text and "Equivalence reason:" in text:
        return "equivalent-alternatives"
    return "invalid"


def superpowers_task_fixture_errors(text: str) -> list[str]:
    task_match = re.search(
        r"## Implementation tasks(?P<body>.*?)(?:\n## Model and Sub-agent Strategy|\n## Implementation handoff|\n## Phase implementation handoff|\Z)",
        text,
        flags=re.DOTALL,
    )
    if task_match is None:
        return ["missing implementation-task section"]
    task_body = task_match.group("body")
    errors: list[str] = []
    if "Dependencies:" not in task_body:
        errors.append("missing dependencies")
    if "Interfaces:" not in task_body:
        errors.append("missing interfaces")
    if "Consumes:" not in task_body or "Produces:" not in task_body:
        errors.append("missing task input/output contract")
    if re.search(r"(?m)^\s*- \[[ xX]\]", task_body):
        errors.append("uses checkbox task steps")
    if not re.search(r"(?m)^\s*1\.\s+", task_body):
        errors.append("missing numbered task step")
    return errors


def superpowers_global_constraints_fixture_errors(text: str) -> list[str]:
    if "## Global Constraints" not in text:
        return []
    if "Self-containment reason:" not in text:
        return ["global constraints lack a self-containment reason"]
    return []


def superpowers_dispatch_fixture_route(text: str) -> str:
    if all(
        field in text
        for field in [
            "Active model policy:",
            "Recommended sub-agent model:",
            "Generation:",
            "Capability tier:",
            "Reasoning effort:",
        ]
    ):
        return "in-envelope"
    if "outside the approved envelope" in text and "approval" in text:
        return "approval"
    return "invalid"


def assert_harness_simplification_scenarios() -> None:
    check_id = "scenarios.harness-simplification"
    lifecycle = ".agents/skills/dev-doc-harness/references/artifact-contract.md"
    freeze = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"
    quality = ".agents/skills/dev-doc-harness/references/durable-planning-quality.md"
    readiness_source_blocks = [
        ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.090.small.readiness-approval.md",
        ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.090.large.readiness-approval.md",
    ]
    readiness_templates = [
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
    ]
    verification_source_block = ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.030.common.commitments-verification.md"
    plan_check_source_block = ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.050.common.task-plan.md"

    assert_text_contains(check_id, quality, r"Mappings are optional", "optional mapping guidance")
    assert_text_contains(check_id, freeze, r"without\s+pausing between planned\s+tasks", "uninterrupted approved execution")
    assert_text_contains(check_id, lifecycle, r"same evidence purpose", "equivalent adjustment variance route")
    assert_text_contains(
        check_id,
        lifecycle,
        r"material.+outcome.+architecture.+API.+data.+security.+privacy.+compliance",
        "material amendment threshold",
    )
    assert_text_contains(
        check_id,
        "README.md",
        r"An example of a minimalistic bootstrap in the global `AGENTS\.md`",
        "README global bootstrap",
    )
    assert_text_contains(check_id, "README.md", r"same evidence purpose", "canonical equivalent-evidence variance route")
    assert_text_not_contains(
        check_id,
        "README.md",
        r"(?s)Changes to architecture.*?Plan\s+Checks.*?require an amendment and approval",
        "unconditional Plan Check amendment list",
    )

    for path in [*readiness_source_blocks, *readiness_templates]:
        assert_text_not_contains(
            check_id,
            path,
            r"Specification Commitments are atomic,\s*classified,\s*bounded",
            "mandatory commitment classification",
        )

    for path in [verification_source_block, *CURRENT_SPEC_SCHEMA_PATHS[1:]]:
        assert_text_contains(
            check_id,
            path,
            r"Applicability.*owning phase.*optional",
            "optional Verification Criterion applicability/owner cue",
        )
    for path in [plan_check_source_block, *CURRENT_PLAN_SCHEMA_PATHS]:
        assert_text_contains(
            check_id,
            path,
            r"whether[\s\S]*all[\s\S]*required[\s\S]*equivalent[\s\S]*alternatives[\s\S]*why",
            "multi-check required-versus-equivalent cue",
        )

    variance_template = ".agents/skills/dev-doc-harness/assets/templates/variance-log.md"
    assert_text_contains(
        check_id,
        variance_template,
        r"Material changes use `plan-amendment\.md`",
        "material changes bypass the variance log",
    )
    assert_text_not_contains(check_id, variance_template, r"Variance class:.*Material", "material variance class")

    local_links = "Related: `SPEC-001` -> `TASK-001`; `VER-001` -> `CHECK-001`."
    justified_mapping = "## Mapping\nMapping benefit: `coverage`\n`SPEC-001` -> `TASK-001`"
    unjustified_mapping = "## Mapping\n`SPEC-001` -> `TASK-001`"
    if traceability_fixture_errors(local_links):
        add_failure(check_id, "concise local-link fixture failed")
    if traceability_fixture_errors(justified_mapping):
        add_failure(check_id, "justified mapping fixture failed")
    if not traceability_fixture_errors(unjustified_mapping):
        add_failure(check_id, "unjustified mapping fixture passed")

    approved_execution = "Frozen package\nFresh start instruction\ncontinue through planned tasks"
    per_task_pause = approved_execution + "\nask after each task"
    if execution_fixture_errors(approved_execution):
        add_failure(check_id, "approved execution fixture failed")
    if not execution_fixture_errors(per_task_pause):
        add_failure(check_id, "per-task pause fixture passed")

    if variance_fixture_route("same scope, outcome, and evidence purpose") != "variance":
        add_failure(check_id, "equivalent adjustment fixture did not route to variance")
    if variance_fixture_route("changes the outcome") != "amendment":
        add_failure(check_id, "material outcome fixture did not route to amendment")
    if variance_fixture_route("invalidates evidence") != "amendment":
        add_failure(check_id, "invalidated evidence fixture did not route to amendment")

    cross_phase_criterion = "Applicability: `Cross-phase`\nOwning phase: `Phase 02`"
    missing_owner_criterion = "Applicability: `Cross-phase`"
    if verification_criterion_fixture_errors(cross_phase_criterion):
        add_failure(check_id, "cross-phase criterion with an owning phase failed")
    if not verification_criterion_fixture_errors(missing_owner_criterion):
        add_failure(check_id, "cross-phase criterion without an owning phase passed")

    all_required_checks = "Plan checks: `CHECK-001`, `CHECK-002`\nAll required: `Yes`"
    equivalent_alternatives = (
        "Plan checks: `CHECK-001`, `CHECK-002`\n"
        "Equivalent alternatives: `Yes`\n"
        "Equivalence reason: either check proves the same evidence purpose"
    )
    if multi_check_fixture_mode(all_required_checks) != "all-required":
        add_failure(check_id, "all-required two-check fixture did not preserve required evidence")
    if multi_check_fixture_mode(equivalent_alternatives) != "equivalent-alternatives":
        add_failure(check_id, "equivalent-alternative fixture with an explicit reason was not recognized")
    if multi_check_fixture_mode(all_required_checks) == multi_check_fixture_mode(equivalent_alternatives):
        add_failure(check_id, "all-required and equivalent-alternative fixtures were conflated")


def assert_superpowers_adapter_contract() -> None:
    check_id = "compat.superpowers-adapter-contract"
    lifecycle = ".agents/skills/dev-doc-harness/references/artifact-contract.md"
    models = ".agents/skills/dev-doc-harness/references/subagent-model-policy.md"
    freeze = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"
    header_blocks = [
        ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.010.small.header-inputs.md",
        ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.010.phase.header-objective-inputs.md",
    ]
    traceability_block = ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.020.common.traceability-approach-surfaces.md"
    model_block = ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.055.common.model-strategy.md"
    handoff_block = ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.small.handoff.md"
    task_block = ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.050.common.task-plan.md"

    assert_text_contains(
        check_id,
        "AGENTS.md",
        r"Superpowers[\s\S]+methodology[\s\S]+(?:harness|Dev Doc Harness)[\s\S]+artifact(?:-| )location[\s\S]+lifecycle",
        "AGENTS.md Superpowers/harness ownership boundary",
    )
    assert_text_contains(
        check_id,
        "README.md",
        r"overrid(?:e|es)[\s\S]+Superpowers[\s\S]+default[\s\S]+(?:spec|plan)[\s\S]+location",
        "README.md path-preference override",
    )
    for path in ["AGENTS.md", "README.md"]:
        assert_text_contains(check_id, path, r"docs/work-items/<work-id>", f"{path} canonical work-item path")

    assert_text_contains(check_id, lifecycle, r"conditional.+(?:convert|conversion).+Superpowers", "conditional plan conversion")
    assert_text_contains(check_id, lifecycle, r"ephemeral", "ephemeral execution aids")
    assert_text_contains(check_id, lifecycle, r"independently executable.+verifiable", "no-Superpowers fallback")
    assert_text_contains(check_id, freeze, r"before.+Superpowers.+(?:pre-flight|execution)", "authorized Superpowers entry")
    assert_text_contains(check_id, freeze, r"without.+second generic.+method question", "no second execution-mode choice")
    assert_text_contains(check_id, models, r"explicit.+(?:capability tier|allocation).+reasoning effort", "explicit dispatch allocation")
    assert_text_contains(check_id, models, r"silent(?:ly)? inherit", "silent-inheritance prohibition")
    assert_text_contains(check_id, models, r"outside.+approved.+(?:envelope|policy).+approval", "out-of-envelope approval")

    for path in header_blocks:
        assert_text_contains(check_id, path, r"Execution method", "conditional execution metadata")
        assert_text_not_contains(check_id, path, r"## Superpowers execution meta-header", "obsolete execution meta-header")
    assert_text_contains(check_id, traceability_block, r"Global Constraints", "global-constraints prompt")
    assert_text_contains(check_id, traceability_block, r"self-contained", "global-constraints self-containment test")
    assert_text_not_contains(check_id, model_block, r"Next-stage recommendation", "duplicated approved selection prompt")
    assert_text_contains(check_id, handoff_block, r"Next-stage recommendation", "handoff approved selection prompt")
    assert_text_contains(check_id, model_block, r"Upcoming-stage sub-agent assessment", "upcoming-stage assessment prompt")
    assert_text_contains(check_id, task_block, r"Interfaces", "task-interface prompt")
    assert_text_contains(check_id, task_block, r"numbered", "numbered task-step prompt")

    for path in PLAN_TEMPLATE_FILES:
        assert_text_contains(check_id, path, r"Execution method", "generated execution metadata")
        assert_text_not_contains(check_id, path, r"## Superpowers execution meta-header", "obsolete generated meta-header")
        assert_text_contains(check_id, path, r"Global Constraints", "generated global-constraints prompt")
        assert_text_contains(check_id, path, r"Interfaces", "generated task-interface prompt")
        assert_text_contains(check_id, path, r"Next-stage recommendation", "generated approved selection prompt")
        errors = superpowers_task_fixture_errors(read_repo_text(path))
        if errors:
            add_failure(check_id, f"{path} task shape: {', '.join(errors)}")

    valid_task = (
        "## Implementation tasks\n"
        "### `TASK-001` Validate adapter\n\n"
        "Dependencies: approved plan.\n\n"
        "Interfaces:\n\n"
        "1. Consumes: approved policy.\n"
        "2. Produces: validation evidence.\n\n"
        "Implementation:\n\n"
        "1. Run the validator.\n\n"
        "#### `CHECK-001` Verify adapter\n"
    )
    checkbox_task = valid_task.replace("1. Run the validator.", "- [ ] Run the validator.")
    dependency_only_task = valid_task.replace("Interfaces:\n\n1. Consumes: approved policy.\n2. Produces: validation evidence.\n\n", "")
    if superpowers_task_fixture_errors(valid_task):
        add_failure(check_id, "numbered task fixture failed")
    if "uses checkbox task steps" not in superpowers_task_fixture_errors(checkbox_task):
        add_failure(check_id, "checkbox task fixture passed")
    if "missing interfaces" not in superpowers_task_fixture_errors(dependency_only_task):
        add_failure(check_id, "dependency-only task fixture passed")

    justified_global_constraints = "## Global Constraints\nSelf-containment reason: a shared execution rule is otherwise absent."
    duplicate_global_constraints = "## Global Constraints\nRepeat the approved spec."
    if superpowers_global_constraints_fixture_errors(justified_global_constraints):
        add_failure(check_id, "justified global-constraints fixture failed")
    if not superpowers_global_constraints_fixture_errors(duplicate_global_constraints):
        add_failure(check_id, "unjustified global-constraints fixture passed")

    in_envelope_dispatch = (
        "Active model policy: `economy-default`\n"
        "Recommended sub-agent model: Generation: `latest available`; "
        "Capability tier: `fast/economy`; Reasoning effort: `medium`"
    )
    out_of_envelope_dispatch = "A dispatch outside the approved envelope requires approval."
    if superpowers_dispatch_fixture_route(in_envelope_dispatch) != "in-envelope":
        add_failure(check_id, "in-envelope dispatch fixture failed")
    if superpowers_dispatch_fixture_route(out_of_envelope_dispatch) != "approval":
        add_failure(check_id, "out-of-envelope dispatch fixture did not route to approval")


def execution_method_fixture_route(text: str) -> str:
    """Resolve the documented execution-method decision from a literal fixture."""
    if (
        "Fresh explicit operator override" in text
        and "Selected model available" in text
        and "Actual runtime selection: recorded" in text
        and "Plan amendment: not required solely for this runtime choice" in text
    ):
        return "operator-model-override"
    if "Fresh explicit operator override" in text and "Selected method available" in text:
        return "operator-override"
    if "Superpowers: available" in text:
        if "Sub-agent-driven conditions: true" in text:
            return "superpowers:subagent-driven-development"
        if "Host-native execution proposed as default" in text:
            return "invalid"
        return "superpowers:executing-plans"
    if "Superpowers: unavailable" in text:
        if "Reviewer sub-agent: unavailable" in text:
            if "Operator authorization: proceed without independent review" in text:
                return "host-native execution authorized no-review"
            return "host-native execution awaiting operator decision"
        return "host-native execution"
    return "invalid"


def reviewer_fixture_route(text: str) -> str:
    """Check the route-specific review obligation without relying on a framework."""
    if "Method: superpowers:subagent-driven-development" in text:
        if "Independent reviewer after each Plan Task" in text and "Independent final whole-branch reviewer" in text:
            return "preferred-reviewed"
    if "Method: superpowers:executing-plans" in text:
        if "Preserve executing-plans checkpoints" in text and "Reviewer capability disclosure" in text:
            return "fallback-disclosed"
    if "Method: host-native execution" in text:
        if "Independent reviewer sub-agent" in text and "curated artifacts" in text and "named lens" in text and "evidence-backed findings" in text and "execution orchestration session owns final integration" in text:
            return "native-reviewed"
        no_review_record = (
            "Independent review: not run" in text
            and "Reason:" in text
            and "Assurance gap:" in text
            and "Focused self-review and validation:" in text
            and "Completion report: state whether independent review ran" in text
        )
        if (
            "Reviewer sub-agent: unavailable" in text
            and no_review_record
            and "Ask once whether to proceed without independent review" in text
            and "Operator authorization: pending" in text
        ):
            return "awaiting-operator-decision"
        if (
            "Reviewer sub-agent: unavailable" in text
            and no_review_record
            and "Operator authorization: proceed without independent review" in text
            and "Sub-agents: None" in text
        ):
            return "operator-authorized-no-review"
        if (
            "Operator declined independent review" in text
            and no_review_record
            and "Operator authorization: proceed without independent review" in text
            and "Sub-agents: None" in text
        ):
            return "operator-declined-review-authorized"
        if "Sub-agents: None" in text:
            return "invalid"
    return "invalid"


def assert_execution_method_fallbacks() -> None:
    check_id = "execution.method-fallbacks"
    lifecycle = ".agents/skills/dev-doc-harness/references/artifact-contract.md"
    models = ".agents/skills/dev-doc-harness/references/subagent-model-policy.md"
    freeze = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"
    router = ".agents/skills/dev-doc-harness/SKILL.md"

    method_fixtures = {
        "superpowers:subagent-driven-development": "Superpowers: available\nSub-agent-driven conditions: true",
        "superpowers:executing-plans": "Superpowers: available\nSub-agent-driven conditions: unavailable or unsuitable",
        "host-native execution": "Superpowers: unavailable\nReviewer sub-agent: available",
        "host-native execution awaiting operator decision": "Superpowers: unavailable\nReviewer sub-agent: unavailable\nIndependent review decision: pending",
        "host-native execution authorized no-review": "Superpowers: unavailable\nReviewer sub-agent: unavailable\nOperator authorization: proceed without independent review",
        "invalid": "Superpowers: available\nHost-native execution proposed as default",
        "operator-override": "Fresh explicit operator override\nSelected method available",
        "operator-model-override": "Fresh explicit operator override\nSelected model available\nActual runtime selection: recorded\nPlan amendment: not required solely for this runtime choice",
    }
    for expected, fixture in method_fixtures.items():
        if execution_method_fixture_route(fixture) != expected:
            add_failure(check_id, f"{expected} method fixture did not route correctly")

    reviewer_fixtures = {
        "preferred-reviewed": "Method: superpowers:subagent-driven-development\nIndependent reviewer after each Plan Task\nIndependent final whole-branch reviewer",
        "fallback-disclosed": "Method: superpowers:executing-plans\nPreserve executing-plans checkpoints\nReviewer capability disclosure",
        "native-reviewed": "Method: host-native execution\nIndependent reviewer sub-agent\ncurated artifacts\nnamed lens\nevidence-backed findings\nexecution orchestration session owns final integration",
        "awaiting-operator-decision": "Method: host-native execution\nReviewer sub-agent: unavailable\nIndependent review: not run\nReason: reviewer tooling is unavailable\nAssurance gap: no independent review\nFocused self-review and validation: required\nCompletion report: state whether independent review ran\nAsk once whether to proceed without independent review\nOperator authorization: pending",
        "operator-authorized-no-review": "Method: host-native execution\nReviewer sub-agent: unavailable\nIndependent review: not run\nReason: reviewer tooling is unavailable\nAssurance gap: no independent review\nFocused self-review and validation: required\nCompletion report: state whether independent review ran\nOperator authorization: proceed without independent review\nSub-agents: None",
        "operator-declined-review-authorized": "Method: host-native execution\nOperator declined independent review\nIndependent review: not run\nReason: operator declined review\nAssurance gap: no independent review\nFocused self-review and validation: required\nCompletion report: state whether independent review ran\nOperator authorization: proceed without independent review\nSub-agents: None",
        "invalid": "Method: host-native execution\nSub-agents: None",
    }
    for expected, fixture in reviewer_fixtures.items():
        if reviewer_fixture_route(fixture) != expected:
            add_failure(check_id, f"{expected} reviewer fixture did not route correctly")

    assert_text_contains(check_id, lifecycle, r"superpowers:subagent-driven-development", "preferred execution method")
    assert_text_contains(check_id, lifecycle, r"superpowers:executing-plans", "Superpowers fallback method")
    assert_text_contains(check_id, lifecycle, r"host-native execution.*Superpowers.*unavailable", "host-native default boundary")
    assert_text_contains(
        check_id,
        lifecycle,
        re.escape("rule:models.execution-review-contract"),
        "route-specific reviewer-contract owner",
    )
    if "independent review can run" in read_repo_text(models).lower():
        add_failure(check_id, "native method cascade retains obsolete review-availability blocker")
    assert_text_contains(
        check_id,
        models,
        re.escape("rule:models.execution-review-contract"),
        "execution-review contract rule",
    )
    assert_text_not_contains(
        check_id,
        models,
        re.escape("in `## Execution method and reviewer contract`"),
        "heading-literal reviewer-contract reference",
    )
    assert_text_contains(check_id, models, r"Independent reviewer after each Plan Task", "preferred per-Plan-Task review")
    assert_text_contains(check_id, models, r"Independent final whole-branch reviewer", "preferred final review")
    assert_text_contains(check_id, models, r"Preserve executing-plans checkpoints", "fallback checkpoints")
    assert_text_contains(check_id, models, r"Reviewer capability disclosure", "fallback reviewer disclosure")
    assert_text_contains(check_id, models, r"host-native execution.*Independent reviewer sub-agent", "host-native independent review")
    assert_text_contains(check_id, models, r"independent reviewer.*default", "native independent-review default")
    assert_text_contains(check_id, models, r"ask once.*proceed without independent review", "one-time no-review decision")
    assert_text_contains(check_id, models, r"Sub-agents: None.*operator authorization", "authorized native no-review route")
    assert_text_contains(check_id, models, r"completion report.*independent review", "no-review completion evidence")
    assert_text_contains(check_id, models, r"execution orchestration session owns final integration", "execution integration ownership")
    assert_text_contains(check_id, models, r"external method session.*execution controller", "Superpowers session interpretation")
    assert_text_contains(check_id, freeze, r"fresh explicit operator.*method.*model", "execution-start override")
    assert_text_contains(check_id, freeze, r"record.*actual.*selection", "recorded runtime selection")
    assert_text_contains(check_id, freeze, r"without.*plan amendment.*solely", "no amendment for runtime selection")
    assert_text_contains(check_id, freeze, r"runtime selection.*completion report", "override completion-report record")
    assert_text_contains(check_id, freeze, r"variance log only when.*noteworthy allowed variance", "conditional variance-log record")
    assert_text_contains(check_id, freeze, r"without.*second generic.*method question", "freeze start selection")
    assert_text_contains(check_id, router, r"execution-method cascade", "router execution route")
    assert_text_contains(
        check_id,
        router,
        re.escape("rule:models.execution-review-contract"),
        "router reviewer-contract owner",
    )


def proposed_subagent_model_fixture_errors(text: str) -> list[str]:
    required = [
        "Active model policy",
        "Recommended sub-agent model",
        "Generation",
        "Capability tier",
        "Reasoning effort",
        "Orchestration mode",
        "Availability/fallback",
    ]
    errors = [f"proposed role missing {field}" for field in required if field not in text]
    if re.search(r"(?:Generation|Capability tier|Reasoning effort):\s*`?not exposed`?", text, flags=re.IGNORECASE):
        errors.append("recommended sub-agent model uses not exposed")
    if re.search(r"Resolved target profile:\s*`?not exposed`?", text, flags=re.IGNORECASE):
        errors.append("optional resolved target profile should be omitted when not exposed")
    return errors


def delegation_fixture_route(text: str) -> str:
    if "Sub-agents: None" in text and "Fit reason:" in text:
        return "none"
    if "Authorization state: `Approved`" in text and "in-envelope" in text:
        return "approved"
    if "Authorization state: `Pending`" in text and "Ask the operator" in text:
        return "pending"
    if "unavailable" in text and "orchestration-session fallback" in text:
        return "fallback"
    if "outside the approved envelope" in text and "Ask the operator" in text:
        return "reapproval"
    return "invalid"


def combined_package_fixture_route(text: str) -> str:
    """Classify the planning package shape at the freeze boundary."""
    if "Work size: large/phased" in text and "Frozen package: spec only" in text:
        return "large-anchor-valid"
    if "Work size: small/medium" not in text:
        return "invalid"
    if "Frozen package: spec and plan" in text:
        return "combined-valid"
    if "Frozen package: spec only" not in text:
        return "invalid"
    if not re.search(r"Staging authorization: operator-(?:requested|approved)", text):
        return "invalid"
    if not re.search(r"Staging reason: .+", text):
        return "invalid"
    if "Next activity: plan drafting" not in text:
        return "invalid"
    return "staged-valid"


def assert_combined_package_default() -> None:
    check_id = "lifecycle.combined-package-default"
    lifecycle = ".agents/skills/dev-doc-harness/references/artifact-contract.md"
    freeze = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"
    router = ".agents/skills/dev-doc-harness/SKILL.md"
    small_spec = ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md"
    agents = "AGENTS.md"
    readme = "README.md"
    operator_note = ".agents/skills/dev-doc-harness/docs/operator-note.md"

    fixtures = {
        "combined-valid": "Work size: small/medium\nFrozen package: spec and plan",
        "invalid": "Work size: small/medium\nFrozen package: spec only",
        "staged-valid": (
            "Work size: small/medium\nFrozen package: spec only\n"
            "Staging authorization: operator-requested\n"
            "Staging reason: Contract evidence must be gathered first\n"
            "Next activity: plan drafting"
        ),
        "large-anchor-valid": "Work size: large/phased\nFrozen package: spec only",
    }
    for expected, fixture in fixtures.items():
        if combined_package_fixture_route(fixture) != expected:
            add_failure(check_id, f"{expected} package fixture did not route correctly")

    if combined_package_fixture_route("Work size: small/medium\nComplexity: high but one-thread-manageable\nFrozen package: spec and plan") != "combined-valid":
        add_failure(check_id, "one-thread-manageable work did not retain the small/medium combined package")

    assert_text_contains(check_id, lifecycle, r"uncertain.*small/medium.*demonstrably", "uncertain sizing boundary")
    assert_text_contains(check_id, lifecycle, r"spec-only.*operator-(?:requested|approved)", "authorized staged exception")
    assert_text_contains(check_id, router, r"both.*<spec-filename>.*<plan-filename>.*same turn", "combined drafting instruction")
    assert_text_contains(check_id, router, r"both canonical files", "combined checklist")
    assert_text_contains(check_id, freeze, r"complete.*combined small/medium", "draft package completeness")
    assert_text_contains(check_id, freeze, r"complete.*combined small/medium", "approval package completeness")
    assert_text_contains(check_id, freeze, r"large/phased anchor", "large anchor retained")
    assert_text_contains(check_id, small_spec, r"Companion plan", "small spec companion plan")
    assert_text_contains(check_id, small_spec, r"operator-(?:requested|approved)", "small spec staged authorization")
    for path in [agents, readme, operator_note]:
        assert_text_contains(check_id, path, r"combined small/medium", "operator combined-planning guidance")


def assert_planning_template_clarity() -> None:
    check_id = "clarity.planning-template-contract"
    router = ".agents/skills/dev-doc-harness/SKILL.md"
    lifecycle = ".agents/skills/dev-doc-harness/references/artifact-contract.md"
    models = ".agents/skills/dev-doc-harness/references/subagent-model-policy.md"
    quality = ".agents/skills/dev-doc-harness/references/durable-planning-quality.md"
    freeze = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"
    skill_completion = read_repo_text(router).split("## Completion checklist", 1)[-1].split("## Planning Artifact Freeze Gate", 1)[0]
    if not re.search(r"(?m)^- \[ \] ", skill_completion):
        add_failure(check_id, "SKILL.md completion guidance is not a literal checkbox checklist")

    commitment_paths = [
        quality,
        ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.030.common.commitments-verification.md",
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
    ]
    for path in commitment_paths:
        assert_text_not_contains(check_id, path, r"Classification is optional|Constraint · Preserve", "undefined commitment classification")
    assert_text_contains(
        check_id,
        ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.030.common.commitments-verification.md",
        r"additional[\s\S]*SPEC[\s\S]*uses[\s\S]*Statement[\s\S]*local[\s\S]*Verification Criterion",
        "complete repeated commitment structure",
    )

    planned_commit_paths = [
        ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.070.small.planned-commits.md",
        ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.070.large.planned-commits-freeze.md",
        ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.060.small.planned-commits.md",
        ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.060.phase.planned-commits.md",
        ".agents/skills/dev-doc-harness/assets/templates/plan-amendment.md",
    ]
    for path in planned_commit_paths:
        assert_text_contains(check_id, path, r"Stage.*Planned subject", "concise planned-commit columns")
        assert_text_not_contains(check_id, path, r"Changelog title or snippet|\| Notes \|", "duplicate planned-commit field")

    header_blocks = [
        ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.010.small.header-inputs.md",
        ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.010.phase.header-objective-inputs.md",
    ]
    for path in [*header_blocks, *PLAN_TEMPLATE_FILES]:
        assert_text_contains(check_id, path, r"Execution method", "execution method metadata")
        assert_text_not_contains(check_id, path, r"## Superpowers execution meta-header", "obsolete Superpowers meta-header section")

    plan_model_source = ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.055.common.model-strategy.md"
    large_model_source = ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.060.large.phase-decomposition-model.md"
    model_sources = [plan_model_source, large_model_source]
    model_consumers = [
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
    ]
    for path in [models, large_model_source, *model_consumers]:
        assert_text_contains(check_id, path, r"Current orchestration session", "planning observations group")
        assert_text_contains(check_id, path, r"Next-stage recommendation", "approved selection group")
    assert_text_contains(check_id, plan_model_source, r"Upcoming-stage sub-agent assessment", "plan strategy assessment")
    assert_text_not_contains(check_id, plan_model_source, r"Current planning Codex task", "duplicated plan observations group")
    assert_text_not_contains(check_id, plan_model_source, r"Next-stage recommendation", "duplicated plan selection group")

    proposed_role = (
        "Active model policy: `economy-default`\n"
        "Recommended sub-agent model:\nGeneration: `latest available`\nCapability tier: `balanced`\n"
        "Reasoning effort: `high`\nOrchestration mode: `bounded delegated sub-agents`\n"
        "Availability/fallback: `Terra medium or equivalent`"
    )
    unknown_target = proposed_role.replace("Generation: `latest available`", "Generation: `not exposed`")
    redundant_resolved_target = proposed_role + "\nResolved target profile: `not exposed`"
    if proposed_subagent_model_fixture_errors(proposed_role):
        add_failure(check_id, "valid proposed-role model fixture was rejected")
    if not proposed_subagent_model_fixture_errors(unknown_target):
        add_failure(check_id, "unknown proposed-role generation fixture was accepted")
    if not proposed_subagent_model_fixture_errors(redundant_resolved_target):
        add_failure(check_id, "redundant unresolved target-profile fixture was accepted")

    small_spec = ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md"
    small_plan = ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md"
    phase_plan = ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md"
    assert_text_contains(check_id, small_spec, r"Transition owner.*plan", "small spec plan transition ownership")
    assert_text_not_contains(check_id, small_spec, r"Implementation Handoff", "duplicate small-spec implementation handoff")
    assert_text_contains(check_id, small_plan, r"Implementation handoff", "small plan implementation handoff")
    assert_text_contains(check_id, phase_plan, r"Phase implementation handoff", "phase implementation handoff")
    assert_text_contains(check_id, phase_plan, r"Phase completion report", "phase completion report")
    assert_text_not_contains(check_id, phase_plan, r"Post-phase transition", "retired phase post-transition handoff")

    for path in [lifecycle, ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md", phase_plan]:
        assert_text_contains(check_id, path, r"rolling", "rolling phase loop")
        assert_text_contains(check_id, path, r"stable[\s\S]*independent", "explicit batch-planning exception")

    delegation_paths = [router, models, freeze, *model_sources, *model_consumers]
    for path in delegation_paths:
        assert_text_contains(check_id, path, r"upcoming-stage.*sub-agent|upcoming stage.*sub-agent", "upcoming-stage delegation assessment")
        assert_text_contains(check_id, path, r"Sub-agents: None", "stage-specific no-use rationale")
        assert_text_contains(check_id, path, r"operator.*(?:approve|authorization)|(?:approve|authorization).*operator", "delegation approval route")

    router_text = read_repo_text(router)
    for route in ["Draft or review large anchor specs", "Draft or review phase plans", "Freeze planning packages"]:
        row_match = re.search(rf"(?m)^\| {re.escape(route)} \|(?P<row>.+)$", router_text)
        if row_match is None:
            add_failure(check_id, f"missing router row for {route}")
        elif not re.search(r"upcoming-stage sub-agent assessment", row_match.group("row"), flags=re.IGNORECASE):
            add_failure(check_id, f"router row for {route} omits the upcoming-stage sub-agent assessment")

    fixtures = {
        "pending": "Authorization state: `Pending`\nAsk the operator to approve the recorded role.",
        "approved": "Authorization state: `Approved`\nUse the in-envelope strategy without another request.",
        "none": "Sub-agents: None\nFit reason: tightly coupled policy ownership.",
        "fallback": "Tooling unavailable; use the orchestration-session fallback.",
        "reapproval": "This role is outside the approved envelope. Ask the operator before dispatch.",
    }
    for expected, fixture in fixtures.items():
        if delegation_fixture_route(fixture) != expected:
            add_failure(check_id, f"{expected} delegation fixture did not route correctly")


def next_stage_summary_fixture_errors(text: str, *, frozen: bool) -> list[str]:
    """Validate the compact next-stage interface consumed by artifacts and chat."""
    required_title = "Approved next stage" if frozen else "Next-stage recommendation"
    errors = [
        f"missing {required_title}"
        for title in [required_title]
        if title not in text
    ]
    forbidden_title = "Next-stage recommendation" if frozen else "Approved next stage"
    if forbidden_title in text:
        errors.append(f"contains incompatible {forbidden_title}")
    for group in ["Next lifecycle stage", "Orchestration", "Model", "Execution requirements and contingencies"]:
        if group not in text:
            errors.append(f"missing {group} group")
    if not re.search(
        r"Next lifecycle stage:\s*Stage:\s*`(?:plan drafting|plan execution|phase-plan drafting|phase execution|documented resumed stage)`",
        text,
    ):
        errors.append("lifecycle stage is missing or unsupported")
    if "First Plan Task" in text or re.search(r"(?m)^Activity:", text):
        errors.append("retired task-level transition fields are present")
    if not re.search(r"Method:.*Orchestration mode:.*Run in:.*Review", text, flags=re.DOTALL):
        errors.append("orchestration fields are incomplete")
    if re.search(r"(?m)^Orchestration mode fit:", text):
        errors.append("noncanonical orchestration mode fit field is present")
    if re.search(r"(?<!Orchestration )Mode:", text):
        errors.append("orchestration mode uses shorthand label")
    if not re.search(r"Generation:.*Capability tier:.*Reasoning", text, flags=re.DOTALL):
        errors.append("model fields are incomplete")
    if not re.search(r"Run in:\s*(?:same orchestration session|new orchestration session)(?=;|\n|$)", text):
        errors.append("Run in uses an unsupported value")
    if "Run in: same orchestration session" in text:
        if not re.search(r"profile\s+`known suitable`", text, flags=re.IGNORECASE):
            errors.append("same orchestration session lacks a known-suitable profile")
        if not re.search(r"Context risk:\s*`(?:suitable|immaterial)`", text, flags=re.IGNORECASE):
            errors.append("same orchestration session lacks suitable or immaterial context risk")
        if not re.search(r"Continuity benefit:\s*`[^`\n]+`", text, flags=re.IGNORECASE):
            errors.append("same orchestration session lacks a concrete continuity benefit")
    if re.search(r"(?:\d+[% ]+context|remaining context|compaction prediction)", text, flags=re.IGNORECASE):
        errors.append("context speculation is present")
    return errors


def next_stage_template_contract_errors(
    text: str,
    *,
    expected_stage: str,
    expected_method_prompt: str | None = None,
    expected_review_prompt: str | None = None,
) -> list[str]:
    """Validate that a reusable planning template can render the four-group contract."""
    errors: list[str] = []
    ordered_groups = r"Next-stage recommendation[\s\S]+Next lifecycle stage[\s\S]+Orchestration[\s\S]+Model[\s\S]+Execution requirements and contingencies"
    if not re.search(ordered_groups, text, flags=re.IGNORECASE):
        errors.append("missing ordered four-group next-stage recommendation")
    if f"Stage: `{expected_stage}`" not in text:
        errors.append(f"missing Stage: `{expected_stage}`")
    if not re.search(r"Method:[\s\S]*?Orchestration mode:[\s\S]*?Run in:[\s\S]*?Review:", text):
        errors.append("missing complete orchestration fields")
    if re.search(r"(?m)^Orchestration mode fit:", text):
        errors.append("contains noncanonical orchestration mode fit prompt")
    if expected_method_prompt is not None and f"Method: `{expected_method_prompt}`" not in text:
        errors.append(f"missing stage-appropriate Method prompt `{expected_method_prompt}`")
    if expected_review_prompt is not None and f"Review: `{expected_review_prompt}`" not in text:
        errors.append(f"missing stage-appropriate Review prompt `{expected_review_prompt}`")
    if not re.search(r"Generation:[\s\S]*?Capability tier:[\s\S]*?Reasoning:", text):
        errors.append("missing complete model fields")
    if not re.search(r"Run in:\s*`<same orchestration session / new orchestration session>`", text):
        errors.append("missing canonical Run in choices")
    if re.search(r"(?<!Orchestration )\bMode:", text):
        errors.append("uses shorthand Mode field")
    return errors


def assert_next_stage_summary() -> None:
    check_id = "presentation.next-stage-summary"
    models = ".agents/skills/dev-doc-harness/references/subagent-model-policy.md"
    freeze = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"
    architecture = ".agents/skills/dev-doc-harness/references/maintenance-architecture.md"
    readme = "README.md"
    header_sources = [
        ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.010.small.header-inputs.md",
        ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.010.phase.header-objective-inputs.md",
    ]
    handoff_sources = [
        (
            ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.small.handoff.md",
            "plan execution",
            "<execution method for plan execution>",
            "<execution Plan Task/final-review arrangement>",
        ),
        (
            ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.phase.handoff.md",
            "phase execution",
            "<execution method for phase execution>",
            "<execution Plan Task/final-review arrangement>",
        ),
    ]
    generated_plans = [
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
    ]
    staged_spec_source = ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.085.small.handoff.md"
    large_anchor_source = ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.060.large.phase-decomposition-model.md"
    large_anchor_readiness_source = ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.090.large.readiness-approval.md"
    small_readiness_source = ".agents/skills/dev-doc-harness/assets/templates/blocks/spec.090.small.readiness-approval.md"
    small_spec = ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md"
    large_spec = ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md"
    evidence_preservation_rule = "rule:" + "evidence.preservation"
    amendment_template = ".agents/skills/dev-doc-harness/assets/templates/plan-amendment.md"

    draft_fixture = """Current orchestration session: Resolved model profile `known suitable`; Context visibility: `material`\nContinuity rationale: Context risk: `immaterial`; Continuity benefit: `active repository investigation`\n\nNext-stage recommendation\nNext lifecycle stage: Stage: `plan execution`\nOrchestration: Method: `superpowers:subagent-driven-development`; Orchestration mode: `bounded delegated sub-agents`; Run in: same orchestration session; Review: Plan Task plus final reviewer\nModel: Generation: `latest available`; Capability tier: `balanced`; Reasoning: `medium`\nExecution requirements and contingencies: Load frozen package; authorization and material-variance stop apply"""
    frozen_fixture = draft_fixture.replace("Next-stage recommendation", "Approved next stage").replace("same orchestration session", "new orchestration session")
    invalid_fixture = draft_fixture.replace("same orchestration session", "same session")
    missing_run_in_fixture = draft_fixture.replace("; Run in: same orchestration session", "")
    shorthand_mode_fixture = draft_fixture.replace("Orchestration mode:", "Mode:")
    extra_mode_fit_fixture = draft_fixture.replace(
        "\nModel:", "\nOrchestration mode fit: `bounded review isolation without concurrent writes`\nModel:"
    )
    retired_fixture = draft_fixture.replace("Next lifecycle stage: Stage: `plan execution`", "Activity: First Plan Task: `TASK-001`")
    unknown_same_task_fixture = draft_fixture.replace(
        "Resolved model profile `known suitable`; Context visibility: `material`",
        "Resolved model profile `not exposed`; Context visibility: `material`",
    )
    mixed_draft_fixture = draft_fixture + "\nApproved next stage"
    mixed_frozen_fixture = frozen_fixture + "\nNext-stage recommendation"
    no_current_diagnostics_fixture = draft_fixture.split("\n\n", 1)[1].replace(
        "same orchestration session", "new orchestration session"
    )
    if next_stage_summary_fixture_errors(draft_fixture, frozen=False):
        add_failure(check_id, "valid draft summary fixture was rejected")
    if next_stage_summary_fixture_errors(frozen_fixture, frozen=True):
        add_failure(check_id, "valid frozen summary fixture was rejected")
    if next_stage_summary_fixture_errors(no_current_diagnostics_fixture, frozen=False):
        add_failure(check_id, "valid summary without optional current-session diagnostics was rejected")
    for stage in ["plan drafting", "phase-plan drafting", "plan execution", "phase execution", "documented resumed stage"]:
        stage_fixture = draft_fixture.replace("plan execution", stage)
        if stage in {"plan drafting", "phase-plan drafting"}:
            stage_fixture = stage_fixture.replace("superpowers:subagent-driven-development", "host-native planning").replace(
                "Plan Task plus final reviewer", "planning-review arrangement"
            )
        if next_stage_summary_fixture_errors(stage_fixture, frozen=False):
            add_failure(check_id, f"valid {stage} summary fixture was rejected")
    if not next_stage_summary_fixture_errors(invalid_fixture, frozen=False):
        add_failure(check_id, "invalid Run in fixture was accepted")
    if not next_stage_summary_fixture_errors(missing_run_in_fixture, frozen=False):
        add_failure(check_id, "missing Run in fixture was accepted")
    if not next_stage_summary_fixture_errors(shorthand_mode_fixture, frozen=False):
        add_failure(check_id, "shorthand Mode fixture was accepted")
    if not next_stage_summary_fixture_errors(extra_mode_fit_fixture, frozen=False):
        add_failure(check_id, "extra orchestration mode fit field fixture was accepted")
    if not next_stage_summary_fixture_errors(retired_fixture, frozen=False):
        add_failure(check_id, "retired task-level transition fixture was accepted")
    if not next_stage_summary_fixture_errors(unknown_same_task_fixture, frozen=False):
        add_failure(check_id, "unknown-profile same-session fixture was accepted")
    if not next_stage_summary_fixture_errors(mixed_draft_fixture, frozen=False):
        add_failure(check_id, "mixed draft state-label fixture was accepted")
    if not next_stage_summary_fixture_errors(mixed_frozen_fixture, frozen=True):
        add_failure(check_id, "mixed frozen state-label fixture was accepted")

    def draft_state_heading_errors(text: str) -> list[str]:
        headings = re.findall(r"(?m)^(#{2,3}) (Next-stage recommendation|Approved next stage)$", text)
        if headings != [("###", "Next-stage recommendation")]:
            return ["must render exactly one level-three draft next-stage heading"]
        return []

    duplicate_level_fixture = "## Next-stage recommendation\n\n### Next-stage recommendation\n"
    if not draft_state_heading_errors(duplicate_level_fixture):
        add_failure(check_id, "duplicate state heading at another Markdown level was accepted")

    for path in header_sources:
        text = read_repo_text(path)
        if len(re.findall(r"(?m)^Current orchestration session:", text)) != 1:
            add_failure(check_id, f"{path} must render one current-task metadata field")
        if re.search(r"(?m)^##+ Current orchestration session$", text):
            add_failure(check_id, f"{path} renders a current-task section instead of metadata")
        if re.search(r"(?m)^##+ Next-stage recommendation$", text):
            add_failure(check_id, f"{path} renders next-stage summary before handoff")
        assert_text_contains(check_id, path, r"Resolved model profile.+Context visibility", "compact current-session diagnostics")
        assert_text_contains(check_id, path, r"omit unless exposed and material", "current-session omission rule")
        assert_text_not_contains(check_id, path, r"Generation, capability tier, reasoning", "duplicated current-session model facets")

    strategy_source = ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.055.common.model-strategy.md"
    assert_text_contains(check_id, strategy_source, r"Upcoming-stage sub-agent assessment", "plan strategy assessment")
    assert_text_not_contains(check_id, strategy_source, r"Current planning Codex task", "duplicated plan current-task section")
    assert_text_not_contains(check_id, strategy_source, r"Next-stage recommendation", "duplicated plan next-stage summary")

    for path, expected_stage, expected_method_prompt, expected_review_prompt in handoff_sources:
        text = read_repo_text(path)
        for error in draft_state_heading_errors(text):
            add_failure(check_id, f"{path} {error}")
        assert_text_contains(check_id, path, r"rename it `### Approved next stage` at freeze", "freeze-time next-stage rename")
        for error in next_stage_template_contract_errors(
            text,
            expected_stage=expected_stage,
            expected_method_prompt=expected_method_prompt,
            expected_review_prompt=expected_review_prompt,
        ):
            add_failure(check_id, f"{path} {error}")

    governed_transition_templates = [
        (
            large_anchor_source,
            "phase-plan drafting",
            "<planning method for phase-plan drafting>",
            "<planning-review arrangement>",
        ),
        (
            amendment_template,
            "<documented resumed stage>",
            "<planning or execution method for Stage>",
            "<planning-review arrangement or execution Plan Task/final-review arrangement>",
        ),
    ]
    for path, expected_stage, expected_method_prompt, expected_review_prompt in governed_transition_templates:
        text = read_repo_text(path)
        for error in next_stage_template_contract_errors(
            text,
            expected_stage=expected_stage,
            expected_method_prompt=expected_method_prompt,
            expected_review_prompt=expected_review_prompt,
        ):
            add_failure(check_id, f"{path} {error}")
        if not next_stage_template_contract_errors(
            text.replace("Orchestration mode:", "Mode:", 1), expected_stage=expected_stage
        ):
            add_failure(check_id, f"{path} shorthand Orchestration mode mutation was accepted")
        run_in_line = "Run in: `<same orchestration session / new orchestration session>`; "
        if not next_stage_template_contract_errors(text.replace(run_in_line, "", 1), expected_stage=expected_stage):
            add_failure(check_id, f"{path} missing Run in mutation was accepted")
        model_heading = "\n### Model" if "\n### Model" in text else "\n#### Model"
        extra_mode_fit_text = text.replace(
            model_heading,
            f"\nOrchestration mode fit: `<why this topology fits>`\n{model_heading}",
            1,
        )
        if not next_stage_template_contract_errors(extra_mode_fit_text, expected_stage=expected_stage):
            add_failure(check_id, f"{path} extra orchestration mode fit mutation was accepted")

    assert_text_contains(
        check_id,
        staged_spec_source,
        r"staging reason[\s\S]*spec-only frozen package",
        "compact staged-spec exception facts",
    )
    assert_text_contains(
        check_id,
        staged_spec_source,
        r"Next lifecycle stage:\s*`plan drafting`",
        "staged-spec plan-drafting transition",
    )
    assert_text_not_contains(
        check_id,
        staged_spec_source,
        r"(?mi)^#{1,6}\s+Next-stage recommendation\s*$",
        "retired staged-spec next-stage recommendation",
    )
    assert_text_not_contains(
        check_id,
        staged_spec_source,
        r"(?mi)^#{1,6}\s+(?:Orchestration|Model|Execution requirements and contingencies|Method|Generation|Capability tier|Reasoning|Upcoming-stage sub-agent assessment)\s*$|^(?:Method:|Generation:|Capability tier:|Reasoning:|Upcoming-stage sub-agent assessment:)",
        "retired staged-spec next-stage summary fields",
    )

    for path in [small_readiness_source, large_anchor_readiness_source, small_spec, large_spec]:
        assert_text_contains(
            check_id,
            path,
            r"All relevant operator input is preserved in (?:this )?specification or through `module:evidence` and `"
            + re.escape(evidence_preservation_rule)
            + r"`",
            "operator-input preservation readiness check",
        )

    for rule_id in ["rule:models.selection-dimensions", "rule:models.orchestration-mode", "rule:models.next-stage-continuity"]:
        assert_text_contains(check_id, amendment_template, re.escape(rule_id), f"amendment template {rule_id} route")

    for path in generated_plans:
        text = read_repo_text(path)
        if len(re.findall(r"(?m)^Current orchestration session:", text)) != 1:
            add_failure(check_id, f"{path} must render one current-task metadata field")
        for error in draft_state_heading_errors(text):
            add_failure(check_id, f"{path} {error}")
        handoff_index = min((text.find(heading) for heading in ("## Implementation handoff", "## Phase implementation handoff") if heading in text), default=-1)
        summary_index = text.find("### Next-stage recommendation")
        if handoff_index < 0 or summary_index < handoff_index:
            add_failure(check_id, f"{path} places the next-stage summary before its handoff or transition")
        tasks_index = text.find("## Implementation tasks")
        checks_index = text.find("#### `CHECK-001`")
        if min(tasks_index, checks_index) < 0 or summary_index < max(tasks_index, checks_index):
            add_failure(check_id, f"{path} places the next-stage summary before implementation tasks or checks")

    large_spec = ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md"
    large_spec_text = read_repo_text(large_spec)
    if len(re.findall(r"(?m)^### Current orchestration session diagnostics$", large_spec_text)) != 1:
        add_failure(check_id, "large anchor spec no longer has its single current-task strategy presentation")
    if len(re.findall(r"(?m)^### Next-stage recommendation(?: \(draft only\))?$", large_spec_text)) != 1:
        add_failure(check_id, "large anchor spec no longer has its single next-stage strategy presentation")
    for path in [large_anchor_source, large_spec]:
        text = read_repo_text(path)
        for error in draft_state_heading_errors(text):
            add_failure(check_id, f"{path} {error}")
        assert_text_contains(
            check_id,
            path,
            r"rename it `### Approved next stage` at freeze",
            "large-anchor freeze-time next-stage rename",
        )
        assert_text_contains(
            check_id,
            path,
            r"Do not render both headings together",
            "large-anchor mutually exclusive state headings",
        )
    assert_text_contains(
        check_id,
        large_anchor_readiness_source,
        r"Next-stage recommendation[^\n]+relabeled `Approved next stage`",
        "large-anchor readiness relabel check",
    )

    assert_text_contains(check_id, models, r"Current orchestration session", "current orchestration session separation")
    assert_text_contains(check_id, models, r"Next-stage recommendation", "draft recommendation label")
    assert_text_contains(check_id, models, r"Next lifecycle stage[\s\S]*Orchestration[\s\S]*Model[\s\S]*Execution requirements and contingencies", "ordered next-stage groups")
    assert_text_contains(check_id, models, r"Stage:[^\n]+plan drafting[^\n]+phase-plan drafting", "canonical plan-drafting stage notation")
    assert_text_contains(check_id, freeze, r"Approved next stage", "frozen next-stage label")
    assert_text_contains(check_id, freeze, r"chat", "chat projection")
    assert_text_contains(check_id, models, r"Run in.*same orchestration session.*new orchestration session", "Run in values")
    assert_text_contains(check_id, models, r"Next lifecycle stage[\s\S]+Orchestration mode[\s\S]+Review[\s\S]+Plan Task[\s\S]+final review", "canonical reviewer terms")
    assert_text_contains(
        check_id,
        models,
        r"Orchestration and Model choices[^\n]+non-obvious[^\n]+rationale",
        "conditional whole-selection rationale",
    )
    required_notation = read_markdown_h2_section(models, "Required notation")
    if "Orchestration mode fit:" in required_notation:
        add_failure(check_id, "required notation adds an orchestration mode fit field")
    assert_text_not_contains(check_id, readme, r"Orchestration mode[^\n]+fit reason", "README extra mode-fit field")
    assert_text_contains(check_id, architecture, r"Task/session terminology", "models terminology catalog")

    draft_review = read_markdown_h2_section(freeze, "Draft review checkpoint")
    approval_freeze = read_markdown_h2_section(freeze, "Approval freeze checkpoint")
    if not re.search(r"Next-stage recommendation[\s\S]+Next lifecycle stage[\s\S]+Orchestration[\s\S]+Model[\s\S]+Execution requirements and contingencies", draft_review, flags=re.IGNORECASE):
        add_failure(check_id, "draft review does not own the four-group next-stage recommendation")
    owner_pattern = (
        re.escape("rule" + ":models.selection-dimensions")
        + r"[\s\S]+"
        + re.escape("rule" + ":lifecycle.stage-boundaries")
    )
    if not re.search(owner_pattern, draft_review, flags=re.IGNORECASE):
        add_failure(check_id, "draft review does not cite the selection and lifecycle owners")
    if not re.search(r"Next lifecycle stage[\s\S]+Stage:[\s\S]+Method[\s\S]+Orchestration mode[\s\S]+Run in[\s\S]+Review[\s\S]+Model[\s\S]+Generation[\s\S]+Capability tier[\s\S]+Reasoning", draft_review, flags=re.IGNORECASE):
        add_failure(check_id, "draft-review group definition is incomplete")
    if re.search(r"Orchestration mode with (?:its|a) fit reason", draft_review, flags=re.IGNORECASE):
        add_failure(check_id, "draft-review projection adds an orchestration mode fit field")
    assert_text_not_contains(check_id, freeze, r"documented non-execution transition that has no `Run in`", "no-Run-in continuity exception")
    assert_text_not_contains(check_id, freeze, r"same-task|new-task recommendation|current task", "retired continuity terminology")
    if not re.search(r"Draft review checkpoint[\s\S]+Approved next stage", approval_freeze, flags=re.IGNORECASE):
        add_failure(check_id, "approval freeze does not reference the draft-review group definition")
    if re.search(r"Next lifecycle stage[\s\S]+Orchestration[\s\S]+Execution requirements and contingencies", approval_freeze, flags=re.IGNORECASE):
        add_failure(check_id, "approval freeze repeats the full next-stage group definition")

    post_freeze = read_markdown_h2_section(freeze, "Post-freeze transition routing")
    if not re.search(r"effective next-stage values:\s*start with[^\n]+frozen[^\n]+Approved next stage[^\n]+apply[^\n]+explicit operator override", post_freeze, flags=re.IGNORECASE):
        add_failure(check_id, "execution handoff does not derive effective values from the frozen selection and operator override")
    if not re.search(r"(?:do not|without)[^\n]+rewrit[^\n]+frozen", post_freeze, flags=re.IGNORECASE):
        add_failure(check_id, "runtime override guidance does not preserve the frozen artifact")

    stateful_source_paths = [
        ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.small.handoff.md",
        ".agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.phase.handoff.md",
        large_anchor_source,
    ]
    stateful_generated_paths = [
        ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
        ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
        large_spec,
    ]
    state_heading_pattern = r"(?m)^#{2,3} (Next-stage recommendation|Approved next stage)$"
    for path in [*stateful_source_paths, *stateful_generated_paths]:
        headings = set(re.findall(state_heading_pattern, read_repo_text(path)))
        if headings == {"Next-stage recommendation", "Approved next stage"}:
            add_failure(check_id, f"{path} renders both draft and frozen next-stage headings")


def run_checks() -> None:
    for path in REQUIRED_FILES:
        assert_path_exists("paths.required-files", path)
    write_check_result("paths.required-files")

    owners, owner_rows = get_owner_graph()
    references = get_reference_records()
    assert_graph_references(owners, references)
    write_check_result("graph.references")

    assert_owner_heading_parser_contract()
    assert_owner_headings(owner_rows)
    write_check_result("graph.owner-headings")

    assert_template_routes()
    write_check_result("graph.template-routes")

    assert_route_contains("Classify work size", ["module:lifecycle", "rule:lifecycle.work-sizing"])
    assert_route_requires("Draft or review small/medium specs and plans", ["module:lifecycle", "module:naming", "module:quality", "module:models"], "router.required-routes")
    assert_route_requires("Draft or review large anchor specs", ["module:lifecycle", "module:naming", "module:quality", "module:models", "module:artifact-style"], "router.required-routes")
    assert_route_requires("Draft or review phase plans", ["module:naming", "module:quality", "module:lifecycle", "module:models"], "router.required-routes")
    assert_route_contains("Freeze planning packages", ["module:freeze-gate", "module:lifecycle"])
    assert_route_contains(
        "Execute approved work and record variance",
        ["module:lifecycle", "module:execution-quality", "rule:models.execution-review-contract"],
    )
    assert_route_contains("Use or review sub-agent strategy", ["module:models", "rule:models.strategy-required"])
    assert_route_contains("Evidence-heavy review or reports", ["module:evidence"])
    assert_route_contains("Release, package, or team adoption work", ["module:release"])
    assert_route_contains("Update templates or router guidance", ["module:architecture"])
    assert_route_contains("Superpowers or spec-kit compatibility", ["module:lifecycle"])
    write_check_result("router.required-routes")

    assert_route_budgets()
    write_check_result("router.route-budget")

    assert_router_maintenance_architecture()
    write_check_result("router.maintenance-architecture")

    assert_route_contains("Release, package, or team adoption work", ["module:release"], "release.route")
    write_check_result("release.route")

    discoverability = [
        {"path": ".agents/skills/dev-doc-harness/SKILL.md", "pattern": "Classify work size", "label": "work sizing"},
        {"path": ".agents/skills/dev-doc-harness/references/naming-conventions.md", "pattern": "rule:naming.work-item-paths", "label": "naming convention owner"},
        {"path": ".agents/skills/dev-doc-harness/SKILL.md", "pattern": "Planning Artifact Freeze Gate", "label": "planning freeze gates"},
        {"path": ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md", "pattern": "stop before implementation", "label": "stop before implementation"},
        {"path": ".agents/skills/dev-doc-harness/references/artifact-contract.md", "pattern": "Immutable snapshots", "label": "immutable snapshots"},
        {"path": ".agents/skills/dev-doc-harness/references/artifact-contract.md", "pattern": "Variance policy", "label": "variance and amendments"},
        {"path": ".agents/skills/dev-doc-harness/references/implementation-changelog.md", "pattern": "before implementation commits", "label": "implementation changelog before commit"},
        {"path": ".agents/skills/dev-doc-harness/references/artifact-contract.md", "pattern": "Documentation assessment", "label": "documentation assessment"},
        {"path": ".agents/skills/dev-doc-harness/SKILL.md", "pattern": "Superpowers compatibility", "label": "Superpowers compatibility"},
        {"path": ".agents/skills/dev-doc-harness/references/maintenance-architecture.md", "pattern": "Historical artifacts are tracked documentation", "label": "historical artifact handling"},
    ]
    for topic in discoverability:
        assert_text_contains("discoverability.safety", topic["path"], topic["pattern"], topic["label"])
    assert_agents_bootstrap_contract()
    write_check_result("discoverability.safety")

    assert_skill_openai_metadata()
    write_check_result("skill.openai-metadata")

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
        ".agents/skills/dev-doc-harness/references/maintenance-architecture.md",
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
            {"path": "AGENTS.md", "pattern": r"very small mechanical edits[\s\S]+(?:skip|without) durable artifacts", "label": "root sizing summary"},
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
            {"path": ".agents/skills/dev-doc-harness/references/implementation-changelog.md", "pattern": "before an implementation commit", "label": "implementation changelog expectation"},
        ],
    )
    assert_scenario_evidence(
        "scenario:variance.high-impact-amendment",
        [
            {"path": ".agents/skills/dev-doc-harness/references/artifact-contract.md", "pattern": "<amendment-filename>", "label": "amendment path"},
            {"path": ".agents/skills/dev-doc-harness/references/naming-conventions.md", "pattern": "plan_amendment-NN", "label": "amendment filename grammar"},
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
            {"path": "AGENTS.md", "pattern": r"docs/superpowers[\s\S]+only when[\s\S]+already exists[\s\S]+previous documentation packages", "label": "root continuity gate"},
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
            {"path": ".agents/skills/dev-doc-harness/references/maintenance-architecture.md", "pattern": "Historical artifacts are tracked documentation", "label": "historical handling"},
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

    assert_documentation_assessment_contract()
    write_check_result("documentation.assessment")

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

    assert_harness_simplification_scenarios()
    write_check_result("scenarios.harness-simplification")

    assert_superpowers_adapter_contract()
    write_check_result("compat.superpowers-adapter-contract")

    assert_execution_method_fallbacks()
    write_check_result("execution.method-fallbacks")

    assert_planning_template_clarity()
    write_check_result("clarity.planning-template-contract")

    assert_combined_package_default()
    write_check_result("lifecycle.combined-package-default")

    assert_next_stage_summary()
    write_check_result("presentation.next-stage-summary")


def main() -> int:
    run_checks()
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
