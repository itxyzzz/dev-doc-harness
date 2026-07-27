# Harness Execution Flow Clarity Plan

Work ID: `2026-07-27_harness-execution-flow-clarity`
Short ID: `harness-execution-flow-clarity`
Status: Approved
Harness release: `0.8+`
Schema: `schema:plan.small-medium`
Policy references: `module:architecture`, `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:artifact-style`, `module:freeze-gate`, `module:execution-quality`, `rule:lifecycle.planning-shape`, `rule:lifecycle.superpowers-compatibility`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.final-review`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`
Execution method: `superpowers:subagent-driven-development`

> For agentic workers: use `superpowers:subagent-driven-development` as the default to implement this plan one Plan Task at a time. Start it in the Codex task selected by the independent continuity decision. If Superpowers is installed but that skill cannot run or its conditions do not fit, use `superpowers:executing-plans` in a new Codex task. Use native Codex execution by default only when Superpowers is unavailable, and only with an independent reviewer sub-agent. A fresh explicit operator start instruction may select another available method or model without a plan amendment solely for that runtime choice.

## Goal

Implement the approved execution cascade, independent-review behavior, grouped next-stage presentation, chat projection, and combined small/medium planning guard without changing the harness lifecycle or adding new framework layers.

## Input artifacts

1. Specification: `spec_harness-execution-flow-clarity.md`.
2. Architecture decisions: `snapshots/architecture.snapshot.md`.
3. Behavioral cases: `snapshots/test-cases.snapshot.md`.
4. Canonical owners:
   1. `.agents/skills/dev-doc-harness/references/artifact-contract.md`.
   2. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`.
   3. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`.
   4. `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`.
   5. `.agents/skills/dev-doc-harness/references/artifact-style.md`.
5. Routing and bootstrap surfaces: `AGENTS.md` and `.agents/skills/dev-doc-harness/SKILL.md`.
6. Template source blocks and assembly manifests under `.agents/skills/dev-doc-harness/assets/templates/`.
7. Validation owner: `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
8. Operator-facing summaries: `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md`.
9. External method contracts: installed Superpowers 6.2.0 `subagent-driven-development` and `executing-plans` skills. These are read-only inputs and are not implementation targets.
10. Unresolved implementation context: None.

## Traceability approach

1. Local links from each Plan Task to its Specification Commitments and Plan Checks are sufficient because the work has three aligned implementation boundaries.
2. A separate traceability matrix would repeat those links without reducing coverage risk.

## Global constraints

1. Keep existing module and rule ownership; add the compact execution glossary inside `module:models` rather than creating a new policy module or standalone glossary. Do not add a schema family, workflow engine, scheduler, or durable execution artifact.
2. Do not modify the external Superpowers plugin or enumerate skills beyond the two execution routes required by this work item.
3. Preserve draft review, explicit approval, approval commit, stop-before-implementation, fresh start authorization, variance routing, and orchestration-owned final integration.
4. Update generated templates only through source blocks and `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write`.
5. Keep normal operator-facing labels short, distinguish Codex tasks from numbered Plan Tasks and sub-agent runs, and group the next stage as Activity, Orchestration, Model, and Fallbacks and limits.
6. Native Codex execution is selected by default only when Superpowers is unavailable. Whether selected by default or by explicit operator override, it requires an independent reviewer sub-agent; otherwise stop and report the blocker.
7. Do not rewrite frozen historical work-item artifacts or consolidate root `CHANGELOG.md` during ordinary work-item commits.
8. Treat the planned execution method, model/profile, reasoning effort, and Codex-task continuity as defaults that a fresh explicit operator start instruction may override without an amendment when scope, Plan Tasks, commit boundaries, mandatory review, and material safety boundaries remain unchanged.

## Change surfaces

### Canonical policy and routing

1. `AGENTS.md`: expose the concise Superpowers execution preference, operator execution-start override, and combined-planning default at repository bootstrap level.
2. `.agents/skills/dev-doc-harness/SKILL.md`: make combined drafting and approved execution-method routing explicit in the operation table and completion checks.
3. `.agents/skills/dev-doc-harness/references/artifact-contract.md`: own the ordered Superpowers compatibility route and strengthen the small/medium package-shape rule.
4. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`: define the compact execution terminology, route-specific reviewer outcomes, independent method and Codex-task-continuity selection, and simplified current-versus-next-stage notation.
5. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: validate companion-plan completeness, preserve the operator's explicit execution-start override, and require the grouped next-stage chat result.
6. `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`: start the planned or explicitly operator-selected method without a second generic method question and apply deterministic frozen-package loading in the selected execution Codex task.
7. `.agents/skills/dev-doc-harness/references/artifact-style.md`: add a short presentation cue for grouped next-stage content without owning execution semantics.

