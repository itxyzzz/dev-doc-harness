## Validation Plan

| Command | Expected result |
|---|---|
| `<exact command, manual check, review finding, or operator acceptance path>` | `<expected signal and linked AC/risk/phase coverage>` |

Every validation entry must state the expected signal before implementation starts. Add command exit behavior, important output text, manual observation, review criterion, or operator acceptance condition as applicable.

## Plan variance handling

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

Record the draft review, approval commit, and post-freeze implementation authorization status for this plan.
