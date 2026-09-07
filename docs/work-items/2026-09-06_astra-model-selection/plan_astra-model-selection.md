# Astra Model Selection Plan

Work ID: `2026-09-06_astra-model-selection`
Short ID: `astra-model-selection`
Status: Approved
Harness release: `0.10+`
Schema: `schema:plan.medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `rule:models.strategy-required`, `rule:models.selection-dimensions`, `rule:lifecycle.variance-policy`
Execution method: `superpowers:subagent-driven-development`

## Input Artifacts

1. Draft spec: `spec_astra-model-selection.md`.
2. Architecture input: the spec's not-applicable architecture decision.
3. Required snapshots or deltas: none.
4. Repository inputs: `.agents/skills/dev-doc-harness/references/subagent-model-policy.md` and `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
5. Unresolved implementation context: none.

## Change surfaces

1. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: add the generation/default, Terra, Astra, and no-latest-as-default regression assertions before changing guidance; update model-selection fixtures to use a concrete default generation.
2. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`: state that Astra is latest but not default, retain GPT-5.6/Terra as the regular-work default, constrain Astra to Sol-equivalent escalation, and remove latest-strongest wording.
3. `.agents/skills/dev-doc-harness/references/subagent-role-examples.md`: replace `latest available` generation recommendations with explicit policy-selected-generation guidance.
4. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.medium.handoff.md`, `plan.085.phase.handoff.md`, and `spec.060.large.phase-decomposition-model.md`: replace latest-generation placeholders before regenerating their consumer templates.
5. `.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md`: replace the latest-generation placeholder.
6. Generated medium and large plan/spec templates: refresh only with `assemble_templates.py` after the source-block changes.
7. `changelog/implementation.md`: record the implementation change immediately before the implementation commit, using the current changelog module's required format.

## Implementation approach

Add minimal policy-validator checks first and run them to prove the desired generation/default wording is absent. Then state the shared GPT-5.6/Terra and Astra/Sol constraints, replace active latest-generation prompts with policy-selected-generation prompts, regenerate templates, run the validator, and have the approved read-only reviewer inspect semantics and test coverage.

## Implementation tasks

### `TASK-001` Add generation and policy-invariant regression assertions

Dependencies: Frozen combined package and fresh operator start authorization.

Interfaces:

1. Consumes: `SPEC-001`, `SPEC-002`, and the `assert_model_selection_dimensions` policy-test function.
2. Produces: Normalized-text assertions that require the approved GPT-5.6 default, Terra baseline, latest-but-not-default Astra status, Astra/Sol constraint, and explicit-generation guidance.

Implementation:

1. In `assert_model_selection_dimensions`, add assertions for `GPT-5.6 remains the default generation for regular bounded work`, `Terra remains the baseline for regular bounded work`, `Astra is the latest concrete model, but it is not the default`, and `Astra may be used only as a Sol-equivalent alternative`.
2. Add checks that active model-selection policy, role examples, source blocks, generated templates, and amendment template require a policy-selected concrete generation and contain no `latest available` or `latest strongest model class` selection instruction.
3. Replace model-generation fixture values in the validator from `latest available` with the explicit default `GPT-5.6`.
4. Run the focused validator before editing guidance and confirm it fails only because the new policy constraints and explicit-generation guidance are absent.

Exit criteria: The focused validator fails for the expected missing generation/default, Astra, and no-latest-as-default assertions.

#### `CHECK-001` Verify the regression check is red

Covers: `VER-002`.

