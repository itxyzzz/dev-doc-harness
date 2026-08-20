# Plan Template Alignment Plan

Work ID: `2026-08-03_plan-template-alignment`
Short ID: `plan-template-alignment`
Status: Approved
Harness release: `0.8+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:architecture`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`
Execution method: `superpowers:executing-plans`

## Input Artifacts

Read these before finalizing implementation planning:

1. Approved spec: `spec_plan-template-alignment.md`.
2. Architecture input: None; the spec records the existing source-block, manifest, assembly, and validator architecture as sufficient.
3. Required snapshots or deltas: None.
4. Relevant repository files: `AGENTS.md`; `.agents/skills/dev-doc-harness/SKILL.md`; the seven canonical policy references cited in the spec; both plan manifests; affected `plan.030`, `plan.040`, `plan.050`, `plan.080`, `plan.085`, and `plan.090` blocks; `scripts/assemble_templates.py`; `scripts/test_harness_policy.py`; and the two assembled plan templates.
5. Unresolved implementation context to confirm before editing: None identified. The phase documentation-matrix redesign is explicitly out of scope.

The plan consumes the approved spec and must not reinterpret its decisions. If a material template, lifecycle, policy, or validation boundary changes after freeze, use `rule:lifecycle.variance-policy` and an amendment when required.

## Traceability approach

Use stable task and check IDs plus local `Covers` links. A complete mapping is unnecessary because each task has a bounded source/manifest/validator surface and local links provide the required coverage.

## Change surfaces

1. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.040.common.model-strategy.md`: rename to `plan.055.common.model-strategy.md` without changing its shared strategy prompts.
2. `.agents/skills/dev-doc-harness/assets/templates/assemblies/small-medium-work-item-plan.json` and `large-phased-work-item-phase-plan.json`: update the renamed source path and place it after `plan.050.common.task-plan.md`.
3. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.090.small.readiness-completion-approval.md`: replace the small readiness checklist with the approved coverage-oriented wording.
4. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.030.phase.fresh-thread-readiness.md`: rename to `plan.030.phase.session-readiness.md`, render a top-level phase-session section, and correct its approved-anchor amendment route.
5. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.080.phase.documentation-tasks-handoff.md`: retain the documentation-tasks content unchanged and split its completion-report content into a new block.
6. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.phase.handoff.md`, new `plan.087.phase.completion-report.md`, and `plan.090.phase.readiness-completion-approval.md`: separate phase execution handoff, completion reporting, and phase readiness.
7. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: update direct source-path, heading, ordering, and negative retired-contract assertions only where required.
8. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md` and `large-phased-work-item-phase-plan.md`: regenerate through the assembler; do not edit directly.

## Implementation approach

Preserve the source-block/manifest design. First move the unchanged common strategy block and modify the two manifest orders. Next revise the small readiness and phase-only session/handoff/completion/readiness sources, splitting only the phase completion-report content from the unchanged documentation-tasks block. Then update targeted structural assertions, regenerate outputs, and run complete validation. Keep the phase documentation-matrix structure unchanged.

## Implementation tasks

### `TASK-001` Reorder the shared strategy block in both plan assemblies

Dependencies: Approved planning package and fresh execution authorization.

Interfaces:

1. Consumes: `SPEC-001`, `VER-001`, the shared strategy block, both plan manifests, and generated-template assembly conventions.
2. Produces: One renamed shared strategy block referenced after the common task block by both manifests.

Implementation:

1. Rename `blocks/plan.040.common.model-strategy.md` to `blocks/plan.055.common.model-strategy.md` without changing its policy prompts.
2. In the small-plan manifest, replace the old path and place `plan.055.common.model-strategy.md` immediately after `plan.050.common.task-plan.md` and before `plan.060.small.planned-commits.md`.
3. In the phase-plan manifest, replace the old path and place the renamed block immediately after `plan.050.common.task-plan.md` and before `plan.060.phase.planned-commits.md`.
4. Confirm no current manifest retains `plan.040.common.model-strategy.md`.

Exit criteria: Both assemblies use one renamed strategy source and emit it after implementation tasks.

#### `CHECK-001` Verify shared strategy source and manifest order

Covers: `VER-001`.

Method: Run `rg -n "plan\.0(40|55)\.common\.model-strategy|plan\.050\.common\.task-plan|plan\.060" .agents/skills/dev-doc-harness/assets/templates/assemblies/small-medium-work-item-plan.json .agents/skills/dev-doc-harness/assets/templates/assemblies/large-phased-work-item-phase-plan.json`.

Expected result: Both manifests list `plan.050`, then `plan.055`, then their applicable `plan.060`; neither lists `plan.040.common.model-strategy.md`.

Evidence record: Implementation completion report with the command summary.

### `TASK-002` Replace the small-plan readiness checklist

Dependencies: `TASK-001`.

Interfaces:

1. Consumes: `SPEC-002`, `VER-002`, `plan.090.small.readiness-completion-approval.md`, and the operator-approved checklist.
2. Produces: A small readiness block that checks plan self-sufficiency, task/check quality, documentation-matrix application through normal tasks, next-stage strategy fit, and unresolved decisions.

Implementation:

1. Replace only the readiness checklist in `plan.090.small.readiness-completion-approval.md` with these six checks:

```md
- [ ] This plan document is self-sufficient: the declared inputs, architecture decisions, change surfaces, implementation approach, tasks and checks allow a fresh executor session to implement it fully without reconstructing hidden context or inventing scope.
- [ ] Each implementation task has a bounded outcome, clear dependencies and interfaces where relevant, executable steps, and observable exit criteria.
- [ ] Plan Checks cover the full set of Verification Criteria; each is nested under its owning task, states an expected result, and identifies where evidence will be recorded.
- [ ] The companion specification’s documentation artifact matrix has been applied: every required documentation or changelog change is embedded in an implementation task, and every non-applicable or deferred item retains its recorded reason.
- [ ] The next-implementation-stage recommended orchestration, model, and sub-agent strategy are fully documented and appropriate for the tasks and scope.
- [ ] No placeholder, unresolved implementation decision, missing owner, or ownerless deferral remains.
```

2. Leave the existing Completion and Approval sections unchanged.
3. Do not add a documentation-tasks section or change the current-session header or grouped next-stage selection.

Exit criteria: The small plan has the exact approved readiness intent without creating a second documentation-classification owner.

#### `CHECK-002` Verify small-plan readiness contract

Covers: `VER-002`.

Method: Run `rg -n -C 1 "This plan document is self-sufficient|Plan Checks cover the full set|documentation artifact matrix has been applied|next-implementation-stage recommended|Documentation Tasks" .agents/skills/dev-doc-harness/assets/templates/blocks/plan.090.small.readiness-completion-approval.md`.

Expected result: The four distinctive approved phrases appear in the small readiness source; it contains no `## Documentation Tasks` heading.

