# Lifecycle Stage Boundaries Plan

Work ID: `2026-07-31_lifecycle-stage-boundaries`
Short ID: `lifecycle-stage-boundaries`
Status: Approved
Harness release: `0.8+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `module:execution-quality`, `rule:lifecycle.planning-shape`, `rule:lifecycle.immutable-snapshots`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:execution-quality.execution-thread-start`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

Execution method: `superpowers:executing-plans`
Current planning Codex task: Model/profile, reasoning, and context visibility: `not exposed`.

## Input artifacts

1. Draft specification: `spec_lifecycle-stage-boundaries.md`.
2. Architecture input: None; this work item has no architecture snapshot.
3. Required snapshots or deltas: None.
4. Relevant repository files and review input: the lifecycle, freeze-gate, model, execution-start, router, template-source, generated-template, and validator files listed in Change surfaces; README lifecycle text as a read-only consistency baseline; the three operator review comments on `planning-freeze-gates.md`.
5. Unresolved implementation context to confirm before editing: None. The operator approved the design: canonical lifecycle description after `## Work item folders`; `Next lifecycle stage` replaces Activity/First Plan Task; remove the special handoff-snapshot lifecycle path.

## Traceability approach

Local `SPEC-*`, `VER-*`, `TASK-*`, and `CHECK-*` links are sufficient because each commitment maps directly to one or more policy/test surfaces. No separate mapping is needed.

## Change surfaces

1. `.agents/skills/dev-doc-harness/references/artifact-contract.md`: canonical two-shape lifecycle-stage-boundary description directly after `## Work item folders`; remove the explicit-handoff-snapshot lifecycle trigger and align transition terms.
2. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: make approval the only formal freeze checkpoint, remove duplicate completeness prose, use `Next lifecycle stage`, and retain ordinary approved-package continuity without `First Plan Task`.
3. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md` and `references/context-and-quality-gates.md`: consume the canonical stage term and remove task-level transition requirements.
4. `.agents/skills/dev-doc-harness/SKILL.md`: remove explicit handoff as a draft-freeze alternative while keeping the existing approval freeze gate. `README.md` is read-only; report a real semantic conflict only if one is found.
5. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.060.large.phase-decomposition-model.md`, `spec.070.large.planned-commits-freeze.md`, `spec.085.small.handoff.md`, `spec.085.large.handoff.md`, `plan.010.phase.header-objective-inputs.md`, `plan.085.small.handoff.md`, `plan.085.phase.handoff.md`, `plan.090.small.readiness-completion-approval.md`, and `plan.090.phase.readiness-completion-approval.md`: update the source-of-truth prompts and readiness checks.
6. `.agents/skills/dev-doc-harness/assets/templates/{small-medium-work-item-plan.md,large-phased-work-item-spec.md,large-phased-work-item-phase-plan.md}`: regenerated outputs only, using the existing assembly manifests and assembler.
7. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: update presentation fixtures/assertions and add focused conformance coverage for the canonical lifecycle-stage boundary and absence of the removed special path.
8. `docs/work-items/2026-07-31_lifecycle-stage-boundaries/changelog/implementation.md`: implementation-commit source fragment.

## Implementation approach

First change the validator contract so it represents the agreed policy and fails while the old language is present. Then update the lifecycle owner and its consumers, edit template source blocks and regenerate outputs, and run the complete validation set. Do not edit historical work-item artifacts. Do not touch or stage the unrelated evidence-reference modification.

## Model and sub-agent strategy

Upcoming-stage sub-agent assessment:

1. Sub-agents: One review-only final reviewer.
2. Fit reason: The policy, template, and validator surfaces are tightly coupled, so implementation remains in one orchestration thread; a separate final reviewer can independently test policy ownership and terminology consistency after the integrated change is complete.
3. Authorization state: Approved by the operator through review feedback.
4. Execution method: `superpowers:executing-plans`; use its task-by-task workflow after fresh post-freeze authorization.
5. Run in: `new Codex task`, because the current profile and context suitability are not exposed. The operator may explicitly override this runtime choice after freeze.

Sub-agent `final-policy-reviewer`:

