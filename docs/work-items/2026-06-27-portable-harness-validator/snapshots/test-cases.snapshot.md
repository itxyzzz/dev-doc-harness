# Portable Harness Validator Test Cases Snapshot

Work ID: `2026-06-27-portable-harness-validator`
Short ID: `portable-harness-validator`
Status: Approved
Harness release: `0.3.0`
Policy references: `module:lifecycle`, `module:quality`, `module:execution-quality`

## Current pass contract

The current PowerShell validator passes on branch `cross-platorm-script` with this output:

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

## Required validation cases

| Case | Command or action | Expected result |
|---|---|---|
| PowerShell baseline before deletion | `powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` | Exit code `0`; output matches the current pass contract. |
| Python syntax | `python -m py_compile .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | Exit code `0`; no output. |
| Python parity before deletion | `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | Exit code `0`; output contains the same check IDs in the same order as the PowerShell baseline. |
| Python final validation after deletion | `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | Exit code `0`; output contains the same current pass contract and no `FAIL` lines. |
| Current-surface stale reference scan | `rg -n "Test-HarnessPolicy|powershell -NoProfile|pwsh .*Test-HarnessPolicy|\.ps1" README.md AGENTS.md .agents/skills/dev-doc-harness` | No active current-surface references to the removed PowerShell validator command. |
| Historical preservation review | Inspect `git diff -- docs/work-items` | No frozen historical artifact is rewritten solely to replace old PowerShell command examples. |
| Dependency review | Inspect imports in `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | Imports come only from Python standard-library modules. |

## Failure evidence cases

Implementation should preserve failure behavior through at least one temporary local mutation before final diff review. The mutation must be reverted before completion.

| Case | Temporary mutation | Expected result |
|---|---|---|
| Missing required file | Temporarily point one required current-surface path in the Python validator to a path that does not exist. | Validator prints `FAIL paths.required-files: Missing path:` or `FAIL paths.required-files: Missing file before read:` and exits nonzero. |
| Stale route target | Temporarily point one route assertion to a missing path or check label. | Validator prints the matching route or graph failure and exits nonzero. |
| Placeholder detection | Temporarily add a forbidden marker to a current-surface file, then revert it. | Validator prints `FAIL placeholders.current-surfaces:` and exits nonzero. |

## Review expectations

- Parity is based on check IDs, order, exit code, and representative failure behavior, not only on a successful final run.
- The Python validator must normalize repository-relative paths to forward slashes in diagnostics.
- Historical work-item artifacts remain historical evidence and are not part of stale active-command cleanup.
