## Implementation Tasks

Write one section per implementation, test, validation, documentation, or handoff task. Tasks should be SMART:

1. Specific enough that a fresh implementation agent or delegated sub-agent knows which files, behavior, tests, docs, or decisions are in scope.
2. Measurable through a linked Specification Commitment, Verification Criterion, Plan Check, review finding, or explicit artifact update.
3. Achievable within the approved scope and one orchestration thread with bounded delegation.
4. Relevant to the approved Specification Commitments, mapped Architecture Decisions, Verification Criteria, risk, interface, documentation need, or Plan Check enablement.
5. Time-bounded by lifecycle checkpoint, such as before editing, before validation, before commit, or during final review.

Order tasks by implementation dependency and reviewability. Use a stable task ID in each full-name heading. Each task must include `Dependencies`, `Implementation`, and `Exit criteria`. Add `Notes` only when boundaries, risks, or traceability are not already clear from the two Plan mappings.

Do not force vertical slices when shared setup, tests, refactors, or interface updates need to happen first.

### `TASK-001` Implementation Task — `<short imperative title>`

Dependencies:

1. `<None, task ids, artifacts, prior phase, or external event>`.

Implementation:

1. `<specific implementation, test, validation, documentation, or handoff step with files/scope>`.
2. `<next concrete step, or remove this row when not needed>`.

Exit criteria:

1. `<observable completion signal, validation result, review finding, or artifact update>`.

Notes:

1. `<optional boundary, gotcha, risk-specific guidance, or per-task trace IDs when useful>`.

### `TASK-002` Implementation Task — `<short imperative title>`

Dependencies:

1. `<TASK-001 or None>`.

Implementation:

1. `<specific validation, documentation, changelog, or review task with files/scope>`.

Exit criteria:

1. `<observable completion signal, validation result, review finding, or artifact update>`.

## Plan Checks

Write one block per frozen evidence-producing procedure. One check may cover multiple Verification Criteria without merging their meanings. Multiple checks for one criterion are conjunctive by default; equivalent alternatives use an explicit `Any one of` group with an equivalence rationale.

### `CHECK-001` Plan Check — `<short procedure title>`

Covers:

1. `VER-001`.

Procedure:

1. `<exact command, test, inspection, analysis, demonstration, or review procedure>`.

Expected result:

1. `<observable pass signal>`.

Evidence record:

1. `<where the execution instance, actual result, evidence, and pass/fail/blocker status will be recorded>`.

Stage or environment:

1. `<pre-edit, implementation, review, pre-commit, phase, or named environment>`.

Task/check coordination:

1. `<TASK-NNN dependency that enables this check, or check result that gates a task or stage>`.
