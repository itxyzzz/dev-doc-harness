# Planning Template Clarity Implementation Plan

Work ID: `2026-07-18_planning-template-clarity`
Short ID: `planning-template-clarity`
Status: Approved
Harness release: `0.7+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:artifact-style`, `module:freeze-gate`, `module:execution-quality`, `rule:lifecycle.planning-shape`, `rule:lifecycle.large-phase-orchestration`, `rule:lifecycle.superpowers-compatibility`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:models.strategy-required`, `rule:models.execution-continuity`, `rule:execution-quality.execution-thread-start`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`
Execution method: `Superpowers executing-plans` after harness freeze and fresh implementation authorization
Harness authority: scope, artifact location, model-policy bounds, commit boundaries, freeze, variance, validation, and final integration

Artifact style: approved final content. The plan is executable by a fresh task from the frozen package and keeps each change at its canonical policy, template, generated-output, or validation owner.

## Goal

Implement the approved planning-template clarification so current harness policy and templates distinguish observed runtime state from execution recommendations, present one handoff per boundary, use rolling phase planning, and stay concise.

## Input Artifacts

Read these before editing:

1. `docs/work-items/2026-07-18_planning-template-clarity/spec_planning-template-clarity.md`.
2. `docs/work-items/2026-07-18_planning-template-clarity/snapshots/architecture.snapshot.md`, especially `DEC-001` through `DEC-003`.
3. `docs/work-items/2026-07-18_planning-template-clarity/snapshots/test-cases.snapshot.md`.
4. `AGENTS.md` and `.agents/skills/dev-doc-harness/SKILL.md`.
5. `.agents/skills/dev-doc-harness/references/artifact-contract.md`, `subagent-model-policy.md`, `durable-planning-quality.md`, `planning-freeze-gates.md`, `context-and-quality-gates.md`, `artifact-style.md`, `policy-architecture.md`, and `naming-conventions.md`.
6. `.agents/skills/dev-doc-harness/assets/templates/assemblies/*.json`, the source blocks named under Change Surfaces, the four generated work-item templates, `plan-amendment.md`, and `architecture-snapshot.md`.
7. `.agents/skills/dev-doc-harness/scripts/assemble_templates.py`, `test_harness_policy.py`, and `consolidate_changelog_fragments.py`.
8. `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md`.
9. `docs/work-items/2026-07-18_superpowers-adapter-contract/` as implemented historical context. Do not edit it.
10. The current branch, worktree status, approval state, amendments, and variance log at execution startup.

## Traceability Approach

Local links are sufficient; a separate full mapping would add no execution or validation benefit.

1. `SPEC-001` and `VER-001`: `TASK-002`, `TASK-003`, `TASK-004`, `CHECK-001`, and `CHECK-003`.
2. `SPEC-002` and `VER-002`: `TASK-001`, `TASK-002`, `TASK-003`, `CHECK-001`, and `CHECK-004`.
3. `SPEC-003` and `VER-003`: `TASK-001`, `TASK-002`, `TASK-003`, `CHECK-001`, `CHECK-004`, and `CHECK-005`.
4. `SPEC-004` and `VER-004`: `TASK-001`, `TASK-002`, `TASK-003`, `CHECK-001`, `CHECK-003`, and `CHECK-004`.
5. `SPEC-005` and `VER-005`: `TASK-001`, `TASK-002`, `TASK-003`, `CHECK-001`, and `CHECK-003`.
6. `SPEC-006` and `VER-006`: `TASK-001` through `TASK-004`, `CHECK-001`, `CHECK-002`, and `CHECK-003`.
7. `SPEC-007` and `VER-007`: all tasks and checks.
8. `SPEC-008` and `VER-008`: `TASK-001` through `TASK-005`, `CHECK-001`, `CHECK-003`, and `CHECK-004`.

## Global Constraints

1. Do not edit frozen historical work items, including `docs/work-items/2026-07-18_superpowers-adapter-contract/`.
2. Edit source blocks and assembly manifests before generated templates; never hand-edit a generated template.
3. Keep existing module and rule ownership. Do not add a module, classification taxonomy, phase scheduler, task-creation automation, or semantic quality parser.
4. Preserve freeze approvals, immutable snapshots, variance handling, work-item changelog fragments, and operator-owned root-changelog consolidation.
5. Keep the implementation in one cohesive commit unless a material and independently reviewable split is approved through the variance route.
6. Use numbered implementation steps in the canonical plan even though Superpowers is the selected execution methodology.
7. At each transition, record the upcoming-stage sub-agent assessment. Request operator approval before useful unapproved dispatch, and do not repeat the request for an approved in-envelope role.

