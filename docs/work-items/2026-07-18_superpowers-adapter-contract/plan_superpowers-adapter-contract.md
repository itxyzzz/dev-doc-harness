# Superpowers Adapter Contract Implementation Plan

Work ID: `2026-07-18_superpowers-adapter-contract`
Short ID: `superpowers-adapter-contract`
Status: Approved
Harness release: `0.7+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:artifact-style`, `module:execution-quality`, `module:freeze-gate`, `rule:lifecycle.superpowers-compatibility`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.variance-policy`, `rule:models.strategy-required`, `rule:models.approved-strategy-authorized`, `rule:models.economy-default`, `rule:execution-quality.execution-thread-start`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

Artifact style: final-content draft. This plan preserves the approved coexistence boundary and uses numbered task steps; it does not create a second durable Superpowers plan.

## Input Artifacts

1. Approved spec: `spec_superpowers-adapter-contract.md`.
2. Architecture input: `snapshots/architecture.snapshot.md`, especially `DEC-001`.
3. Required snapshot drafted with this plan: `snapshots/test-cases.snapshot.md`.
4. Repository guidance and canonical owners: `AGENTS.md`, `README.md`, `.agents/skills/dev-doc-harness/SKILL.md`, `.agents/skills/dev-doc-harness/references/artifact-contract.md`, `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`, `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`, `.agents/skills/dev-doc-harness/docs/operator-note.md`, and `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
5. Plan-template source and generated outputs: `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.010.small.header-inputs.md`, `plan.010.phase.header-objective-inputs.md`, `plan.020.common.traceability-approach-surfaces.md`, `plan.040.common.model-strategy.md`, `plan.050.common.task-plan.md`, `assemblies/small-medium-work-item-plan.json`, `assemblies/large-phased-work-item-phase-plan.json`, `small-medium-work-item-plan.md`, and `large-phased-work-item-phase-plan.md`.
6. Template and changelog tools: `.agents/skills/dev-doc-harness/scripts/assemble_templates.py` and `.agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py`.
7. Unresolved implementation context: none. The implementation preflight must confirm actual source-block ownership and preserve generated-template freshness before editing.

## Traceability approach

Local links provide sufficient coverage without a separate mapping:

1. `SPEC-001` and `VER-001` are implemented by `TASK-001`, `TASK-004`, and `CHECK-001` through `CHECK-003`.
2. `SPEC-002` and `VER-002` are implemented by `TASK-002`, `TASK-003`, and `CHECK-001` through `CHECK-003`.
3. `SPEC-003` and `VER-003` are implemented by `TASK-002`, `TASK-003`, and `CHECK-002`.
4. `SPEC-004` and `VER-004` are implemented by `TASK-001`, `TASK-004`, and `CHECK-002` through `CHECK-004`.
5. `SPEC-005` and `VER-005` are implemented by `TASK-002`, `TASK-003`, and `CHECK-002` through `CHECK-004`.
6. `SPEC-006` and `VER-006` are implemented by `TASK-004`, `TASK-005`, and `CHECK-001` through `CHECK-005`.

## Change Surfaces