### Template sources and generated outputs

1. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.010.small.header-inputs.md` and `plan.010.phase.header-objective-inputs.md`: make the default method recommendation required for substantial implementation plans while preserving the operator's execution-start override.
2. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.040.common.model-strategy.md`: replace the dense form with `Current planning Codex task` and grouped Next-stage recommendation content.
3. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.small.handoff.md` and `plan.085.phase.handoff.md`: carry the grouped approved next stage and deterministic artifact-loading rule.
4. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.090.small.readiness-completion-approval.md` and `plan.090.phase.readiness-completion-approval.md`: check method selection, reviewer outcome, and grouped presentation.
5. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.010.small.header.md`: require the combined package's companion-plan path.
6. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.060.large.phase-decomposition-model.md`: use a recommendation or strategy envelope for future phases instead of calling it approved prematurely.
7. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.085.small.handoff.md` and `spec.090.small.readiness-approval.md`: require an operator-authorized exception before a small/medium spec can stand alone.
8. Generated outputs: `small-medium-work-item-spec.md`, `small-medium-work-item-plan.md`, `large-phased-work-item-spec.md`, and `large-phased-work-item-phase-plan.md`.

### Validation, documentation, and changelog sources

1. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: add focused route, reviewer, presentation, chat, and package-shape fixtures.
2. `README.md`: explain the normal execution cascade, readable next-stage chat result, and combined-planning behavior.
3. `.agents/skills/dev-doc-harness/docs/operator-note.md`: provide the compact operator view and remove superseded jargon-heavy descriptions.
4. `docs/work-items/2026-07-27_harness-execution-flow-clarity/deltas/testing-guide.delta.md`: summarize focused checks and commands.
5. `docs/work-items/2026-07-27_harness-execution-flow-clarity/deltas/operator-manual.delta.md`: preserve the operator-facing behavior change.
6. `docs/work-items/2026-07-27_harness-execution-flow-clarity/changelog/implementation.md`: record newest-first entries synchronized with the three planned implementation subjects.

## Implementation approach

1. Implement three independently reviewable patches matching the approved design boundaries.
2. For each patch, add or adjust focused fixtures first and confirm the new check fails for the intended missing behavior.
3. Update the canonical owner before routing, templates, generated outputs, and operator summaries.
4. Regenerate templates with `--write`; do not hand-edit generated output as a source.
5. Run focused and full checks before each planned commit, then use the Plan-Task-scoped reviewer required by `superpowers:subagent-driven-development`.

## Current planning Codex task

1. Model/profile: `not exposed`.
2. Reasoning effort: `not exposed`.
3. Context signal: `not exposed`.

## Approved next stage

### Activity

1. Activity: implement the approved plan.
2. First Plan Task: `TASK-001`.
3. First deliverable: the execution and reviewer fallback order, with focused validator protection.

### Orchestration

1. Method: `superpowers:subagent-driven-development`.
2. Run in: `new Codex task`, after the planning freeze and a fresh operator start instruction.
3. Plan Task reviewers: one independent reviewer after each Plan Task and one final whole-branch reviewer, as required by `superpowers:subagent-driven-development`.
4. Plan Task execution: sequential waves; no parallel write-capable implementers because the Plan Tasks share canonical policy and validator files.
5. Continuity reason: the current model/profile and context suitability are not exposed, while execution has multiple Plan Tasks, commits, validation cycles, reviewer/fix loops, and final integration. Method selection does not determine this location.

### Model

1. Execution controller and Plan Task implementers: active `economy-default`, balanced tier, medium reasoning; current mapping is Terra medium when available.
2. Plan Task reviewers: balanced tier, medium reasoning with a single Plan-Task-specific lens.
3. Final reviewer: flagship tier, medium reasoning because cross-surface policy drift needs stronger integration judgment; current mapping is Sol medium when available.

### Fallbacks and limits

1. If Superpowers is installed but `subagent-driven-development` cannot run or no longer fits the plan, use `superpowers:executing-plans` in a new Codex task with the frozen package and preserve its checkpoints.
2. If Superpowers is unavailable, use native Codex in a new Codex task for this work item, only with an independent reviewer sub-agent using curated artifacts and a named lens.
3. If both Superpowers and reviewer sub-agents are unavailable, stop and report the mandatory-review blocker.
4. The execution Codex task must load applicable `AGENTS.md`, the repository-local harness, the exact frozen spec, frozen plan, required snapshots, applicable amendments and variance records, approval commit and expected baseline, first Plan Task, and variance stop condition through `rule:execution-quality.execution-thread-start`.
5. Use curated artifacts; do not require a full planning-history fork. Treat the planning conversation as a useful cache, not execution authority.
6. Authorization state: planning package, model envelope, method fallback, reviewer roles, Codex-task location, and write scope approved; implementation still requires a fresh explicit operator start instruction after this freeze commit.
7. Operator start override: a fresh explicit instruction may replace the planned method, model/profile, reasoning effort, or Codex-task continuity without an amendment solely for that selection. Record the actual values and proceed when available and compatible; report only a concrete blocker.
8. Stop for approval before changing the canonical fallback order, reviewer requirement, lifecycle ownership, module boundaries, freeze behavior, release scope, or any Specification Commitment or Verification Criterion. An in-scope operator execution-start override is not such a change.

## Execution roles

### Plan Task implementer

1. Purpose: implement one `TASK-NNN` and its focused tests.
2. Context strategy: curated artifacts through the Plan Task brief, this plan, the Plan Task's source paths, and prior Plan Task interfaces.
3. Output: scoped policy/template/test/documentation changes, validation evidence, planned commit, and a Plan Task report.
4. Model: active `economy-default`, balanced tier, medium reasoning, Terra medium when available.
5. Write authority: only files named by the assigned Plan Task plus its changelog and delta updates.
6. Concurrency: one implementer at a time.

### Plan Task reviewer

1. Purpose: verify specification compliance and implementation quality after each Plan Task.
2. Context strategy: curated artifacts containing the Plan Task brief, implementer report, relevant spec decisions, changed diff, and validation evidence.
3. Output: evidence-backed findings with severity, reproduction or validation path, and both required verdicts.
4. Model: active `economy-default`, balanced tier, medium reasoning.
5. Write authority: read-only review report.

### Final reviewer

1. Purpose: perform the broad whole-branch review after all three Plan Tasks.
2. Context strategy: curated artifacts containing the frozen package, full branch diff, validation evidence, variance record if any, and prior reviewer findings.
3. Output: integration findings, residual risk, and merge-readiness recommendation.
4. Model: active `economy-default`, flagship tier, medium reasoning, Sol medium when available.
5. Write authority: read-only review report.

## Implementation Plan Tasks

### `TASK-001` Restore execution and review defaults

Dependencies: approved and frozen planning package plus fresh post-freeze start authorization.

Interfaces:

1. Consumes: `SPEC-001`, `SPEC-002`, `DEC-001`, method cases `TC-001` through `TC-003` and `TC-026`, and reviewer cases `TC-008` through `TC-011`.
2. Produces: one canonical execution-method cascade and route-specific reviewer contract consumed by `TASK-002` handoff presentation and `TASK-003` planning-package routing.

Implementation:

1. In `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, add `execution.method-fallbacks` to the expected check IDs and add a focused assertion function that exercises these exact outcomes:
   1. Superpowers available + sub-agent-driven conditions true -> `superpowers:subagent-driven-development`.
   2. Superpowers available + preferred route unavailable or unsuitable -> `superpowers:executing-plans`.
   3. Superpowers unavailable + reviewer sub-agent available -> native Codex.
   4. Superpowers unavailable + reviewer sub-agent unavailable -> blocked.
   5. Superpowers available + native Codex proposed without a fresh explicit operator override -> invalid as the default.
   6. Fresh explicit operator start instruction selects another available method or model -> accepted and recorded without a plan amendment solely for that selection.