## Change Surfaces

### Canonical policy and router

1. `.agents/skills/dev-doc-harness/references/artifact-contract.md`: concise Superpowers precedence, meaningful commit granularity, combined-package transition ownership, and rolling large-phase orchestration.
2. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`: separate planning-task observations from approved execution selection and define the conservative continuity default.
3. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`: remove undefined commitment classification and preserve complete repeated commitment structure.
4. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: verify and present explicit execution selection separately from observed runtime state; consume the package's transition owner and next activity.
5. `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`: start fresh execution from the approved selection and rolling transition inputs without a second generic Superpowers choice.
6. `.agents/skills/dev-doc-harness/references/policy-architecture.md`: update a catalog or route summary only if needed to keep current owner descriptions accurate; do not add a module.
7. `.agents/skills/dev-doc-harness/SKILL.md`: literal completion checklist, compact compatibility cues, and explicit upcoming-stage sub-agent assessment in each planning and execution route.

### Specification template sources

1. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.030.common.commitments-verification.md`: remove classification and clarify the full repeated commitment structure.
2. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.070.small.planned-commits.md`: two-column planned commits.
3. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.070.large.planned-commits-freeze.md`: two-column planned commit patterns and rolling-phase notes.
4. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.085.small.handoff.md`: planning shape and transition ownership only for combined planning; compact staged exception.
5. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.085.large.handoff.md`: anchor-to-first-phase planning handoff and rolling sequence cue.
6. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.090.small.readiness-approval.md` and `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.090.large.readiness-approval.md`: adjust checklist wording only where removed fields or rolling order require it.
7. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.060.large.phase-decomposition-model.md`: default strategy envelope in the anchor plus phase-specific selection refinement and upcoming-stage sub-agent assessment, with observed-versus-recommended semantics.

### Plan template sources and assemblies

1. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.010.small.header-inputs.md` and `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.010.phase.header-objective-inputs.md`: replace the normal Superpowers meta-header section with actual conditional header fields.
2. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.040.common.model-strategy.md`: planning observations, explicit approved execution selection, upcoming-stage sub-agent assessment, approval state, and compact bounded strategy.
3. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.060.small.planned-commits.md` and `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.060.phase.planned-commits.md`: stage plus subject only.
4. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.common.handoff.md`: replace with specialized small-plan and phase-plan handoff blocks, then remove the unused common block.
5. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.080.phase.documentation-tasks-handoff.md`: require actual phase outputs for the post-phase transition.
6. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.090.small.readiness-completion-approval.md` and `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.090.phase.readiness-completion-approval.md`: align readiness and completion with explicit selection and transition ownership.
7. `.agents/skills/dev-doc-harness/assets/templates/assemblies/small-medium-work-item-plan.json` and `.agents/skills/dev-doc-harness/assets/templates/assemblies/large-phased-work-item-phase-plan.json`: reference the specialized handoff blocks.
8. `.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md`: simplify planned commits and record the upcoming-stage sub-agent assessment consistently.

### Generated outputs, guidance, and validation

1. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`, `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`, `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`, and `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`: regenerate through the assembler.
2. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: focused red/green assertions and synthetic fixtures for `TC-001` through `TC-016`.
3. `README.md`: update the lifecycle diagram and short compatibility explanation for rolling phases and one transition owner.
4. `.agents/skills/dev-doc-harness/docs/operator-note.md`: concise operator-visible model and transition distinction.
5. This work item's testing and operator deltas plus its implementation changelog source.

## Implementation Approach

Start with focused structural tests that describe the intended active surfaces and fail against the current policy/templates. Then update canonical owners so each semantic decision exists once. Change source blocks and assemblies to consume those rules, regenerate all four templates, and update only the operator summaries whose current flow would otherwise contradict the new lifecycle. Finish with focused and full validation, fragment lint, generated-output freshness, diff review, and one scoped implementation commit.

The implementation must not use stronger model allocation to resolve a missing requirement. A contradiction in the frozen package or material change to policy ownership, model selection, sub-agent authorization, lifecycle, commit semantics, or handoff scope is an amendment condition.

