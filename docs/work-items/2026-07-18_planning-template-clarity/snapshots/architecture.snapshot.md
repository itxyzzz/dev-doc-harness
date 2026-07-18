# Planning Template Clarity Architecture Snapshot

Work ID: `2026-07-18_planning-template-clarity`
Short ID: `planning-template-clarity`
Status: Approved
Harness release: `0.7+`
Schema: `schema:snapshot.architecture`
Policy references: `module:lifecycle`, `module:models`, `module:quality`, `module:freeze-gate`, `rule:lifecycle.work-item-architecture-decisions`, `rule:lifecycle.immutable-snapshots`, `rule:lifecycle.variance-policy`, `rule:quality.spec-handoff`

## Purpose

Freeze the ownership and transition decisions that the fresh implementation task must preserve while clarifying current harness policy and template surfaces.

## Decision Ledger

### `DEC-001` Separate runtime observations from execution selection

Selected approach:

1. Record planning-task model, profile, reasoning, and context observations separately from the approved execution selection.
2. Permit `not exposed` only for observations and actual runtime results that the operator or platform does not expose.
3. Require the approved execution selection to state an actionable target model/profile or policy-relative selection instruction, capability tier, reasoning effort, orchestration mode, fallback, continuity, and rehydration requirement.
4. Prefer a fresh curated-artifact task for substantial work when the intended model changes or current suitability cannot be verified; retain same-task continuation when suitability is known or a concrete continuity reason is recorded.
5. At every transition into spec drafting, plan or phase-plan drafting, amendment or replanning, implementation, or consequential review, assess bounded sub-agent value. Ask the operator to authorize a useful unapproved strategy; otherwise record a stage-specific no-use reason.

Affected boundaries:

1. Repositories: this repository only.
2. Components or modules: `module:models`, `module:freeze-gate`, `module:execution-quality`, shared plan strategy source block, large-spec strategy source block, and their generated templates.
3. Interfaces, schemas, config, or infra: `schema:plan.small-medium`, `schema:plan.phase`, and `schema:spec.large-phased` recording prompts; no runtime config or infrastructure.
4. Agentic, process, documentation, or phase boundaries: planning-stage startup, planning-to-execution handoff, fresh-task startup, sub-agent authorization, and consequential review.

Source spec sections:

1. `SPEC-004`, `SPEC-008`, `RISK-001`, `RISK-002`, and `RISK-006`.

Validation cues:

1. `VER-004`, `VER-008`, `CHECK-001`, `CHECK-002`, and `CHECK-004`.

Rejected alternatives:

1. Keep one mixed list and rely on authors to infer which fields are observations.
2. Allow the recommended execution model or effort to be `not exposed`.
3. Require a fresh task unconditionally even when the current profile is known and suitable.
4. Treat an ambient no-dispatch default or operator silence as a substitute for assessing delegation value.

### `DEC-002` Give each transition one owner and use rolling phase planning

Selected approach:

1. The plan owns the implementation transition for a combined small/medium package; the spec records planning shape and ownership only.
2. An explicitly staged spec-only package owns only its plan-drafting transition until a later plan freezes.
3. Large/phased work normally loops through one phase plan and one phase implementation at a time, using actual prior-phase outputs as inputs to the next plan.
4. A phase plan records both its current-phase implementation handoff and the expected post-phase transition; the implementation completion report supplies the actual values.

Affected boundaries:

1. Repositories: this repository only.
2. Components or modules: lifecycle and freeze policy, small-spec and large-spec handoff blocks, small-plan and phase-plan handoff blocks, phase documentation/handoff block, assemblies, generated templates, README flow, and scenario validation.
3. Interfaces, schemas, config, or infra: small/medium planning shape, large/phased state sequence, and execution-thread startup inputs.
4. Agentic, process, documentation, or phase boundaries: combined freeze, staged planning, phase-plan freeze, phase implementation completion, and next-phase planning.

Source spec sections:

1. `SPEC-005`, `SPEC-006`, and `RISK-003`.

Validation cues:

1. `VER-005`, `VER-006`, `CHECK-001`, `CHECK-002`, and `CHECK-003`.

Rejected alternatives:

1. Keep the complete handoff in both small spec and plan.
2. Leave a generic conditional handoff heading in every plan without naming its actual transition.
3. Draft all phase plans by default before any phase implementation.
4. Remove operator approval gates or automatically create and start the next task.

### `DEC-003` Keep policy concise and templates structural

Selected approach:

1. Canonical owners define Superpowers precedence, commitment structure, commit granularity, model semantics, and lifecycle transitions once.
2. Templates record work-item decisions with compact prompts: no commitment-classification taxonomy, no duplicate changelog-title field, and no policy essays.
3. Superpowers execution metadata appears in the actual plan metadata and its task/commit defaults apply only when compatible with the approved harness plan.
4. Structural validation protects ownership, field presence or absence, source/generated consistency, and explicit route wording without evaluating subjective model fit or commit quality.

Affected boundaries:

1. Repositories: this repository only.
2. Components or modules: lifecycle, quality, model, freeze, execution-quality, artifact-style, router, templates, assembly manifests, generated outputs, and validator.
3. Interfaces, schemas, config, or infra: current planning schemas and validation output; no runtime interface.
4. Agentic, process, documentation, or phase boundaries: Superpowers-to-harness execution boundary, template authoring, commit planning, and planning-package review.

Source spec sections:

1. `SPEC-001`, `SPEC-002`, `SPEC-003`, `SPEC-007`, `RISK-004`, and `RISK-005`.

Validation cues:

1. `VER-001`, `VER-002`, `VER-003`, `VER-007`, and all Plan Checks.

Rejected alternatives:

1. Add a new policy module or commitment taxonomy.
2. Copy expanded Superpowers workflows into the harness.
3. Treat every plan task as a mandatory commit boundary.
4. Build a semantic validator for operator judgment.

## Decision Drivers

1. The operator wants a simple, clear harness that does not make hidden runtime claims or require manual reconstruction of routine lifecycle transitions.
2. Current template duplication and mixed field semantics can produce structurally valid but operationally confusing artifacts.
3. Fresh implementation will use a different, intentionally selected balanced-tier profile, so the handoff must remain usable without chat history.
4. Existing canonical ownership and source-block assembly are sound and should be refined rather than replaced.
5. Operator approval should unlock a useful bounded strategy without repeated negotiation, while higher-priority runtime and safety limits remain authoritative.

## Constraints

1. Preserve current rule IDs and module boundaries unless a new independent ownership concern is unavoidable.
2. Preserve the harness freeze gate, operator approval, immutable historical artifacts, changelog-before-commit rule, and orchestration-owned integration.
3. Do not infer remaining context or silently substitute model tier, effort, orchestration, write scope, concurrency, or task creation.
4. Update generated templates only through their source blocks and manifests.
5. Do not dispatch a useful proposed sub-agent until the operator authorizes its recorded scope when approval is required; do not ask again for an approved in-envelope dispatch.

## Future Durable-Doc Boundary

No repository-level architecture document is required. This snapshot is sufficient for the work item, and no `deltas/architecture-summary.delta.md` file will be created.

## Approval

- Status: Approved
- Superseded by: None