2. Add reviewer fixtures that require per-Plan-Task and final review for the preferred route, preserve executing-plans checkpoints and capability disclosure, require an independent reviewer for native Codex, and reject native `Sub-agents: None`.
3. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`; confirm the new check fails because current active guidance lacks the ordered route and native-review stop.
4. Update the Superpowers compatibility section in `artifact-contract.md` to own the ordered method cascade without duplicating either external skill's internal mechanics.
5. Update `subagent-model-policy.md` to define route-specific reviewer outcomes, native-review mandatory behavior, the no-review stop, execution-Codex-task-owned final integration, the operator's execution-start override, and the Superpowers interpretation that `current session` is the execution controller's session rather than necessarily the planning Codex task.
6. Update `context-and-quality-gates.md`, `planning-freeze-gates.md`, and the execute route in `SKILL.md` so the planned or explicitly operator-selected method starts after fresh authorization without a second generic method question or an unnecessary amendment dispute.
7. Add concise matching bootstrap and operator guidance to `AGENTS.md`, `README.md`, and `docs/operator-note.md`; do not enumerate unrelated Superpowers skills.
8. Create `deltas/testing-guide.delta.md` and `deltas/operator-manual.delta.md` with the final route and validation expectations from this Plan Task.
9. Create `changelog/implementation.md` with a newest-first entry headed `2026-07-27 feat: harness-execution-flow-clarity -- restore execution and review defaults`, metadata `Release target: unreleased`, `Package impact: distributable`, and `Release-note: source-only`.
10. Run the full validator, changelog lint, and `git diff --check`; all must pass.
11. Commit only this Plan Task's policy, routing, documentation, validation, delta, and changelog changes with `feat: harness-execution-flow-clarity -- restore execution and review defaults`.

Exit criteria: the ordered execution route and reviewer obligations are canonical, operator-visible, validator-protected, and committed; Plan Task review reports both specification compliance and implementation quality approved.

### `TASK-002` Simplify and surface the next stage

Dependencies: `TASK-001` complete and its review approved.

Interfaces:

1. Consumes: the method and reviewer outcomes from `TASK-001`, plus `SPEC-003`, `DEC-002`, continuity cases `TC-004` through `TC-007`, and presentation cases `TC-012` through `TC-018`.
2. Produces: one grouped next-stage representation used by current plans, large anchor strategy envelopes, freeze chat output, and the package-completeness message in `TASK-003`.

Implementation:

1. Extend `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` with `presentation.next-stage-summary` and fixtures that require:
   1. `Current planning Codex task` separate from the future selection.
   2. `Next-stage recommendation` for Draft artifacts and `Approved next stage` only at frozen boundaries.
   3. Activity, Orchestration, Model, and Fallbacks and limits in that order.
   4. Method, Run in, and Plan Task reviewers under Orchestration.
   5. Model and Reasoning under Model.
   6. `Run in` limited to `same Codex task` or `new Codex task`.
   7. Chat projection at draft review, freeze, and execution handoff.
   8. Independent method and Codex-task-continuity selection, including valid sub-agent-driven execution in a new Codex task.
   9. A new-Codex-task default for substantial work when current profile or context suitability is `not exposed`, and same-Codex-task acceptance only with a known-suitable profile, suitable or immaterial context risk, and a concrete recorded continuity benefit.
   10. Rejection of numeric context thresholds, invented remaining-context estimates, and compaction predictions.
   11. `First Plan Task`, per-Plan-Task reviewer, and final reviewer fields using the canonical terminology.
   12. Routine omission of model-policy source, override scope, expiry, and open-ended rehydration explanations.
2. Run the full validator and confirm `presentation.next-stage-summary` fails against the current dense field set and missing chat projection.
3. Add a compact `Execution terminology` section to `subagent-model-policy.md` defining `Codex task`, `planning Codex task`, `execution Codex task`, `Plan Task`, `sub-agent run` or `sub-agent assignment`, and the external term `execution session`. State that `Codex task` is the local label for the corresponding top-level agent conversation or thread in other tools, including tools such as Claude Code or Google Antigravity, and that adapted distributions may use their platform-native label. Keep it under the existing `module:models` ownership; do not add a new module, standalone glossary, or required router hop.
4. Rewrite the selection-dimensions, execution-continuity, required-notation, and related common guidance in `subagent-model-policy.md` so current facts and next-stage recommendations have distinct status and fields, method does not determine Codex-task location, and continuity works without hidden context estimates.
5. Update `planning-freeze-gates.md` and `context-and-quality-gates.md` to render and consume the grouped summary. A new execution Codex task unconditionally loads applicable repository instructions, the local harness, exact frozen package, amendments and variance records, approval commit and expected baseline, first Plan Task, and variance stop condition. Same-Codex-task execution rereads the package after a model switch or another recorded continuity risk.
6. Add only the short grouping and plain-label presentation rule to `artifact-style.md`; do not move method, model, reviewer, continuity, or lifecycle semantics into the style module.
7. Update `policy-architecture.md` only to include execution terminology in the existing `module:models` catalog description; do not create or route a new module.
8. Update `plan.010.small.header-inputs.md`, `plan.010.phase.header-objective-inputs.md`, `plan.040.common.model-strategy.md`, both plan handoff blocks, and both plan readiness blocks to show the grouped draft and frozen forms with unambiguous Codex-task and Plan-Task labels.
9. Update `spec.060.large.phase-decomposition-model.md` so the anchor records a next-stage recommendation or default envelope rather than a prematurely approved future-phase selection.
10. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write`; verify the four generated spec and plan templates are refreshed only from their manifests.
11. Replace jargon-heavy current descriptions in `README.md` and `docs/operator-note.md` with the grouped operator view, a short link or pointer to the canonical terminology, and the rule that chat repeats the authoritative artifact values.
12. Prepend a changelog entry headed `2026-07-27 feat: harness-execution-flow-clarity -- simplify next-stage presentation` to `changelog/implementation.md`, retaining exactly one metadata set for the new entry.
13. Update both deltas with the final field groups, chat boundary, terminology ownership, and focused validation behavior.
14. Run the assembler check, full validator, changelog lint, targeted `rg` checks for obsolete required labels, and `git diff --check`; all must pass.
15. Commit this Plan Task's policy, template source, generated template, documentation, validation, delta, and changelog changes with `feat: harness-execution-flow-clarity -- simplify next-stage presentation`.