## Model and Sub-agent Strategy

### Planning-task observations

1. Current model/profile: `Sol`, exposed by the operator.
2. Current capability tier: `flagship` under the active GPT-5.6 mapping.
3. Current reasoning effort: `high`, exposed by the operator.
4. Current context state: `not exposed`; no remaining-token estimate or compaction threshold is inferred.
5. Planning continuity decision: preserve the current task because the operator explicitly chose not to switch during package drafting.

### Approved execution selection

1. Target model/profile: `Terra`, the current balanced-tier mapping.
2. Capability tier: `balanced`.
3. Reasoning effort: `high`, selected for cross-policy dependency traversal and source/generated-template reconciliation.
4. Orchestration mode: `single-agent`.
5. Execution method: `Superpowers executing-plans` inside the frozen harness plan.
6. Availability fallback: `Terra` with `medium` reasoning. If no balanced-tier selection is available, stop and ask rather than silently using Sol, Luna, platform multi-agent mode, or another tier.
7. Execution continuity: `new task with curated-artifact handoff` because the intended execution profile differs and the current context state is not exposed.
8. Artifact rehydration required: `Yes`; read the exact frozen package, applicable instructions, current worktree, and validation baseline before editing.
9. Model-policy source: `AGENTS.md` active `economy-default` policy plus the operator-approved balanced-tier choice in this work item.
10. Override scope and expiry: this work item's implementation and final integration only; later work returns to the active repository policy unless separately overridden.

### Sub-agents

Planning-stage assessment:

1. Sub-agents: `None` for the remaining package-drafting and feedback-resolution stage.
2. Fit reason: the operator supplied one coherent review item against a single staged package, the edits are tightly coupled, and independent drafting would add merge and context overhead without a separate evidence lens.

Upcoming implementation-stage assessment:

1. Bounded implementation workers: `None`; canonical policy, source blocks, manifests, generated outputs, and validator assertions change sequentially and share ownership decisions.
2. Independent final reviewer: `Useful`, proposed below. Independent context can detect policy/template/transition drift after the integrated change without splitting write ownership.

Proposed sub-agent `REVIEW-001`:

1. Purpose: read-only final review after `TASK-004` and before the implementation commit, using one lens: policy, template, and transition coherence against `SPEC-001` through `SPEC-008`.
2. Context strategy: `curated artifacts`.
3. Input context: frozen spec, plan, architecture and test-case snapshots; changed diff; assembly, policy-validator, and fragment-lint evidence; variance log when present.
4. Output artifact: evidence-backed findings with severity, exact file references, and a reproduction or validation path; no durable report unless evidence policy independently requires one.
5. Model policy: active `economy-default`.
6. Target allocation: Terra, balanced tier, high reasoning.
7. Availability fallback: Terra, balanced tier, medium reasoning; orchestration-thread review when sub-agents or explicit allocation controls are unavailable.
8. Write authority: read-only.
9. Concurrency: one reviewer, not parallel with implementation; dispatch only after integrated changes and primary checks are available.
10. Blast radius if wrong: medium; a missed contradiction could preserve the exact ambiguity this work item is intended to remove, but the orchestration thread retains final integration and validation ownership.
11. Authorization state: `Approved` by the operator with the planning package. Do not ask again for this in-envelope dispatch.

## Implementation Tasks

### `TASK-001` Add failing structural contract checks

Dependencies: frozen planning package and fresh implementation-task startup.

Interfaces:

1. Consumes: `SPEC-001` through `SPEC-008`, `TC-001` through `TC-016`, current validator helpers, current source blocks, and current generated outputs.
2. Produces: a focused failing validator group named `clarity.planning-template-contract` that defines the structural target without scanning frozen history.

Implementation:

1. Add `assert_planning_template_clarity()` to `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` and invoke it from `run_checks()` near related lifecycle, model, template, and Superpowers checks.
2. Assert that `SKILL.md` completion items use literal `- [ ]` syntax.
3. Assert that current quality policy, the shared commitment block, and generated spec templates omit `Classification is optional` and `Constraint · Preserve`, while the shared block states that later commitments follow the complete `SPEC-001` structure.
4. Assert that all current planned-commit source blocks and `plan-amendment.md` record stage and subject and do not require `Changelog title or snippet` or per-row `Notes` fields.
5. Assert that plan header blocks and generated plans contain conditional execution-method metadata and omit a `## Superpowers execution meta-header` section.
6. Assert that both reusable model-strategy sources and generated consumers contain distinct `Planning-task observations` and `Approved execution selection` groups; add synthetic positive and negative fixtures proving that unknown observations are valid but unknown target model/tier/effort/continuity are invalid.
7. Assert that the small spec records plan transition ownership without a complete duplicate handoff, the small plan has an implementation handoff, and the phase plan distinguishes current-phase implementation from post-phase transition.
8. Assert that lifecycle and active large/phased surfaces contain the rolling phase loop and explicit stable-independent batch-planning exception.
9. Assert that router outcomes, model policy, freeze guidance, applicable source blocks, and generated templates require an upcoming-stage sub-agent assessment, a stage-specific no-use rationale, and an explicit operator-approval request for useful unapproved delegation. Add fixtures for pending, approved, declined/unavailable fallback, and out-of-envelope strategies.
10. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` and confirm it fails only on the newly asserted current-surface expectations. Preserve the failure summary in the implementation report or a short implementation note if it helps later review.

Exit criteria: the new focused check is registered, fails for the intended current-policy/template gaps, and does not introduce unrelated failures or historical-artifact scans.

### `TASK-002` Clarify canonical lifecycle, model, quality, and freeze policy

Dependencies: `TASK-001` red-phase evidence.

Interfaces:

1. Consumes: `DEC-001` through `DEC-003`, the failing structural expectations, existing rule ownership, and the implemented Superpowers adapter boundary.
2. Produces: one canonical semantic source for model observations and selection, continuity, commit granularity, handoff ownership, rolling phases, repeated commitment structure, and Superpowers precedence.

Implementation:

1. Update `artifact-contract.md` so the Superpowers section maps only known conflicts: canonical artifact location, harness plan form, approved commit boundaries, freeze and variance route, review, finishing, and integration. State that other Superpowers methodology remains external and usable inside that envelope.
2. In the lifecycle commit section, make one cohesive implementation package the default commit boundary and allow splits only at stable, independently reviewable and revertible boundaries with relevant checks passing. State that task count alone does not determine commit count.
3. In small/medium planning shape, make the plan the combined package's implementation-transition owner and restrict a spec-only transition to an explicitly recorded staged exception.
4. Rewrite the normal large/phased sequence as an explicit rolling loop: anchor freeze; phase-plan draft and freeze; phase implementation; actual-output handoff; next-phase planning; repeat. Keep multi-phase batch planning as an explicit stable-and-independent exception.
5. Update `subagent-model-policy.md` selection notation to separate planning-task observations from approved execution selection. Preserve `not exposed` for observations and actual runtime results, but require actionable future selection values.
6. Update continuity guidance so substantial work prefers a fresh curated-artifact task when its intended profile changes or current model/profile/context suitability cannot be verified. Preserve justified same-task continuation and the prohibition on inferred context thresholds.
7. Remove commitment classification from `durable-planning-quality.md` and state that every commitment has the same Statement plus local criterion structure unless cross-cutting evidence is explicitly linked.
8. Update `planning-freeze-gates.md` to verify approved execution selection separately from observed planning state and route from the package's transition owner, frozen package, and documented next activity.
9. Update `context-and-quality-gates.md` so fresh execution loads the approved selection and exact transition inputs, including actual prior-phase outputs when entering later phase planning.
10. Convert the `SKILL.md` completion list to literal checkboxes and keep its compatibility wording as a short route to canonical owners.
11. In `subagent-model-policy.md` and each applicable `SKILL.md` planning/execution route, require an upcoming-stage feasibility assessment. When useful delegation is not already authorized, require a concrete proposal and explicit operator request; when not useful, require `Sub-agents: None` with a fit reason. State that operator approval overrides only the default against unrequested dispatch and does not override higher-priority runtime limits.
12. Preserve the current rule that an approved strategy begins with normal post-freeze authorization and does not require a repeated in-envelope sub-agent confirmation.
13. Update `policy-architecture.md` only if its module catalog or router summary would otherwise misdescribe ownership after these edits.
14. Run the focused validator. Expected result: canonical-policy assertions pass; source-template and generated-output assertions remain failing until `TASK-003` and `TASK-004`.

Exit criteria: each reusable semantic decision has one canonical owner, existing rule IDs remain valid, and no new module or duplicate methodology is introduced.

### `TASK-003` Reshape source templates and handoff assemblies

Dependencies: `TASK-002` canonical semantics.

Interfaces:

1. Consumes: updated canonical rules, `DEC-001` through `DEC-003`, and current assembly manifests.
2. Produces: concise source blocks and manifests that express the approved current artifact shapes without duplicating policy.

Implementation:

1. Update `spec.030.common.commitments-verification.md` to remove classification and add the complete-structure sentence before the abbreviated `SPEC-002` example.
2. Simplify `spec.070.small.planned-commits.md`, `spec.070.large.planned-commits-freeze.md`, `plan.060.small.planned-commits.md`, `plan.060.phase.planned-commits.md`, and `plan-amendment.md` to stage plus planned subject. Keep only concise prose for subject deferral or exceptional multi-commit boundaries.
3. Move the conditional Superpowers execution method and workflow into actual header fields in `plan.010.small.header-inputs.md` and `plan.010.phase.header-objective-inputs.md`. Remove the normal meta-header section and its explanatory artifact content.
4. Rewrite `plan.040.common.model-strategy.md` as compact planning-observation and approved-execution-selection groups followed by optional bounded sub-agent entries. Remove the ambiguous generic recommended-change field.
5. Apply the same observation/selection distinction to `spec.060.large.phase-decomposition-model.md`, but make the anchor record a default envelope and require each later phase plan to make its concrete selection.
6. Simplify `spec.085.small.handoff.md` to planning shape, transition owner, staged-exception reason when applicable, and next activity. It must state that the combined plan owns the implementation handoff.
7. Update `spec.085.large.handoff.md` to hand the anchor to first-phase planning and state the rolling phase default and explicit batch exception.
8. Replace `plan.085.common.handoff.md` with `plan.085.small.handoff.md` and `plan.085.phase.handoff.md`. The small block always records the implementation handoff. The phase block records the current-phase implementation handoff and expected post-phase transition.
9. Update the small-plan and phase-plan assembly manifests to reference their specialized handoff blocks, then remove the unused common handoff block.
10. Update `plan.080.phase.documentation-tasks-handoff.md` so the phase completion output includes actual outputs, validation, variance, commit state, and inputs for the documented next phase or completion activity.
11. Add a compact upcoming-stage sub-agent assessment and authorization state to the relevant spec-to-plan, anchor-to-phase-plan, amendment/replanning, and plan-to-execution prompts. Avoid duplicating the full per-role strategy outside `module:models` and the plan strategy block.
12. Adjust readiness/completion blocks only where necessary to verify explicit execution selection, sub-agent assessment/authorization, single transition ownership, and planned-subject/changelog synchronization.
13. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`. Expected result: nonzero because generated templates have not yet been regenerated, with no manifest or missing-block error.

