## Task Plan

Write one section per implementation, test, validation, documentation, or handoff task. Tasks should be SMART:

1. Specific enough that a fresh implementation agent or delegated sub-agent knows which files, behavior, tests, docs, or decisions are in scope.
2. Measurable through a linked acceptance criterion, validation command, review finding, or explicit artifact update.
3. Achievable within the approved scope and one orchestration thread with bounded delegation.
4. Relevant to the approved spec, phase objective, acceptance criterion, risk, interface, documentation need, or commit boundary.
5. Time-bounded by lifecycle checkpoint, such as before editing, before validation, before commit, or during final review.

Order tasks by implementation dependency and reviewability. Use a stable task ID in each `###` heading. Each task must include `Dependencies`, `Implementation`, and `Exit criteria`. Add `Notes` only when the task needs boundaries, gotchas, risk-specific guidance, or optional per-task traceability that is not already clear from the `Spec Traceability` matrix.

Do not force vertical slices when shared setup, tests, refactors, or interface updates need to happen first.

### `T-001` `<short imperative task title>`

Dependencies:

1. `<None, task ids, artifacts, prior phase, or external event>`.

Implementation:

1. `<specific implementation, test, validation, documentation, or handoff step with files/scope>`.
2. `<next concrete step, or remove this row when not needed>`.

Exit criteria:

1. `<observable completion signal, validation result, review finding, or artifact update>`.

Notes:

1. `<optional boundary, gotcha, risk-specific guidance, or per-task trace IDs when useful>`.

### `T-002` `<short imperative task title>`

Dependencies:

1. `<T-001 or None>`.

Implementation:

1. `<specific validation, documentation, changelog, or review task with files/scope>`.

Exit criteria:

1. `<observable completion signal, validation result, review finding, or artifact update>`.
