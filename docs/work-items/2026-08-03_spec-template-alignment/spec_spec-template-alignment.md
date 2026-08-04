# Spec Template Alignment Spec

Work ID: `2026-08-03_spec-template-alignment`
Short ID: `spec-template-alignment`
Status: Approved
Harness release: `0.8+`
Schema: `schema:spec.small-medium`
Companion plan: `plan_spec-template-alignment.md`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:architecture`, `rule:lifecycle.planning-shape`, `rule:lifecycle.large-phase-orchestration`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

## Goal

Make the assembled small/medium and large/phased specification templates more concise, internally consistent, and easier to use for planning, while retaining their existing lifecycle and large-anchor-specific behavior.

## Source and Intent

Source input:

1. Operator review of the current small/medium specification template and ten recent small/medium specs.
2. Operator-approved design decisions from this task: preserve the default small planning-shape block; compress only its staged spec-only exception; retain the documentation artifact matrix; move one Assumptions and Open Questions section after repository context; rename and compact the shared impact section; and make only conservative large-anchor changes.

Desired operator/user outcome:

1. Template authors edit source blocks, then regenerate the published flat templates through the existing assembly command.
2. Small specs retain their normal combined-plan transition, and large anchors retain their distinct phase-planning, model, and operational content without redundant prose.

Success summary:

1. The two assembled spec templates express the agreed section order and impact-surface terminology, the small staged exception contains only its essential lifecycle facts, and the large template resolves identified flow and routing inconsistencies.
2. The policy validator protects the revised staged-exception and large-anchor contracts, and assembly freshness plus full harness validation pass.

## Scope Boundary

### In scope

1. Edit only the current specification-template source blocks, their published assembled outputs, and directly affected structural assertions in `scripts/test_harness_policy.py`.
2. Move the shared prompts after Repository Context into one `## Assumptions and Open Questions` section, with `### Assumptions` and `### Open questions` subsections.
3. Rename the shared interface/data/control-flow section to `Impact Surfaces` and use the operator-approved compact prompt plus its four specified assessment subsections.
4. Preserve the default small planning-shape block; reduce the explicit staged spec-only exception to the staging reason, frozen package, and `plan drafting` next lifecycle stage.
5. Replace the small readiness checklist with the agreed six consistency, evidence-preservation, and fresh-session checks.
6. Apply the approved conservative large-anchor changes: top-level operations heading; one owner for rolling/batch prose; conditional freeze-gate loading; precise anchor-to-phase boundary; and a concise but large-specific readiness checklist.
7. Regenerate `small-medium-work-item-spec.md` and `large-phased-work-item-spec.md` from their manifests and run the relevant validation.

### Non-scope

1. Changing `artifact-contract.md` or the documentation artifact matrix schema.
2. Changing the small/medium plan, large phase-plan, amendment, or architecture-snapshot template schema.
3. Changing lifecycle-stage meanings, freeze-gate mechanics, model-policy semantics, or the selected `economy-default` policy.
4. Rewriting frozen historical work-item artifacts.
5. Creating an architecture snapshot for this work item; the implementation follows the established block/manifest/assembly design and introduces no new architectural boundary.

## Repository Context

### Current state

1. The two published spec templates are generated from ordered source blocks and manifests by `scripts/assemble_templates.py`.
2. `spec.020.common.intent-scope-context.md` is shared by the small and large spec manifests, and currently places Assumptions and Open questions under Scope Boundary.
3. `spec.040.common.interfaces-risks.md` is shared by the two spec manifests and currently emits `## Interfaces, Data, and Control Flow`.
4. Small-only handoff and readiness blocks are distinct from the large anchor's phase-decomposition/model, operations, freeze, handoff, and readiness blocks.
5. `scripts/test_harness_policy.py` currently validates a full Next-stage recommendation in the staged small-spec source, even though the agreed small staged exception will no longer render one.

### Evidence read

1. `AGENTS.md` and `.agents/skills/dev-doc-harness/SKILL.md`.
2. `.agents/skills/dev-doc-harness/references/artifact-contract.md`, `durable-planning-quality.md`, `naming-conventions.md`, `maintenance-architecture.md`, and `subagent-model-policy.md`.
3. The small/medium and large/phased assembled spec templates, their manifests, and blocks `spec.010`, `spec.020`, `spec.040`, `spec.050`, `spec.060`, `spec.070`, `spec.085`, and `spec.090` relevant to this change.
4. `.agents/skills/dev-doc-harness/scripts/assemble_templates.py` and focused `scripts/test_harness_policy.py` assertions for staged and large-anchor next-stage contracts.
5. Ten recently modified `schema:spec.small-medium` work-item specs dated 2026-07-27 through 2026-08-02, plus the available historical large/phased spec.

### Constraints and compatibility

