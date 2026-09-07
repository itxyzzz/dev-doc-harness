# Quality and Efficiency Policy Plan

Work ID: `2026-08-27_quality-efficiency-policy`
Short ID: `quality-efficiency-policy`
Status: Approved
Harness release: `0.10+`
Schema: `schema:plan.medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:execution-quality`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`
Execution method: `superpowers:subagent-driven-development`

## Input Artifacts

1. Draft spec: `spec_quality-efficiency-policy.md`.
2. Architecture input: `snapshots/architecture.snapshot.md` (`DEC-001` through `DEC-003`).
3. Required snapshot: `snapshots/test-cases.snapshot.md`.
4. Relevant repository files: `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`, `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, root `AGENTS.md`, root `README.md`, the two source blocks, three generated templates, assembly manifests, and `scripts/assemble_templates.py`.
5. Unresolved implementation context to confirm before editing: None.

## Traceability approach

Local commitment-to-task and verification-to-check references provide the required fresh-executor handoff without a separate mapping table.

## Global Constraints

Self-containment reason: implementation changes a canonical policy and its consumer graph. Every task must preserve the approved decisions below.

1. Keep generic model, delegation, escalation, authorization, reviewer, isolation, context, write-authority, concurrency, reporting, and final-integration rules outside the profiles.
2. Update generated templates only through `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write`.
3. Do not modify pre-existing `docs/work-items/**`, historical `CHANGELOG.md` records, or `docs/releases/0.7.0.md`.
4. Do not add Pro-mode work, cost calculations, new required planning fields, or a new delegation approval route.

## Change surfaces

1. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`: hierarchy, owner IDs, profile names, lightweight model/orchestration biases, and concise non-obvious selection rationale.
2. `AGENTS.md` and `README.md`: current profile-selection vocabulary only.
3. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.055.medium-and-large.model-strategy.md` and `blocks/spec.060.large.phase-decomposition-model.md`: active policy prompt vocabulary only.
4. `.agents/skills/dev-doc-harness/assets/templates/medium-work-item-plan.md`, `large-phased-work-item-spec.md`, and `large-phased-work-item-phase-plan.md`: assembler-generated outputs only.
5. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: nested-section extraction, profile assertions, active-guidance assertion, and current fixture vocabulary.
6. `deltas/operator-manual.delta.md`, `changelog/implementation.md`, and `implementation-notes/variance-log.md`: implementation evidence and operator guidance created during `TASK-005`.

## Implementation approach

First extend the focused validator so the current hierarchy and profile names fail the new contract. Then update the canonical policy and active guidance, update source blocks, regenerate templates, and resolve validator failures only at their canonical or source owner. Finish with the required operator-guidance delta, implementation evidence, and independent policy review before one cohesive implementation commit.

## Implementation tasks

### `TASK-001` Establish the validator contract

Dependencies: frozen package and fresh implementation authorization.

Interfaces:

1. Consumes: `SPEC-001` through `SPEC-003`, `DEC-001` through `DEC-003`, and `TC-001` through `TC-005`.
2. Produces: focused validator expectations for the changed hierarchy, profiles, and active vocabulary.

Implementation:

1. Re-read the frozen spec, plan, architecture snapshot, test-case snapshot, applicable `AGENTS.md`, current policy, and baseline validation output before editing.
2. In `test_harness_policy.py`, retain `read_markdown_h2_section()` for unrelated H2 consumers and add a targeted H3-aware section reader for `### Model selection` inside `## Upcoming-stage selection`.
3. Change `assert_model_selection_dimensions()` to use the H3-aware reader for Model selection. Update the active-policy assertion, profile assertion labels, and literal fixtures from `enterprise-default`/`economy-default` to `quality-first`/`efficiency-first`.
4. Add assertions for the nested heading hierarchy; renamed rule IDs; profile deferral to generic safeguards; both profiles' delegation bias; preserved independent review; and the agreed direct/high and fast/economy profile boundaries.
5. Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` and record the expected failures caused by the still-old canonical policy and live consumers. Stop if a baseline-unrelated failure appears.

Exit criteria: `TC-001` through `TC-005` have focused validator coverage, and the validator fails only for the pre-migration contract.

#### `CHECK-001` Verify the validator red phase

Covers: `VER-001`, `VER-002`, `VER-003`.

Method: Run the focused validator after its contract changes and inspect the reported contract failures.

Expected result: the old contract fails at the changed selection/profile assertions, with no unrelated failure.

Evidence record: execution log and `implementation-notes/variance-log.md`.

### `TASK-002` Update the canonical hierarchy and profile definitions

Dependencies: `TASK-001` red validator contract.

Interfaces:

1. Consumes: the focused contract from `TASK-001` and `DEC-001` through `DEC-003`.
2. Produces: the canonical hierarchy, renamed rule owners, and lightweight profile bodies.

Implementation:

1. Nest `### Model selection` beside `### Orchestration selection` within `## Upcoming-stage selection`; move its facets below it and rename the profile heading `#### Model and orchestration selection policies`.
2. Rename profile rule IDs and bodies to `quality-first` and `efficiency-first`, with no live alias.
3. Keep generic rules outside profile bodies. Give quality-first its stronger justified allocation and additional bounded-coverage bias; give efficiency-first its least-total-delivery-cost and least-fan-out bias while retaining the generic review/isolation floor.
4. Preserve the agreed Terra/Sol ladder, direct flagship/high exception, and fast/economy support-work boundary as profile-local refinements.
5. Allow only decisive-factor prose in the existing conditional combined-selection rationale; do not add calculations, fields, or approval routes. Run the policy validator.