1. `AGENTS.md` and the compact global `AGENTS.md` bootstrap snippet in `README.md`: name the project-level or global Superpowers path preference and retain the harness work-item package and freeze gate as the durable boundary after downstream instructions are merged.
2. `README.md` outside the global bootstrap snippet and `.agents/skills/dev-doc-harness/docs/operator-note.md`: give maintainers and operators a compact, non-duplicative explanation of the adapter and its no-Superpowers fallback.
3. `.agents/skills/dev-doc-harness/SKILL.md`: route adapter work to lifecycle, model, execution-quality, template, and freeze-gate owners without copying their rules.
4. `.agents/skills/dev-doc-harness/references/artifact-contract.md`: own canonical placement, conditional plan conversion, post-freeze Superpowers entry, ephemeral-aid boundary, and concise fallback task-sizing cue.
5. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`: own the policy envelope and explicit per-dispatch allocation requirement for Superpowers task agents.
6. `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`: own execution-start and environment-compensation wording that keeps Superpowers inside an approved route and preserves the fallback.
7. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.010.small.header-inputs.md`, `plan.010.phase.header-objective-inputs.md`, `plan.020.common.traceability-approach-surfaces.md`, `plan.040.common.model-strategy.md`, and `plan.050.common.task-plan.md`: prompt the conditional merged execution meta-header, conditional Global Constraints, distinct task interfaces and dependencies, numbered executable steps, and explicit Superpowers allocation notation.
8. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md` and `large-phased-work-item-phase-plan.md`: generated outputs refreshed only through the assembler.
9. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: focused active-surface assertions and synthetic fixtures for the contract; no scan or rewrite of frozen historical work items.
10. `docs/work-items/2026-07-18_superpowers-adapter-contract/deltas/testing-guide.delta.md`, `deltas/operator-manual.delta.md`, and `changelog/implementation.md`: implementation-local documentation and changelog source created during execution.

## Implementation Approach

First establish a single durable boundary in the root guidance and lifecycle, execution-quality, and model-policy owners. Keep reusable rules in their canonical owner and make routers and operator guides point to them, rather than restating them.

Then change the shared plan-template source blocks. Both small/medium plans and large/phased phase plans receive the same executable-plan rules where the source block is shared; their generated outputs are regenerated together. The conditional meta-header is a compact bridge into an already approved Superpowers execution route, not a second approval prompt or a replacement for harness scope, variance, or integration ownership.

Finally add targeted structural checks and synthetic positive and negative fixtures, then verify assembly freshness, policy validation, active-surface wording, and the final diff. The implementation deliberately validates current local behavior, so it does not preserve mutable external Superpowers version evidence and it does not persist Superpowers task briefs, ledgers, or review packages.

## Model and Sub-agent Strategy

Planning recommendation:

1. Model generation: `not exposed`.
2. Capability tier: `balanced`.
3. Reasoning effort: `medium`.
4. Resolved profile: `not exposed`.
5. Model-policy source: `AGENTS.md` active repository policy, `economy-default`.
6. This is a policy-relative recommendation for plan drafting, not a claim about this task's actual runtime allocation.

Execution recommendation:

1. Orchestration mode: `single-agent` for integration; Superpowers may be used as an execution method after the frozen package and fresh authorization permit it.
2. Main task allocation: `balanced` with `medium` reasoning as the economy-default recommendation for this bounded policy and validator change.
3. Small mechanical Superpowers executor allocation: `fast/economy` with `medium` reasoning when the task is limited to a clearly bounded generated-output or fixture change with deterministic checks.
4. Consequential review allocation: `balanced` with `medium` reasoning for the adapter-boundary and validator review; escalate through the approved policy only when residual ambiguity, evidence failure, or material variance justifies it.
5. Every Superpowers dispatch must name its policy-relative tier and reasoning effort. It must record model generation and resolved profile as `not exposed` unless the platform exposes them, and must not silently inherit an unknown session allocation.
6. Availability and fallback: when Superpowers or explicit allocation controls are unavailable, the orchestration thread performs the same bounded task and checks under the recorded economy-default intent; it does not silently select a broader tier, effort, write authority, or concurrency mode.
7. Execution continuity: `same task` after the plan freeze and a fresh operator instruction to begin. If the platform or operator selects a different task, use a curated-artifact handoff containing the frozen spec, architecture snapshot, plan, test-case snapshot, approved strategy, first task, and variance stop condition.
8. Context visibility: `not exposed`.
9. Artifact rehydration: `Yes` before implementation because the frozen package must be reread; no Superpowers execution package becomes durable by default.

Plan-drafting sub-agents: none. The frozen inputs, source ownership, and decision boundary are tightly coupled, and an independent read-only review would not materially improve this drafting pass.

## Implementation Tasks

### `TASK-001` Establish the canonical Superpowers boundary

Dependencies: approved frozen spec and architecture snapshot.

Interfaces:

1. Consumes: the path, lifecycle, and ownership constraints in `SPEC-001`, `SPEC-004`, `DEC-001`, the root `AGENTS.md`, and the README adoption and global-bootstrap guidance.
2. Produces: one discoverable path-preference and lifecycle contract for repository-local and global `AGENTS.md` guidance, the harness router, lifecycle reference, and execution-quality reference.

Implementation:

1. Update the root `AGENTS.md` and the compact global `AGENTS.md` bootstrap snippet in `README.md` so the instructions that downstream operators merge into project-specific or global guidance explicitly override Superpowers' default spec and plan locations for harness-managed work, while retaining `docs/work-items/<work-id>/` as the canonical durable package.
2. Update `.agents/skills/dev-doc-harness/references/artifact-contract.md` to define the conditional conversion of Superpowers planning content into the canonical package, the one freeze-and-continuity route before Superpowers execution, the ephemeral status of task briefs and similar aids, and the concise no-Superpowers fallback that asks only for independently executable and verifiable tasks.
3. Update `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md` to require an approved route before Superpowers pre-flight or execution, to retain the recorded fallback when Superpowers is unavailable, and to prohibit a second generic Superpowers-mode choice after freeze.
4. Update `.agents/skills/dev-doc-harness/SKILL.md` only with routes or short discoverability cues that point to these canonical owners.

Exit criteria: both reusable `AGENTS.md` instruction surfaces identify project-specific or global guidance as the location preference, name one durable harness route, and permit Superpowers only inside the authorized execution boundary.

### `TASK-002` Define plan and model-policy contract prompts

Dependencies: `TASK-001`.

Interfaces:

1. Consumes: the durable lifecycle boundary from `TASK-001` and `SPEC-002`, `SPEC-003`, and `SPEC-005`.
2. Produces: reusable source-block prompts for conditional executable metadata, self-contained task context, interface/dependency separation, numbered steps, and explicit allocation notation.

Implementation:

1. Update `.agents/skills/dev-doc-harness/references/subagent-model-policy.md` to define the approved Superpowers dispatch envelope: deliberate policy-relative tier and reasoning effort per dispatch; `not exposed` for unreported generation, profile, and runtime reasoning; completion reporting that distinguishes recommendation from observed allocation; and the existing approval route for work outside the policy, fallback, concurrency, write-authority, or review boundary.
2. Update `plan.010.small.header-inputs.md` and `plan.010.phase.header-objective-inputs.md` with an optional merged execution meta-header that is present only when the frozen plan records Superpowers as the authorized method. The prompt must retain harness control of scope, variance, model bounds, and final integration.
3. Update `plan.020.common.traceability-approach-surfaces.md` with a conditional Global Constraints prompt: include a concise summary or reference only when it makes the plan or task self-contained, and do not repeat stable commitments, architecture decisions, task instructions, or checks solely to fill the section.
4. Update `plan.040.common.model-strategy.md` to prompt a planning recommendation, main-task recommendation, and consequential-role recommendation without asserting hidden runtime values, and to prompt explicit in-envelope Superpowers allocations where delegation is authorized.
5. Update `plan.050.common.task-plan.md` so every task declares dependencies separately from interfaces; interfaces name consumed inputs and produced outputs when they matter; executable task steps are numbered and do not use checkbox task lists.

Exit criteria: source blocks guide a fresh planner to choose the compact adapter form only when applicable and preserve every approved model, task-context, and lifecycle boundary.

### `TASK-003` Regenerate canonical plan templates

Dependencies: `TASK-002`.

Interfaces:

1. Consumes: changed source blocks and existing assembly manifests.
2. Produces: synchronized generated small/medium and phase-plan templates with no direct hand edits.

Implementation:

1. Confirm `.agents/skills/dev-doc-harness/assets/templates/assemblies/small-medium-work-item-plan.json` and `large-phased-work-item-phase-plan.json` already assemble the changed source blocks; edit a manifest only if a required changed block is not included.
2. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` to regenerate `small-medium-work-item-plan.md` and `large-phased-work-item-phase-plan.md`.
3. Inspect both generated outputs to confirm the optional meta-header, conditional Global Constraints, distinct interfaces and dependencies, numbered task steps, and explicit allocation prompt appear once in the intended section and do not create a duplicate lifecycle route.

