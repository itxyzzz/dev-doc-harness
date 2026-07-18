# Planning Template Clarity Spec

Work ID: `2026-07-18_planning-template-clarity`
Short ID: `planning-template-clarity`
Status: Approved
Harness release: `0.7+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:artifact-style`, `module:freeze-gate`, `module:execution-quality`, `rule:lifecycle.planning-shape`, `rule:lifecycle.large-phase-orchestration`, `rule:lifecycle.superpowers-compatibility`, `rule:lifecycle.commit-message-format`, `rule:models.selection-dimensions`, `rule:models.execution-continuity`, `rule:quality.specification-commitments`, `rule:freeze.approval-freeze`

Artifact style: approved final content. Keep the policy changes compact, put reusable semantics in their canonical owner, and make templates record decisions without reproducing policy.

## Goal

Make the harness planning templates unambiguous about model recommendations, execution continuity, Superpowers metadata, commitment structure, commit boundaries, handoff ownership, and rolling phase execution without adding a new process layer.

## Source and Intent

Source input:

1. The operator reviewed the current harness after the Superpowers adapter implementation and supplied ordered comments on `SKILL.md`, both specification templates, both plan templates, model-selection notation, planned commits, handoffs, and phased execution order.
2. The operator approved the resulting design review and requested this combined planning package.
3. The operator exposed the current planning allocation as Sol with high reasoning, chose to preserve it for planning continuity, and approved a balanced-tier allocation for the fresh implementation task.
4. During draft review, the operator required every harness stage to assess whether bounded sub-agents would improve the upcoming spec, plan, execution, or review stage and to request explicit authorization when useful.

Desired operator outcome:

1. A planner can fill the current templates without confusing the planning task's observed runtime with the model and reasoning configuration recommended for execution.
2. An operator sees one clear next activity at each freeze or completion boundary and does not need to reconstruct the normal small/medium or phased sequence manually.
3. Superpowers remains usable inside the harness boundary without importing its conflicting artifact, task-checkbox, per-task-commit, or post-plan execution-choice defaults.

Success summary:

1. Canonical policy states the few decisions that apply across templates; source blocks consume those decisions in compact final-artifact shapes.
2. Small/medium planning has one combined package and one implementation handoff by default, while large/phased work follows a visible rolling plan-then-implement loop.
3. Focused structural validation protects these boundaries without becoming a semantic parser for operator judgment.

## Scope Boundary

### In scope

1. Clarify the Superpowers compatibility mapping for artifact location, plan form, execution authorization, commit boundaries, review, and finishing while keeping the canonical harness package and freeze route authoritative.
2. Convert the `SKILL.md` completion section to a literal checklist.
3. Remove the undefined optional commitment-classification cue and clarify that every additional `SPEC-*` commitment follows the complete `SPEC-001` structure.
4. Simplify planned-commit sections to stage plus planned subject while retaining subject/changelog synchronization as canonical policy.
5. Separate planning-task observations from the approved execution selection and make the latter explicit even when the former is not exposed.
6. Prefer a fresh task with curated-artifact handoff when a substantial execution task cannot verify that the current model/profile and context state are suitable.
7. Make the plan the sole implementation-transition owner for a combined small/medium package and keep the spec-only handoff limited to an explicitly staged exception.
8. Make rolling phase planning the large/phased default: plan one phase, freeze it, implement it, then plan the next phase from actual prior outputs.
9. Update source blocks, assembly manifests when needed, generated templates, focused validator assertions, and concise operator/testing guidance.
10. Require an explicit upcoming-stage sub-agent feasibility assessment at each harness planning transition, with an operator-approval request when useful and a recorded rationale when no delegation is proposed.

### Non-scope

1. Add a commitment-classification taxonomy, new policy module, phase scheduler, task-creation automation, or second handoff artifact by default.
2. Change the active `economy-default` policy, permanent capability tiers, GPT-5.6 tier mapping, concurrency limits, or operator override authority.
3. Change the external Superpowers plugin or enumerate every Superpowers skill in harness policy.
4. Require one commit per task or one commit per plan regardless of reviewability, reversibility, and validation state.
5. Rewrite frozen historical work-item artifacts to match the clarified current templates.
6. Infer an exact remaining context value, prescribe compaction from an inferred threshold, or require the current task to expose runtime details it cannot expose.
7. Treat operator approval as permission to bypass higher-priority system, platform, sandbox, availability, task-scope, write-authority, or concurrency restrictions.

### Assumptions