1. Purpose: Review the final integrated policy, source-block, generated-template, and validator diff for lifecycle ownership, removal of the special handoff-snapshot route, and retained freeze/authorization boundaries.
2. Context strategy: Curated artifacts and diff.
3. Input context: Frozen spec and plan, changed-file diff, validator/assembler/changelog-lint output, and the current versions of affected canonical references and source blocks.
4. Output artifact: Review-only findings with severity, evidence, reproduction or validation path, and a clear `no findings` result when applicable.
5. Model policy: Operator override to Sol High for this final review.
6. Model generation: `gpt-5.6-sol` when available.
7. Capability tier: Flagship.
8. Resolved profile: `gpt-5.6-sol` with `high` reasoning effort.
9. Availability/fallback: If Sol High is unavailable, stop before commit and request operator direction; do not silently substitute another reviewer model.
10. Reasoning effort: `high`, selected by the operator for an independent final review of cross-cutting policy semantics.
11. Selection reason: The reviewer performs no edits and evaluates only the integrated final state, avoiding conflicting parallel ownership of tightly coupled policy changes.
12. Parallel execution: No; it runs after all implementation checks pass and before the implementation commit.
13. Write authority: None; review-only.
14. Blast radius if wrong: Medium; an incorrect review could miss a policy inconsistency, but the orchestration thread retains integration ownership and validation evidence.

## Implementation tasks

### `TASK-001` Define validator expectations for lifecycle stages

Dependencies: Approved planning package and fresh execution authorization.

Interfaces:

1. Consumes: `SPEC-001` through `SPEC-004`, the existing `assert_lifecycle_transition_targets`, `assert_execution_thread_start`, and `assert_next_stage_summary` checks.
2. Produces: A validator that encodes `Next lifecycle stage`, the allowed frozen-package-to-stage mapping, absence of `First Plan Task`, and absence of the special handoff-snapshot route in current reusable policy/template sources.

Implementation:

1. In `test_harness_policy.py`, update next-stage fixtures and `next_stage_summary_fixture_errors` so the required first group is `Next lifecycle stage`, it accepts an explicit valid stage, and it rejects the retired `Activity`/`First Plan Task` shape.
2. Add or update assertions that require `artifact-contract.md` to own a lifecycle-stage-boundaries section after work-item-folder guidance and to describe the established small/medium, staged-spec, large-anchor, and phase-plan transitions.
3. Update the execution-start and transition-target assertions to require the documented next lifecycle stage, not a first task, while retaining current fresh authorization, `Run in`, reviewer, and variance assertions.
4. Add targeted no-retired-route assertions over current reusable policy, source blocks, and generated templates only; exclude `docs/work-items/**` because frozen history intentionally remains unchanged.
5. Run the focused validator command before changing policy/template sources; record the expected failure showing that the repository still has the old contract.

Exit criteria: The validator's targeted checks fail only because the existing sources still use the old Activity/First Plan Task and special-handoff wording, proving the new requirement is enforced before policy changes.

#### `CHECK-001` Validator fails against the retired contract

Covers: `VER-001`, `VER-002`, `VER-003`.

Method: Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` after changing the validator but before changing policy/template sources.

Expected result: Non-zero exit with failures that identify missing lifecycle-stage wording or retired summary/handoff language; no unrelated failure is introduced.

Evidence record: Implementation completion report and `changelog/implementation.md` summary.

### `TASK-002` Make lifecycle and freeze policy approval-only and stage-based

Dependencies: `TASK-001`.

Interfaces:

1. Consumes: The failing validator requirements and the two lifecycle shapes presented in `README.md` as a read-only baseline.
2. Produces: Canonical lifecycle-stage terminology, approval-only freeze mechanics, and consistent ordinary continuity wording for policy consumers.

Implementation:

1. Add a concise `## Lifecycle stage boundaries` section immediately after `## Work item folders` in `artifact-contract.md`. State the two lifecycle variations and the valid next stage for an explicitly staged small/medium spec, a combined small/medium package, a large anchor, a phase plan, and an amendment resumption.
2. Update the later lifecycle sections only as needed to reference the canonical stage terminology. Remove `explicit handoff snapshot`/`explicit handoff` as an alternative freeze trigger or immutable-state condition; keep the established approval-commit freeze and approved-package transition ownership.
3. In `planning-freeze-gates.md`, scope `## Approval freeze checkpoint` to explicit package approval. Replace its duplicated package-completeness paragraph with a short recheck that points to the draft-review completeness rule. Rename the four-group first heading from `Activity` to `Next lifecycle stage`, remove `First Plan Task`, and update route inputs/chat-handoff wording to use the recorded stage.
4. In `subagent-model-policy.md` and `context-and-quality-gates.md`, replace task-level start language with the canonical next lifecycle stage. Preserve the requirement to load the exact frozen package, apply fresh authorization, and route variance correctly.
5. In `SKILL.md`, remove explicit handoff as a draft-freeze alternative while keeping the existing approval freeze gate. Do not edit `README.md`; compare the implemented canonical wording against its existing intentional simplification and report a real semantic conflict only if one exists.