Exit criteria: source blocks and manifests are internally complete, specialized transition ownership is explicit, and the only expected assembly failure is stale generated output.

### `TASK-004` Regenerate templates and align operator guidance

Dependencies: `TASK-003` source-block and manifest changes.

Interfaces:

1. Consumes: updated source blocks, manifests, canonical rules, and existing README/operator-note summaries.
2. Produces: fresh generated templates and concise operator guidance consistent with the rolling lifecycle and explicit execution selection.

Implementation:

1. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` to regenerate all configured templates and run its built-in freshness and policy validation.
2. Inspect the four generated work-item templates. Confirm each changed concept appears exactly where its assembly requires and no removed section or duplicate handoff survives.
3. Update the README lifecycle diagram and nearby explanation so the large path visibly loops from phase implementation output to next-phase planning while preserving approval gates and the explicit batch-planning exception.
4. Update README compatibility prose only enough to state that the approved harness plan governs numbered tasks and commit boundaries when generic Superpowers defaults conflict.
5. Update `.agents/skills/dev-doc-harness/docs/operator-note.md` with the planning-observation versus execution-selection distinction and the combined and rolling-phase transition rules.
6. Include the upcoming-stage sub-agent assessment and one scoped operator-approval request in the operator guidance, with no repeated confirmation for approved in-envelope dispatch.
7. Update this work item's `deltas/operator-manual.delta.md` and `deltas/testing-guide.delta.md` only if implementation wording or exact validation signals differ from the approved draft.
8. Run the focused validator. Expected result: `PASS clarity.planning-template-contract`; repair only active-surface or fixture failures within the frozen scope.

Exit criteria: generated templates are source-derived and fresh, operator summaries are concise and non-normative, and the focused clarity check passes.

### `TASK-005` Validate, record, and commit the implementation

Dependencies: `TASK-004` generated outputs and guidance.

Interfaces:

1. Consumes: all implementation changes, Plan Checks, planned implementation subject, and current worktree state.
2. Produces: final validation evidence, synchronized implementation changelog source, one scoped implementation commit, and a completion report with actual allocation and variance.

Implementation:

1. Create `docs/work-items/2026-07-18_planning-template-clarity/changelog/implementation.md` before committing. Use heading `## 2026-07-18_planning-template-clarity -- clarify models handoffs and phases`, exactly one metadata set, and concise Added/Changed bullets tied to the delivered policy, templates, routing, and validation.
2. Run every Plan Check and repair only failures within the frozen scope.
3. If `REVIEW-001` is explicitly approved and platform support is available, dispatch the recorded read-only reviewer after primary checks pass. The orchestration thread evaluates and integrates findings; any out-of-envelope review request returns to the operator.
4. If `REVIEW-001` is declined or unavailable, run the same policy/template/transition coherence lens in the orchestration thread and record the fallback in the completion report.
5. Confirm the implementation subject `docs: planning-template-clarity -- clarify models handoffs and phases` supplies the same title snippet as the implementation changelog heading.
6. Review `git diff --check`, `git diff --stat`, `git diff --name-only`, and the complete diff for unrelated edits, duplicated policy, generated noise, placeholders, contradictions, and frozen-history changes.
7. Stage only the approved implementation surfaces, generated outputs, work-item deltas, and implementation changelog source.
8. Commit with `docs: planning-template-clarity -- clarify models handoffs and phases` only after all required checks pass.
9. Report the commit hash and subject, de-facto model/profile and reasoning when exposed, sub-agent assessment and actual use, fallback use, orchestration mode, artifact rehydration, files changed, checks run, variance, and residual risk.

