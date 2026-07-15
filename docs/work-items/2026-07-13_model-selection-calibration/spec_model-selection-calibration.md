# Model-Selection Calibration Spec

Work ID: `2026-07-13_model-selection-calibration`
Short ID: `model-selection-calibration`
Status: Approved
Harness release: `0.6+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:models.economy-default`, `rule:models.strategy-required`, `rule:models.final-review`, `rule:quality.spec-handoff`

## Goal

Make the active `economy-default` model-selection guidance operationally efficient for the GPT-5.6 Sol, Terra, and Luna mapping while preserving operator authority, policy-relative tiers, and existing authorization boundaries.

## Source and Intent

Source input:

1. The operator requested improved model-selection guidance from the completed research handoff and selected combined small/medium planning on 2026-07-14.
2. `handoff/research-handoff.md` records the agreed compact decision model, likely live policy surfaces, and explicit stop condition.
3. `evidence/model-selection-research.md` preserves external evidence and a local historical calibration; its external claims are supporting context, not a universal policy guarantee.

Desired operator/user outcome:

1. A planner can select, escalate, de-escalate, or independently review a substantial work item under `economy-default` without confusing capability tier, reasoning effort, lifecycle stage, or approval authority.

Success summary:

1. The canonical model policy establishes Terra medium as the suggested bounded-work baseline, gives concise evidence-aware change signals, and keeps the policy small.
2. Role examples, reusable strategy prompts, and policy validation reinforce the canonical rule without creating a duplicate decision system or adding a surface that lacks a distinct enforcement or usability purpose.

## Scope Boundary

### In scope

1. Calibrate the current `economy-default` policy and its escalation rules for the GPT-5.6 Sol, Terra, and Luna mapping.
2. Clarify that effort escalation and capability-tier escalation are distinct decisions, and add lifecycle-aware de-escalation and residual-uncertainty requirements.
3. Refine existing independent-review guidance with a separate task, curated artifacts, a single named review lens, evidence-backed findings, and orchestration-owned integration.
4. Update only the shared model-strategy source blocks, generated templates, advisory role examples, and non-duplicative validator assertions that have a distinct, concrete role in keeping the policy coherent.
5. Create the required work-item architecture, test-case, testing-guide, and operator-manual artifacts.

### Non-scope

1. Changing the active repository policy selector in `AGENTS.md`, permanent tier names, authorization layers, concurrency cap, or platform multi-agent semantics.
2. Mandating a concrete model or reasoning configuration, or removing the operator's override authority.
3. Rewriting `README.md` unless implementation review identifies a concise operator-facing gap that cannot be served by the canonical policy and operator-manual delta.
4. Editing the frozen 2026-07-11 model-selection work item, treating external benchmark values as repository-local measurements, or adding a large model-selection decision tree.

### Assumptions

1. The active repository policy remains `economy-default` unless the operator changes `AGENTS.md`.
2. The current provider mapping remains Sol to `flagship`, Terra to `balanced`, and Luna to `fast/economy` for this implementation; the durable tier vocabulary remains vendor-neutral.
3. The policy validator remains the appropriate enforcement point for structural, non-duplicative policy assertions.
4. The current planning author uses Terra high because the policy surfaces are coupled; this is an authoring-effort selection and does not alter the proposed executor baseline.

### Open questions

1. None identified after repository-context review. Any provider mapping change discovered during implementation is a variance decision, not an inferred policy rewrite.

## Repository Context

### Current state

1. `references/subagent-model-policy.md` separates permanent capability tiers, reasoning effort, orchestration mode, authorization layers, and the active `economy-default` selection policy, but its economy guidance remains broad.
2. `references/subagent-role-examples.md` contains advisory role shapes, while `assets/templates/blocks/plan.040.common.model-strategy.md` and `assets/templates/blocks/spec.060.large.phase-decomposition-model.md` own reusable strategy prompts for generated templates.
3. `scripts/test_harness_policy.py` already protects the tier vocabulary, provider mapping, economy start/escalation signal, and generated-template field shape; `scripts/assemble_templates.py --write` regenerates templates and runs that validator.
4. `README.md` correctly routes model policy to its canonical owner and already warns that templates own field shape rather than reusable semantics.