Exit criteria: `TC-001`, `TC-003`, `TC-004`, and `TC-005` pass against the canonical policy; any remaining failure identifies a direct consumer handled by later tasks.

#### `CHECK-002` Confirm canonical migration

Covers: `VER-001`, `VER-002`, `VER-003`.

Method: Inspect the owner table, nested hierarchy, profile bodies, and validator output after the canonical edit.

Expected result: the policy satisfies the new hierarchy and profile contract; remaining failures, if any, name only direct live consumers in `TASK-003` or `TASK-004`.

Evidence record: validator output and diff review.

### `TASK-003` Migrate active root guidance and template sources

Dependencies: `TASK-002` canonical names and rule IDs.

Interfaces:

1. Consumes: canonical profile vocabulary and the two source-block prompt interfaces.
2. Produces: aligned root guidance and assembler inputs.

Implementation:

1. Update `AGENTS.md` to select `efficiency-first` and name `quality-first` as the unselected alternative; update the README bootstrap example to select `efficiency-first`.
2. Replace the two listed active-model-policy values in `plan.055.medium-and-large.model-strategy.md` and `spec.060.large.phase-decomposition-model.md` with `quality-first` and `efficiency-first`.
3. Do not copy canonical profile semantics into root guidance or template prompts. Run the policy validator and inspect direct active-guidance failures.

Exit criteria: root guidance and template sources use the new vocabulary, with no profile-rule duplication.

### `TASK-004` Regenerate templates and prove active-consumer parity

Dependencies: `TASK-003` updated root guidance and source blocks.

Interfaces:

1. Consumes: modified source blocks and active vocabulary.
2. Produces: current generated templates and complete active-consumer validation.

Implementation:

1. Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` once; do not edit generated templates directly.
2. Inspect the regenerated prompts in the medium-plan, large-spec, and large-phase-plan templates to confirm that only profile vocabulary changed.
3. Run the assembler check, policy validator, and a scoped old/new-name search over active policy, root guidance, source blocks, generated templates, and validator code.
4. Retain old-name matches only in immutable historical records outside active scope.

Exit criteria: all active consumers use new names, assembled outputs are current, and `VER-004` passes.

#### `CHECK-003` Confirm active-consumer parity

Covers: `VER-002`, `VER-004`.

Method: Run assembler write/check, the policy validator, and `rg -n 'enterprise-default|economy-default|quality-first|efficiency-first' AGENTS.md README.md .agents/skills/dev-doc-harness --glob '!docs/releases/**'`.

Expected result: current surfaces use only new names; any old-name match is outside the scoped live set and documented as historical.

Evidence record: assembler/validator output and scoped-search summary.

### `TASK-005` Create the required handoff evidence

Dependencies: `TASK-004` passing active-consumer parity.

Interfaces:

1. Consumes: final implementation scope and validation evidence.
2. Produces: required operator guidance, implementation changelog, and variance record.

Implementation:

1. Create `deltas/operator-manual.delta.md` describing the two profiles, their shared generic floor, and optional fan-out bias without restating canonical rules.
2. Create `changelog/implementation.md` with release target `unreleased`, package impact `distributable`, and Changed entries for hierarchy/profile migration and template/validator parity.
3. Create `implementation-notes/variance-log.md` with `None` unless useful routine variance occurred; stop for an amendment if protected policy boundaries change.

Exit criteria: all required implementation evidence has an owner and accurately reflects the integrated change.

### `TASK-006` Independently review, validate, and commit

Dependencies: `TASK-005` implementation evidence.

Interfaces:

1. Consumes: complete implementation diff, required evidence, and approved reviewer strategy.
2. Produces: review disposition, final validation evidence, and one cohesive implementation commit.

Implementation:

1. Run the independent policy reviewer after `TASK-002`, after `TASK-004`, and on the integrated diff. Supply the frozen package, relevant diff, validation output, and the lens: profile-boundary duplication, hierarchy correctness, reviewer-floor preservation, stale live vocabulary, and generated-output ownership.
2. Resolve blocking in-scope findings, rerun affected checks, and record nonblocking residual risk.
3. Run changelog lint, assembler check, policy validator, scoped Pro-mode search, and `git diff --check`.
4. Inspect the full diff and work-item paths; confirm no historical file changed and only this work item's new evidence is added under `docs/work-items`.
5. Stage approved implementation paths and evidence, verify staged names/whitespace, then commit `docs: quality-efficiency-policy -- align model and orchestration profiles`.

Exit criteria: `VER-001` through `VER-004` have passing evidence, no blocking review finding remains, and the cohesive commit contains only approved current surfaces and implementation evidence.

#### `CHECK-004` Validate final policy, review, and documentation evidence

Covers: `VER-001`, `VER-002`, `VER-003`, `VER-004`.

Method: Run independent reviews at the three stated checkpoints, then changelog lint, assembler check, full validator, scoped old-name and Pro-mode searches, `git diff --check`, and path-limited diff review.

Expected result: every validation command exits `0`; the Pro-mode search returns no result (its normal no-match exit code is accepted); current policy and consumer surfaces agree; old names are absent from active scope; no unrelated or historical file is changed.

Evidence record: command output summaries, diff review, and final completion report.

## Model and Sub-agent Strategy

Upcoming-stage sub-agent assessment:

1. Sub-agents: bounded delegated implementation executor and independent policy reviewer.
2. Fit reason: the canonical policy, source/generated templates, root guidance, and validator are tightly coupled for writing but benefit from independent evidence-based review at the canonical, consumer-parity, and final integration points.
3. Authorization state: Approved — the operator authorized use of sub-agents when useful in this task.
4. The no-proactive-dispatch constraint does not apply because this strategy is explicitly approved; final integration remains with the orchestration session.

Sub-agent `implementation-task executor`:

1. Purpose: Execute one approved Plan Task at a time within its named paths and return validation evidence.
2. Context strategy: `curated artifacts`.
3. Input context: frozen spec, plan, required snapshots, applicable task files, current diff, and prior-task validation output.
4. Output artifact: focused patch, commands run, and task report.
5. Active model policy: `efficiency-first` after implementation starts; current source policy is migrated by `TASK-002`.
6. Recommended sub-agent model: Generation `latest available`; Capability tier `balanced`; Reasoning effort `high` because policy/validator reconciliation spans multiple current surfaces.
7. Resolved target profile: `GPT-5.6 Terra high` when exposed.
8. Availability/fallback: orchestration session executes the same bounded task with the frozen inputs.
9. Selection reason: Terra high fits clear but cross-surface implementation while preserving the efficiency-first profile.
10. Parallel execution: No — canonical policy, validator, and generated templates are shared integration surfaces.
11. Blast radius if wrong: Medium — a bad edit can misdirect later selection or leave generated templates stale.
12. Write authority: only paths named by the active Plan Task.
13. Concurrency: single executor run.

Sub-agent `independent policy reviewer`:

1. Purpose: Review the canonical-policy integration, active-consumer regeneration, and final integrated diff for hierarchy drift, profile duplication, weakened guardrails, stale names, and generated-output ownership errors.
2. Context strategy: `curated artifacts`.
3. Input context: frozen package, checkpoint or final diff, changed files, validator/assembler output, and the named review lens in `TASK-006`.
4. Output artifact: evidence-backed findings with severity, validation path, and residual risk.
5. Active model policy: `efficiency-first` after implementation starts; the reviewer allocation is a documented tier escalation for policy-wide impact.
6. Recommended sub-agent model: Generation `latest available`; Capability tier `flagship`; Reasoning effort `medium`.
7. Resolved target profile: `GPT-5.6 Sol medium` when exposed.
8. Availability/fallback: use `superpowers:executing-plans` with its disclosed reviewer arrangement when subagent-driven development is unavailable. When only host-native execution remains, retain the approved independent reviewer; if independent review is unavailable, pause for the existing explicit operator decision before an orchestration-session fallback and record the limitation.
9. Selection reason: a read-only independent lens reduces policy-regression risk without adding concurrent writing or a flagship/high escalation.
10. Parallel execution: No — reviews follow `TASK-002`, `TASK-004`, and integrated validation.
11. Blast radius if wrong: High — missed harness policy drift can affect future work-item selection and review quality.
12. Write authority: read-only.
13. Concurrency: one reviewer at each named checkpoint.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: quality-efficiency-policy -- approve profile selection update` |
| Implementation | `docs: quality-efficiency-policy -- align model and orchestration profiles` |