Evidence record: Implementation completion report with the command summary.

### `TASK-003` Establish the phase session boundary before tasks

Dependencies: `TASK-001`.

Interfaces:

1. Consumes: `SPEC-003`, `VER-003`, the phase session source block, phase manifest, approved-anchor lifecycle boundary, and variance policy.
2. Produces: One top-level phase-session section that lets an author correct a draft phase plan locally or route material anchor changes through amendment.

Implementation:

1. Rename `plan.030.phase.fresh-thread-readiness.md` to `plan.030.phase.session-readiness.md` and update the phase manifest path.
2. Replace the current insertion with `## Phase session readiness` and concise text requiring one orchestration session with documented bounded delegation, no hidden chat context, no excessive coordination, and no oversized boundary.
3. State that a draft phase plan that fails this bar is revised or split before its own freeze without narrowing, dropping, or reinterpreting approved-anchor decisions.
4. State that a material change to the approved anchor's scope, phase decomposition, architecture, commitments, or verification requires an amendment and approval before phase implementation.
5. Do not state or imply that a normal phase-plan author updates an approved anchor spec before freeze.

Exit criteria: The phase session boundary is scannable, uses session terminology, and accurately describes the post-anchor lifecycle.

#### `CHECK-003` Verify phase session readiness wording

Covers: `VER-003`.