### Evidence read

1. `AGENTS.md` and `.agents/skills/dev-doc-harness/SKILL.md`.
2. `.agents/skills/dev-doc-harness/references/artifact-contract.md`, `durable-planning-quality.md`, `subagent-model-policy.md`, `subagent-role-examples.md`, and `artifact-style.md`.
3. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`, `small-medium-work-item-plan.md`, source model-strategy blocks, and their assembly manifests.
4. `.agents/skills/dev-doc-harness/scripts/assemble_templates.py` and the `assert_model_selection_dimensions` section of `scripts/test_harness_policy.py`.
5. `docs/work-items/2026-07-13_model-selection-calibration/evidence/model-selection-research.md`, `handoff/research-handoff.md`, and `artifact-index.md`.
6. `docs/work-items/2026-07-11_model-selection-dimensions/` and `docs/work-items/2026-07-13_multi-changelog-fragments/` as historical planning-format context.

### Constraints and compatibility

1. Canonical policy remains concise; reusable detail belongs in `subagent-model-policy.md`, not duplicated in templates, README, or historical artifacts.
2. A frozen spec or plan is lifecycle evidence that should reduce ambiguity; it never substitutes for an explicit unresolved requirement or variance approval.
3. Stronger allocation remains a suggestion subject to the operator-approved strategy, runtime permission, and platform availability.
4. Existing model-selection dimensions, `ultra` classification, fresh-confirmation boundaries, and final-integration ownership must remain compatible.

## Specification Commitments and Local Verification Criteria

### `SPEC-001` Specification Commitment — Calibrate the bounded-work baseline

Kind: `Behavior`

Intent: `Change`

Concerns: `model selection`, `cost and latency`

Statement:

1. Under `economy-default`, the canonical policy shall present Terra medium as the suggested baseline for substantial bounded work with explicit outputs and validation, while preserving policy-relative tier language and operator override authority.
2. The policy shall identify Terra high as an effort increase for fuller dependency or edge-case traversal, Sol medium as a tier increase for unresolved ambiguity, competing interpretations, unclear causal chains, or difficult judgment, and Sol high as an exceptional, written-reason escalation for a high-impact unresolved conflict or evidence gap.

Rationale:

1. The research supports a balanced default with deliberate, limited escalation instead of ceremonial use of stronger configurations.

#### `VER-001` Verification Criterion — The calibrated allocation ladder is explicit and bounded

Covers:

1. `SPEC-001`.

Criterion:

1. The canonical `economy-default` guidance names the Terra-medium baseline, the effort and tier change signals, the exceptional Sol-high condition, and continued operator override authority without changing permanent tier definitions.

Expected evidence:

1. Passing targeted assertions in `test_harness_policy.py` and review of `subagent-model-policy.md`.

### `SPEC-002` Specification Commitment — Make escalation lifecycle-aware

Kind: `Constraint`

Intent: `Establish`

Concerns: `ambiguity`, `variance`, `approval`

Statement:

1. The canonical policy shall distinguish effort escalation, where the task model remains suitable but needs more deliberate traversal, from tier escalation, where capability, ambiguity handling, or judgment is limiting.
2. The canonical policy shall direct later-stage escalation to name the residual uncertainty or newly discovered variance, shall direct bounded remaining work to de-escalate when frozen artifacts, deterministic checks, or a fixed review lens remove ambiguity, and shall treat missing product input, undecided requirements, and plan contradictions as variance or approval problems rather than spending triggers.

Rationale:

1. Completed planning artifacts should narrow work; stronger models cannot legitimately resolve a missing decision or bypass lifecycle controls.

#### `VER-002` Verification Criterion — Escalation is not ceremonial or an approval substitute

Covers:

1. `SPEC-002`.

Criterion:

1. The policy explicitly requires a named residual uncertainty or new variance for later-stage escalation, permits de-escalation after work becomes bounded, and routes missing decisions and contradictions to the existing variance or approval path.

Expected evidence:

1. Passing targeted validator assertions and manual policy review for the stated distinctions.

### `SPEC-003` Specification Commitment — Define efficient independent review

Kind: `Behavior`

Intent: `Change`

Concerns: `review quality`, `context isolation`

Statement:

1. The canonical policy and advisory role examples shall define independent review as a separate task or thread with curated approved artifacts, diff, validation evidence, and a short role prompt; the reviewer shall use one named lens and report evidence-backed findings with severity and a reproduction or validation path.
2. The guidance shall allow an independent reviewer to use a stronger allocation than a clear-plan executor when defect-detection value warrants it, without making that allocation a default or transferring final integration ownership from the orchestration thread.

Rationale:

1. Review quality derives from independent context and a bounded evidence lens, not merely from a higher-capability configuration or duplicated review process.

#### `VER-003` Verification Criterion — Review independence and ownership remain clear

Covers:

1. `SPEC-003`.

Criterion:

1. Current policy and advisory examples state the separate curated-context review shape, defined lens, evidence requirement, permitted asymmetric reviewer allocation, and orchestration-owned final integration without introducing a second reviewer gate.

Expected evidence:

1. Passing targeted validator assertions and review of the changed policy and role-example sections.

### `SPEC-004` Specification Commitment — Keep reusable surfaces aligned without duplication

Kind: `Quality`

Intent: `Maintain`

Concerns: `template ownership`, `policy validation`

Statement:

1. Shared model-strategy source blocks and their generated templates shall prompt planners to record a baseline, distinguish an effort change from a tier change, and name residual uncertainty for a later-stage escalation, while directing reusable semantics to the canonical policy.
2. The policy validator shall protect the calibrated baseline, lifecycle/variance boundary, independent-review essentials, and generated-template freshness without prescribing a universal allocation or duplicating the full policy prose.
3. Each changed supporting surface shall have one distinct purpose: canonical policy defines semantics, advisory examples illustrate a bounded role, templates capture decisions, generated files mirror their sources, and validation protects concrete regression boundaries; no supporting surface shall add a second allocation ladder, new lifecycle gate, or unrelated model-selection feature.

Rationale:

1. A compact canonical rule needs discoverable prompts and focused regression checks, but duplicated decision trees or supporting edits without a distinct role would drift and increase maintenance cost.

#### `VER-004` Verification Criterion — Generated prompts and checks preserve canonical ownership

Covers:

1. `SPEC-004`.

Criterion:

1. Source blocks and all regenerated target templates contain the required compact prompts, template assembly is current, validator assertions pass, and changed supporting surfaces each demonstrate their distinct purpose while README canonical-owner wording remains unchanged.

Expected evidence:

1. Successful `assemble_templates.py --check` and `test_harness_policy.py` output plus a reviewable diff limited to the selected live surfaces.

## Architecture Decisions

Architecture snapshot status:

1. `Required`: the work changes a cross-surface policy ownership boundary between canonical guidance, advisory examples, reusable prompts, and structural validation.

Decision summary:

1. Drivers: make `economy-default` practical after the GPT-5.6 mapping while retaining low ceremony and operator authority.
2. Constraints: permanent tiers, authorization layers, provider-neutral vocabulary, and frozen historical artifacts remain intact.
3. Selected approach: centralize normative allocation and lifecycle semantics in `subagent-model-policy.md`; use role examples, template prompts, and focused validator checks only when each supplies a compact, distinct supporting function.
4. Affected boundaries: canonical policy, advisory examples, source template blocks, generated templates, structural policy validation, and work-item documentation.
5. Rejected alternatives: policy-only change; a broad README rewrite; a duplicated decision tree in templates; a mandatory model configuration.
6. Validation cues: `VER-001` through `VER-004` and `CHECK-001` through `CHECK-004`.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. Harness planning interface: model and sub-agent strategy prompts gain compact calibration cues.
2. Validator interface: existing policy-validation output gains focused assertions; command-line invocation remains unchanged.

### Data, config, and persistence

1. No runtime data model, persistence, migration, release identity, or executable configuration changes.
2. `AGENTS.md` remains the active-policy selector and is not changed by this work item.

### State and control flow

1. Planning selection flow becomes baseline allocation, explicit effort-or-tier decision when changing allocation, lifecycle-aware de-escalation after uncertainty is reduced, or variance/approval routing when a requirement remains undecided.
2. Review flow becomes a curated-artifact independent task with one lens and evidence-backed findings, followed by orchestration-thread integration.

### Safety, security, privacy, migration, and rollback

1. No security, privacy, migration, or destructive-operation impact was identified after repository-context review.
2. Incorrect guidance can cause cost, latency, or quality loss; rollback is a focused revert of the implementation commit, leaving permanent tier and approval controls intact.

## Risks and Rejected Alternatives

### `RISK-001` External calibration is treated as a universal local optimum

Decision or mitigation:

1. Preserve the evidence report as context, frame allocations as suggestions, require operator approval, and keep escalation rationale tied to the concrete task.

### `RISK-002` Templates become a second canonical decision tree

Decision or mitigation:

1. Keep detailed rules only in `subagent-model-policy.md`; source blocks contain short recording prompts and route planners to the canonical module.

### `RISK-003` Stronger models are used to conceal undecided scope

Decision or mitigation:

1. State that missing product input, plan contradictions, and unresolved requirements are variance or approval problems and test for that boundary.

### `RISK-004` Independent review duplicates existing gates or loses ownership

Decision or mitigation:

1. Refine the existing reviewer shape with one defined lens and preserve orchestration-owned integration; do not add a new mandatory review lifecycle.

### `RISK-005` Supporting guidance costs more to maintain than it returns

Decision or mitigation:

1. Apply a just-enough surface test during implementation and independent review: retain a supporting edit only when it has a distinct canonical, illustrative, prompt, generated-output, or regression-protection role that cannot be met by an existing changed surface; otherwise remove it from the diff.

## Planned commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `plan: model-selection-calibration -- approve calibrated economy guidance` | `2026-07-13_model-selection-calibration -- approve calibrated economy guidance` | Approval commit for the combined planning package and source fragment. |
| Implementation | `docs: model-selection-calibration -- calibrate economy model guidance` | `2026-07-13_model-selection-calibration -- calibrate economy model guidance` | Canonical policy, supporting prompts/examples, regenerated templates, validator, and deltas. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source | Living | Yes | Before each commit | `docs/work-items/2026-07-13_model-selection-calibration/changelog/*.md` | Draft planning and implementation entries are prepared; root consolidation remains checkpoint-owned. |
| Root changelog consolidation | Living | No | N/A | `CHANGELOG.md` | Do not edit for the plan-only freeze; consolidation is operator-owned. |
| Test cases | Snapshot | Yes | Before implementation | `snapshots/test-cases.snapshot.md` | Captures policy, prompt, assembly, and ownership cases. |
| Testing guide delta | Living delta | Yes | During implementation | `deltas/testing-guide.delta.md` | Records validation commands and expected signals. |
| Operator manual delta | Living delta | Yes | During implementation | `deltas/operator-manual.delta.md` | Records concise planner and reviewer selection guidance. |
| API reference delta | Living delta | No | N/A | N/A | No public API. |
| Architecture snapshot | Snapshot | Yes | Before implementation | `snapshots/architecture.snapshot.md` | Freezes canonical-owner and supporting-surface boundaries. |
| Architecture summary delta | Living delta | No | N/A | N/A | No repository-level architecture document is introduced. |

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Specification Commitments are atomic, classified, bounded, and contain every implementation obligation in their Statements.
- [x] Verification Criteria have valid Covers sets and expected evidence.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Interfaces, data, control flow, and safety impacts are checked.
- [x] Risks and rejected alternatives are listed.
- [x] Documentation artifact matrix decisions have paths or reasons.
- [x] Planned commit subjects and changelog title snippets are synchronized.
- [x] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