Method: Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` after adding the assertions and before changing the policy.

Expected result: Nonzero exit with failures identifying the missing GPT-5.6 default, Terra-baseline, latest-but-not-default Astra, Astra/Sol-equivalent, and explicit-generation constraints; no unrelated regression is accepted.

Evidence record: Execution report and implementation changelog fragment.

### `TASK-002` State the explicit generation and selection boundary

Dependencies: `TASK-001`.

Interfaces:

1. Consumes: The approved wording in `SPEC-001` and the red regression assertions from `TASK-001`.
2. Produces: A current-provider mapping and reusable generation prompts that keep vendor-neutral tiers unchanged, make GPT-5.6/Terra's regular-work role explicit, and confine Astra to Sol-equivalent escalation.

Implementation:

1. Replace the GPT-5.6-only current-mapping sentence with a current concrete-mapping statement that identifies GPT-6.0 Astra as the latest model and a `flagship` alternative to Sol.
2. Add the approved plain-language constraints in the Model selection section: GPT-5.6 remains the default generation for regular bounded work; Terra remains that baseline; Astra is latest but not default; and Astra may be used only as a Sol-equivalent alternative after a justified flagship escalation.
3. Replace `latest available` and `latest strongest model class` selection guidance in the active policy, role examples, source blocks, amendment template, and validator fixtures with explicit policy-selected-generation wording.
4. Regenerate all templates affected by changed source blocks with `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py`.
5. Preserve the existing Terra medium/high and Sol medium/high profile-local escalation bullets; do not add Astra to normal-work bullets.
6. Review the diff to verify that no active model-selection text implies a newer model replaces the GPT-5.6/Terra default or weakens the existing escalation criteria.

Exit criteria: Active model-selection guidance requires a policy-selected concrete generation, exposes the intended GPT-5.6/Terra and Astra/Sol relationship, and retains existing vendor-neutral tier meanings.

#### `CHECK-002` Verify policy assertions are green

Covers: `VER-001`, `VER-002`.

Method: Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` and `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Expected result: Both commands exit 0; templates are fresh, `PASS models.selection-dimensions` is reported, and no active selection surface retains latest-as-default guidance.

Evidence record: Validator output and implementation changelog fragment.

### `TASK-003` Review and record the cohesive update

Dependencies: `TASK-002` and the approved reviewer strategy.

Interfaces:

1. Consumes: The changed policy, changed validator, `CHECK-002` output, and reviewer findings when authorized.
2. Produces: A resolved review record, current implementation changelog fragment, and one cohesive implementation commit.

Implementation:

1. Ask the approved read-only reviewer to assess the GPT-5.6/Terra default, latest-but-not-default Astra status, Astra/Sol-only constraint, all active generation prompts, and validator coverage; resolve any evidence-backed finding in scope.
2. Immediately before committing, load `module:implementation-changelog` and create or update `changelog/implementation.md` with the required current fragment format.
3. Rerun the full policy validator after any review adjustment.
4. Commit only the policy, validator, and implementation changelog fragment with `docs: constrain-astra-model-selection`.

Exit criteria: Validation is green, the reviewer contract is satisfied or its authorized fallback is documented, and the cohesive implementation commit exists.

#### `CHECK-003` Confirm semantic and regression coverage

Covers: `VER-001`, `VER-002`.

Method: Inspect the final diff and reviewer report against the two commitment statements; run the full policy validator.

Expected result: The diff contains no latest-as-default or Astra-as-default implication; all validator and template-freshness checks pass; any reviewer finding is resolved or recorded with evidence.

Evidence record: Final execution report, reviewer report or authorized fallback disclosure, and commit hash.

## Model and Sub-agent Strategy

Upcoming-stage sub-agent assessment:

1. Sub-agents: one bounded read-only final reviewer.
2. Fit reason: The policy, examples, templates, and validator are tightly coupled, so parallel writing would add risk; an isolated read-only reviewer can independently detect a remaining latest-as-default or Astra-as-default interpretation.
3. Authorization state: Pending operator approval.
4. The active no-proactive-delegation constraint prevents dispatch until the operator approves this bounded strategy.

Sub-agent `final-policy-reviewer`:

1. Purpose: Review the final diff for the GPT-5.6/Terra default, latest-but-not-default Astra, Astra/Sol-only constraint, active-generation prompts, and validator coverage.
2. Context strategy: curated artifacts.
3. Input context: frozen spec and plan, changed policy and validator diff, and validator output.
4. Output artifact: evidence-backed findings with severity, validation path, and recommendation.
5. Active model policy: `efficiency-first`.
6. Recommended sub-agent model: Generation `GPT-5.6`; Capability tier `flagship`; Reasoning effort `medium`.
7. Availability/fallback: use Sol medium when available; otherwise retain the main-session focused self-review only if the operator explicitly authorizes the missing-review fallback.
8. Selection reason: a stronger isolated reviewer is justified by the policy's process-wide blast radius while avoiding concurrent writes.
9. Parallel execution: No; review follows `TASK-002`.
10. Blast radius if wrong: Medium; a missed ambiguity could cause future work to select Astra or another latest model as the regular-work default.
11. Write authority: read-only.
12. Concurrency: single run.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `docs: astra-model-selection-plan` |
| Implementation | `docs: constrain-astra-model-selection` |

## Validation and variance

1. `CHECK-001` must establish the new validator assertions are meaningful before guidance is added.
2. `CHECK-002` and `CHECK-003` must run template freshness and the current harness policy validator.
3. A material expansion beyond the canonical policy and its validator requires an amendment and operator approval.

## Implementation handoff

### Next-stage recommendation

#### Next lifecycle stage

Stage: `plan execution`.

#### Orchestration

- Method: `superpowers:subagent-driven-development`.
- Orchestration mode: `bounded delegated sub-agents`.
- Run in: `same orchestration session`.
- Review: One independent read-only reviewer after `TASK-002`, then final integration by the orchestration session.

#### Model

- Generation: `GPT-5.6`.
- Capability tier: `balanced`.
- Reasoning: `medium`.

#### Execution requirements and contingencies

Load the frozen package before editing. The reviewer requires explicit operator approval; if unavailable or declined, disclose the assurance gap and obtain explicit authorization for the focused self-review fallback. Stop for any material scope or policy-architecture variance.

### Execution startup

1. Frozen package: approved `spec_astra-model-selection.md` and `plan_astra-model-selection.md`.
2. Artifact rehydration: load applicable instructions, the frozen package, current baseline, and any variance record before `TASK-001`.
3. Variance stop condition: stop for a change beyond the active selection guidance/template/validator surfaces or any weakening of the GPT-5.6/Terra/Astra boundary.

## Readiness

- [x] The declared inputs, tasks, checks, and handoff are sufficient for a fresh executor.
- [x] Each task has a bounded outcome, dependencies, interfaces, steps, and exit criteria.
- [x] Plan Checks cover both Verification Criteria.
- [x] Documentation assessment needs no additional durable output.
- [x] Next-stage model and reviewer strategy are explicit.
- [x] No placeholder, unresolved implementation decision, missing owner, or ownerless deferral remains.

## Completion

- Required work and evidence are complete; any noteworthy variance is recorded.
- Planned changes are committed, or the blocker is stated.

## Approval

- Status: Approved
- Superseded by: None
