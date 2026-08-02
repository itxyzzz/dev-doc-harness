# Plan Amendment 004: Deduplicate Plan State and Restore Conditional Style Routing

Work ID: `2026-07-27_harness-execution-flow-clarity`
Short ID: `harness-execution-flow-clarity`
Status: Approved
Harness release: `0.8+`
Schema: `schema:plan.amendment`
Policy references: `module:architecture`, `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:artifact-style`, `module:freeze-gate`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:models.selection-dimensions`, `rule:models.strategy-required`, `rule:style.template-prompts`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Original plan reference

- Amendment ID: `AMD-004`
- Frozen package: `spec_harness-execution-flow-clarity.md`, `plan_harness-execution-flow-clarity.md`, `snapshots/architecture.snapshot.md`, `snapshots/test-cases.snapshot.md`, and approved Amendments 001 through 003.
- Approval commits: `219258cfc5a3b79c19175121ed8076976d440701`, `37f2713f5d28e732b4c5493edbe1f83eaf29bd1a`, `d886788dc05d746dfa3ae6cf162199dbfde611f0`, and `48f000c`.
- Expected implementation baseline: `ef7bbe4f5dec011b196f7b5dd335dd56a7b327fc`.
- Affected decisions and evidence: `SPEC-003` statements 1 through 3 and 8; `VER-003`; `DEC-002` statements 1 through 5; `TC-012` through `TC-014`, `TC-017`, and `TC-024`; original plan `TASK-002` step 8; `CHECK-003`; validator checks `models.selection-dimensions`, `plain-language.policy`, and `presentation.next-stage-summary`.
- Original instruction: plans separate current planning Codex task facts from the state-dependent next-stage summary, use the four ordered next-stage groups, and keep source blocks and generated templates synchronized. Amendment 003 excluded further template changes from its ownership-only correction.

## Discovered issue

Post-implementation review found that current small/medium and phase-plan templates render the same planning-state information in multiple places. Header blocks contain both `Current planning Codex task` and `Next-stage recommendation`; the shared model-strategy block repeats both; and the handoff blocks repeat current-task and state-dependent summary instructions near the transition they govern. The generated plans therefore obscure the intended distinction instead of presenting each state once at its natural lifecycle boundary.

The same review found a separate ownership regression in routine small/medium planning. `module:architecture`, `module:quality`, and `module:artifact-style` make the full artifact-style module conditional unless readability risk is material, but the small spec and plan source blocks, the small/medium router entry, and validator assertions require it unconditionally. The current template and validator behavior contradict the canonical owner and exceeds the routine route budget.

These are material template-schema and router corrections because they change current reusable plan layout, module loading, and the validator evidence for both. Frozen artifacts remain unchanged.

## Proposed change

1. Give each plan-state value one location in current small/medium and phase plans:
   1. Put `Current planning Codex task` once in header metadata, without a dedicated Markdown section.
   2. Keep the shared `Model and Sub-agent Strategy` block focused on the upcoming-stage sub-agent assessment, bounded role details, and their model allocations; remove the repeated current-task and next-stage summary blocks from it.
   3. Put the single state-dependent `Next-stage recommendation` or `Approved next stage` summary in the final implementation-handoff or phase-transition area, with Activity, Orchestration, Model, and Fallbacks and limits in the existing order.
2. Update `module:models` required-notation guidance to state this placement for plans and phase plans. Preserve the large anchor spec's existing single grouped strategy presentation because it does not have the same plan-header and implementation-handoff duplication.
3. Keep current semantics unchanged: Draft artifacts recommend, frozen artifacts approve; chat mirrors the authoritative values; `Run in` retains exactly the two canonical values; and runtime overrides apply only through the existing freeze and transition rules.
4. Restore conditional artifact-style loading across every routine small/medium planning surface:
   1. `SKILL.md` requires `module:lifecycle`, `module:quality`, and `module:models` for routine small/medium specs and plans, and lists `module:artifact-style` as conditional when readability risk is material.
   2. Small spec and plan source headers use the baseline readability guidance from `module:quality` and contain only a short conditional cue to load `module:artifact-style` when the artifact becomes large or hard to scan.
   3. Remove `module:artifact-style` from the unconditional policy-reference lists in those routine small/medium source headers.
   4. Keep large anchor specs unconditionally routed to `module:artifact-style` and keep phase plans conditional when they become large or hard to scan.
5. Update focused validation to protect placement and routing structurally rather than merely requiring each phrase in every source block.
6. Regenerate templates only through `assemble_templates.py --write`; do not hand-edit generated outputs as independent sources.

## Implementation tasks

### `AMD-004-TASK-001` Place plan state once and align style-module routing

**Files**

- Modify: `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
- Modify: `.agents/skills/dev-doc-harness/SKILL.md`
- Modify: `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.010.small.header-inputs.md`
- Modify: `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.010.phase.header-objective-inputs.md`
- Modify: `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.040.common.model-strategy.md`
- Modify: `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.small.handoff.md`
- Modify: `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.phase.handoff.md`
- Modify: `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.010.small.header.md`
- Regenerate: `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
- Regenerate: `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- Regenerate: `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
- Modify: `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`
- Update: `docs/work-items/2026-07-27_harness-execution-flow-clarity/deltas/testing-guide.delta.md`
- Update: `docs/work-items/2026-07-27_harness-execution-flow-clarity/changelog/implementation.md`
- Do not modify: frozen spec, plan, snapshots, prior amendments, `planning-freeze-gates.md`, `artifact-style.md`, `durable-planning-quality.md`, large-anchor source blocks or generated template, `AGENTS.md`, `README.md`, or `docs/operator-note.md`.

**Interfaces**

- Consumes: the approved four-group schema and current-versus-next-stage distinction from `rule:models.selection-dimensions`; baseline readability from `module:quality`; conditional style loading from `module:architecture` and `module:artifact-style`; source-block assembly; and existing freeze/chat behavior.
- Produces: one current-task header field, one state-dependent plan handoff summary, one focused sub-agent-strategy block, conditional routine small/medium style routing, regenerated current templates, and validator evidence for those boundaries.

1. Add focused validator assertions before changing policy or template sources:
   1. Each plan header source block contains one compact `Current planning Codex task:` metadata field and no `## Current planning Codex task` or next-stage heading.
   2. The shared plan model-strategy block contains the upcoming-stage sub-agent assessment and no current-task or next-stage heading.
   3. Each plan handoff source block contains exactly one Draft state heading, documents its freeze-time rename to `Approved next stage`, and contains Activity, Orchestration, Model, and Fallbacks and limits in that order.
   4. Each generated small/medium or phase plan contains exactly one current-task metadata field and one state-dependent summary heading, with the summary after implementation tasks and checks and within the handoff or transition area.
   5. The large anchor spec retains its existing single current-task and next-stage strategy presentation.
   6. The routine small/medium router route and source headers do not require `module:artifact-style`; they contain the canonical conditional loading cue instead.
   7. The large anchor route remains mandatory and the phase-plan route remains conditional for artifact style.
2. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`. Expected RED result: `models.selection-dimensions`, `plain-language.policy`, and `presentation.next-stage-summary` fail because current sources duplicate state and require routine small/medium style loading.
3. Update `subagent-model-policy.md` under `## Required notation` so plan and phase-plan placement is explicit: current-task facts are header metadata, the grouped next-stage summary is near the final handoff, and the shared strategy section owns the upcoming-stage sub-agent assessment and any bounded role records. Keep required fields and the large-anchor presentation intact.
4. Update the small/medium router row in `SKILL.md`: move `module:artifact-style` from Required route to Optional or conditional route with the same material-readability condition used by the canonical owners. Do not change the large-anchor or phase-plan route semantics.
5. Update both plan header source blocks:
   1. Replace the current-task section with one metadata line.
   2. Remove the top next-stage summary.
   3. For the small plan only, remove the unconditional style policy reference and mandatory style sentence; replace them with the quality baseline and conditional style cue already used by the phase-plan header.
6. Update `plan.040.common.model-strategy.md` to retain the canonical model-policy route, upcoming-stage sub-agent assessment, bounded role fields, authorization behavior, and model allocations while removing the repeated current-task and grouped next-stage blocks.
7. Update both plan handoff source blocks to render the only plan-level state-dependent summary. Use a Draft `### Next-stage recommendation` heading in the template, instruct the author to rename it `### Approved next stage` at freeze without changing values, and nest the four ordered groups beneath it. Preserve the existing frozen package, next activity, artifact rehydration, phase output, and variance-stop fields without duplicating the grouped values elsewhere.
8. Update `spec.010.small.header.md` to remove the unconditional style policy reference and mandatory loading instruction, then add the same quality-baseline and conditional style cue used by routine small/medium plans.
9. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write`. Expected result: the small spec, small plan, and phase plan regenerate; the large anchor template remains byte-for-byte unchanged.
10. Run the focused validator again. Expected GREEN result: `PASS models.selection-dimensions`, `PASS plain-language.policy`, and `PASS presentation.next-stage-summary`, with all existing checks passing.
11. Update `deltas/testing-guide.delta.md` with the unique-placement, ordering, large-anchor-preservation, and conditional-style-route checks.
12. Prepend a matching newest-first entry to `changelog/implementation.md` with the implementation subject below and the existing `unreleased`, `distributable`, and `source-only` metadata values.
13. Run the full validation set:
   1. `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
   2. `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`.
   3. `python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --lint`.
   4. The installed skill creator's `quick_validate.py` against `.agents/skills/dev-doc-harness`.
   5. Targeted searches for plan-state headings and unconditional small/medium artifact-style loading.
   6. `git diff --check` and scoped status/diff inspection.