1. The active repository policy remains `economy-default`.
2. The operator-provided Sol/high planning allocation is authoritative for this planning task even though the platform does not expose the remaining context state.
3. Terra remains the current selectable mapping for the balanced tier during implementation; if that mapping changes, the executor uses the then-current balanced-tier mapping or stops when no approved balanced option is available.
4. The existing source-block assembly model remains the correct way to update generated templates.
5. The existing validator remains appropriate for high-signal structural assertions and synthetic fixtures.
6. Explicit operator approval can authorize a recorded bounded sub-agent strategy when repository or session defaults require that approval; it does not override higher-priority runtime restrictions.

### Open questions

1. None. The design decisions required for implementation are resolved in this spec and its architecture snapshot.

## Repository Context

### Current state

1. `rule:lifecycle.superpowers-compatibility` already makes the harness package canonical and places Superpowers execution after the harness freeze, but it does not explicitly reconcile Superpowers' checkbox tasks and per-task commit default with current harness task and commit policy.
2. `module:models` currently lists model generation, capability tier, reasoning effort, resolved profile, and continuity together. The reusable plan prompt therefore permits `not exposed` in fields that readers may interpret as the required execution recommendation.
3. The small spec says its plan owns the combined transition but still renders a detailed handoff. The plan renders only a generic conditional handoff section.
4. `rule:lifecycle.large-phase-orchestration` permits freezing one or more phase plans and does not present plan phase 1, implement phase 1, then plan phase 2 as the default loop.
5. Planned-commit sections repeat changelog title/snippet and notes fields even though lifecycle and naming policy already require synchronization.
6. The current policy validator passes, so these are semantic clarity and workflow usability changes rather than broken package structure.

### Evidence read

1. `AGENTS.md`, `.agents/skills/dev-doc-harness/SKILL.md`, and harness release marker `0.7+`.
2. `references/artifact-contract.md`, `planning-freeze-gates.md`, `subagent-model-policy.md`, `durable-planning-quality.md`, `artifact-style.md`, `context-and-quality-gates.md`, `policy-architecture.md`, and `naming-conventions.md`.
3. Current small/medium and large/phased spec and plan templates, their source blocks, and assembly manifests.
4. `.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md` and `architecture-snapshot.md`.
5. `.agents/skills/dev-doc-harness/scripts/assemble_templates.py` and `test_harness_policy.py`.
6. `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md`.
7. The approved and implemented `2026-07-18_superpowers-adapter-contract` package, plus relevant harness-simplification and model-selection-calibration history.
8. Installed Superpowers `6.1.1` brainstorming and writing-plans guidance.

### Constraints and compatibility

1. Templates own artifact shape and prompts; canonical references own reusable lifecycle, model, quality, and compatibility semantics.
2. The repository harness overrides Superpowers' default durable artifact locations and planning lifecycle.
3. Existing stable rule IDs should be retained unless a genuinely new independently owned rule is required; this work does not require one.
4. Generated templates must be changed through source blocks and assembly manifests, not direct edits.
5. Historical work items remain immutable evidence and are outside current-template conformance checks.
6. Root `CHANGELOG.md` remains an operator-owned consolidation surface; work-item fragments are updated before commits.

## Commitments and Verification

Every additional `SPEC-*` commitment in this section follows the complete `SPEC-001` structure: Statement plus a local `VER-*` subsection unless its evidence is genuinely cross-cutting and linked in a shared verification section.

### `SPEC-001` Keep one explicit Superpowers adapter boundary

Statement:

1. Current harness guidance must map Superpowers methodology to the harness artifact, freeze, model-policy, variance, commit, review, and integration boundaries without enumerating every external skill.
2. Conditional Superpowers execution information must appear as actual plan metadata rather than as a normal document section that resembles a second execution stage.
3. Superpowers task-checkbox, per-task-commit, and post-plan execution-mode defaults must yield to the approved harness plan where they conflict.

#### `VER-001` Adapter precedence is compact and complete

Covers: `SPEC-001`.

Criterion: Active lifecycle, router, execution-quality, template, and operator guidance identifies one durable package and approval route and resolves the known plan-form and commit-boundary conflicts.

Expected evidence: Focused validator assertions, generated-template inspection, and active-guidance review.

### `SPEC-002` Use one complete commitment shape

Statement:

1. Current quality policy and spec templates must remove the undefined optional classification cue.
2. The shared commitment template must state that later commitments use the same Statement and local Verification Criterion structure as `SPEC-001`, except when a genuinely cross-cutting criterion supplies the linked evidence.