Exit criteria: all Plan Checks pass, the implementation changelog and subject are synchronized, frozen planning and historical inputs are unchanged, and one scoped implementation commit exists.

## Plan Checks

All checks are required. Equivalent local commands are allowed only when they prove the same evidence purpose and follow the variance policy.

### `CHECK-001` Planning-template contract passes

Covers: `VER-001` through `VER-008`.

Method: run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Expected result: exit code `0`; every existing check passes and the output includes `PASS clarity.planning-template-contract`.

### `CHECK-002` Generated templates match source assemblies

Covers: `VER-001` through `VER-008`.

Method: run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`.

Expected result: exit code `0`; all four generated planning templates match their source blocks and manifests, with no missing or unused required assembly reference.

### `CHECK-003` Transition routes are singular and rolling

Covers: `VER-001`, `VER-004`, `VER-005`, and `VER-006`.

Method: run `rg -n -i "transition owner|implementation handoff|post-phase transition|rolling|batch planning|curated-artifact|Superpowers execution meta-header" .agents/skills/dev-doc-harness/references .agents/skills/dev-doc-harness/assets/templates README.md .agents/skills/dev-doc-harness/docs/operator-note.md` and inspect the matches.

Expected result: active surfaces show plan-owned combined implementation handoff, distinct phase transitions, the rolling phase default, the explicit batch exception, and no normal `## Superpowers execution meta-header` section in current source or generated plan templates.

### `CHECK-004` Model, commitment, and commit shapes are concise

Covers: `VER-002`, `VER-003`, `VER-004`, and `VER-008`.

Method: run `rg -n -i "Planning-task observations|Approved execution selection|upcoming-stage|Sub-agents: None|Authorization state|Classification is optional|Constraint · Preserve|Changelog title or snippet|\| Notes \|" .agents/skills/dev-doc-harness/references .agents/skills/dev-doc-harness/assets/templates` and inspect current-owner and generated-template matches.

Expected result: observation and selection headings appear in their intended active consumers; upcoming-stage assessment and authorization prompts are present; removed classification and duplicate planned-commit fields do not appear in current policy or template surfaces; structural grammar examples outside these surfaces are not treated as failures.

### `CHECK-005` Changelog grammar and final diff are clean

Covers: `VER-003` and `VER-007`.

