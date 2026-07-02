## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during spec and phase-plan review, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets.

Anchor spec approval:

1. Planned subject: `<planning-commit-subject>`.
2. Changelog title or snippet: `<changelog-heading>`.
3. Notes: `Approval commit for this anchor spec.`

Phase plan approval pattern:

1. Planned subject: `<planning-commit-subject>`.
2. Changelog title or snippet: `<changelog-heading>`.
3. Notes: `Replace or refine in each concrete phase plan.`

Implementation pattern:

1. Planned subject: `<commit-subject>`.
2. Changelog title or snippet: `<changelog-heading>`.
3. Notes: `Replace with concrete rows in phase plans.`

## Planning artifact freeze gates

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.multi-gate-flow`.

Record the draft review, approval commit or handoff snapshot, and pause before implementation, later phase-plan drafting, or later phase execution. The initial planning package is anchor-spec-only by default under `rule:lifecycle.large-phase-orchestration`; do not create concrete phase-plan files during this package unless the operator explicitly requests combined planning.