Exit criteria: current and future model information cannot be conflated, method and Codex-task continuity remain independent, routine next-stage output uses the four approved groups and canonical terminology, the same values appear in chat at the required boundaries, generated templates are fresh, and Plan Task review is approved.

### `TASK-003` Enforce combined small-medium planning

Dependencies: `TASK-002` complete and its review approved.

Interfaces:

1. Consumes: `SPEC-004`, `SPEC-005`, `DEC-003`, `TC-019` through `TC-025`, and the grouped next-stage/package message produced by `TASK-002`.
2. Produces: the final small/medium package-completeness guard, explicit staged exception, retained large-anchor behavior, complete documentation, and full validation evidence for final review.

Implementation:

1. Extend `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` with `lifecycle.combined-package-default` and fixtures for:
   1. Normal small/medium package with both canonical filenames -> valid.
   2. Small/medium spec alone without operator authorization -> invalid.
   3. Small/medium spec alone with an operator-requested or approved staged reason and `plan drafting` next activity -> valid.
   4. Large/phased anchor spec alone -> valid.
   5. Complex but one-thread-manageable work -> small/medium.
2. Run the full validator and confirm the new check fails because the current freeze trigger accepts an individual small/medium spec without proving the companion-plan or staged-exception state.
3. Update the work-sizing and small/medium planning-shape sections in `artifact-contract.md` to keep uncertain work small/medium unless the one-thread boundary demonstrably fails and to require operator authorization for spec-only staging.
4. Update the small/medium draft route, freeze route, and completion checklist in `SKILL.md` so combined drafting creates and presents both files in the same turn.
5. Update `planning-freeze-gates.md` to validate small/medium package completeness before draft review and again before approval freeze, while preserving the large/phased anchor route.
6. Update `spec.010.small.header.md` with the companion plan and combined planning shape, then update `spec.085.small.handoff.md` and `spec.090.small.readiness-approval.md` to make the authorized staged exception explicit.
7. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` and confirm `small-medium-work-item-spec.md` is regenerated without changing the large anchor default.
8. Align `AGENTS.md`, `README.md`, and `docs/operator-note.md` with the same operational default and exception requirement.
9. Prepend a changelog entry headed `2026-07-27 feat: harness-execution-flow-clarity -- enforce combined planning` to `changelog/implementation.md`.
10. Update both deltas with the final combined-package and validation behavior.
11. Run the assembler check, full harness validator, changelog lint, targeted package-shape searches, and `git diff --check`; all must pass.
12. Inspect `git diff --stat` and `git status --short` to confirm only planned implementation, delta, and changelog paths changed and no authoring placeholders remain.
13. Commit this Plan Task with `feat: harness-execution-flow-clarity -- enforce combined planning`.
14. Produce the full-branch review package and dispatch the final independent reviewer using the frozen package, complete diff, validation evidence, prior findings, and a single integration/regression lens.

Exit criteria: normal small/medium planning requires both artifacts, only an authorized staged exception permits spec-only, large anchors remain unchanged, all validation is green, and final review has no unresolved load-bearing findings.

## Plan checks

### `CHECK-001` Execution fallback order

Covers: `VER-001`.

Method: Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` after `TASK-001` and inspect the `PASS execution.method-fallbacks` result plus the focused fixture definitions.

