# Plan Amendment 003: Entity Section Ownership

Work ID: `2026-07-30_durable-planning-quality-clarity`
Short ID: `durable-planning-quality-clarity`
Status: Approved
Harness release: `0.8+`
Schema: `schema:plan.amendment`
Policy references: `module:quality`, `module:lifecycle`, `module:models`, `module:freeze-gate`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Original plan reference

- Amendment ID: `AMD-003`
- File: `plan_amendment-02_task-bound-checks_durable-planning-quality-clarity.md`
- Section or task: `TASK-008` through `TASK-010`
- Original instruction: place Verification Criteria and Plan Checks in the plan-quality list while defining the entities later at peer heading level.

## Discovered issue

The plan-quality bullet can imply that Verification Criteria are part of tasks. The peer-level entity headings also obscure the ownership model: specs own commitments and criteria, while plans own tasks and executable checks.

## Proposed change

1. Move `Specification Commitments` and `Verification Criteria` under `Spec quality bar` as level-three sections.
2. Move `Plan Tasks` and `Plan Checks` under `Plan quality bar` as level-three sections.
3. Replace the ambiguous plan-quality bullet with concise wording that tasks contain executable checks and those checks link to relevant Verification Criteria.
4. Update only the affected owner-heading and structural validator assertions.

## Impact assessment

Outcome: the document hierarchy makes spec and plan entity ownership visible without changing `CHECK` → `VER` semantics or the task-bound schema.

Risk: the validator could preserve obsolete level-two expectations. Update it to require the new nested section layout and reject the old ambiguous wording.

Documentation: update the implementation changelog fragment only. No template, root changelog, runtime, lifecycle, or execution-quality change is needed.

## Implementation tasks

### `TASK-011` Rehome entity sections and validate ownership

Modify `durable-planning-quality.md`, `test_harness_policy.py`, and the implementation changelog fragment.

1. Move the two spec-owned entity sections directly below the spec quality bar and the two plan-owned entity sections directly below the plan quality bar.
2. Use level-three headings and update the owned-rule table accordingly.
3. Replace the confusing bullet without adding new policy.
4. First add a failing assertion for the nested heading layout; run the validator, then make the policy change.
5. Run the full validator and `git diff --check`; update the changelog fragment before the implementation commit.

Exit criteria: section nesting and wording distinguish spec-owned `SPEC`/`VER` from plan-owned `TASK`/`CHECK` without changing any other model behavior.

## Model and sub-agent strategy

Model policy: active repository `economy-default`.

1. Execution method: `superpowers:executing-plans` in this same task.
2. Sub-agents: None; this is a small, coupled heading-and-assertion correction with deterministic validation, and further delegation would add no coverage beyond the completed Sol High reviews.
3. Final integration: the execution Codex task owns the edit, validation, and completion report.

## Approval

- Required: Yes
- Status: Approved
- Approval evidence: Operator approved the staged amendment on 2026-07-31.
- Superseded by: None

## Planned commits

| Stage | Planned subject |
|---|---|
| Amendment approval | `plan: entity-section-ownership -- approve hierarchy amendment` |
| Amended implementation | `docs: entity-section-ownership -- clarify spec-plan hierarchy` |

## Planning artifact freeze gate

This amendment changes only quality-document hierarchy and its validator. It must pass `module:freeze-gate` before implementation. After approval and the amendment-approval commit, implementation remains paused until a fresh explicit operator instruction.