#### `VER-002` Commitment examples cannot imply optional obligations

Covers: `SPEC-002`.

Criterion: The current shared spec block and both generated spec templates contain the repeated-structure clarification and no unsupported classification example.

Expected evidence: Assembly check, focused searches, and validator assertions on active template surfaces.

### `SPEC-003` Plan reviewable commit boundaries without duplicate fields

Statement:

1. Planned-commit template sections must record only the stage and planned commit subject; essential exception notes may follow the table as prose.
2. Canonical lifecycle policy must define a cohesive implementation package as the default commit boundary and permit splits only at stable, independently reviewable and revertible boundaries with relevant checks passing.
3. A Superpowers task receives its own commit only when that task is also an approved meaningful commit boundary.
4. Subject and changelog-title synchronization remains mandatory policy even though templates no longer duplicate the changelog title field.

#### `VER-003` Commit planning is concise and meaningful

Covers: `SPEC-003`.

Criterion: Current spec, plan, phase-plan, and amendment planned-commit prompts use stage plus subject and direct exceptional granularity decisions to canonical policy.

Expected evidence: Source-block and generated-template checks, amendment-template inspection, and changelog-policy regression tests.

### `SPEC-004` Separate observed planning state from approved execution selection

Statement:

1. Model policy and strategy templates must distinguish planning-task observations from the approved execution selection.
2. Planning-task model generation, profile, reasoning effort, and context signal may be `not exposed` when the operator or platform does not expose them.
3. The approved execution selection must explicitly record a target model/profile or policy-relative selection instruction, capability tier, reasoning effort, orchestration mode, availability fallback, continuity, and artifact-rehydration requirement; these recommendation fields must not use `not exposed`.
4. For substantial work, a new task with curated-artifact handoff must be preferred when the intended model/profile changes or when current model/profile or context suitability cannot be verified, unless a concrete continuity reason outweighs that risk.
5. Policy must not infer remaining context or require compaction from an unexposed threshold.

#### `VER-004` Recommended execution cannot disappear into runtime uncertainty

Covers: `SPEC-004`.

Criterion: The model owner, freeze gate, shared plan strategy block, large-spec strategy block, and generated templates clearly separate unknown observations from an explicit future execution choice and conservative continuity route.

Expected evidence: Positive and negative validator fixtures for exposed and unexposed planning state, explicit execution selection, same-task justification, and fresh-task fallback.

### `SPEC-005` Give the combined package one implementation-transition owner

Statement:

1. A combined small/medium spec must record planning shape and identify its plan as the implementation-transition owner without duplicating the plan's full handoff.
2. The small/medium plan must always contain the implementation handoff required at its actual freeze boundary.
3. An explicitly staged spec-only exception must record its reason, frozen spec package, and plan-drafting next activity; the later plan must supply the implementation handoff before it freezes.
4. Freeze routing must consume the transition owner and exact documented next activity rather than infer a stage from a generic handoff heading.

#### `VER-005` Each small/medium boundary has one handoff

Covers: `SPEC-005`.

Criterion: The lifecycle owner, small-spec handoff block, small-plan handoff block, assembly manifests, and generated templates present one non-duplicated transition for both default and exceptional planning shapes.

Expected evidence: Scenario assertions for combined planning, staged spec-only planning, plan freeze, and fresh-task execution handoff.

### `SPEC-006` Make rolling phase planning the normal large-work sequence

Statement:

1. The normal large/phased sequence must freeze the anchor, draft and freeze one phase plan, implement that phase, capture its actual outputs, and then draft the next phase plan from the anchor, amendments, and prior-phase outputs.
2. Batch planning or freezing multiple phase plans before implementation must be an explicit recorded exception limited to stable and independently plannable phases.
3. A phase plan must distinguish its handoff to current-phase implementation from its expected post-phase transition to next-phase planning or work-item completion.
4. The completion report must supply actual prior-phase outputs, variance, validation, and commit state so the operator only approves or starts the named next activity rather than reconstructing it.

#### `VER-006` Phase order is visible and stateful

Covers: `SPEC-006`.

Criterion: Lifecycle, freeze, phase-plan, large-spec, README flow, and focused scenario checks show the rolling loop and its explicit batch-planning exception.

Expected evidence: Generated phase-plan inspection, scenario traversal assertions, and documentation review.

### `SPEC-007` Keep enforcement proportional

Statement:

1. Implementation must update canonical owners, necessary routers and operator summaries, source templates, generated outputs, assembly manifests when ownership changes, and focused validator assertions only.
2. Validation must protect discoverability, source/generated consistency, required field shape, and lifecycle routing without parsing subjective model fit or commit quality.
3. Frozen historical work items must remain unchanged and excluded from current-template conformance enforcement.

#### `VER-007` The diff remains focused and history-safe

Covers: `SPEC-007`.

Criterion: The final diff contains only approved active surfaces, generated outputs, validator updates, work-item documentation, and changelog source; all required checks pass.

Expected evidence: Assembly check, full policy validator, fragment lint, diff inspection, and frozen-history check.

### `SPEC-008` Assess sub-agent feasibility before every upcoming stage

Statement:

1. Before starting a harness-managed spec, plan, phase plan, amendment or replanning, implementation, or consequential review stage, the orchestration agent must assess whether bounded sub-agents would materially improve isolation, independent review, parallel throughput, specialized execution, or risk reduction.
2. When sub-agents are useful and not already authorized, the agent must record the proposed roles, context, outputs, model/effort envelope, write authority, concurrency, and fallback, then explicitly ask the operator to authorize that bounded use before dispatch.
3. Explicit operator approval authorizes the recorded strategy despite a repository or session default against unrequested dispatch, but it cannot override higher-priority system or platform restrictions, unavailable tooling, or the approved task scope.
4. When sub-agents are not useful, the artifact or transition record must state `Sub-agents: None` with a stage-specific fit reason rather than relying on operator silence or an ambient default.
5. Once the operator approves a strategy in the frozen package, execution must not ask again for in-envelope dispatch; a new request is required only for a role, model/effort, write scope, concurrency, or boundary outside that approval.

#### `VER-008` Delegation is considered and authorized instead of silently suppressed

Covers: `SPEC-008`.

Criterion: The model-policy owner, router outcomes, freeze gate, applicable spec and plan prompts, execution startup, and operator guidance require an upcoming-stage assessment, explicit approval request for useful unapproved delegation, recorded no-use rationale, and no repeated in-envelope confirmation.

Expected evidence: Positive and negative fixtures for useful pending delegation, explicitly approved delegation, declined or unavailable fallback, recorded no-use rationale, and out-of-envelope reapproval.

## Architecture Decisions

Architecture snapshot status:

1. `Required`: `snapshots/architecture.snapshot.md` records the policy/template ownership split and transition state model needed by the fresh implementation task.

Decision summary:

1. Drivers: remove ambiguous template fields; preserve one lifecycle; reduce repeated handoff and commit data; make phased work self-routing; keep Superpowers useful without importing its conflicting defaults.
2. Constraints: canonical owners remain authoritative; generated templates remain source-derived; operator approval gates remain; current model/context exposure may be partial.
3. Selected approach: make small canonical-policy clarifications, then reshape shared source blocks and their assemblies to consume them.
4. Affected boundaries: lifecycle, model, quality, freeze, execution-quality, router, template blocks and manifests, generated templates, validator, README/operator note, and future work-item artifacts.
5. Rejected alternatives: template-only wording changes; a new transition module; a commitment taxonomy; unconditional new tasks; one commit per task; automatic phase scheduling.
6. Validation cues: `VER-001` through `VER-008`, `DEC-001` through `DEC-003`, and the plan checks.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. Planner-to-template interface: required fields distinguish observations, recommendations, planning shape, and transition ownership.
2. Plan-to-freeze interface: the plan supplies the exact implementation transition for combined small/medium work.
3. Phase-completion-to-next-plan interface: actual outputs and variance become inputs to the next phase plan.
4. Superpowers-to-harness interface: methodology runs inside the approved plan, commit, model, variance, and integration envelope.
5. Validator-to-policy interface: focused assertions protect structural contracts without becoming a full artifact interpreter.

### Data, config, and persistence

1. No product data, runtime configuration, persistence, migration, or external API changes are in scope.
2. The changed repository policy and template files are durable process inputs.

### State and control flow

1. Small/medium default: draft spec and plan together, approve and freeze together, then use the plan's implementation handoff.
2. Staged small/medium exception: freeze the spec with an explicit reason and plan-drafting next activity, then freeze the later plan before implementation.
3. Large/phased default: freeze anchor, plan phase, freeze phase plan, implement phase, hand actual outputs to next-phase planning, and repeat.
4. At any material post-freeze divergence, stop for the existing amendment and approval route.