14. Dispatch one independent reviewer with a template ownership, route consistency, and regression lens. Give the reviewer this amendment, the affected owner modules, source blocks and manifests, generated diffs, RED/GREEN evidence, and full validation output. Resolve or report every finding.
15. Update the changelog fragment if reviewer fixes alter the delivered scope, then stage and commit only the reviewed files named above. Exclude `.superpowers/sdd/plan_harness-execution-flow-clarity/task-3-report.md` and every other unrelated pre-existing change.

Exit criteria: current planning facts appear once as plan header metadata; the state-dependent next stage appears once near the plan handoff; the shared strategy block no longer duplicates either; routine small/medium style loading is conditional across router, source, generated, and validator surfaces; large anchor and phase-plan style rules remain correct; generated templates are current; all validation passes; and independent review has no unresolved load-bearing finding.

## Impact assessment

- Outcome: plan and phase-plan templates become shorter and follow the lifecycle reading order approved by the operator. Routine small/medium agents no longer load a full style module unless readability risk makes it relevant.
- Evidence: focused RED/GREEN structural assertions, generated-template inspection, preserved large-anchor behavior, route checks, full harness validation, template assembly, skill validation, changelog lint, targeted searches, and independent review.
- Interfaces: `module:models` notation placement, the small/medium router route, small spec and plan header schemas, the shared plan strategy block, plan handoff/transition schemas, current generated templates, and validator fixtures. No runtime API, data, infrastructure, security, privacy, compliance, or release interface changes.
- Risk: removing duplicated fields could accidentally drop a required next-stage or sub-agent value. Positive field, ordering, placement, and generated-template checks preserve the complete schema. Conditional style routing could be weakened too far; explicit large-anchor mandatory and phase/routine conditional assertions protect the owner rules.
- Documentation: testing-guide delta and implementation changelog only. Operator behavior and canonical freeze/chat semantics do not change, so no operator-manual or README update is required.
- Rollback: revert the amended implementation commit to restore the prior template layout and routing assertions.

## Current planning Codex task

- Model/profile: current Codex model; exact resolved profile is not exposed.
- Reasoning: not exposed.
- Context visibility: not exposed.

## Next-stage recommendation

### Activity

- Next activity: implement this amendment after approval freeze and fresh authorization.
- First Plan Task: `AMD-004-TASK-001`.

### Orchestration

- Method: `superpowers:executing-plans` because the amendment has one tightly coupled policy, template, generated-output, and validator task rather than independently writable Plan Tasks.
- Run in: `new Codex task` because the current profile and context suitability are not exposed; use the frozen amendment and curated work-item artifacts.
- Plan Task reviewers: one independent final reviewer with a template ownership, route consistency, and regression lens.

### Model

- Implementation: balanced tier, medium reasoning; Terra medium when available.
- Final review: balanced tier, high reasoning; Terra high when available.

### Fallbacks and limits

- Sub-agents: None for implementation because all writable surfaces share one schema and validator boundary. One independent reviewer is the bounded review use.
- If `superpowers:executing-plans` is unavailable or unsuitable, use native Codex with the same independent-review requirement and recorded availability result.
- Load the frozen package, Amendment 004, approval/baseline, affected owner modules, template sources and manifests, First Plan Task, and variance stop through `rule:execution-quality.execution-thread-start`.
- A fresh explicit operator start instruction may override the available method, model/profile, reasoning effort, or Codex-task continuity without an amendment solely for that runtime choice.
- Stop for another amendment before changing the four next-stage groups or their semantics, freeze/chat behavior, execution continuity values, reviewer contract, large-anchor style requirement, source-block assembly boundary, or operator-visible lifecycle outcome.

## Approval

- Required: Yes
- Status: Approved
- Approval evidence: operator approved the staged amendment in the current Codex task on 2026-07-29.
- Superseded by: None

## Planned commits

| Stage | Planned subject |
|---|---|
| Amendment approval | `amendment 004: harness-execution-flow-clarity -- place plan state once and restore conditional style routing` |
| Amended implementation | `fix: harness-execution-flow-clarity -- deduplicate plan state and restore conditional style routing` |

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`. Implementation remains paused until this amendment is approved and frozen in its own planning commit, followed by fresh operator authorization.