Method: Run `rg -n -C 2 "^## Phase session readiness$|one orchestration session|hidden chat context|amendment|update the anchor spec before freeze" .agents/skills/dev-doc-harness/assets/templates/blocks/plan.030.phase.session-readiness.md`.

Expected result: The source contains the new heading, session boundary, and amendment path; it does not contain the retired anchor-edit phrase.

Evidence record: Implementation completion report with the command summary.

### `TASK-004` Separate the phase execution handoff and completion report

Dependencies: `TASK-003`.

Interfaces:

1. Consumes: `SPEC-004`, `VER-004`, the phase documentation-tasks/handoff source, current phase handoff source, phase manifest, execution-start rule, and rolling/batch lifecycle policy.
2. Produces: An unchanged documentation-tasks section, a current-phase execution handoff, and a later-facing completion-report contract with no preselected successor lifecycle.

Implementation:

1. Retain the `## Documentation Tasks` text and entries unchanged, moving it to a source block named `plan.080.phase.documentation-tasks.md` if splitting the current combined source is needed.
2. Create `plan.087.phase.completion-report.md` containing `## Phase completion report` and the existing implementation-completion reporting obligations: assigned scope; files; commands/tests; assumptions or residual risk; recommended next step; de-facto sub-agent use; uncommitted-change blocker state; and actual outputs, validation evidence, variance, commit state, and later-stage inputs.
3. Change `plan.085.phase.handoff.md` heading to `## Phase implementation handoff` and state that it is finalized at the phase plan's frozen boundary and owns only `phase execution`.
4. Retain the existing grouped next-stage recommendation with `Stage: phase execution`, including its method, orchestration, model, and fallback groups.
5. Replace `### Current-phase implementation handoff` with `### Phase-execution startup`, recording the frozen package, artifact rehydration/startup rule, and variance stop condition; cite `rule:execution-quality.execution-thread-start`.
6. Remove `### Post-phase transition` entirely. Do not select a later lifecycle stage or future-stage sub-agent strategy in this phase plan.
7. In the phase manifest, render documentation tasks, phase implementation handoff, then phase completion report, then readiness.
8. Preserve the rolling-default and batch-exception sentence, explaining that batched or parallel execution uses each approved phase plan's documented coordination boundary and does not create an automatic later transition.

Exit criteria: A frozen phase plan hands off its own phase execution, and its later completion report records actual facts without creating a second lifecycle decision.

#### `CHECK-004` Verify phase handoff and completion separation

Covers: `VER-004`.

Method: Run `rg -n -C 2 "^## (Phase implementation handoff|Phase completion report)$|^### (Phase-execution startup|Post-phase transition)$|Artifact rehydration|execution-thread-start|Stage: `phase execution`|rolling|Batch" .agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.phase.handoff.md .agents/skills/dev-doc-harness/assets/templates/blocks/plan.087.phase.completion-report.md`.

Expected result: The new headings, startup rule, and phase-execution stage appear in the authoritative sources; no `Post-phase transition` heading appears; rolling and batch guidance remains present.

Evidence record: Implementation completion report with the command summary.

### `TASK-005` Replace the phase readiness checklist at the true phase boundary

Dependencies: `TASK-004`.

Interfaces:

1. Consumes: `SPEC-005`, `VER-005`, phase inputs, task/check contract, phase execution handoff, completion report, and unchanged documentation obligations.
2. Produces: A phase-specific readiness checklist without a speculative future-stage selection.

Implementation:

1. Replace the phase readiness checklist with concise checks that confirm: self-sufficient preservation of approved anchor, amendments, and prior outputs; one-session bounded phase scope; bounded task shape; full Verification Criteria coverage by nested checks; clear assigned documentation/changelog obligations; the phase-execution handoff's frozen package, artifact rehydration, variance stop, and appropriate current-stage strategy; completion-report expectations; and no unresolved decision or ownerless deferral.
2. Retain the existing Completion and Approval sections unchanged.
3. Do not reintroduce `Post-phase transition` or a future-stage sub-agent assessment.

Exit criteria: The phase checklist verifies the artifact's current execution boundary and its required evidence record without deciding its successor.

