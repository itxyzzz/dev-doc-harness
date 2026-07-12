# New-Task Handoff Visibility Spec

Work ID: `2026-07-12_new-task-handoff-visibility`
Short ID: `new-task-handoff-visibility`
Status: Approved
Harness release: `0.5+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:artifact-style`, `module:models`, `module:execution-quality`, `module:freeze-gate`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.work-item-architecture-decisions`, `rule:lifecycle.variance-policy`, `rule:models.execution-continuity`, `rule:execution-quality.execution-thread-start`, `rule:freeze.approval-freeze`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

## Goal

Restore clear planning-package boundaries while making a recommended `new task with curated-artifact handoff` transition useful in the conversation. The harness must distinguish combined small/medium planning from an intentionally staged planning package, and every actual freeze handoff must visibly identify its next activity, then offer approval-gated task creation with the recorded model settings when supported. When creation is unavailable, the visible handoff remains the manual fallback.

## Source and Intent

Source input:

1. The operator observed that current 0.5+ behavior after the GPT-5.6 model-selection work creates a short handoff that can omit the latest relevant frozen artifacts and stays hidden in a document.
2. The operator identified an incompatible post-freeze interaction: the agent says to confirm before implementation even when the approved/recommended continuity is a new task, which presses for same-task continuation and interrupts the intended transition.
3. The operator confirmed that planning approval remains unchanged. After freeze, a recommended new-task transition must show the handoff directly, recommend a new task with the recorded model generation, resolved profile when exposed, capability tier, and reasoning effort, and ask approval to create that task.
4. The operator required a portable fallback: if task creation or the requested model settings are unavailable on the current platform, preserve the earlier copy-ready handoff flow rather than failing the transition.
5. The operator identified a process-quality regression: a small/medium spec draft was treated as an independent spec-to-plan transition even though the canonical default is a combined spec-and-plan package. The harness must make the planning shape and actual next activity explicit rather than letting generic handoff prompts blur them.

Desired operator/user outcome:

1. A visible handoff can start a new task without reopening repository discovery or searching for the current frozen planning package.
2. In a capable environment, an approved recommended transition creates that new task with its handoff prompt and recorded model/reasoning settings.
3. In any environment, a new-task recommendation preserves a copy-ready manual fallback and an explicit operator override to continue in the current task.
4. Operators and fresh agents can tell whether a package is a combined small/medium package, an explicit small/medium staged exception, or a large/phased anchor, and can see the actual next activity before approving a transition.

Success summary:

1. The freeze-gate result is selected by the approved execution-continuity value and current task-creation capability.
2. The new-task result includes the current exact frozen inputs, proposed model settings, and canonical rule references; it creates the task only after explicit approval.
3. Same-task and explicitly justified alternatives keep their appropriate transition flow.
4. Generic template prompts cannot turn an unfrozen or combined small/medium spec into an implied plan-drafting freeze boundary.

## Scope Boundary

### In scope

1. Define the post-freeze conversational outcome when execution continuity is `new task with curated-artifact handoff`, including capability-gated task creation after explicit approval, at every freeze-to-next-work boundary: anchor spec to phase-plan drafting, plan or phase plan to implementation, and approved amendment to resumed execution or replanning.
2. Require the visible copy-ready handoff to name the exact latest authoritative frozen artifacts relevant to execution: the approved spec, plan or phase plan, required architecture snapshot, applicable amendments, required evidence, and any other current execution input named by the plan.
3. Require the handoff to cite existing harness guidance rather than restate it: applicable `AGENTS.md`, the repository harness, `rule:execution-quality.execution-thread-start`, approved strategy/fallback, first activity, and approval-required variance stop condition.
4. Require the visible result to recommend the recorded proposed model configuration: model generation, resolved profile when exposed, capability tier, reasoning effort, orchestration mode, and fallback.
5. Update canonical policy, freeze-gate guidance, current templates, operator guidance, Codex adapter guidance, and focused validation so their behavior and wording agree.
6. Preserve a concise explicit-continuation escape hatch: the operator may direct continuation in the current task, but the new-task result must not ask them to make that choice.
7. Make the default combined small/medium planning shape and any explicit staged-planning exception discoverable in lifecycle, template, freeze-gate, and validation surfaces.

### Non-scope

1. Remove the normal planning-package draft review or approval/freeze gate.
2. Start implementation automatically, create a task without the operator's explicit post-freeze approval, or override runtime permission and platform-availability constraints.
3. Change when `module:models` recommends `new task with curated-artifact handoff`, the active `economy-default` policy, model tiers, reasoning efforts, orchestration modes, or context-visibility semantics.
4. Reopen frozen historical work-item packages or copy full planning requirements into handoff text.
5. Change the execution behavior selected for `same task` or a justified alternative beyond making the distinct route explicit and testable.
6. Require all small/medium work to stage planning; an explicit staged small/medium package remains available when its recorded reason and next activity justify it.

### Assumptions

1. The continuity value, approved strategy, proposed model configuration, fallback, first activity, and required execution inputs are recorded in the frozen planning package before the freeze gate produces a handoff.
2. The agent can display a Markdown/text handoff in its user-facing response even when the same text is also retained in a planning artifact.
3. A platform may expose a task-creation action with model and reasoning settings, only task creation without settings, or no task-creation action.
4. A fresh task will still perform the execution-thread-start preflight and respect runtime restrictions.
5. A next-task handoff is valid only at an actual frozen package boundary; its first activity must be the next documented planning or execution activity, not an inferred default.

### Open questions

1. None identified after repository-context review and operator design approval.

## Repository Context

### Current state

1. `module:models` defines the three continuity choices and prefers `new task with curated-artifact handoff` when the model generation, tier, resolved profile, or platform multi-agent profile changes.
2. `rule:execution-quality.execution-thread-start` already defines artifact rehydration and a no-rediscovery startup protocol for a new task.
3. The current approval freeze checkpoint first asks for confirmation of strategy settings and whether implementation should begin now, then separately says that a new task should receive a copy-ready handoff.
4. The current common handoff template lists the required handoff fields but does not make the conversation response itself a required, continuity-selected output.
5. The frozen `2026-07-11_model-selection-dimensions` package introduced the continuity model and intended the handoff to be copy-ready, minimal, and artifact-grounded.
6. The current Codex session exposes project-scoped task creation with an initial prompt plus model and reasoning-effort fields; the supported host combinations include GPT-5.6 Sol, Terra, and Luna with their documented effort values.
7. The published README routes small/medium work to “Draft spec and plan,” while the large/phased route is anchor-spec-first. The current lifecycle reference defines the large/phased staged sequence but does not make an intentional small/medium staged exception equally explicit.
8. The latest `2026-07-11_commitment-verification-model` package intentionally froze an approved small/medium spec before plan drafting, but its work-item-specific handoff was not a change to the canonical lifecycle rule.

### Evidence read

1. `AGENTS.md` supplied in the operator request.
2. `.agents/skills/dev-doc-harness/SKILL.md`.
3. `.agents/skills/dev-doc-harness/references/artifact-contract.md`.
4. `.agents/skills/dev-doc-harness/references/naming-conventions.md`.
5. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`.
6. `.agents/skills/dev-doc-harness/references/artifact-style.md`.
7. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`.
8. `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`.
9. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`.
10. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`.
11. `.agents/skills/dev-doc-harness/assets/templates/blocks/handoff.085.common.execution-thread.md`.
12. `docs/work-items/2026-07-11_model-selection-dimensions/spec_model-selection-dimensions.md`.
13. `docs/work-items/2026-07-11_model-selection-dimensions/plan_model-selection-dimensions.md`.

### Constraints and compatibility

1. The repository remains on active `economy-default`; this work changes transition presentation, not model-selection policy.
2. Canonical policy ownership stays split: `module:models` owns continuity selection, `module:execution-quality` owns startup, and `module:freeze-gate` owns the post-freeze operator interaction.
3. The exact frozen artifacts must be selected from the current package rather than hard-coded to a historical work item or limited to only a spec and plan.
4. The handoff must remain concise and must not duplicate requirements already owned by the frozen package or canonical policy.
5. Task creation must be capability-gated and must use the exact recorded model/reasoning settings only when the platform supports them; it must not silently substitute a different setting.
6. A runtime may still block the recorded strategy; the handoff and task-creation prompt cannot claim that a new task bypasses permission or availability checks.
7. Current template sources and generated template outputs must remain assembler-consistent, and focused harness validation must pass.
8. Any unrelated operator work must remain untouched.
9. A generic handoff block must not override lifecycle classification; the actual package shape, approval state, and named next activity determine whether a handoff is emitted and what it starts.

## Specification Commitments and Local Verification Criteria

### `SPEC-001` Specification Commitment — visible new-task handoff

Kind: `Behavior`

Intent: `Change`

Concerns: `operator-flow`, `fresh-thread`, `artifact-discovery`

Statement:

1. After the planning package is frozen, when its approved execution continuity is `new task with curated-artifact handoff`, the agent must present the package's copy-ready handoff as a visible primary result in the current conversation.
2. The visible handoff must identify the exact current frozen execution inputs: approved spec, applicable plan or phase plan, required snapshots, applicable amendments, required evidence, and any additional plan-named execution input.
3. The visible handoff must direct the new task to applicable `AGENTS.md`, the repository harness, and `rule:execution-quality.execution-thread-start`; it must identify the approved strategy and fallback, first activity, and approval-required variance stop condition without restating frozen requirements.

Rationale:

1. A handoff that is hidden or incomplete forces a new task to rediscover the current package and defeats the fresh-task boundary.

#### `VER-001` Verification Criterion — new-task handoff is executable from the conversation

Covers:

1. `SPEC-001`.

Criterion:

1. The canonical contract and template prompts require a visible copy-ready new-task result with all required current artifact categories and canonical startup references, and a representative policy scenario demonstrates that it can start the named first activity without repository rediscovery.

Expected evidence:

1. Focused validator coverage for visible handoff fields and continuity-selected output.
2. A documented representative scenario or test case with exact artifact references and a named first activity.

### `SPEC-002` Specification Commitment — approval-gated task creation

Kind: `Behavior`

Intent: `Change`

Concerns: `approval-boundary`, `operator-flow`, `model-selection`

Statement:

1. Every approval freeze checkpoint that hands work to a next planning or execution activity must retain normal planning approval and freeze mechanics, then select its post-freeze execution result from the approved execution-continuity value and current task-creation capability.
2. For `new task with curated-artifact handoff` when the platform exposes a compatible task-creation action, the current task must display the handoff, recommend creation of a new task with the recorded model generation, resolved profile when exposed, capability tier, reasoning effort, orchestration mode, and fallback, and ask for approval specifically to create that task.
3. Only after explicit operator approval may the agent invoke the platform task-creation action. The created task must receive the displayed handoff as its initial prompt and the recorded concrete model/reasoning settings when those settings are exposed and supported.
4. The result may state that the operator can explicitly direct continuation in the current task, but this must be an opt-in instruction rather than a question or recommended alternative.

Rationale:

1. A new-task recommendation should create a clean transition rather than immediately steering the operator back to same-task execution, while the creation itself remains an explicit external action that requires approval.

#### `VER-002` Verification Criterion — task creation is explicit and correctly configured

Covers:

1. `SPEC-002`.

Criterion:

1. Freeze-gate guidance and representative scenarios distinguish normal planning approval from post-freeze execution routing. A compatible new-task route visibly recommends and asks approval for task creation with the recorded model configuration, then creates the task only after approval; it has no prompt to start implementation in the current task and retains an explicit-continuation opt-in.

Expected evidence:

1. Focused validator assertions over freeze-gate language, task-creation capability checks, model-setting propagation, and transition scenarios.
2. Review of the updated canonical freeze-gate, adapter, and template wording.

### `SPEC-003` Specification Commitment — manual handoff fallback

Kind: `Behavior`

Intent: `Preserve`

Concerns: `portability`, `availability`, `operator-flow`

Statement:

1. When the platform does not expose task creation, or cannot create a task with the recorded required model or reasoning configuration, the agent must visibly provide the same copy-ready handoff as the manual fallback.
2. The fallback must state the unavailable capability or configuration mismatch without inventing a substitute model, reasoning effort, or platform action.

Rationale:

1. The harness runs beyond Codex and a task-creation adapter may be unavailable or unable to honor the approved model strategy.

#### `VER-003` Verification Criterion — unavailable creation preserves the manual route

Covers:

1. `SPEC-003`.

Criterion:

1. A representative unavailable-capability and unsupported-configuration scenario visibly returns the manual copy-ready handoff, preserves the proposed model configuration as information, and performs no task-creation action.

Expected evidence:

1. Focused validator checks and documented representative scenarios.

### `SPEC-004` Specification Commitment — preserve alternative continuity routes

Kind: `Constraint`

Intent: `Preserve`

Concerns: `compatibility`, `authorization`

Statement:

1. `same task` and each explicitly justified alternative must retain a transition flow that is appropriate to its recorded choice, including the existing post-freeze execution authorization requirement where implementation is intended to continue in the current task.
2. No route may imply that the harness approval boundary supersedes runtime permission, platform availability, or approval-required variance handling.

Rationale:

1. The change must correct the new-task mismatch without weakening the existing authorization and safety boundaries.

#### `VER-004` Verification Criterion — non-new-task flows remain authorized and bounded

Covers:

1. `SPEC-004`.

Criterion:

1. Updated policy and validation preserve explicit same-task and justified-alternative behavior, runtime/fallback constraints, and variance-stop handling.

Expected evidence:

1. Focused validator checks and review cases for all continuity values.

### `SPEC-005` Specification Commitment — consistent discoverable guidance

Kind: `Deliverable`

Intent: `Change`

Concerns: `documentation`, `template-parity`, `validation`

Statement:

1. Current canonical policy, freeze-gate guidance, reusable handoff-template source, generated planning templates, README/operator guidance, the Codex task-creation adapter contract, and harness validation must express the continuity-selected conversation result consistently.
2. The implementation must edit source blocks and assembly manifests before regenerating template outputs; it must not hand-edit generated templates.

Rationale:

1. The interaction appears in policy, templates, and user-facing guidance, so an isolated wording change would leave future work items inconsistent.

#### `VER-005` Verification Criterion — current consumers agree

Covers:

1. `SPEC-005`.

Criterion:

1. Template assembly and full harness validation pass, and the current consumer surfaces contain no contradictory new-task continuation prompt, stale hidden-only handoff contract, or unguarded task-creation/model-setting claim.

Expected evidence:

1. Successful template assembly check.
2. Successful full harness-policy validation.
3. Focused repository search and diff review.

### `SPEC-006` Specification Commitment — explicit planning shape and handoff target

Kind: `Constraint`

Intent: `Establish`

Concerns: `planning-lifecycle`, `freeze-gate`, `context-isolation`

Statement:

1. Small/medium work must draft its spec and plan as one planning package by default; the package's plan owns the post-freeze implementation handoff.
2. A small/medium spec-only freeze is permitted only as an explicit recorded exception with a reason, a named next activity of plan drafting, and a spec handoff that targets that activity.
3. Large/phased anchor-spec freezes must continue to target later phase-plan drafting, while plan, phase-plan, and amendment freezes target their documented next execution or replanning activity.
4. Templates, freeze-gate output, and validation must expose the planning shape, frozen artifact set, and named next activity before a handoff or task-creation offer is rendered.

Rationale:

1. A handoff is a transition between concrete work states. Treating every spec as an implicit plan-drafting boundary loses the lifecycle decision that makes the next task understandable and reviewable.

#### `VER-006` Verification Criterion — handoff target matches the frozen package

Covers:

1. `SPEC-006`.

Criterion:

1. Representative combined small/medium, explicit staged small/medium, large/phased anchor, plan/phase-plan, and amendment packages render only the handoff appropriate to their approved next activity; no generic template produces an implied or mismatched transition.

Expected evidence:

1. Focused validator cases for each planning shape and freeze boundary.
2. Template review demonstrating that a combined small/medium spec does not independently solicit a plan-drafting transition.

## Architecture Decisions

Architecture snapshot status: `Required` because this work changes the ownership boundary and control flow among continuity selection, freeze-gate presentation, templates, and fresh-task startup.

Decision summary:

1. Drivers: the operator needs a visible, self-sufficient thread starter, a clean new-task boundary, an approved direct path to create that configured task, and an unambiguous connection between planning shape and transition target.
2. Constraints: preserve canonical lifecycle classification, frozen-package authority, explicit creation approval, runtime restrictions, portable fallback, and current template assembly.
3. Selected approach: first determine the approved package shape and named next activity, then use continuity and current capability to route the post-freeze response; display the artifact-grounded handoff directly and offer approval-gated task creation only at that actual boundary.
4. Affected boundaries: `module:lifecycle`, `module:models`, `module:freeze-gate`, `module:execution-quality`, handoff template source/manifests/generated outputs, README/operator guidance, Codex task-creation adapter, and validator scenarios.
5. Rejected alternatives: keep a universal post-freeze question; hide the handoff only in artifacts; make every spec an implied plan handoff; repeat all planning guidance in the handoff; automatically create a task without approval; silently substitute an unavailable model configuration.
6. Validation cues: `VER-001` through `VER-006`, template assembly, full harness validation, and representative transition scenarios.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. Agent-facing Markdown/text output and an approval-gated optional task-creation action at the approval-freeze transition.
2. The reusable `## Next-task handoff` template contract and all generated planning templates that consume it.
3. Canonical policy interfaces identified by `rule:models.execution-continuity`, `rule:execution-quality.execution-thread-start`, and `rule:freeze.approval-freeze`.

