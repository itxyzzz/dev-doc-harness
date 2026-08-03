# Plan Template Alignment Spec

Work ID: `2026-08-03_plan-template-alignment`
Short ID: `plan-template-alignment`
Status: Approved
Harness release: `0.8+`
Schema: `schema:spec.small-medium`
Companion plan: `plan_plan-template-alignment.md`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:architecture`, `rule:lifecycle.planning-shape`, `rule:lifecycle.large-phase-orchestration`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

## Goal

Make the assembled small/medium plan and large/phased phase-plan templates more coherent for a fresh implementation session while preserving the canonical lifecycle, model-policy, and documentation-matrix boundaries.

## Source and Intent

Source input:

1. Operator investigation of `small-medium-work-item-plan.md`, canonical lifecycle, quality, model-policy, freeze-gate references, and the phase-plan template.
2. Operator-approved small-plan readiness wording and design decisions: documentation classification stays in the companion specification's documentation artifact matrix; applicable documentation work remains embedded in the flat implementation-task list; current-session header metadata remains unchanged.
3. Operator-approved phase-plan findings: make session readiness a visible phase boundary, distinguish the frozen phase-execution handoff from the implementation completion report, and support rolling, batched, and parallel execution without the phase plan inventing a later lifecycle transition.

Desired outcome:

1. Template authors can compose a coherent plan in dependency order: inputs and boundaries, executable tasks, stage-specific sub-agent strategy, validation, and a compact frozen handoff.
2. A phase plan treats its approved next stage as `phase execution`; actual completion outputs inform later coordination without pre-selecting a next phase-planning stage.

## Scope Boundary

### In scope

1. Move the shared `Model and Sub-agent Strategy` source block after the common task block in both plan assemblies, renaming it consistently from `plan.040.common.model-strategy.md` to `plan.055.common.model-strategy.md`.
2. Replace the small/medium plan readiness checklist with the operator-approved six checks for fresh-session self-sufficiency, task quality, Plan Check coverage, documentation-matrix application through tasks, stage strategy fit, and unresolved decisions.
3. Rename and promote the phase fresh-thread insertion to a top-level phase-session-readiness section; use `session` terminology and the correct draft-phase-plan versus approved-anchor amendment route.
4. Rework the phase-plan tail after its unchanged documentation-tasks content: distinguish the frozen `Phase implementation handoff` from a later `Phase completion report`, remove the premature `Post-phase transition`, and add artifact rehydration plus the consumer-side execution-start rule.
5. Replace the phase readiness checklist with focused checks for anchor preservation, fresh-session execution, task/check quality, current phase-execution handoff, completion reporting, and unresolved decisions.
6. Update only directly affected policy-validator assertions, regenerate both assembled plan templates, and run full harness validation.

### Non-scope

1. Changing the documentation artifact matrix schema or moving phase documentation obligations out of `## Documentation Tasks`; that follow-up is intentionally deferred.
2. Changing `artifact-contract.md`, lifecycle-stage meanings, freeze-gate mechanics, model-policy semantics, the current-session header format, or the selected `economy-default` policy.
3. Changing the assembled small/medium spec, large anchor-spec template, amendment template, or architecture-snapshot template.
4. Rewriting frozen historical work-item artifacts.
5. Creating a work-item architecture snapshot; this work uses the existing source-block, manifest, assembly, and structural-validator architecture without a new component or boundary.

## Repository Context

### Current state

1. Both published plan templates are generated from ordered source blocks and assembly manifests by `scripts/assemble_templates.py`.
2. `plan.040.common.model-strategy.md` is shared by the small/medium and phase-plan manifests and currently appears before `plan.050.common.task-plan.md`.
3. The small plan's readiness section is concise but repeats model-notation structure instead of testing plan executability and coverage.
4. The phase-only `plan.030.phase.fresh-thread-readiness.md` is an unheaded insertion under Implementation approach and says a phase planner may update an anchor spec before freeze, despite the phase-plan template consuming an approved anchor spec.
5. The phase tail uses `## Handoff output` for the implementation completion report, then `## Phase transitions` for a freeze-time phase-execution handoff plus a speculative post-phase transition.
6. `scripts/test_harness_policy.py` asserts the current strategy block path, phase-transition headings, post-phase transition, phase session boundary wording, and generated-template freshness.

### Evidence read

