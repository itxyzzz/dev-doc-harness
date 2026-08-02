# Plan Amendment 002: Task-Bound Checks

Work ID: `2026-07-30_durable-planning-quality-clarity`
Short ID: `durable-planning-quality-clarity`
Status: Approved
Harness release: `0.8+`
Schema: `schema:plan.amendment`
Policy references: `module:architecture`, `module:lifecycle`, `module:quality`, `module:execution-quality`, `module:models`, `module:freeze-gate`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Original plan reference

- Amendment ID: `AMD-002`
- File: `plan_amendment-01_task-check-conformance_durable-planning-quality-clarity.md`
- Section or task: `TASK-005` through `TASK-007` and `CHECK-006` through `CHECK-008`
- Original instruction: place local checks with their task and permit cross-cutting or end-to-end checks in a shared Plan Checks section.

## Discovered issue

Permitting a shared Plan Checks section creates a second allocation layer outside the executable task list. That makes plan execution and ownership variable: a check can lack a parent task, and an executor cannot always treat the main body as one flat sequence of self-contained tasks.

## Proposed change

1. Define the executable plan body as a flat list of `TASK-NNN` entries. Dependencies may permit parallel execution, but every task remains self-contained and has its own outcome, implementation steps, exit criteria, and checks.
2. Require every `CHECK-NNN` to be nested inside exactly one parent `TASK-NNN`; remove standalone and shared Plan Checks sections from current authoring templates and validators.
3. Keep `Covers: VER-NNN` as the semantic evidence link. Parentage is structural through nesting, not a variable `Related task(s)` field.
4. Require a multi-area or end-to-end verification activity to be an explicit integration or verification task with its own nested checks. A check may not be cross-cutting without a parent task.
5. Update quality and execution-quality guidance, policy catalog wording, source block, generated templates, testing delta, implementation fragment, and validator fixtures to enforce the flat-task model.

## Impact assessment

Affected outcome: every generated plan presents one predictable executable task list; checks are task work, not a separate plan workstream.

Proof impact: each check still proves a `VER-NNN`, but its enclosing task supplies execution ownership and sequencing. An end-to-end check is valid only inside an explicit end-to-end task.

Interfaces and data: no runtime interfaces or persisted data change. The document schema changes from level-three task and check siblings plus an optional shared section to level-three task entries with nested check entries.

Risk: a permissive parser could still accept a top-level or mixed shared check. The validator must reject check headings outside a task and prove that an end-to-end check nested in a named integration task is valid.

Documentation: update the matching implementation changelog fragment and testing-guide delta. No root `CHANGELOG.md` consolidation is included.

## Implementation tasks

### `TASK-008` Replace variable check allocation with task-bound checks

Modify `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`, `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`, and `.agents/skills/dev-doc-harness/references/policy-architecture.md`.

1. State that the main plan body is a flat task list; dependencies determine permitted parallelism without creating a second execution hierarchy.
2. State that each check is nested in exactly one task and that a standalone/shared check is invalid.
3. Preserve `CHECK` → `VER` evidence semantics and execution-time evidence/status ownership.
4. Replace cross-cutting/end-to-end shared-check wording with the explicit integration-task rule.
5. Keep lifecycle and freeze ownership unchanged.

Exit criteria: the canonical rules give every check a single executable parent and make the flat task list sufficient to schedule the plan.

### `TASK-009` Render checks inside task templates

Modify `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.050.common.task-plan.md` and regenerate the affected small/medium and phase-plan templates.

1. Render `### TASK-NNN` as the only top-level entries in the implementation body.
2. Render `#### CHECK-NNN` inside the task after its implementation and exit criteria, with criterion coverage, method, expected result, and evidence-record fields.
3. Remove the shared `## Plan checks` section and `Related task(s)` field.
4. Include a concrete final integration-task example for end-to-end validation when that activity is required.
5. Regenerate with `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write`; do not hand-edit generated outputs.

Exit criteria: generated templates make the task list the sole execution structure and make any end-to-end verification an ordinary parent task.

### `TASK-010` Enforce and verify the nested schema

Modify `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, `docs/work-items/2026-07-30_durable-planning-quality-clarity/deltas/testing-guide.delta.md`, and `docs/work-items/2026-07-30_durable-planning-quality-clarity/changelog/implementation.md`.

1. First add a failing positive fixture with a task-nested check and a failing negative fixture for a check outside a task or in a shared checks section.
2. Update the fixture parser and high-signal assertions to require nested check headings and reject the removed shared-section/related-task schema.
3. Run template assembly, the full policy validator, `git diff --check`, and a complete-diff review.
4. Update the testing guide and changelog fragment before the implementation commit.

Exit criteria: the validator accepts a flat task list with nested checks and rejects variable, standalone, or cross-cutting check allocation.

## Model and sub-agent strategy

Model policy: active repository `economy-default`.

1. Execution method: `superpowers:executing-plans`; policy, source-block generation, and validator changes have shared ownership and must be integrated in order.
2. Continuity: `same Codex task`; the frozen packages and recent review evidence remain available here.
3. Writer delegation: `Sub-agents: None`; all changed surfaces are coupled and a split writer would overlap the parser and source block.
4. Independent review: one read-only final reviewer after deterministic validation, using a flat-task-executability and schema-enforcement lens.
5. Reviewer profile: retain the operator-approved `gpt-5.6-sol` at high reasoning. Write authority: none. Fallback: report unavailability rather than silently changing the review boundary.
6. Final integration: the execution Codex task owns implementation, validation, variance judgment, and the user-facing completion report.

## Approval

- Required: Yes
- Status: Approved
- Approval evidence: Operator approved the staged amendment on 2026-07-31 and directed the minimum concise implementation.
- Superseded by: None

## Planned commits

| Stage | Planned subject |
|---|---|
| Amendment approval | `plan: task-bound-checks -- approve flat-task amendment` |
| Amended implementation | `docs: task-bound-checks -- make checks task-bound` |

## Planning artifact freeze gate

This amendment supersedes shared and standalone Plan Check allocation. It must pass `module:freeze-gate` before implementation. After approval and the amendment-approval commit, implementation remains paused until a fresh explicit operator instruction.
