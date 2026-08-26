# Lean/Small Flow Test Cases

Work ID: `2026-08-21_lean-small-flow`
Status: Approved

| Scenario | Input | Method | Expected result |
|---|---|---|---|
| `scenario:planning.lean-small-auto` | Bounded low-risk work with a known local change surface | Inspect lifecycle sizing rule and run focused policy-validator scenario | The router selects `lean/small`; the selected route names its compact inputs and combined package. |
| `scenario:planning.lean-small-override` | Explicit operator request for lean/small work | Inspect lifecycle override rule and validator assertion | The operator may select `lean/small` without renaming established flows. |
| `scenario:planning.lean-small-escalation` | Lean work that reveals material interface, migration, security, architecture, or uncertainty risk | Inspect lifecycle/freeze rules and validator assertion | The work escalates to small/medium or large/phased before freeze; it does not silently remain lean. |
| `scenario:templates.lean-small-compact` | Lean manifests, blocks, and generated templates | Run assembler freshness check and template assertions | Two generated lean templates use only lean blocks and retain statuses, `SPEC`/`VER`/`TASK`/`CHECK` links, validation, and approval state. |
| `scenario:templates.lean-small-exclusions` | Lean router and generated templates | Run negative-reference validator assertions | No model policy, role examples, artifact style, implementation changelog, model strategy, handoff, or excluded current small/medium block semantics are required or rendered. |
| `scenario:freeze.lean-small-equivalence` | Lean draft and freeze policy | Inspect freeze branch and run validator | Lean retains draft review, operator approval, approval commit, immutable snapshot, and pause-before-implementation mechanics without frozen model/sub-agent selection. |
| `scenario:lifecycle.large-policy-isolation` | Lifecycle core and new large-only reference | Search rule owners and run validator | Detailed large layout and both existing large rule IDs have one new large-only owner; large callers preserve behavior. |
| `scenario:compat.existing-flow-preservation` | Existing small/medium and large template/route assertions | Run full policy validator | Existing assertions continue to pass; lean coverage is additive and no flow registry refactor is required. |
| `scenario:history.lean-small-preservation` | Final implementation diff | Run `git diff --check` and inspect `git diff --name-only` | No frozen historical work item, release note, or `CHANGELOG.md` history is rewritten; no whitespace errors exist. |

## TASK-004 acceptance coverage

`CHECK-004` records the full policy-validator and template-freshness output, whitespace check, and name-only historical-preservation review in the task execution report. The scenarios above are the durable evidence matrix for `VER-001` through `VER-005`.
