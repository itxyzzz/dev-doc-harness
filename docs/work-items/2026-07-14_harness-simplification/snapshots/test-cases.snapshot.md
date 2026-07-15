# Harness Simplification Test Cases Snapshot

Work ID: `2026-07-14_harness-simplification`
Status: Approved
Source spec: `spec_harness-simplification.md`

## Test cases

### `TC-001` IDs remain and formal presentation shrinks

Given current authoring templates,

When the simplified templates are generated,

Then `SPEC`, `VER`, `TASK`, `CHECK`, `DEC`, and variance IDs remain searchable
anchors wherever those entity lists appear, while unused formal names and
classification fields are not required.

Covers: `VER-001`.

### `TC-002` A small plan uses local links

Given a straightforward plan with a few commitments and checks,

When the plan identifies related tasks and checks beside each item,

Then it passes without a complete cross-product mapping table.

Covers: `VER-002`.

### `TC-003` A mapping has a concrete reason

Given a plan with cross-cutting coverage or deterministic validator input,

When it includes a full mapping,

Then the mapping names the coverage, handoff, or automation benefit it provides.

Covers: `VER-002`.

### `TC-004` Approved execution continues through planned tasks

Given a combined package is frozen and the operator sends a fresh instruction
to begin implementation,

When the agent completes ordinary planned local edits and non-destructive
validation,

Then it continues through the planned tasks without extra confirmation.

Covers: `VER-003`.

### `TC-005` Equivalent check adjustment is a variance

Given a planned test command is replaced by an equivalent command that proves
the same criterion,

When the change is noteworthy,

Then the agent records a variance note and continues without an amendment.

Covers: `VER-004`.

### `TC-006` Material evidence or outcome change is an amendment

Given a proposed change alters a user-visible outcome or means the planned
evidence no longer establishes that outcome,

When the agent identifies the change,

Then it stops for an amendment and operator approval.

Covers: `VER-004`.

### `TC-007` Global and local instructions agree

Given the README's copy-ready global bootstrap and repository-local harness,

When an ordinary work-item planning freeze is described,

Then the bootstrap defers detailed changelog and transition mechanics to the
repository-local harness and has no conflicting root-changelog requirement.

Covers: `VER-005`.

### `TC-008` Active prose gets smaller

Given the named changed current author-facing Markdown surfaces,

When their nonblank lines and words are counted before and after the change,

Then both totals decrease unless an approved material variance records why.

Covers: `VER-006`.

## Approval

- Status: Approved
- Superseded by: None
