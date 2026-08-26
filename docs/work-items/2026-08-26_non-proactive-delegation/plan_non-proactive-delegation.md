# Non-proactive Delegation Plan

Work ID: `2026-08-26_non-proactive-delegation`
Short ID: `non-proactive-delegation`
Status: Approved
Harness release: `unknown`
Schema: `schema:plan.medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.non-proactive-delegation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`
Execution method: `host-native documentation maintenance`

## Input Artifacts

1. Draft spec: `spec_non-proactive-delegation.md`.
2. Architecture input: Architecture Decisions in the draft spec; no architecture snapshot is required.
3. Required snapshots or deltas: None.
4. Relevant repository sources: `.agents/skills/dev-doc-harness/SKILL.md`, `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`, and `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.055.medium-and-large.model-strategy.md`.
5. Unresolved implementation context to confirm before editing: None identified.

## Change surfaces

1. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`: canonical rule ID and dispatch-gate policy.
2. `.agents/skills/dev-doc-harness/SKILL.md`: compact all-route dispatch-gate reminder, operational outcome wording, small-route boundary preservation, and completion checklist.
3. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.055.medium-and-large.model-strategy.md`: compact strategy prompt.
4. `.agents/skills/dev-doc-harness/assets/templates/medium-work-item-plan.md`: generated output from the strategy source block.

## Implementation approach

1. Define the rule once in `module:models`, then refer to it concisely in the router and source block.
2. Give small planning the concise router reminder without loading `module:models`, requiring a Model and Sub-agent Strategy, or recording a sub-agent assessment.
3. Regenerate assembled templates from source rather than editing generated output directly.
4. Validate the complete harness policy graph after the documentation edits.

## Implementation tasks

### `TASK-001` Define the canonical delegation rule

Dependencies: None.

Interfaces:

1. Consumes: The existing `### Sub-agent authorization` policy and the approved wording from this spec.
2. Produces: `rule:models.non-proactive-delegation` in the policy owner table and canonical authorization section.

Implementation:

1. Add the rule ID to the policy owner table.
2. Add concise normative text distinguishing the dispatch restriction from the required assessment and operator-approval request.
3. Preserve the existing authorization-envelope and fallback rules.

Exit criteria: The policy explicitly disallows using the restriction to silently choose single-agent execution.

#### `CHECK-001` Inspect canonical rule

Covers: `VER-001`.

Method: Inspect the new rule ID and authorization passage in `subagent-model-policy.md`.

Expected result: The passage names dispatch, assessment, operator approval, and the prohibited silent-single-agent interpretation.

Evidence record: Final change summary and validator output.

### `TASK-002` Add router and template safeguards

Dependencies: `TASK-001`.

Interfaces:

1. Consumes: The canonical rule from `TASK-001`.
2. Produces: A concise router outcome/checklist and model-strategy prompt that point to the same decision rule.

Implementation:

1. Add a compact all-route dispatch-gate reminder to the router without copying the full policy text.
2. Preserve the small planning route's explicit exclusion of `module:models`, model fields, and sub-agent assessment/strategy notation.
3. Update the router's sub-agent strategy outcome and completion checklist.
4. Update the model-strategy source block immediately after its authorization-state prompt.
5. Keep `module:models` as the sole owner of normative semantics.

Exit criteria: A plan author is instructed to assess potentially useful delegation and ask before dispatch despite a non-proactive restriction, while small planning remains lightweight and does not load the full sub-agent policy.

#### `CHECK-002` Inspect operational safeguards

Covers: `VER-002`.

Method: Inspect the changed router lines and model-strategy source block.

Expected result: The router provides the compact reminder without routing small planning to `module:models`; the router and template reject omission of assessment or the operator-approval request where the full strategy route applies.

Evidence record: Final change summary and validator output.

### `TASK-003` Regenerate and validate harness surfaces

Dependencies: `TASK-002`.

Interfaces:

1. Consumes: Updated template source block and policy/router sources.
2. Produces: Synchronized assembled templates and passing policy validation evidence.

Implementation:

1. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write`.
2. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
3. Inspect the generated `medium-work-item-plan.md` and the relevant diff for the intended wording only.

Exit criteria: Generated-template synchronization and the policy validator both pass.

#### `CHECK-003` Validate generated and policy surfaces

Covers: `VER-003`.

Method: Run the template assembler and harness policy validator.

Expected result: The assembler completes without stale-output errors and the validator reports success.

Evidence record: Command output captured in the final change summary.

## Model and Sub-agent Strategy

Upcoming-stage sub-agent assessment:

1. Sub-agents: None.
2. Fit reason: The policy/doc edits are tightly coupled to one canonical interpretation, including the small-route boundary, and one generated output; deterministic assembly and policy validation provide sufficient review value for this bounded documentation change.
3. Authorization state: Not needed.
4. The non-proactive delegation constraint is not the reason for this choice; it would govern dispatch only if delegation were useful and approved.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `spec: non-proactive-delegation` |
| Implementation | `docs: non-proactive-delegation -- enforce delegation approval gate` |

One cohesive implementation commit is planned after validation.

## Validation and variance

1. `CHECK-001` and `CHECK-002` provide focused policy and prompt inspection.
2. `CHECK-003` runs the template assembler and harness policy validator.
3. Any need to change additional policy owners, templates, validation logic, model selection, concurrency, or review rules is material variance and requires an amendment plus operator approval.

## Implementation handoff

### Approved next stage

#### Next lifecycle stage

Stage: `plan execution`.

#### Orchestration

- Method: `host-native documentation maintenance`.
- Orchestration mode: `single-agent`.
- Run in: `same orchestration session`.
- Review: `orchestration-session focused self-review plus deterministic template and policy validation`.

#### Model

- Generation: `latest available`.
- Capability tier: `balanced`.
- Reasoning: `medium`.

#### Execution requirements and contingencies

The operator must approve and freeze this combined package before implementation. Stop for an amendment if the change expands beyond the named policy, router, source block, generated template, or validation surfaces.

### Execution startup

1. Frozen package: `spec_non-proactive-delegation.md` and `plan_non-proactive-delegation.md`.
2. Artifact rehydration: Read both frozen artifacts and the three named source files before editing.
3. Variance stop condition: Stop for any material scope, policy-owner, or validation-surface change.

## Readiness

- [x] This plan is self-sufficient for a fresh executor session.
- [x] Each implementation task has bounded steps and observable exit criteria.
- [x] Plan Checks cover every Verification Criterion and identify evidence.
- [x] Required documentation outputs are assigned to tasks.
- [x] The next-stage orchestration, model, and sub-agent strategy are fully documented and appropriate to this scope.
- [x] No placeholder, unresolved implementation decision, missing owner, or ownerless deferral remains.

## Completion

- Required work and evidence are pending plan approval and execution.

## Approval

- Status: Approved
- Superseded by: None