#### `CHECK-005` Verify phase readiness scope

Covers: `VER-005`.

Method: Run `rg -n -C 1 "approved anchor|one orchestration session|Plan Checks cover|artifact rehydration|Phase completion report|Post-phase transition|Upcoming-stage sub-agent assessment" .agents/skills/dev-doc-harness/assets/templates/blocks/plan.090.phase.readiness-completion-approval.md`.

Expected result: The new readiness checks appear in the authoritative source; the retired post-phase and future-stage-assessment phrases do not appear in the phase readiness source.

Evidence record: Implementation completion report with the command summary.

### `TASK-006` Update structural checks, assemble, and validate the plan templates

Dependencies: `TASK-001`, `TASK-002`, `TASK-003`, `TASK-004`, `TASK-005`.

Interfaces:

1. Consumes: Revised authoritative blocks and manifests, `SPEC-006`, `VER-006`, `VER-007`, and current structural assertions.
2. Produces: Targeted validator coverage plus regenerated plan templates and recorded validation evidence.

Implementation:

1. Replace direct references to `plan.040.common.model-strategy.md` in `scripts/test_harness_policy.py` with `plan.055.common.model-strategy.md` where the renamed source is the intended owner.
2. Replace assertions for `## Phase transitions`, `Current-phase implementation handoff`, and `Post-phase transition` with positive assertions for `## Phase implementation handoff`, `Phase-execution startup`, `## Phase completion report`, artifact rehydration, and the execution-start rule, plus negative assertions for retired headings.
3. Update the phase session-boundary assertion to require the new heading and amendment path and reject the retired approved-anchor edit wording.
4. Add focused checks for the distinctive small and phase readiness contracts without creating a semantic parser or weakening unrelated assertions.
5. Retain existing generated-template schema, state-heading, rolling/batch, model notation, assembly-freshness, and policy-owner coverage.
6. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` to regenerate the two plan outputs.
7. Run the full policy validator, the assembly freshness check, whitespace validation, generated-template diff review, and worktree status check.
8. Create `changelog/implementation-fragment.md` only after execution starts and update `CHANGELOG.md` before the implementation commit, using the planned subject unless a recorded variance changes it.

Exit criteria: Generated outputs are fresh; full policy validation passes; the validator protects the revised contracts and rejects retired plan-template structure.

#### `CHECK-006` Run complete current-harness validation

Covers: `VER-006`, `VER-007`.

Method: Run these commands in order:

1. `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`
2. `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`
3. `git diff --check`
4. `git diff -- .agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md .agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
5. `git status --short`

Expected result: Both Python commands exit 0; whitespace validation produces no errors; the generated-template diff contains only planned source-derived structural changes; and the worktree contains only planned implementation targets, the implementation changelog fragment, and root changelog update.

Evidence record: Implementation completion report with command summaries and the final changed-file list.

## Model and Sub-agent Strategy

Upcoming-stage sub-agent assessment:

1. Sub-agents: One bounded read-only independent reviewer, defined below.
2. Fit reason: Source-block moves, manifest order, phase-tail restructuring, generated outputs, and structural assertions are tightly coupled for writing, but an isolated final review of the integrated diff improves requirements-traceability and regression-risk detection without introducing write conflicts.
3. Authorization state: Approved by the operator on 2026-08-03 for Sol at medium reasoning.

Sub-agent `plan-template-final-reviewer`:

1. Purpose: Review the integrated implementation diff and validation evidence for plan/spec traceability, stale source-path or heading contracts, generated-output regressions, and unintended scope expansion before the implementation commit.
2. Context strategy: `curated artifacts`.
3. Input context: Frozen spec and plan, affected source blocks and manifests, changed diff, generated plan outputs, `test_harness_policy.py` result, assembler freshness result, and whitespace-validation result.
4. Output artifact: Evidence-backed review findings with severity, affected paths, reproduction or validation paths, residual risk, and recommended next step.
5. Active model policy: `economy-default` selected by repository `AGENTS.md`.
6. Recommended sub-agent model: Generation `GPT-5.6`; Capability tier `flagship`; Reasoning effort `medium`; the operator selected Sol medium for this independent review.
7. Resolved target profile: `Sol medium`.
8. Availability/fallback: Sol medium is available for the planning-package review. If it becomes unavailable for execution review, stop and ask the operator before substituting a model or reviewer arrangement.
9. Selection reason: A read-only reviewer has a separate context and can inspect the final assembled/template-validator contract without touching tightly coupled source files.
10. Parallel execution: No; run after all planned source, manifest, generated-output, and validation work is integrated.
11. Blast radius if wrong: Medium; a missed template or validator inconsistency could make future planning artifacts misleading, but the change has no runtime product impact.
12. Write authority: `read-only`.
13. Concurrency: `single run` after integrated validation.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: plan-template-alignment -- approve plan template cleanup` |
| Implementation | `docs: plan-template-alignment -- align assembled plan templates` |

One cohesive implementation commit is the default because renamed/moved source blocks, manifests, generated templates, validator expectations, and the implementation changelog must remain synchronized.

## Validation and variance

Plan Checks `CHECK-001` through `CHECK-006` provide the required evidence. Before freeze, update this draft directly for operator feedback. After freeze, record noteworthy implementation drift in `implementation-notes/variance-log.md`; use an amendment for material scope, lifecycle, schema, model-policy, validation-contract, documentation-matrix, or phase-coordination changes.

Allowed minor variance:

1. Adjust Markdown line wrapping or assertion patterns when required by the final approved source wording while preserving every stated positive and negative contract.
2. Use a differently numbered source-block filename only when it remains order-consistent, is reflected in both manifests and validator assertions, and does not add duplicate shared policy text.

Operator approval required before continuing:

1. Moving phase documentation obligations out of their existing section or changing the companion-spec documentation-matrix schema.
2. Changing lifecycle-stage values, freeze-gate mechanics, current-session diagnostics, the shared model-policy content, published template paths, schemas, or unrelated plan-template surfaces.
3. Weakening assembly freshness, rolling/batch guidance, state-heading checks, or unrelated structural validator coverage.
4. Expanding the work to alter canonical policy references rather than templates and their direct structural checks.

## Implementation handoff

### Next-stage recommendation

#### Next lifecycle stage

Stage: `plan execution`.

#### Orchestration

Method: `superpowers:executing-plans`; Orchestration mode: `bounded delegated sub-agents`; Run in: `new orchestration session`; Review: preserve execution checkpoints, then run the approved read-only `plan-template-final-reviewer` on Sol medium after integrated validation and before the implementation commit.

#### Model

Generation: `latest available`; Capability tier: `balanced`; Reasoning: `medium`.

#### Fallbacks and limits

Use the frozen spec and plan, affected source blocks, manifests, generated templates, and current validator assertions. Stop for an approval-required variance listed above.

1. Frozen package: approved `spec_plan-template-alignment.md` and `plan_plan-template-alignment.md`.
2. Artifact rehydration: Load the frozen package, relevant instructions and policy references, affected sources/manifests, assembler, and focused validator assertions before editing.
3. Variance stop condition: Stop for any approval-required change listed in Validation and variance.

## Readiness

- [x] This plan document is self-sufficient: declared inputs, architecture decisions, change surfaces, implementation approach, tasks, and checks allow a fresh executor session to implement it without reconstructing hidden context or inventing scope.
- [x] Each task has a bounded outcome, dependencies and interfaces, numbered executable steps, an observable exit criterion, and one or more nested checks where needed.
- [x] The checks cover all Verification Criteria and state their expected evidence.
- [x] The companion specification's documentation artifact matrix has been applied: implementation documentation and changelog work is embedded in `TASK-006`; items not applicable are recorded in the matrix.
- [x] The next-implementation-stage recommendation and stage-specific sub-agent assessment are explicit and appropriate for the task coupling and scope.
- [x] No placeholder, unresolved implementation decision, missing owner, or ownerless deferral remains.

## Completion

- Required work and evidence are complete; any noteworthy variance is recorded.
- Planned changes are committed, or the blocker is stated.

## Approval

- Status: Approved
- At freeze, relabel the grouped recommendation **Approved next stage** and mirror it in chat.
- Superseded by: None