### Data, config, and persistence

1. No runtime data model, persistence, migration, or configuration change is required.
2. Durable planning artifacts continue to carry the current execution input paths and approved strategy fields used to render the visible handoff.

### State and control flow

1. Planning classifies the package before a freeze: combined small/medium, explicit staged small/medium, or large/phased anchor, plan, phase plan, or amendment.
2. Combined small/medium planning drafts the spec and plan together and freezes them together; its plan names the implementation transition.
3. An explicit staged small/medium spec freeze names plan drafting as its next activity. A large/phased anchor spec names phase-plan drafting; plan, phase-plan, and amendment packages name their documented implementation or replanning activity.
4. At each actual freeze-to-next-work boundary, continuity and current capability route the response. A compatible `new task with curated-artifact handoff` displays the handoff and asks approval to create the configured task; after approval it creates that task. An unavailable or incompatible creation capability returns the visible manual handoff. `same task` keeps the current confirmation/start route; a justified alternative documents its explicit route.
5. A created or manually started new task begins through `rule:execution-quality.execution-thread-start`; conflicts still use `rule:lifecycle.variance-policy`.

### Safety, security, privacy, migration, and rollback

1. No security, privacy, data migration, or destructive operation is introduced.
2. The change must not represent a copy-ready prompt or approved task-creation action as automatic implementation authorization or as a bypass of runtime permission and availability controls.
3. Rollback is a documentation/template/validator revert; no stored user or runtime data requires recovery.

