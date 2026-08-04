## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned implementation subjects are reviewable during spec and phase-plan review.

| Stage | Planned subject |
|---|---|
| Anchor spec approval | `<planning-commit-subject>` |
| Phase-plan approval pattern | `<planning-commit-subject>` |
| Phase implementation pattern | `<commit-subject>` |

## Planning artifact freeze gates

At draft review or approval, use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.multi-gate-flow`.

Record the draft review, approval commit, and pause before the documented next lifecycle stage. The initial planning package is anchor-spec-only by default under `rule:lifecycle.large-phase-orchestration`; do not create concrete phase-plan files during this package unless the operator explicitly requests combined planning.