One cohesive implementation commit is the default. Planning approval contains only this package's spec, plan, and snapshots.

## Validation and variance

`CHECK-001` establishes the validator red phase. `CHECK-002` proves canonical-policy migration. `CHECK-003` proves current-consumer and source/generated parity. `CHECK-004` proves independent review, final policy, documentation, and diff integrity.

Routine variance may adjust exact prose, assertion helper layout, or source-block formatting when it preserves the approved hierarchy, profile names, generic-rule boundary, validation purpose, and generated-output ownership. Create an amendment and obtain approval before changing a generic guardrail, profile semantics, rule-ID migration approach, scope boundary, required evidence, or historical-immutability boundary.

## Implementation handoff

### Next-stage recommendation

#### Next lifecycle stage

Stage: `plan execution`.

#### Orchestration

- Method: `superpowers:subagent-driven-development`.
- Orchestration mode: `bounded delegated sub-agents`.
- Run in: `new orchestration session` in the existing local checkout on branch `policies-update`.
- Review: independent reviewer after canonical-policy integration, active-consumer regeneration, and on the final whole-branch policy diff.

#### Model

- Generation: `latest available`.
- Capability tier: `balanced` for execution, with the documented `flagship` reviewer allocation.
- Reasoning: `high` for execution; `medium` for independent review.

#### Execution requirements and contingencies

1. Rehydrate the frozen spec, plan, architecture snapshot, test-case snapshot, applicable instructions, current branch/worktree state, and baseline commands before editing.
2. If subagent-driven development is unavailable, use `superpowers:executing-plans` with its reviewer disclosure. If only host-native execution remains, retain the approved independent reviewer; if it is unavailable, pause for the existing explicit operator decision before a controller self-review and record the limitation. Do not broaden write authority or concurrency.
3. Stop for an amendment before changing generic safeguards, profile semantics, rule-ID migration, scope, or required evidence.

### Execution startup

1. Frozen package: `spec_quality-efficiency-policy.md`, `plan_quality-efficiency-policy.md`, `snapshots/architecture.snapshot.md`, and `snapshots/test-cases.snapshot.md`.
2. Artifact rehydration: the new execution session reads the frozen package, applicable instructions, branch `policies-update`, current local-checkout status, and baseline commands through `rule:execution-quality.execution-thread-start` after the planning approval commit and fresh implementation authorization.
3. Variance stop condition: any material change listed in Validation and variance requires an amendment and operator approval.

## Readiness

- [x] Declared inputs, decisions, change surfaces, tasks, and checks permit a fresh executor to implement without reconstructing chat context.
- [x] Tasks have bounded ownership, dependencies, interfaces, executable steps, and observable exit criteria.
- [x] Nested checks cover every Verification Criterion and identify evidence records.
- [x] Required documentation outputs have an owner task.
- [x] The next-stage orchestration, model, reviewer, context, authorization, fallback, write-authority, and concurrency strategy are explicit.
- [x] No placeholder, unresolved implementation decision, missing owner, or ownerless deferral remains.

## Completion

1. `SPEC-001` through `SPEC-004` conform through `CHECK-001` through `CHECK-004`.
2. Current policy, root guidance, source/generated templates, validator, and required implementation evidence agree.
3. The implementation fragment lints, no historical artifact changed, and the cohesive implementation commit is complete.

## Approval

- Status: Approved
- Superseded by: None