## Risks and Rejected Alternatives

### `RISK-001` incomplete artifact enumeration

Decision or mitigation:

1. Derive the handoff's exact input list from the frozen current package and its plan rather than a fixed spec-and-plan pair; test a package that also needs a snapshot, amendment, or evidence.

### `RISK-002` accidental task creation or configuration substitution

Decision or mitigation:

1. Keep planning approval/freeze unchanged, require a separate explicit creation approval, retain `same task` confirmation behavior, require exact supported settings, and state that a new task still performs startup and runtime-permission checks.

### `RISK-003` duplicate or contradictory guidance

Decision or mitigation:

1. Keep reusable semantics in their existing canonical owners, let templates provide compact prompts, and enforce parity through source-first regeneration and focused tests.

### `RISK-004` portability and adapter drift

Decision or mitigation:

1. Keep the core contract capability-gated, validate the Codex adapter separately, and preserve the visible manual handoff when creation or selected settings are unavailable.

## Planned commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `plan: new-task-handoff-visibility -- clarify transition targets` | `2026-07-12_new-task-handoff-visibility -- clarify transition targets` | Approval commit for the combined spec-and-plan package, snapshots, pointer stub, and planning fragment. |
| Implementation | `docs: new-task-handoff-visibility -- create configured continuity tasks` | `2026-07-12_new-task-handoff-visibility -- create configured continuity tasks` | Canonical policy, templates, generated outputs, guidance, Codex adapter, validation, and implementation fragment. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source | Living | Yes | Before each commit | `docs/work-items/2026-07-12_new-task-handoff-visibility/changelog/*.md` | Create `planning-approval.md` only when this draft is approved for freeze; create `implementation.md` before an implementation commit. |
| Root changelog consolidation | Living | No | Operator-owned checkpoint | `CHANGELOG.md` | Do not edit for the ordinary planning approval or implementation commits. |
| Test cases | Snapshot | Yes | Before implementation | `snapshots/test-cases.snapshot.md` | Defines representative continuity routes, creation approval, configuration propagation, and artifact-enumeration checks. |
| Testing guide delta | Living delta | No | During or after implementation | `deltas/testing-guide.delta.md` | Existing harness validation guidance remains sufficient. |
| Operator manual delta | Living delta | Yes | After implementation | `deltas/operator-manual.delta.md` | Proposes concise operator-facing transition behavior documentation if the README alone is insufficient. |
| API reference delta | Living delta | No | During or after implementation | `deltas/api-reference.delta.md` | No public runtime API. |
| Architecture snapshot | Snapshot | Yes | Before implementation | `snapshots/architecture.snapshot.md` | Captures the selected ownership and control-flow boundary. |
| Architecture summary delta | Living delta | No | After review | `deltas/architecture-summary.delta.md` | No repository-wide architecture document is currently changed. |
| Superpowers design pointer | Pointer stub | Yes | Before spec review | `docs/superpowers/specs/2026-07-12-new-task-handoff-visibility-design.md` | Points to this canonical draft without duplicating it. |

## Next-task handoff

Planning shape: `combined small/medium`; this draft spec and its implementation plan are created and frozen as one planning package.

This spec does not independently emit a next-task handoff. The combined package's plan owns the post-freeze implementation handoff and records its continuity, context visibility, artifact rehydration, proposed model configuration, and capability-gated task-creation route.

If this package were changed to an explicit staged small/medium exception before approval, this section would instead record the reason and a plan-drafting handoff. That change would require direct draft revision and review before freeze.

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Specification Commitments are atomic, classified, bounded, and contain every implementation obligation in their Statements.
- [x] Verification Criteria have valid Covers sets, expected evidence, deterministic local/cross-cutting placement, and no hidden procedure or scope.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Interfaces, data, control flow, and safety/privacy/migration impacts are checked.
- [x] Risks and rejected alternatives are listed or explicitly absent after review.
- [x] Documentation artifact matrix decisions have paths or reasons.
- [x] Planned commit subjects and changelog title snippets are synchronized.
- [x] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain before approval or handoff.

## Approval

- Status: Approved
- Superseded by: None
