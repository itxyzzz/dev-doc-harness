## Planning shape and transition ownership

Use `rule:lifecycle.planning-shape`, `rule:models.next-stage-continuity`, `rule:freeze.approval-freeze`, and `rule:execution-quality.execution-thread-start`.

Default combined package:

1. Planning shape: `combined medium`.
2. Companion plan: `<plan-filename>` is drafted and presented with this spec in the same planning turn.
3. Transition owner: `<plan-filename>` owns the `plan execution` transition after the combined package freezes.
4. Next lifecycle stage: `plan execution`.

For an explicit staged spec-only exception:

1. Staging reason: `<operator-requested or operator-approved staging reason>`.
2. Spec-only frozen package: `<spec-filename>`.
3. Next lifecycle stage: `plan drafting`.