Exit criteria: generated plan templates are fresh, source-derived, and show the selected contract without unresolved source-block syntax.

### `TASK-004` Publish concise operator-facing adapter guidance

Dependencies: `TASK-001`, `TASK-002`, and `TASK-003`.

Interfaces:

1. Consumes: canonical lifecycle and model-policy language from `TASK-001` and `TASK-002`.
2. Produces: aligned maintainer and operator explanations that point to, rather than duplicate, the canonical rules.

Implementation:

1. Update `README.md` outside the global `AGENTS.md` bootstrap snippet with the operational sequence: merged project-specific or global guidance overrides Superpowers output defaults; the harness package is the durable record; the harness freeze and fresh authorization complete before Superpowers execution; execution aids remain ephemeral; and the fallback preserves independently executable and verifiable tasks.
2. Update `.agents/skills/dev-doc-harness/docs/operator-note.md` with the same boundary in package-local operator language, including conditional meta-header use and no silent allocation inheritance.
3. Keep `docs/superpowers` guidance limited to its existing historical pointer-stub exception. Do not create a directory or a new pointer stub in this work item.

Exit criteria: a maintainer can find the concrete adapter sequence from root documentation or the package operator note without encountering a competing approval or artifact path.

### `TASK-005` Add focused structural validation and fixtures

Dependencies: `TASK-001` through `TASK-004`.

