## Planning shape and transition ownership

Use `rule:lifecycle.planning-shape`, `rule:models.execution-continuity`, `rule:freeze.approval-freeze`, and `rule:execution-quality.execution-thread-start`.

Default combined package:

1. Planning shape: `combined small/medium`.
2. Transition owner: `<plan-filename>` owns the implementation handoff after the combined package freezes.
3. Next activity: `<implementation activity named by the approved plan>`.

For an explicitly approved staged spec-only exception, record the staging reason,
the spec-only frozen package, and `plan drafting` as the next activity. Do not
duplicate the later plan's implementation handoff here.