1. Source blocks and manifests are the maintainer-facing source of truth; assembled flat templates must be regenerated, not hand-edited.
2. Published template paths and schema identifiers remain stable.
3. The default small planning-shape block remains present. Only the explicitly staged spec-only exception loses its embedded Next-stage recommendation.
4. The large anchor's `Next-stage recommendation`, phase decomposition, anchor-to-phase transition, and operations content remain present because they are distinct from the small staged exception.
5. Validator changes must protect the revised contract without relaxing unrelated model-policy, transition, assembly-freshness, or large-anchor checks.
6. Historical artifacts are immutable snapshots and are evidence only, not current template-policy owners.

## Assumptions and Open Questions

### Assumptions

1. The existing assembler writes only generated flat templates from ordered manifests and can regenerate the two impacted outputs without manifest changes.
2. The work remains small/medium: all implementation targets are related template blocks and one structural validator, with a bounded validation surface.
3. `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` remains the required regeneration command and runs the harness validator after writing.

### Open questions

None identified after repository-context review. The operator approved each intended template and large-anchor change.

## Commitments and verification

### `SPEC-001` Align shared section order and impact-surface prompts

Statement:

1. The shared source blocks must place one `## Assumptions and Open Questions` section after Repository Context, with `### Assumptions` and `### Open questions` subsections, and must render the agreed compact `## Impact Surfaces` prompt with its four assessment subsections.

#### `VER-001` Shared spec structure is regenerated consistently

Covers: `SPEC-001`.

Criterion: Both assembled specification templates contain the revised section order and Impact Surfaces content, while the source blocks remain their sole shared source.

Expected evidence: Source-block inspection, `assemble_templates.py --check`, and focused heading searches in the two assembled templates.

### `SPEC-002` Simplify small-spec handoff and readiness without changing the default transition

Statement:

1. The small specification template must retain its default combined-package planning-shape and plan-execution transition.
2. Its explicit staged spec-only exception must record only the staging reason, frozen package, and `plan drafting` next lifecycle stage; it must not render a Next-stage recommendation.
3. Its readiness checklist must contain the six operator-approved checks for consistency, operator-input preservation, commitment coverage, verification coverage, fresh-session planning, and unresolved decisions.

#### `VER-002` Small staged and default paths remain distinct

Covers: `SPEC-002`.

Criterion: The generated small spec shows the unchanged default path, the compressed staged exception, and the agreed readiness checklist; validator assertions reject a return of the staged recommendation while retaining default transition protection.

Expected evidence: Source and generated-template review plus focused `test_harness_policy.py` checks.

### `SPEC-003` Preserve large-anchor distinctions while improving its flow and routing

Statement:

1. The large spec must retain its Model and Sub-agent Strategy and `Next-stage recommendation` for `phase-plan drafting`.
2. Triage, debugging, and operations must be a top-level section.
3. Rolling and batch-planning guidance must have one template owner in Anchor-to-phase transition.
4. The freeze-gate section and policy references must defer freeze-gate loading until draft review or approval.
5. Anchor-to-phase wording must distinguish its `phase-plan drafting` selection from later phase-plan phase-execution handoffs.

#### `VER-003` Large anchor remains complete and internally consistent

Covers: `SPEC-003`.

Criterion: The assembled large spec preserves each large-only section and its next-stage contract, contains no duplicate rolling/batch prose in Planned commits, and accurately assigns later execution-handoff details to phase plans.

Expected evidence: Block/assembled-template inspection and full harness-policy validation.

### `SPEC-004` Keep validator coverage aligned with the revised template contracts

Statement:

1. The policy validator must validate the compressed staged small-spec exception directly instead of treating it as a governed full Next-stage recommendation.
2. It must retain existing large-anchor next-stage, rolling/batch, and assembly-freshness protections, updating assertions only where wording or ownership changes.

#### `VER-004` Validation detects stale or incompatible template contracts

Covers: `SPEC-004`.

Criterion: The focused validator logic accepts the generated revised templates and retains failure cases for missing or malformed large-anchor contracts and incompatible staged-small content.

Expected evidence: `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` exits 0 after implementation; a code review identifies targeted rather than broad validator changes.

## Cross-cutting verification

### `VER-005` Generated template integrity

Covers: `SPEC-001`, `SPEC-002`, `SPEC-003`, `SPEC-004`.

Criterion: Generated templates match their manifests and source blocks, have no whitespace errors, and preserve their existing schemas and published paths.

Expected evidence: `assemble_templates.py --check`, full policy validation, and `git diff --check`.

## Architecture Decisions

Architecture snapshot status: `Not applicable` because this work applies the established source-block, manifest, assembly, and validator architecture without introducing a new component, interface, data model, or lifecycle boundary.

Decision summary:

1. Drivers: concise planning artifacts, fresh-session usability, source-block ownership, and large-anchor safety.
2. Constraints: preserve schemas, generated outputs, current router behavior, and unique large-anchor lifecycle content.
3. Selected approach: edit only authoritative blocks and the affected validator contracts, then regenerate the two published spec templates.
4. Affected boundaries: shared spec blocks, small-only handoff/readiness blocks, large-only anchor blocks, generated spec templates, and the structural policy validator.
5. Rejected alternatives: edit flat templates directly; copy the small staged-exception simplification into the large anchor; change the documentation matrix in the same work item; perform broader lifecycle or model-policy restructuring.
6. Validation cues: assembly freshness, full harness-policy validation, focused generated-template searches, and whitespace validation.

## Impact Surfaces

### Interfaces

1. Maintainer authoring interface: the named source-block prompts, published assembled-template headings, and validator-enforced text contracts change.
2. Published template paths and schema identifiers remain unchanged.

### Data, config, and persistence

None. The work changes Markdown templates and a Python structural validator only; no runtime data, persistence, or application configuration is affected.

### State and control flow

1. Maintainer flow remains edit blocks → assemble templates → validate.
2. Draft large-anchor authoring no longer treats freeze-gate guidance as an immediate route dependency; freeze-gate loading remains required when a package reaches review or approval.

### Safety, security, privacy, migration, and rollback

1. No product security, privacy, compliance, migration, or destructive-operation impact is expected.
2. Process-safety risk is a stale or weakened generated template; assembly freshness and the full policy validator mitigate it.
3. Rollback is a cohesive revert of the implementation commit; frozen historical work items are not edited.

## Risks and Rejected Alternatives

### `RISK-001` Shared-block edit unintentionally changes both specifications

Decision or mitigation:

1. Review both generated outputs after changing `spec.020.common.intent-scope-context.md` and `spec.040.common.interfaces-risks.md`; use focused heading/order checks before accepting the assembly result.

### `RISK-002` Simplifying the staged exception weakens the default small path

Decision or mitigation:

1. Retain the default planning-shape block verbatim in intent, keep the existing default transition assertion, and update validator logic only for the staged exception source.

### `RISK-003` Large-anchor cleanup removes phase-specific planning information

Decision or mitigation:

1. Limit large changes to heading level, duplicate ownership, route timing, boundary wording, and readiness consolidation; retain Model and Sub-agent Strategy, phase decomposition, anchor-to-phase transition, operations, and large next-stage recommendation.

### `RISK-004` Validator changes conceal a regression

Decision or mitigation:

1. Replace the obsolete staged full-summary assertion with positive compact staged-path checks and negative checks for the retired summary, while preserving unrelated large-anchor and assembly checks.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: spec-template-alignment -- approve spec template cleanup` |
| Implementation | `docs: spec-template-alignment -- align assembled spec templates` |

One cohesive implementation commit is planned because source-block wording, generated templates, and structural validator assertions form one reviewable template contract.

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Implementation changelog source | Living | Yes | During implementation | `docs/work-items/2026-08-03_spec-template-alignment/changelog/implementation-fragment.md` | Create only after fresh execution authorization; planning approval creates no fragment. |
| Root changelog consolidation | Living | Yes | Planning freeze and implementation commit | `CHANGELOG.md` | The repository gate requires a planning entry before the planning approval commit; record the implementation entry before the implementation commit. |
| Test cases | Snapshot | No | N/A | Not created | Deterministic assembly and policy-validator checks provide the required evidence. |
| Testing guide delta | Living delta | No | N/A | Not created | No operator test-flow change. |
| Operator manual delta | Living delta | No | N/A | Not created | No runtime or operator-facing workflow change beyond template authoring prompts. |
| API reference delta | Living delta | No | N/A | Not created | No public API. |
| Architecture snapshot | Snapshot | No | N/A | Not created | No new work-item architecture decision. |
| Architecture summary delta | Living delta | No | N/A | Not created | No long-lived architecture document change. |

## Planning shape and transition ownership

1. Planning shape: `combined small/medium`.
2. Companion plan: `plan_spec-template-alignment.md` is drafted and presented with this spec in the same planning turn.
3. Transition owner: `plan_spec-template-alignment.md` owns the `plan execution` transition after the combined package freezes.
4. Next lifecycle stage: `plan execution`.

## Spec readiness checklist

- [x] Goal, source and intent, scope, constraints, architecture decisions, commitment statements, and verifications are mutually consistent.
- [x] All relevant operator input is preserved in this specification or through `module:evidence` and `rule:evidence.preservation`.
- [x] Commitment statements are atomic, bounded, and form a complete set that covers the full scope and achieves the goal; no obligation exists only in rationale or examples.
- [x] Verification criteria form a complete set that covers all Commitments and have no hidden procedure or scope.
- [x] This specification file with `snapshots/architecture.snapshot.md` is self-contained so a fresh session can draft the actionable plan without reconstructing original session context.
- [x] No unresolved placeholders, plan-affecting decisions, missing sections, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
