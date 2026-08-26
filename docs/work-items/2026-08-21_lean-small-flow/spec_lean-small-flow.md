# Lean/Small Flow Spec

Work ID: `2026-08-21_lean-small-flow`
Short ID: `lean-small-flow`
Status: Approved
Harness release: `0.9+ development`
Schema: `schema:spec.small-medium`
Companion plan: `plan_lean-small-flow.md`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `rule:lifecycle.documentation-assessment`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.work-item-architecture-decisions`, `rule:naming.derived-patterns`, `rule:quality.spec-handoff`

## Goal

Add a `lean/small` planning route for bounded, low-risk work. It must retain the current draft-review, approval, approval-commit, and pause-before-implementation gates while loading and producing substantially less material than the existing small/medium route.

## Source and intent

The operator identified excess formality, rigidity, and context cost for not-very-large work. The route must be selectable by work-size decision or explicit operation override; it must not load the model policy, role examples, artifact style, or implementation changelog during lean planning and freeze. It must use new compact source assemblies and generated templates, not conditional variants of the current small/medium templates.

## Scope boundary

### In scope

- Add the additive user-facing flow label `lean/small`; use `lean-small` in paths, schemas, manifests, and stable identifiers.
- Define automatic eligibility and an explicit operator override, with escalation to the existing small/medium or large/phased routes before freeze when the lean boundary no longer fits.
- Add compact spec and plan assemblies, generated templates, and dedicated lean blocks. Omit model strategy, sub-agent assessment, style cues, implementation handoff, and changelog instructions.
- Add a lean freeze/transition exception that keeps the current approval mechanics but does not require model-policy notation. After freeze, the same operator manually orchestrates execution or gives explicit execution-orchestration instructions; no new operator or session is implied.
- Move the detailed large-only layout and `rule:lifecycle.large-anchor-spec` / `rule:lifecycle.large-phase-orchestration` to a new large-only lifecycle reference without changing rule IDs or large-flow behavior.
- Defer the implementation changelog reference until a lean implementation commit is imminent.
- Update explicit, additive validator coverage and relevant operator-facing guidance. Do not refactor the validator into a flow registry in this work item.

### Non-scope

- Rename the established `small/medium` or `large/phased` flows, their filenames, schemas, source blocks, or existing route labels.
- Rewrite historical work items, release notes, changelog history, or frozen artifacts.
- Change the approval, immutable-snapshot, variance, or fresh post-freeze authorization rules.
- Change existing small/medium or large flow requirements beyond relocating large-only policy and any no-behavior-change references needed by that relocation.

## Repository context and constraints

- `SKILL.md` currently routes small/medium planning through lifecycle, naming, quality, and models; its templates include `spec.085.small.handoff.md` and `plan.055.common.model-strategy.md`.
- `planning-freeze-gates.md` currently requires model and sub-agent selection during draft review and approval. A lean exception must be explicit there; template omission alone is not sufficient.
- `artifact-contract.md` currently contains the large-only rule owners and detailed large layout, so small/medium planning pays that context cost.
- `assemble_templates.py` has an explicit assembly list. `test_harness_policy.py` uses explicit path lists and route assertions; preserve its current small/medium and large assertions.
- The repository's current `economy-default` policy applies to planning this work item. The lean/small route itself intentionally leaves model and orchestration choice to the operator.

## Commitments and verification

### `SPEC-001` Add a bounded lean/small lifecycle route

Statement:

1. The harness must classify eligible bounded, low-risk, one-session work as `lean/small`, allow an explicit operator override, and require escalation before freeze when material architecture, interface, migration, security, or uncertainty makes the route unsuitable.

#### `VER-001` Lean lifecycle routing

Covers: `SPEC-001`.

Criterion: Lifecycle and router validation demonstrate both the automatic decision and explicit override, preserve the existing medium and large choices, and state the escalation boundary.

Expected evidence: Updated lifecycle/router text and focused validator scenarios pass.

### `SPEC-002` Keep lean planning and freeze context independent of model policy

Statement:

1. The lean/small drafting and freeze route must not require or load `subagent-model-policy.md`, `subagent-role-examples.md`, `artifact-style.md`, or `implementation-changelog.md`; its templates must not contain model/sub-agent strategy, style-loading, implementation-handoff, or changelog prompts.

#### `VER-002` Lean exclusion contract

Covers: `SPEC-002`.

Criterion: Generated lean templates, router requirements, and targeted negative validator assertions prove the excluded policy and template surfaces are absent while the common quality and freeze checks remain present.

Expected evidence: Template assembly freshness and the full harness validator pass.

### `SPEC-003` Provide compact, isolated lean assemblies

Statement:

1. The harness must provide two new lean-small assemblies and generated templates built only from dedicated lean blocks, with compact metadata, scope/decisions/risks, stable commitment-verification-task-check links, validation, approval, and freeze-ready state.

#### `VER-003` Lean template structure

Covers: `SPEC-003`.

Criterion: Each manifest assembles its declared direct blocks, the generated files are current, and validator assertions confirm the required compact sections and IDs.

Expected evidence: `assemble_templates.py --check` and the policy validator pass.

### `SPEC-004` Isolate large-only lifecycle policy from non-large routes

Statement:

1. The detailed large layout and the existing `rule:lifecycle.large-anchor-spec` and `rule:lifecycle.large-phase-orchestration` owners must move to a new large-only lifecycle reference while preserving their IDs, callers, behavior, and validator coverage.

#### `VER-004` Large-policy relocation

Covers: `SPEC-004`.

Criterion: The lifecycle core no longer contains the moved large-only details, large router/template callers reference the new owner, and focused policy checks preserve the rule-owner graph and large-flow scenarios.

Expected evidence: Search inspection, template assembly freshness, and full policy-validator success.

### `SPEC-005` Preserve established flows and historical records

Statement:

1. The implementation must leave current small/medium and large/phased behavior intact, use additive validator coverage instead of a flow-registry refactor, and leave historical artifacts unchanged.

#### `VER-005` Compatibility preservation

Covers: `SPEC-005`.

Criterion: Existing flow assertions remain present, new lean assertions are additive, and the implementation diff contains no historical work-item or release-history edits.

Expected evidence: Validator success, targeted search, `git diff --check`, and name-only diff review.

## Architecture decisions

Architecture snapshot status: `Required — snapshots/architecture.snapshot.md`.

Decision summary:

- Drivers: reduce routine planning context and artifact bloat without weakening review/freeze safeguards.
- Constraints: lean planning must not transitively require model policy; existing flows are compatibility-sensitive; historical records are immutable.
- Selected approach: add isolated lean assets and a route-specific policy branch; split large-only lifecycle material from the core; retain stable existing rule IDs.
- Affected boundaries: skill router, lifecycle/freeze/execution policy, template assembler, validator, and operator guidance.
- Rejected alternatives: conditional shared blocks; a template-only change; renaming all flows now; validator flow-registry refactor in the same change.
- Validation cues: `VER-001` through `VER-005` and the durable test-case snapshot.

## Impact surfaces

### Interfaces

- `SKILL.md` operation labels and required-reference routing.
- Template assembly manifests, generated template paths, schemas, and block contracts.
- Validator route topology and negative-reference assertions.

### State and control flow

- Work-size classification gains a `lean/small` branch and an escalation path.
- Freeze/transition routing gains a lean exception with the existing review/approval/commit/pause sequence but no frozen model strategy.
- Lean execution delays implementation-changelog loading until an implementation commit is imminent.

### Safety, migration, and rollback

- No runtime data, security boundary, migration, or destructive action changes.
- The change is additive; removing the lean router row and assets restores prior route selection if a later rollback is needed.

## Risks and rejected alternatives

### `RISK-001` Template-only simplification leaves hidden model-policy load

Decision or mitigation:

1. Add explicit lifecycle, freeze, and execution-route branches and validator assertions; do not treat omitted headings as a routing guarantee.

### `RISK-002` Lean route becomes an unsafe shortcut

Decision or mitigation:

1. Make automatic eligibility conservative, require an explicit escalation trigger before freeze, and retain all existing approval and variance controls.

### `RISK-003` Compatibility churn expands beyond the outcome

Decision or mitigation:

1. Use additive `lean/small` labels and assets only. Defer terminology migration and do not touch historical artifacts.

### `RISK-004` New templates drift from their assemblies or policy

Decision or mitigation:

1. Extend the explicit assembler list and policy validator with lean-specific required and forbidden assertions; run full validation after generation.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `docs: lean-small-flow-plan -- approve compact harness route` |
| Implementation | `feat: lean-small-flow -- add compact harness route` |

## Documentation assessment

- `DOC-TEST-CASE`: `Required — snapshots/test-cases.snapshot.md; Plan Task: TASK-004`.
- `DOC-TEST-GUIDE`: `Not required`.
- `DOC-OPS-GUIDE`: `Required — README.md and .agents/skills/dev-doc-harness/docs/operator-note.md; Plan Task: TASK-004`.
- `DOC-API-GUIDE`: `Not required`.
- `DOC-ARCH-SUMMARY`: `Not required — work-item architecture is preserved in the required snapshot; no repository-level architecture document is introduced`.

## Planning shape and transition ownership

1. Planning shape: `combined small/medium`.
2. Companion plan: `plan_lean-small-flow.md` is drafted and reviewed with this specification.
3. Transition owner: `plan_lean-small-flow.md` owns the `plan execution` transition after freeze.
4. Next lifecycle stage: `plan execution`.

## Spec readiness checklist

- [x] Goal, scope, decisions, commitments, risks, and verification criteria are mutually consistent.
- [x] Material operator direction, including deferred renaming and historical-artifact preservation, is captured.
- [x] Commitments are bounded and every commitment has local verification evidence.
- [x] Architecture snapshot and documentation outputs have explicit statuses and owners.
- [x] No unresolved planning decision blocks implementation planning.

## Approval

- Status: Approved
- Superseded by: None