Method: run `python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --lint`, `git diff --check`, `git diff --name-only`, and a complete diff review.

Expected result: fragment lint exits `0`; no whitespace errors; changes are limited to approved active policy, router, source blocks, manifests, generated templates, validator, operator summaries, and this work item's implementation documentation; no frozen historical artifact has a diff.

## Planned Commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: planning-template-clarity -- approve clear planning transitions` |
| Implementation | `docs: planning-template-clarity -- clarify models handoffs and phases` |

The implementation is planned as one cohesive commit. A split is allowed only if execution finds a stable, independently reviewable and revertible boundary and the variance route authorizes it.

## Validation and Variance

Before freeze, operator feedback edits this draft package directly. After freeze, routine wording, helper, fixture, or equivalent-command adjustments may proceed when they preserve the approved outcome and evidence purpose; record them only when they help a later reader.

Stop for an amendment before any change that materially alters module ownership, model tier or effort envelope, sub-agent roles or authorization, continuity default, freeze authority, commit semantics, handoff ownership, phase order, current template scope, required evidence, or historical-artifact boundary. A missing requirement or contradiction is an approval problem, not a reason to select a stronger model.

## Documentation Tasks

1. Planning changelog source: create `changelog/planning-approval.md` only after explicit package approval.
2. Implementation changelog source: create `changelog/implementation.md` before the implementation commit.
3. Root changelog: do not consolidate during ordinary planning or implementation commits.
4. Test cases: preserve `snapshots/test-cases.snapshot.md` as the approved behavioral baseline.
5. Testing guide delta: update `deltas/testing-guide.delta.md` only if exact final commands or signals change.
6. Operator manual delta: update `deltas/operator-manual.delta.md` only if the final operator-visible sequence changes within scope.
7. Architecture snapshot: preserve `snapshots/architecture.snapshot.md`; material decision drift requires an amendment.

## Implementation Handoff

Render this handoff after the combined package is approved, frozen, and committed.

1. Frozen package:
   - `docs/work-items/2026-07-18_planning-template-clarity/spec_planning-template-clarity.md`.
   - `docs/work-items/2026-07-18_planning-template-clarity/plan_planning-template-clarity.md`.
   - `docs/work-items/2026-07-18_planning-template-clarity/snapshots/architecture.snapshot.md`.
   - `docs/work-items/2026-07-18_planning-template-clarity/snapshots/test-cases.snapshot.md`.
   - Any approved amendment created before execution.
2. Applicable instructions: repository `AGENTS.md`, `.agents/skills/dev-doc-harness/SKILL.md`, and `rule:execution-quality.execution-thread-start`.
3. Next activity: `TASK-001`—add the failing structural contract checks.
4. Approved execution selection: Terra, balanced tier, high reasoning, single-agent, Superpowers executing-plans.
5. Approved fallback: Terra, balanced tier, medium reasoning; stop if no balanced-tier selection is available.
6. Sub-agent strategy: no write-capable workers; one proposed read-only `REVIEW-001` after integrated implementation and primary validation, using the recorded curated-artifact inputs and coherence lens.
7. Sub-agent authorization: record `Approved` or `Declined` at package approval. If approved, do not ask again for the in-envelope review; use the orchestration-thread fallback if unavailable.
8. Execution continuity: new task with curated-artifact handoff.
9. Rehydration: load the exact frozen package, current branch/worktree, approval commit, amendments, variance log, and validation baseline before editing.
10. Variance stop condition: stop for any material change listed under Validation and Variance.
11. Task creation: ask separately for explicit approval before creating a configured implementation task; otherwise display this as a copy-ready manual handoff.

## Readiness

- [x] Frozen-input candidates, scope, tasks, checks, documentation, and changelog paths are concrete.
- [x] Planning observations and approved execution selection are distinct and complete.
- [x] Every Specification Commitment maps to implementation tasks and evidence.
- [x] The operator approved the proposed `REVIEW-001` sub-agent strategy before package freeze.
- [x] No required decision, unresolved placeholder, missing section, or ownerless deferral remains.

## Completion

- Required policy, source-template, generated-output, validation, and operator-guidance changes are complete.
- All Plan Checks pass and any noteworthy variance is recorded.
- Planned changes are committed, or the completion report states the exact blocker and current worktree status.

## Approval

- Status: Approved
- Superseded by: None