Interfaces:

1. Consumes: active guidance and generated templates only; synthetic fixture strings represent positive and negative adapter cases.
2. Produces: deterministic validator evidence for `VER-001` through `VER-006` without treating frozen historical artifacts as current-policy inputs.

Implementation:

1. Extend `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` with one adapter-contract assertion group that verifies active path-preference guidance, the singular lifecycle boundary, conditional template prompts, the no-checkbox requirement within executable task steps, the Global Constraints self-containment condition, interface/dependency distinction, fallback cue, and explicit allocation rules.
2. Add focused positive and negative fixture helpers in the same validator for: allowed numbered steps versus checkbox task steps; required interfaces versus dependencies; omitted versus necessary Global Constraints; `not exposed` and operator-exposed runtime values; an explicit in-envelope dispatch; and an out-of-envelope dispatch requiring approval.
3. Limit the new assertions to canonical guidance, template source blocks, generated templates, and fixture strings. Preserve the existing historical-artifact compatibility guard and do not add frozen work-item plan scans.
4. Add the planned validator and assembly commands to `deltas/testing-guide.delta.md`, and add the operator-facing adapter and fallback explanation to `deltas/operator-manual.delta.md` during the implementation documentation update.

Exit criteria: the validator rejects each focused contract violation, accepts the approved forms, and continues to treat historical artifacts as history rather than mutable policy.

### `TASK-006` Validate, record the implementation, and commit

Dependencies: `TASK-005`.

Interfaces:

1. Consumes: implementation changes, regenerated templates, validator output, and the approved plan's planned commit subject.
2. Produces: validated implementation evidence, an implementation changelog fragment, and one scoped implementation commit.

Implementation:

1. Create `changelog/implementation.md` before committing with a newest-first entry headed `2026-07-18_superpowers-adapter-contract -- align durable planning and execution`; include exactly one release-target, package-impact, and release-note metadata set and describe the active guidance, template, and validator delivery.
2. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`, `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, and `python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --lint`.
3. Run the focused searches and diff inspections in `CHECK-003` through `CHECK-005`; repair only failures within the approved contract.
4. Review `git diff --check` and `git diff --name-only`, then commit the scoped implementation only after all required checks pass.

Exit criteria: all planned validation evidence passes, the changelog fragment matches the implementation subject, and the implementation commit contains only approved active surfaces, generated outputs, validator fixtures, and required work-item documentation.

## Plan Checks

### `CHECK-001` Template assembly remains source-derived

Covers: `VER-002`, `VER-003`, `VER-005`, and `VER-006`.

Method: run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` after source-block changes.

Expected result: exit code `0`; all assembly manifests are valid and the generated plan templates match their source blocks.

### `CHECK-002` Harness policy validator covers the adapter

Covers: `VER-001` through `VER-006`.

Method: run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Expected result: exit code `0`; the existing harness checks and the new adapter-contract assertions accept active guidance and approved synthetic fixtures while rejecting the specified negative cases.

### `CHECK-003` Active surfaces express one durable boundary

Covers: `VER-001`, `VER-003`, and `VER-004`.

Method: run `rg -n -i "Superpowers|docs/superpowers|work-items|freeze|ephemeral|fallback|Global Constraints|Interfaces|Dependencies" AGENTS.md README.md .agents/skills/dev-doc-harness/SKILL.md .agents/skills/dev-doc-harness/references .agents/skills/dev-doc-harness/docs/operator-note.md .agents/skills/dev-doc-harness/assets/templates`.

Expected result: active surfaces identify the work-item package and harness route as canonical, describe the conditional plan form and fallback, and contain no instruction that creates a second durable Superpowers artifact path or approval route.

### `CHECK-004` Model policy and fixtures remain explicit

Covers: `VER-005`.

Method: inspect the new validator fixture helpers and run `rg -n "not exposed|silent inherit|explicit.*allocation|in-envelope|out-of-envelope|approval" .agents/skills/dev-doc-harness/references/subagent-model-policy.md .agents/skills/dev-doc-harness/assets/templates .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Expected result: the policy and template prompts preserve `not exposed`, require explicit allocation choice for a Superpowers dispatch, and route out-of-envelope choices to approval without claiming hidden thread runtime values.

### `CHECK-005` Scope and history remain narrow

Covers: `VER-006`.

Method: run `git diff --check`, `git diff --name-only`, and `git diff -- docs/work-items/2026-07-18_superpowers-adapter-contract/spec_superpowers-adapter-contract.md docs/work-items/2026-07-18_superpowers-adapter-contract/snapshots/architecture.snapshot.md docs/work-items/2026-07-18_superpowers-adapter-contract/changelog/planning-approval.md`.

