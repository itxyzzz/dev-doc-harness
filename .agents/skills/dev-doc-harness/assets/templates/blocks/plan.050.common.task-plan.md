## Implementation tasks

Use stable task IDs, short titles, and enough detail to act without inventing
scope. Order tasks by dependency.

### `TASK-001` `<short imperative title>`

Dependencies: `<None, task IDs, artifacts, or event>`.

Interfaces:

1. Consumes: `<inputs from a prior task, approved artifact, interface, or None>`.
2. Produces: `<outputs that a later task or fresh executor relies on, or None>`.

Dependencies describe readiness or ordering. Interfaces describe task-boundary
inputs and outputs; do not use one in place of the other.

Implementation:

1. `<specific change, test, documentation, or review step>`.

Use numbered executable steps. Do not use checkbox task lists inside an
implementation sequence.

Exit criteria: `<observable completion signal>`.

#### `CHECK-001` `<short title>`

Covers: `VER-001`.

Method: `<command, test, inspection, analysis, demonstration, or review>`.

Expected result: `<observable pass signal>`.

Evidence record: `<where the result, artifact, log, or review finding is recorded>`.

When multiple checks cover one criterion, state whether all are required or they are equivalent alternatives, and why either alternative proves the same evidence purpose.

For end-to-end validation, add a final task such as `TASK-999 Verify end-to-end integration` and nest its checks inside it.