Expected result: all six method branches resolve exactly as specified; native Codex is invalid as the default while Superpowers is available, and a fresh explicit operator method or model override is accepted without an amendment solely for that selection.

### `CHECK-002` Reviewer-route enforcement

Covers: `VER-002`.

Method: Inspect the focused reviewer fixtures and active policy/template text, then run the full validator.

Expected result: preferred-route per-Plan-Task and final reviews, executing-plans capability disclosure, mandatory native independent review, and the no-review blocker are all asserted; native `Sub-agents: None` fails.

### `CHECK-003` Next-stage group and status validation

Covers: `VER-003`.

Method: Run the full validator and `rg -n -S "Current planning Codex task|Next-stage recommendation|Approved next stage|Activity|Orchestration|Model|Fallbacks and limits|Run in|First Plan Task|Plan Task reviewers|sub-agent run" .agents/skills/dev-doc-harness/assets/templates .agents/skills/dev-doc-harness/references README.md`.

Expected result: current templates and policy contain the ordered grouped representation and canonical task terminology, Draft and frozen labels are distinct, method does not determine Codex-task location, both `same Codex task` and `new Codex task` have deterministic loading guidance, and this work item recommends `new Codex task`.

### `CHECK-004` Obsolete routine jargon removal

Covers: `VER-003`, `VER-005`.