1. `AGENTS.md`, `.agents/skills/dev-doc-harness/SKILL.md`, and the active Superpowers planning instructions.
2. Canonical `artifact-contract.md`, `durable-planning-quality.md`, `subagent-model-policy.md`, `planning-freeze-gates.md`, `context-and-quality-gates.md`, `naming-conventions.md`, and `maintenance-architecture.md`.
3. The two assembled plan templates, both manifests, source blocks `plan.010`, `plan.020`, `plan.030`, `plan.040`, `plan.050`, `plan.060`, `plan.070`, `plan.080`, `plan.085`, and `plan.090` relevant to the change.
4. Current structural-policy checks for plan source paths, handoff headings, phase transition contents, model-strategy notation, and phase session sizing.
5. The approved `2026-08-03_spec-template-alignment` work-item package as a current harness-package pattern.

### Constraints and compatibility

1. Source blocks and manifests are the maintainer-facing sources of truth. Regenerate the published flat templates; do not hand-edit them.
2. Both published template paths and schema identifiers remain stable.
3. The shared model/sub-agent content remains one source block and moves in both assembled plan outputs; its wording and the current-session header are not otherwise redesigned.
4. The small plan remains a flat list of implementation tasks. The companion spec's documentation matrix remains the classification and completeness owner, while documentation and changelog work remains embedded in normal tasks.
5. The phase plan must preserve the default rolling loop and its documented batch exception while allowing each separately approved phase plan to define appropriate bounded or parallel execution coordination.
6. A phase plan's frozen handoff owns `phase execution` only. Later phase-plan drafting or work-item completion remains an outcome of actual execution evidence and current orchestration decisions, not a second selection embedded in this phase plan.
7. Validator changes must retain assembly freshness and all unrelated lifecycle, model-policy, and generated-template protections.

## Assumptions and Open Questions

### Assumptions

1. The existing assembler can rename source blocks through normal repository moves, consume the revised manifests, and regenerate only the two plan outputs.
2. The work remains small/medium: the source blocks, manifests, generated outputs, and focused structural assertions form one bounded template contract.
3. `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` regenerates the affected outputs and invokes the structural validator.

### Open questions

None. The operator has selected the small-plan checklist wording and the phase-plan boundary decisions needed for this package.

## Commitments and verification

### `SPEC-001` Order shared strategy after executable tasks

Statement:

1. Both plan assemblies must render the shared `## Model and Sub-agent Strategy` section after `## Implementation tasks` and before planned commits.
2. The shared source block must be renamed to an order-consistent `plan.055.common.model-strategy.md` path; it must remain the sole shared owner of its prompts.

#### `VER-001` Strategy is ordered consistently in both assembled plans

Covers: `SPEC-001`.

Criterion: Each assembled plan contains `## Implementation tasks`, then `## Model and Sub-agent Strategy`, then `## Planned commits` in that order; the manifests reference the renamed shared source and no current manifest references the retired path.

Expected evidence: Manifest and source-block inspection, focused heading-order checks, `assemble_templates.py --check`, and policy validation.

### `SPEC-002` Make small-plan readiness an executable coverage check

Statement:

1. The small/medium plan readiness checklist must use the six operator-approved checks exactly in intent: self-sufficient plan content, bounded task shape, full Verification Criteria coverage by nested checks, application of the companion spec's documentation matrix through normal tasks, appropriate documented next-stage strategy, and no unresolved decision or ownerless deferral.
2. The current-session header and the existing separate grouped next-stage selection remain unchanged.

#### `VER-002` Small-plan checklist preserves flat-task and policy boundaries

Covers: `SPEC-002`.

Criterion: The generated small plan has all six approved readiness checks, requires documentation and changelog work to be embedded in implementation tasks, and contains no new Documentation Tasks section or altered current-session metadata.

Expected evidence: Source/generated-template inspection and focused validator assertions.

### `SPEC-003` Establish an explicit phase session boundary

Statement:

1. The phase-only readiness insertion must become `## Phase session readiness` at its existing pre-task location.
2. It must state that the phase is executable by one orchestration session with documented bounded delegation and must not require hidden chat context, excessive coordination, or an oversized boundary.
3. It must direct local draft-phase-plan refinement or splitting before phase-plan freeze, and require an amendment before implementation for material changes to an approved anchor; it must not imply ordinary anchor-spec editing after approval.

#### `VER-003` Phase session boundary matches phase-plan lifecycle state

Covers: `SPEC-003`.

