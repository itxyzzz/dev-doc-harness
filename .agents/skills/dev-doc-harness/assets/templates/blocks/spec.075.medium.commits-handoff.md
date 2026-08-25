## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned implementation subjects are reviewable during spec and plan review.

| Stage | Planned subject |
|---|---|
| Planning approval | `<planning-commit-subject>` |
| Implementation | `<commit-subject>` |

Use one cohesive implementation commit by default. Record an essential deferral
or independently reviewable split as concise prose under this table.

## Planning shape and transition ownership

Use `rule:lifecycle.planning-shape`, `rule:models.next-stage-continuity`, `rule:freeze.approval-freeze`, and `rule:execution-quality.execution-thread-start`.

Default combined package:

1. Planning shape: `combined medium`.
2. Companion plan: `<plan-filename>` is drafted and presented with this spec in the same planning turn.
3. Transition owner: `<plan-filename>` owns the `plan execution` transition after the combined package freezes.
4. Next lifecycle stage: `plan execution`.
