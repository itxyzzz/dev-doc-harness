# Portable Harness Validator Spec

Work ID: `2026-06-27-portable-harness-validator`
Short ID: `portable-harness-validator`
Status: Approved
Harness release: `0.3.0`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:quality`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:quality.spec-handoff`

## Goal

Replace the current PowerShell-only harness validator with a Python standard-library validator so harness maintenance validation runs on Windows, macOS, and Linux without requiring PowerShell.

## Scope

- Create `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` as the canonical validator implementation.
- Preserve the current validator output contract: one `PASS <check-id>` line per passing check, one `FAIL <check-id>: <detail>` line per failure detail, and nonzero process exit when any check fails.
- Preserve the current set of check IDs:
  - `paths.required-files`
  - `graph.references`
  - `graph.owner-headings`
  - `graph.template-routes`
  - `router.required-routes`
  - `router.route-budget`
  - `release.route`
  - `discoverability.safety`
  - `phrases.duplicated-policy`
  - `phrases.duplicate-blocks`
  - `placeholders.current-surfaces`
  - `tracking.work-items`
  - `scenarios.golden-traversal`
  - `release.identity`
  - `release.notes`
  - `release.changelog-schema`
  - `release.package-boundary`
  - `release.template-context`
- Use the existing `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` only as a parity oracle during implementation.
- Remove `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` after the Python validator proves parity.
- Update current harness guidance that names the validation command, including `.agents/skills/dev-doc-harness/SKILL.md`, `README.md`, and `.agents/skills/dev-doc-harness/docs/operator-note.md`.
- Update validator-internal current-surface lists and stale-reference checks so current harness surfaces point at the Python command.

## Non-scope

- No new validator check families beyond the behavior needed to preserve the current check contract.
- No semantic parser for plan quality, operator judgment, policy interpretation, or approval state.
- No permanent PowerShell wrapper.
- No rewrite of frozen historical work-item artifacts solely to replace historical PowerShell command examples.
- No Python package, dependency manager, virtual environment, or third-party library requirement.
- No release-note publication beyond the normal changelog and existing release-note source flow.

## Current state

The repository's canonical harness validation command is:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1
```

The command currently passes on this branch with these check lines:

```text
PASS paths.required-files
PASS graph.references
PASS graph.owner-headings
PASS graph.template-routes
PASS router.required-routes
PASS router.route-budget
PASS release.route
PASS discoverability.safety
PASS phrases.duplicated-policy
PASS phrases.duplicate-blocks
PASS placeholders.current-surfaces
PASS tracking.work-items
PASS scenarios.golden-traversal
PASS release.identity
PASS release.notes
PASS release.changelog-schema
PASS release.package-boundary
PASS release.template-context
```

The current script is PowerShell-only and lives at `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`. Current operator-facing docs name that path directly, so the migration changes a public harness maintenance interface.

## Proposed behavior

The canonical validation command becomes:

```bash
python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py
```

The Python validator uses only Python standard-library modules and derives the repository root from the script location. It reads the same current harness surfaces, builds the same owner and reference evidence, applies the same structural checks, prints the same current check IDs, and exits with status `0` only when every check passes.

Implementation proceeds in two safe phases inside one work item:

1. Port the validator to Python while keeping the PowerShell script available for side-by-side parity validation.
2. After parity is demonstrated, delete the PowerShell script and update current harness guidance to make Python the only supported validator command.

Historical frozen work-item artifacts may continue to mention `Test-HarnessPolicy.ps1` as historical evidence. Current reusable policy and operator guidance must not present the PowerShell command as the active validator after the migration.

## Interfaces and data

- Added command interface: `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
- Removed command interface: `powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`.
- Added repository file: `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
- Removed repository file: `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`.
- Changed current documentation surfaces:
  - `.agents/skills/dev-doc-harness/SKILL.md`
  - `README.md`
  - `.agents/skills/dev-doc-harness/docs/operator-note.md`
- Changed validator self-reference data from the PowerShell script path to the Python script path.
- No persistent data, external API, network access, secrets, credentials, or runtime configuration are introduced.

## Risks

- A porting error could silently weaken a structural validation check if parity is checked only by success or failure instead of check-level output and targeted mutation tests.
- Python's regular expression, newline, path, and case-sensitivity behavior differs from PowerShell and must be normalized deliberately.
- Deleting the PowerShell script can break copied commands in downstream notes, so current docs need clear Python guidance and historical docs must remain recognizable as historical.
- The validator is part of the distributable harness package, so the change affects adopters who copy root `AGENTS.md` and `.agents/`.

## Acceptance criteria

- `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` exits `0` and prints all current `PASS` check IDs listed in this spec.
- Before the PowerShell script is deleted, Python validator output has the same pass/fail check ID sequence as the current PowerShell validator on the unchanged current surfaces.
- The Python validator uses only Python standard-library imports.
- `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` is removed before implementation completion.
- Current harness guidance names the Python validator command and does not present the PowerShell command as the active validator.
- Frozen historical work-item artifacts are not rewritten solely to replace historical PowerShell examples.
- `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md` explain that the validator remains a lightweight structural check, not a replacement for operator approval or engineering judgment.
- `CHANGELOG.md` includes a newest-first implementation entry with release target, package impact, and release-note fields before the implementation commit.

## Planned commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `portable-harness-validator spec: plan portable harness validator` | `2026-06-27-portable-harness-validator: plan portable harness validator` | Approval commit for this spec, plan, and required snapshots. |
| Implementation | `portable-harness-validator refactor: replace PowerShell validator with Python` | `2026-06-27-portable-harness-validator: replace PowerShell validator with Python` | Port the validator, prove parity, remove the PowerShell script, and update current docs. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Add planning approval entry during the freeze gate and implementation entry before implementation commit. |
| Test cases | Snapshot | Yes | Before implementation | `snapshots/test-cases.snapshot.md` | Capture current pass checks, parity validation, stale-reference checks, and Python-only dependency expectations. |
| Testing guide delta | Living delta | Yes | During implementation | `deltas/testing-guide.delta.md` | Record the new Python validation command and expected output. |
| Operator manual delta | Living delta | Yes | During implementation | `deltas/operator-manual.delta.md` | Record operator-facing validation command changes for harness adopters. |
| API reference delta | Living delta | No | Not applicable | Not applicable | No public API, schema, or data contract is changed. |
| Architecture snapshot | Snapshot | Yes | Before implementation | `snapshots/architecture.snapshot.md` | Capture the validator boundary, parity-first migration, and current-surface update policy. |
| Architecture summary delta | Living delta | Yes | During implementation | `deltas/architecture-summary.delta.md` | Record that the validator is Python-based, structural, and standard-library only. |

## Approval

- Status: Approved
- Superseded by: record only when this artifact is superseded