Criterion: The generated phase plan uses `session` terminology, renders the phase-session section before tasks, and states an executable local-refinement versus approved-anchor-amendment decision path.

Expected evidence: Source/generated-template inspection and policy-validator checks.

### `SPEC-004` Separate phase execution handoff from completion reporting

Statement:

1. The phase plan must use a freeze-time `## Phase implementation handoff` that owns only `phase execution`.
2. That handoff must retain the grouped next-stage selection and record the frozen package, artifact rehydration/startup rule, and variance stop condition.
3. A separate `## Phase completion report` must specify the executing agent's report without selecting or starting a later lifecycle stage.
4. The phase plan must remove `### Post-phase transition` and its premature next-stage sub-agent assessment.

#### `VER-004` Phase handoff works for rolling and explicitly batched or parallel execution

Covers: `SPEC-004`.

Criterion: The generated phase plan documents its own `phase execution` handoff and completion report, retains rolling as the default and the explicit batch exception, and does not infer `phase-plan drafting` or work-item completion from a generic post-phase subsection.

Expected evidence: Source/generated-template inspection, focused structural validator checks, and full harness validation.

### `SPEC-005` Keep phase readiness focused and phase-specific

Statement:

1. The phase readiness checklist must verify approved-anchor and prior-output preservation, one-session executable scope, bounded tasks, Plan Check coverage, explicit current-phase execution handoff, completion-report expectations, and no ownerless deferrals.
2. The documentation-tasks section remains unchanged in this work item.

#### `VER-005` Phase readiness checks the actual frozen boundary

Covers: `SPEC-005`.

Criterion: The phase readiness checklist does not require a speculative post-phase transition or future-stage sub-agent selection, while preserving the distinct phase execution and completion-report checks.

Expected evidence: Source/generated-template inspection and focused validator assertions.

### `SPEC-006` Maintain generated-template and validator integrity

Statement:

1. The structural validator must update only its path- and wording-sensitive assertions needed for the renamed strategy block, revised phase headings, retired post-phase section, session readiness, and revised readiness contracts.
2. It must retain unrelated assembly-freshness, schema, lifecycle, model-policy, rolling/batch, and state-heading protections.

#### `VER-006` Validation rejects stale plan-template contracts

Covers: `SPEC-001`, `SPEC-002`, `SPEC-003`, `SPEC-004`, `SPEC-005`.

Criterion: Full policy validation accepts the regenerated templates while its focused assertions detect the retired source path and headings or absence of required new handoff/session/readiness structure.

Expected evidence: `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` exits 0 after implementation; focused code review finds targeted assertions rather than relaxed coverage.

## Cross-cutting verification

### `VER-007` Generated template integrity

Covers: `SPEC-001`, `SPEC-002`, `SPEC-003`, `SPEC-004`, `SPEC-005`, `SPEC-006`.

Criterion: The two generated plan templates match their manifests and blocks, retain their schemas and published paths, contain no whitespace errors, and are the only generated template outputs changed by this work.

Expected evidence: `assemble_templates.py --check`, `git diff --check`, generated-template diff review, and `git status --short`.

## Architecture Decisions

Architecture snapshot status: `Not applicable` because the work follows the established source-block, manifest, assembly, and structural-validator architecture without introducing a component, interface, data model, or lifecycle boundary.

Decision summary:

1. Drivers: fresh-session usability, clear freeze versus completion ownership, template ordering consistency, and preservation of canonical policy ownership.
2. Constraints: retain published schemas and paths, one shared model-strategy source, flat small-plan task design, and unchanged documentation-matrix ownership.
3. Selected approach: revise authoritative plan blocks and their manifest order, add a separate phase completion-report block, update structural assertions, then regenerate the two outputs.
4. Affected boundaries: shared model strategy, small readiness, phase session readiness, phase handoff/completion/readiness blocks, the two plan manifests, generated plan templates, and policy-validator assertions.
5. Rejected alternatives: move documentation work into a separate small-plan section; change the current-session header; retain a post-phase lifecycle selection inside a frozen phase plan; duplicate the model-strategy prompt for each template; hand-edit generated outputs.
6. Validation cues: manifest/source order, generated-heading order, focused positive and negative validator assertions, assembly freshness, full policy validation, and whitespace checks.

## Impact Surfaces

### Interfaces

1. Maintainer authoring interface: plan block filenames, manifest order, generated headings, handoff prompts, readiness prompts, and structural-validator contracts change.
2. Published plan-template paths and schema identifiers remain unchanged.