Exit criteria: Live policy contains one canonical lifecycle-stage description, one approval-only formal freeze path, and no task-level summary field or special handoff-snapshot lifecycle state.

#### `CHECK-002` Current policy uses the agreed lifecycle contract

Covers: `VER-001`, `VER-002`, `VER-003`.

Method: Run targeted `rg` searches over `.agents/skills/dev-doc-harness`, excluding `docs/work-items`, for `First Plan Task`, `explicit handoff snapshot`, and the old `#### Activity` summary heading; inspect the new lifecycle section and the approval-freeze checkpoint.

Expected result: Retired terms are absent from current reusable policy except any intentional generic prose that does not denote a lifecycle state; the lifecycle and freeze-gate text name only the agreed stages and approval mechanism.

Evidence record: Implementation completion report with the exact search commands and inspected paths.

### `TASK-003` Update template sources and regenerate plan/spec templates

Dependencies: `TASK-002`.

Interfaces:

1. Consumes: The canonical stage names and approval-only lifecycle policy.
2. Produces: Assembled templates whose prompts, inputs, handoffs, and readiness checks use `Next lifecycle stage` and approved frozen-package continuity.

Implementation:

1. In the large-spec source blocks, replace the Activity/First Plan Task presentation with `Next lifecycle stage: phase-plan drafting`, remove special-handoff wording, and make the large handoff describe the first phase-plan stage without a task-level placeholder.
2. In the small-plan and phase-plan handoff source blocks, replace free-form activity/first-task prompts with the exact `plan execution` or `phase execution` stage, retaining the existing Orchestration, Model, Fallbacks and limits, frozen-package, rehydration, and variance fields.
3. In the phase-plan input block, require the approved frozen anchor spec rather than an alternative handoff-snapshot artifact. Update relevant readiness blocks and small-spec handoff prompts to use the canonical transition language.
4. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py` to regenerate the three rendered templates, then run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`.
5. Inspect generated outputs to confirm they are derived from the changed source blocks and contain no stale retired terminology.

Exit criteria: Every affected source block and generated plan/spec template presents the same stage-based interface and no longer treats a handoff snapshot as a formal input or freeze option.

#### `CHECK-003` Template assembly and rendered terminology are synchronized

Covers: `VER-002`, `VER-003`, `VER-004`.

Method: Run the template assembler in write mode followed by `--check`; search both source blocks and generated templates for the retired terms and inspect the rendered next-stage sections.

Expected result: Assembly completes successfully, `--check` reports no drift, and the rendered templates use `Next lifecycle stage` with no `First Plan Task` or special handoff-snapshot prompt.

Evidence record: Assembler output and targeted inspection summary in the implementation completion report.

### `TASK-004` Validate the harness contract and record the implementation

Dependencies: `TASK-001`, `TASK-002`, `TASK-003`.

Interfaces:

1. Consumes: Updated policy, source blocks, generated templates, and validator.
2. Produces: Passing conformance evidence and a synchronized implementation changelog source fragment.

Implementation:

1. Create `changelog/implementation.md` before staging the implementation commit. Use the planned implementation subject as its heading and record the canonical stage terminology, approval-only freeze route, template regeneration, validator coverage, and any real README semantic conflict found.
2. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` and resolve only failures caused by this work item.
3. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`, `python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --lint`, `git diff --check`, and targeted `rg` searches for retired terms in current sources.
4. Inspect `git status --short` and `git diff --name-only`; verify the unrelated evidence-reference modification remains unmodified and is excluded from staging.
5. Dispatch the authorized `final-policy-reviewer` after validation and before commit, using Sol High with high reasoning and no write authority. Resolve or report every finding before commit; if Sol High is unavailable, stop and request operator direction.

Exit criteria: All planned validation commands pass, the implementation changelog fragment matches the planned subject, and the staged implementation set contains only this work item's approved policy/template/validator files.

#### `CHECK-004` Full harness policy validation passes

Covers: `VER-004`.

Method: Run the full policy validator, assembler check, changelog-fragment lint, whitespace check, and targeted retired-terminology searches.

Expected result: All commands exit successfully; searches find no retired terminology in live current surfaces; the unrelated evidence-reference file is absent from the staged file list.

Evidence record: Command output in the implementation completion report and the implementation changelog fragment.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: lifecycle-stage-boundaries -- approve lifecycle transition clarification` |
| Implementation | `docs: lifecycle-stage-boundaries -- clarify freeze lifecycle stages` |

The implementation uses one cohesive commit after all checks and the authorized final review complete. Do not stage `.agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md` because it is unrelated pre-existing work.

## Validation and variance

Run `CHECK-001` through `CHECK-004` in order. A changed command is acceptable only when it proves the same criterion; record a noteworthy equivalent change in the variance log if it helps later review. Any change that reintroduces a formal handoff lifecycle, changes approval sequencing, changes model/reviewer behavior, or expands the allowed lifecycle stages is material and requires an amendment plus operator approval.

## Implementation handoff

This plan's frozen combined package owns the handoff.

### Next-stage recommendation

Rename it `### Approved next stage` at freeze without changing its values. Do not render both headings together. Mirror the selected frozen values in chat.

#### Next lifecycle stage

Stage: `plan execution`.

#### Orchestration

Method: `superpowers:executing-plans`; Run in: `new Codex task`; Plan Task reviewers: `one Sol High review-only final policy reviewer after validation`.

#### Model

Model: `economy-default policy; use the available balanced/economy-capable profile`; Reasoning: `medium`.

#### Fallbacks and limits

1. Load the approved spec, plan, applicable current policy sources, template source blocks, generated templates, validator, and any variance/amendment before editing.
2. A fresh operator instruction is required after the planning freeze before execution begins.
3. The only authorized delegation is the Sol High review-only final reviewer; do not dispatch additional agents.
4. The authorized Sol High final reviewer has no write authority; stop if it is unavailable rather than silently substituting a reviewer.
5. Stop and obtain approval for material scope, lifecycle, approval-flow, model/review-boundary, or safety changes.
6. Preserve and exclude the unrelated evidence-reference modification from staging.

1. Frozen package: `spec_lifecycle-stage-boundaries.md`, `plan_lifecycle-stage-boundaries.md`, and the planning-approval changelog fragment created at freeze.
2. Artifact rehydration: Follow `rule:execution-quality.execution-thread-start` and inspect the exact frozen package plus relevant current sources before editing.
3. Variance stop condition: Use `rule:lifecycle.variance-policy`; an amendment and operator approval are required for a material change.

## Readiness

- [x] Current planning Codex task facts are separate from the Next-stage recommendation: Next lifecycle stage, Orchestration (Method, Run in, Plan Task reviewers), Model (Model and Reasoning), then Fallbacks and limits.
- [x] Inputs, scope, tasks, checks, documentation, and changelog plan are clear.
- [x] The approved execution selection, implementation handoff, and upcoming-stage sub-agent assessment are explicit.
- [x] No required decision or ownerless deferral remains.

## Completion

- Required work and evidence are complete; any noteworthy variance is recorded.
- Planned changes are committed, or the blocker is stated.

## Approval

- Status: Approved
- At freeze, relabel the grouped recommendation **Approved next stage** and mirror it in chat.
- Superseded by: None
