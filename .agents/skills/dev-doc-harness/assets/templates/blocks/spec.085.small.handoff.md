## Planning shape and transition ownership

Use `rule:lifecycle.planning-shape`, `rule:models.execution-continuity`, `rule:freeze.approval-freeze`, and `rule:execution-quality.execution-thread-start`.

Default combined package:

1. Planning shape: `combined small/medium`.
2. Companion plan: `<plan-filename>` is drafted and presented with this spec in the same planning turn.
3. Transition owner: `<plan-filename>` owns the implementation handoff after the combined package freezes.
4. Next activity: `<implementation activity named by the approved plan>`.

For an explicit staged spec-only exception, record the operator-requested or
operator-approved staging reason, the spec-only frozen package, and `plan drafting`
as the next activity. Do not duplicate the later plan's implementation handoff here.