Method: Run targeted searches over current source blocks and generated templates for required routine uses of `Approved execution selection`, `Execution continuity`, `Artifact rehydration required`, `Override scope and expiry`, and `Model-policy source`; inspect focused fixtures for rejected numeric thresholds and invented context or compaction claims.

Expected result: the obsolete labels are absent from routine generated strategy blocks; conditional override details remain only where an actual override or availability issue requires them; no fixture or canonical field relies on an invented context percentage or a general natural-language linter.

### `CHECK-005` Combined package scenarios

Covers: `VER-004`, `VER-005`.

Method: Run the full validator and inspect `PASS lifecycle.combined-package-default` plus the normal, unauthorized staged, authorized staged, large-anchor, and uncertain-sizing fixtures.

Expected result: only the two valid small/medium shapes pass, large anchor behavior is unchanged, and complexity alone does not force large/phased planning.

### `CHECK-006` Template assembly freshness

Covers: `VER-003`, `VER-004`, `VER-005`.

Method: Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`.

Expected result: exit code 0 and all generated templates match their ordered source blocks and manifests.

### `CHECK-007` Full harness policy validation

Covers: `VER-001`, `VER-002`, `VER-003`, `VER-004`, `VER-005`.

Method: Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Expected result: exit code 0; every existing check and the three new check IDs report `PASS`.

### `CHECK-008` Changelog and diff integrity

Covers: `VER-005`.

Method: Run `python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --lint`, `git diff --check`, `git status --short`, and a placeholder search over current changed artifacts.

Expected result: fragment grammar and duplicate-heading checks pass, the diff has no whitespace errors, only planned paths changed, and no unresolved authoring marker or obsolete generated output remains.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: harness-execution-flow-clarity -- approve execution and planning defaults` |
| Implementation 1 | `feat: harness-execution-flow-clarity -- restore execution and review defaults` |
| Implementation 2 | `feat: harness-execution-flow-clarity -- simplify next-stage presentation` |
| Implementation 3 | `feat: harness-execution-flow-clarity -- enforce combined planning` |