Expected result: no whitespace errors; changes are limited to the approved active owners, templates, generated outputs, validator, and planned work-item documentation; the three frozen inputs have no diff.

All Plan Checks are required. Equivalent local command substitutions may be used only when they prove the same evidence purpose and follow `rule:lifecycle.variance-policy`.

## Documentation Artifact Matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source for plan approval | Living | Yes | Approval freeze only | `changelog/plan-approval.md` | Create after explicit approval; do not alter the frozen spec-only `planning-approval.md` fragment. |
| Changelog source for implementation | Living | Yes | Before implementation commit | `changelog/implementation.md` | Heading matches the implementation planned-subject snippet. |
| Root changelog consolidation | Living | No | Operator-owned checkpoint | `CHANGELOG.md` | Not part of ordinary plan approval or implementation commits. |
| Test cases | Snapshot | Yes | Drafted before plan freeze | `snapshots/test-cases.snapshot.md` | Covers active guidance, generated templates, lifecycle, allocation, and historical-scope cases. |
| Testing guide delta | Living delta | Yes | During implementation | `deltas/testing-guide.delta.md` | Records assembly, validator, and fragment-lint commands. |
| Operator manual delta | Living delta | Yes | During implementation | `deltas/operator-manual.delta.md` | Explains the adapter and no-Superpowers fallback. |
| API reference delta | Living delta | No | Not applicable | N/A | The work changes no public runtime API. |
| Architecture snapshot | Snapshot | Yes | Frozen input | `snapshots/architecture.snapshot.md` | `DEC-001` remains authoritative and unchanged. |
| Architecture summary delta | Living delta | No | Not applicable | N/A | The work-item decision snapshot is sufficient. |
| Compatibility evidence record | Evidence | No | Not applicable | N/A | The plan validates local active behavior and does not enforce a mutable external Superpowers version claim. |

## Planned Commits

Plan approval commit:

1. Planned subject: `plan: superpowers-adapter-contract -- approve implementation plan`.
2. Changelog title or snippet: `2026-07-18_superpowers-adapter-contract -- approve implementation plan`.
3. Notes: after explicit operator approval, commit `plan_superpowers-adapter-contract.md`, `snapshots/test-cases.snapshot.md`, and the new `changelog/plan-approval.md`; do not include frozen spec-only artifacts.

Implementation commit:

1. Planned subject: `docs: superpowers-adapter-contract -- align durable planning and execution`.
2. Changelog title or snippet: `2026-07-18_superpowers-adapter-contract -- align durable planning and execution`.
3. Notes: commit the approved active guidance, template source blocks, generated templates, structural validator, testing and operator deltas, and `changelog/implementation.md` after required checks pass.

## Validation and Variance

Before the plan freezes, operator feedback changes this draft plan and the draft test-case snapshot directly. After freeze, a routine equivalent wording, helper, or command adjustment may proceed when it preserves the approved scope, outcome, and evidence purpose; record it in `implementation-notes/variance-log.md` when it would help a later reader.

Stop for an amendment and operator approval before a change that affects artifact canonicality, lifecycle authority, authorization, concurrency, write authority, model-policy envelope, a required verification criterion, the frozen architecture decision, or the approved scope. Do not reinterpret `DEC-001` to make Superpowers execution aids durable.

## Planning Freeze Boundary

This staged planning package is ready for draft review as `plan_superpowers-adapter-contract.md` and `snapshots/test-cases.snapshot.md`. The approved spec, architecture snapshot, and spec-only planning changelog are frozen inputs and remain unmodified.

After explicit approval, follow `module:freeze-gate`: create the new plan-approval changelog fragment, mark this plan and test-case snapshot approved, stage only the approved plan package and its new fragment, commit with the planned approval subject, and stop. A fresh operator instruction is required before implementation begins.

## Readiness

1. Inputs, scope, tasks, checks, documentation, and changelog paths are concrete.
2. The plan preserves all `SPEC-001` through `SPEC-006` commitments and `DEC-001` without adding a competing Superpowers lifecycle.
3. No required decision, unresolved placeholder, or ownerless deferral remains.

## Completion

1. Required active guidance, template, generated-output, validator, and work-item documentation changes are complete and validated.
2. Any noteworthy variance is recorded, and material variance is approved through an amendment.
3. The scoped implementation is committed, or the completion report states the exact blocker and current worktree status.

## Approval

- Status: Approved
- Superseded by: None