### Safety, security, privacy, migration, and rollback

1. No security, privacy, compliance, migration, or destructive-operation impact was identified after repository-context review.
2. The principal risk is durable workflow confusion that causes an unsuitable execution model, duplicate handoff, stale multi-phase plan, or fragmented commit history.
3. Rollback is a focused revert of the implementation commit; frozen work-item artifacts remain as historical evidence.

## Risks and Rejected Alternatives

### `RISK-001` Model notation becomes longer instead of clearer

Decision or mitigation:

1. Use two compact groups—planning observations and approved execution selection—and remove the separate generic “recommended change” narration when its content is represented by the selection.

### `RISK-002` Conservative continuity creates unnecessary task churn

Decision or mitigation:

1. Apply the fresh-task preference only to substantial work when suitability cannot be verified; retain same-task continuation for a known suitable profile or a documented continuity reason.

### `RISK-003` Rolling phases are mistaken for an automatic executor

Decision or mitigation:

1. Keep every existing freeze and approval gate. The harness names and prepares the next activity; it does not silently create a task or begin the next phase.

### `RISK-004` Commit simplification weakens changelog synchronization

Decision or mitigation:

1. Retain synchronization in lifecycle and naming policy and validate the relationship at commit time rather than storing the same phrase in two template columns.

### `RISK-005` Superpowers compatibility becomes another copied methodology

Decision or mitigation:

1. Map only the conflicting boundaries and route all other execution methodology to Superpowers itself.

### `RISK-006` Delegation approval is confused with unrestricted authority

Decision or mitigation:

1. Make the approval scope explicit: it overrides only the repository or session default that requires an operator request for the recorded bounded strategy. Higher-priority platform limits, task scope, write authority, concurrency, and variance controls remain in force.

## Planned Commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: planning-template-clarity -- approve clear planning transitions` |
| Implementation | `docs: planning-template-clarity -- clarify models handoffs and phases` |

The planned subjects supply the matching changelog title snippets. The implementation remains one cohesive commit unless implementation discovers a stable, independently reviewable and revertible split that is approved through normal variance handling.

## Documentation Artifact Matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source | Living | Yes | Before each commit | `docs/work-items/2026-07-18_planning-template-clarity/changelog/*.md` | Create the planning fragment only after explicit package approval; create the implementation entry before its commit. |
| Root changelog consolidation | Living | No | Operator-owned checkpoint | `CHANGELOG.md` | Ordinary planning and implementation commits do not consolidate root changelog. |
| Test cases | Snapshot | Yes | Before implementation | `snapshots/test-cases.snapshot.md` | Freezes the expected active-policy and template behavior. |
| Testing guide delta | Living delta | Yes | During planning and implementation | `deltas/testing-guide.delta.md` | Records the focused and full validation commands. |
| Operator manual delta | Living delta | Yes | During planning and implementation | `deltas/operator-manual.delta.md` | Records the simplified operator-visible sequence and model distinction. |
| API reference delta | Living delta | No | Not applicable | N/A | No public runtime API changes. |
| Architecture snapshot | Snapshot | Yes | Before implementation | `snapshots/architecture.snapshot.md` | Freezes ownership and transition decisions for the fresh executor. |
| Architecture summary delta | Living delta | No | Not applicable | N/A | The work-item snapshot is sufficient; no repository-level architecture document changes. |

## Planning Shape and Transition Ownership

1. Planning shape: `combined small/medium`.
2. Frozen package after approval: this spec, `plan_planning-template-clarity.md`, `snapshots/architecture.snapshot.md`, and `snapshots/test-cases.snapshot.md`.
3. Transition owner: `plan_planning-template-clarity.md`.
4. Next activity: implement `TASK-001` through `TASK-005` in the fresh balanced-tier task defined by the plan.
5. Staged spec-only exception: not applicable.

This spec does not duplicate the plan's implementation handoff or emit a plan-drafting transition.

## Spec Readiness Checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Specification Commitments are atomic, bounded, and contain every implementation obligation in their Statements.
- [x] Verification Criteria have valid Covers sets, expected evidence, and deterministic local placement.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Interfaces, control flow, and safety impacts are checked.
- [x] Risks and rejected alternatives are listed.
- [x] Documentation artifact matrix decisions have paths or reasons.
- [x] Planned commit subjects provide the matching changelog title snippets.
- [x] No unresolved placeholder, required decision, missing section, or ownerless deferral remains.

## Approval

- Status: Approved
- Superseded by: None