Each implementation commit is an independently reviewable and revertible behavior boundary with its focused checks passing. Plan Task count does not create additional commit boundaries.

## Validation and variance

1. `CHECK-001` through `CHECK-008` are all required; none are equivalent alternatives.
2. A function name, assertion layout, or exact documentation paragraph may vary when it preserves the same routing, review, presentation, package-shape, and evidence outcomes.
3. Record noteworthy equivalent adjustments in `implementation-notes/variance-log.md` only when they help future review.
4. Stop for an amendment and operator approval before changing the execution fallback order, mandatory native reviewer, next-stage group order, combined-planning authorization rule, large-anchor behavior, module ownership, freeze boundary, or validation intent.
5. A fresh explicit operator execution-start override of method, model/profile, reasoning effort, or Codex-task continuity is not an amendment-triggering change when it leaves those canonical rules, scope, Plan Tasks, commit boundaries, mandatory review, and material safety boundaries intact.

## Implementation handoff

1. Frozen package after approval: `spec_harness-execution-flow-clarity.md`, `plan_harness-execution-flow-clarity.md`, `snapshots/architecture.snapshot.md`, `snapshots/test-cases.snapshot.md`, and `changelog/planning-approval.md`, plus any applicable approved amendments or variance records.
2. Next activity: implement the approved plan.
3. First Plan Task: `TASK-001` and its focused red/green validation cycle.
4. Method: `superpowers:subagent-driven-development`.
5. Run in: `new Codex task` with sequential Plan Task implementers, an independent reviewer after each Plan Task, and a final whole-branch reviewer. The execution Codex task retains final integration ownership.
6. Model: balanced tier with medium reasoning for the execution controller, implementers, and Plan Task reviewers; flagship tier with medium reasoning for final review.
7. Default fallback: `superpowers:executing-plans` in a new Codex task with the frozen package while Superpowers is available; native Codex in a new Codex task for this work item when Superpowers is unavailable and an independent reviewer sub-agent can run; otherwise stop. An explicit operator override may select native Codex while Superpowers is available, but the reviewer requirement remains mandatory.
8. Artifact loading: start through `rule:execution-quality.execution-thread-start` and load applicable `AGENTS.md`, the repository-local harness, the exact frozen package, applicable amendments and variance records, approval commit and expected baseline, the first Plan Task, and the variance stop condition. No full planning-history fork is required.
9. Operator start override: a fresh explicit instruction may replace the method, model/profile, reasoning effort, or Codex-task continuity without an amendment solely for that runtime choice; record the actual selection.
10. Variance stop condition: approval is required for any material change named in the Validation and variance section.

## Readiness

- [x] Inputs, scope, Plan Tasks, checks, documentation, and planned changelog sources are clear.
- [x] Each Plan Task has exact source, generated-output, validator, documentation, and commit boundaries.
- [x] The next-stage method, location, reviewers, model, reasoning, fallbacks, artifact loading, and stop condition are explicit.
- [x] The preferred and fallback Superpowers skills match their installed trigger contracts without coupling method to Codex-task continuity.
- [x] A fresh explicit operator execution-start override is accepted without an amendment when material plan and safety boundaries remain unchanged.
- [x] The native execution route includes the operator-required independent reviewer and blocker.
- [x] No required decision, placeholder, or ownerless deferral remains.

## Completion

1. Required policy, routing, templates, generated outputs, validation, operator documentation, deltas, and changelog sources are complete.
2. All Plan Checks pass, the three planned implementation commits exist, Plan Task reviews are approved, final review has no unresolved load-bearing findings, and any noteworthy variance is recorded.

## Approval

- Status: Approved
- Superseded by: None