### Data, config, and persistence

None. The work changes Markdown template sources, JSON manifests, generated Markdown templates, and a Python structural validator only; no runtime data, persistence, or product configuration is affected.

### State and control flow

1. Small-plan authoring flow becomes inputs and task definition before the upcoming-stage delegation assessment, then handoff selection near the final boundary.
2. Phase-plan authoring makes session fit explicit before tasks and distinguishes freeze-time phase execution from end-of-execution reporting.
3. Rolling remains the default; batch or parallel work uses independently approved phase plans and their recorded coordination boundary without a template-created later transition.

### Safety, security, privacy, migration, and rollback

1. No product security, privacy, compliance, migration, or destructive-operation impact is expected.
2. Process-safety risks are stale generated templates or weakened structural checks; assembly freshness and targeted validator coverage mitigate them.
3. Rollback is a cohesive revert of the implementation commit. Frozen historical work-item artifacts remain unchanged.

## Risks and Rejected Alternatives

### `RISK-001` Moving a shared source block affects both plan outputs

Decision or mitigation:

1. Update both manifests deliberately, check source and generated heading order in both outputs, and retain one shared strategy source rather than duplicating its policy prompts.

### `RISK-002` Phase-tail cleanup weakens valid batch or parallel coordination

Decision or mitigation:

1. Preserve rolling-default and explicit batch guidance; scope the revised handoff to the current phase's execution and completion report, leaving coordination choices in the recorded phase strategy and approved plan boundaries.

### `RISK-003` Session-readiness text permits rewriting an approved anchor

Decision or mitigation:

1. State the local draft-phase-plan refinement path separately from the amendment path required for a material approved-anchor change, and add a focused negative validator check for retired anchor-edit wording.

### `RISK-004` Readiness wording becomes a copy of canonical policy

Decision or mitigation:

1. Use short outcome-oriented assertions that test the artifact's readiness; retain detailed reusable policy only in the canonical references.

### `RISK-005` Validator changes obscure an accidental regression

Decision or mitigation:

1. Replace only stale path and heading expectations with direct positive and negative checks, retaining the existing schema, assembly, lifecycle, and model-policy assertions.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: plan-template-alignment -- approve plan template cleanup` |
| Implementation | `docs: plan-template-alignment -- align assembled plan templates` |

One cohesive implementation commit is planned because source-block moves, manifest changes, generated outputs, and their structural assertions form one reviewable plan-template contract.

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Implementation changelog source | Living | Yes | During implementation | `docs/work-items/2026-08-03_plan-template-alignment/changelog/implementation-fragment.md` | Create only after fresh execution authorization; planning approval creates no fragment. |
| Root changelog consolidation | Living | Yes | Planning freeze and implementation commit | `CHANGELOG.md` | The repository gate requires a planning entry before the planning approval commit; record the implementation entry before the implementation commit. |
| Test cases | Snapshot | No | N/A | Not created | Deterministic assembly and policy-validator checks provide the needed evidence. |
| Testing guide delta | Living delta | No | N/A | Not created | No operator test-flow change. |
| Operator manual delta | Living delta | No | N/A | Not created | Template maintenance does not change a product operator workflow. |
| API reference delta | Living delta | No | N/A | Not created | No public API. |
| Architecture snapshot | Snapshot | No | N/A | Not created | No new work-item architecture decision. |
| Architecture summary delta | Living delta | No | N/A | Not created | No durable repository architecture change. |

## Planning shape and transition ownership

1. Planning shape: `combined small/medium`.
2. Companion plan: `plan_plan-template-alignment.md` is drafted and presented with this spec in the same planning turn.
3. Transition owner: `plan_plan-template-alignment.md` owns the `plan execution` transition after the combined package freezes.
4. Next lifecycle stage: `plan execution`.

## Spec readiness checklist

- [x] Goal, source and intent, scope, constraints, architecture decisions, commitment statements, and verifications are mutually consistent.
- [x] All relevant operator input is preserved in this specification.
- [x] Commitment statements are atomic, bounded, and form a complete set that covers the full scope and achieves the goal; no obligation exists only in rationale or examples.
- [x] Verification criteria form a complete set that covers all Commitments and have no hidden procedure or scope.
- [x] This specification is self-contained so a fresh session can draft and execute the actionable companion plan without reconstructing original session context.
- [x] No unresolved placeholders, plan-affecting decisions, missing sections, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
