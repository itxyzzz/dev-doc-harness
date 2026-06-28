# Portable Harness Validator Plan

Work ID: `2026-06-27-portable-harness-validator`
Short ID: `portable-harness-validator`
Status: Approved
Harness release: `0.3.0`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Implementation summary

Replace the PowerShell validator with a Python standard-library implementation while using the existing PowerShell script as a temporary parity oracle. The implementation should first add and run the Python validator beside the PowerShell validator, compare the current check ID sequence, then remove the PowerShell script and update current reusable harness surfaces to name Python as the canonical command.

The Python script should keep the current validation model: structural, graph-oriented, high-signal checks over current harness surfaces. It should not become a broad semantic parser for planning quality or approval judgment. The implementation should preserve the exact current check IDs and output style so existing review expectations remain stable while the command becomes cross-platform.

## Files and interfaces

- Create `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: canonical Python validator.
- Delete `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`: old PowerShell validator after parity is proven.
- Modify `.agents/skills/dev-doc-harness/SKILL.md`: route current harness validation to the Python script.
- Modify `README.md`: replace the active PowerShell validation command with the Python command.
- Modify `.agents/skills/dev-doc-harness/docs/operator-note.md`: replace the package-local active validation command with the Python command.
- Create `docs/work-items/2026-06-27-portable-harness-validator/deltas/testing-guide.delta.md`: proposed long-lived testing guidance update.
- Create `docs/work-items/2026-06-27-portable-harness-validator/deltas/operator-manual.delta.md`: proposed operator guidance update.
- Create `docs/work-items/2026-06-27-portable-harness-validator/deltas/architecture-summary.delta.md`: proposed architecture summary update.
- Create `docs/work-items/2026-06-27-portable-harness-validator/implementation-notes/variance-log.md`: implementation variance record.
- Modify `CHANGELOG.md`: add planning approval entry at freeze and implementation entry before implementation commit.

The supported validator interface after implementation is:

```bash
python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py
```

The unsupported validator interface after implementation is:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1
```

## Model and Sub-agent Strategy

Current orchestration: GPT-5 Codex, reasoning effort not explicitly exposed in this thread.
Fit assessment: The work is a moderate-risk harness maintenance migration. The main risk is behavioral drift in a validation script that guards current policy surfaces. Budget and latency are less important than preserving parity and reviewability, but the task is bounded to one script plus documentation surfaces.
Recommended change: None before implementation. Use the active repository `economy-default` policy; escalate only for final review or if parity failures are subtle.

| Purpose | Context strategy | Input context | Output artifact | Model policy | Model class/profile | Reasoning effort | Reason | Parallel? | Blast radius if wrong |
|---|---|---|---|---|---|---|---|---|---|
| Final migration review | curated artifacts | Approved spec, approved plan, Python validator diff, docs diff, validation output, variance log | Review findings in implementation handoff or chat | active repository policy | latest strongest | high | Validator parity errors can weaken harness review gates | No | Medium: broken or weakened harness validation in copied packages |

Fresh confirmation is required before using this sub-agent strategy because implementation cannot begin until after the freeze gate and fresh operator authorization.

## Tasks

- [ ] Before implementation, read `spec-portable-harness-validator.md`, this plan, `snapshots/test-cases.snapshot.md`, `snapshots/architecture.snapshot.md`, `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`, `.agents/skills/dev-doc-harness/references/policy-architecture.md`, `.agents/skills/dev-doc-harness/SKILL.md`, `README.md`, and `.agents/skills/dev-doc-harness/docs/operator-note.md`.
- [ ] Run the current PowerShell validator to establish the parity oracle:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1
```

Expected result: exit code `0` and the 17 `PASS` lines captured in `snapshots/test-cases.snapshot.md`.

- [ ] Create `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` with standard-library-only structure:

```python
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import sys


@dataclass(frozen=True)
class Failure:
    check_id: str
    detail: str


REPO_ROOT = Path(__file__).resolve().parents[4]
FAILURES: list[Failure] = []

KNOWN_CHECK_IDS = [
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
```

- [ ] Port path and text helpers so all repository paths use forward-slash repo-relative strings in diagnostics:

```python
def join_repo_path(path: str) -> Path:
    return REPO_ROOT / path


def read_repo_text(path: str, check_id: str = "paths.required-files") -> str:
    full_path = join_repo_path(path)
    if not full_path.exists():
        add_failure(check_id, f"Missing file before read: {path}")
        return ""
    return full_path.read_text(encoding="utf-8")


def add_failure(check_id: str, detail: str) -> None:
    FAILURES.append(Failure(check_id=check_id, detail=detail))


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
```

- [ ] Port the static file lists from the PowerShell script into Python constants, changing current validator self-references from `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` to `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` only after the deletion task.
- [ ] Port owner graph construction with Python dictionaries keyed by owner kind (`module`, `rule`, `schema`, `scenario`, `metric`) and preserve the current regular expression evidence for module declarations, rule owner rows, schema anchors, and scenario or metric anchors.
- [ ] Port graph reference checks into `assert_graph_references()` so every current reference collected from router rows, template policy references, README route tables, validation documentation, and validator check definitions has an owner in the current owner graph.
- [ ] Port owner-heading checks into `assert_owner_headings()` so every rule owner-table row that names a local heading points at a heading that exists in the owning reference file.
- [ ] Port template-route checks into `assert_template_routes()` so each current template's `Policy references:` line includes the modules required by the matching operation route.
- [ ] Port required-route checks into `assert_route_contains(check_id: str, path: str, expected_pattern: str, label: str)` so the Python validator can report the same missing-route details for router and release-route evidence.
- [ ] Port route-budget checks into `assert_route_budgets()` so routine routes stay within the architecture budget and freeze or execution routes use the allowed expanded budget only where current policy permits it.

- [ ] Port discoverability, duplicate-phrase, duplicate-block, placeholder, tracking, golden-traversal, release-identity, release-notes, release-changelog-schema, release-package-boundary, and release-template-context checks with the same check IDs and failure messages unless Python path normalization requires an equivalent forward-slash path.
- [ ] Add a `main()` function that runs checks in the same order as the current PowerShell script and exits `1` when any failure exists:

```python
def main() -> int:
    run_checks()
    for check_id in KNOWN_CHECK_IDS:
        write_check_result(check_id)
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] Run Python syntax validation:

```bash
python -m py_compile .agents/skills/dev-doc-harness/scripts/test_harness_policy.py
```

Expected result: exit code `0` and no output.

- [ ] Run the Python validator before deleting the PowerShell script:

```bash
python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py
```

Expected result: exit code `0` and the same 17 `PASS` check IDs as the PowerShell oracle.

- [ ] Compare the PowerShell and Python check ID sequence before deleting the PowerShell script. On Windows, use:

```powershell
$ps = powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1
$py = python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py
Compare-Object $ps $py
```

Expected result: no output.

- [ ] Update `.agents/skills/dev-doc-harness/SKILL.md` so the `Validate current harness surfaces` router row points to `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` and says to run the Python command.
- [ ] Update `README.md` so the harness maintenance validation command is:

```bash
python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py
```

- [ ] Update `.agents/skills/dev-doc-harness/docs/operator-note.md` so package-local validation guidance uses the Python command.
- [ ] Update `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` current-surface lists and required-file checks so the Python script is required and the PowerShell script is no longer required.
- [ ] Delete `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`.
- [ ] Search current reusable surfaces for stale active PowerShell validator references:

```bash
rg -n "Test-HarnessPolicy|powershell -NoProfile|pwsh .*Test-HarnessPolicy|\.ps1" README.md AGENTS.md .agents/skills/dev-doc-harness
```

Expected result: no active validation-command references to `Test-HarnessPolicy.ps1`; frozen historical docs under `docs/work-items` are outside this command and may retain historical examples.

- [ ] Create `deltas/testing-guide.delta.md` with the Python validation command, expected pass-check output, and the note that the validator remains structural.
- [ ] Create `deltas/operator-manual.delta.md` with the operator-facing command migration from PowerShell to Python.
- [ ] Create `deltas/architecture-summary.delta.md` with the architecture note that validator implementation is Python standard-library code and remains graph-oriented and high-signal.
- [ ] Create `implementation-notes/variance-log.md` from the harness variance template and record no variance if implementation follows this plan.
- [ ] Update `CHANGELOG.md` before the implementation commit with:

```md
## 2026-06-27-portable-harness-validator: replace PowerShell validator with Python

Release target: `unreleased`
Package impact: `distributable`
Release-note: `include`

### Changed

- Replaced the PowerShell-only harness validator with a Python standard-library validator and updated current harness validation guidance to use the cross-platform command.
```

- [ ] Run final syntax validation:

```bash
python -m py_compile .agents/skills/dev-doc-harness/scripts/test_harness_policy.py
```

Expected result: exit code `0` and no output.

- [ ] Run final harness validation:

```bash
python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py
```

Expected result: exit code `0`, all 17 current `PASS` check IDs, and no `FAIL` lines.

- [ ] Review the diff and confirm only planned files changed, with no edits to frozen historical work-item artifacts solely for command migration.
- [ ] Commit the implementation with:

```bash
git add .agents/skills/dev-doc-harness/scripts/test_harness_policy.py .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1 .agents/skills/dev-doc-harness/SKILL.md README.md .agents/skills/dev-doc-harness/docs/operator-note.md CHANGELOG.md docs/work-items/2026-06-27-portable-harness-validator
git commit -m "portable-harness-validator refactor: replace PowerShell validator with Python"
```

Expected result: one implementation commit after the planning freeze gate and fresh operator authorization.

## Planned commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `portable-harness-validator spec: plan portable harness validator` | `2026-06-27-portable-harness-validator: plan portable harness validator` | Approval commit for spec, plan, and snapshots. |
| Implementation | `portable-harness-validator refactor: replace PowerShell validator with Python` | `2026-06-27-portable-harness-validator: replace PowerShell validator with Python` | Port, validate, remove PowerShell, update docs and deltas. |

## Validation commands

| Command | Expected result |
|---|---|
| `powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` | Pre-migration parity oracle exits `0` and prints the 17 current `PASS` check IDs. |
| `python -m py_compile .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | Exits `0` and prints no output. |
| `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | Exits `0`, prints all 17 current `PASS` check IDs, and prints no `FAIL` lines. |
| `rg -n "Test-HarnessPolicy|powershell -NoProfile|pwsh .*Test-HarnessPolicy|\.ps1" README.md AGENTS.md .agents/skills/dev-doc-harness` | Finds no active current-surface references to the removed PowerShell validator command. |
| `git diff --name-only` | Before implementation staging, contains only the planned validator, docs, changelog, deltas, variance log, and work-item files. |

## Plan variance handling

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

Draft review status: completed; operator approved the staged planning package.
Approval commit status: completed by the plan-only approval commit.
Post-freeze implementation authorization: not authorized.

## Completion criteria

- Acceptance criteria in `spec-portable-harness-validator.md` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- `CHANGELOG.md` has newest-first entries for planning approval and implementation before each matching commit.
- Commit subjects match the approved planned subjects or recorded variance, and changelog title snippets are synchronized.
- Variance log is present and current.
- De-facto sub-agent use is reported if the final migration review sub-agent is authorized and used.

## Approval

- Status: Approved
- Superseded by: record only when this artifact is superseded
