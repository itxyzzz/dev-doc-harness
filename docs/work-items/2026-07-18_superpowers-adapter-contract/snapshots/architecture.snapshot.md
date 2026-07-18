# Architecture Snapshot: Superpowers Adapter Contract

Work ID: `2026-07-18_superpowers-adapter-contract`
Short ID: `superpowers-adapter-contract`
Status: Approved
Harness release: `0.7+`
Schema: `schema:snapshot.architecture`
Policy references: `module:lifecycle`, `module:quality`, `module:models`, `rule:lifecycle.work-item-architecture-decisions`, `rule:lifecycle.immutable-snapshots`, `rule:lifecycle.variance-policy`, `rule:quality.spec-handoff`

## Purpose

Preserve the coexistence boundary between the Dev Doc Harness and Superpowers so later plan drafting and execution do not recreate duplicate durable artifacts, competing lifecycle gates, or unbounded model-selection rules.

## Decision Ledger

### `DEC-001` Harness owns the durable lifecycle; Superpowers owns in-boundary execution

Selected approach:

1. The harness remains authoritative for durable artifact location, approval and freeze gates, continuity routing, variance, changelog discipline, and final integration.
2. Superpowers operates only after the approved harness continuity route authorizes execution. It may apply task sizing, pre-flight review, explicit per-task dispatch selection, and ephemeral execution aids inside that boundary.
3. Project or global `AGENTS.md` is the durable preference source that overrides Superpowers' default spec and plan locations for harness-managed work.

Affected boundaries:

1. Repositories: `C:\\Work\\Codex\\dev-doc-harness` only.
2. Components or modules: `AGENTS.md`; harness lifecycle, model, execution-quality, and operator guidance; plan-template sources and generated outputs; policy validator.
3. Interfaces, schemas, config, or infra: repository instruction interface to Superpowers; canonical work-item artifact path; plan metadata and model-policy notation.
4. Agentic, process, documentation, or phase boundaries: planning package, freeze gate, same-task or new-task continuity, Superpowers execution, evidence, and final integration.

Source spec sections:

1. `SPEC-001` through `SPEC-006` in `spec_superpowers-adapter-contract.md`.
2. `RISK-001` through `RISK-005` in `spec_superpowers-adapter-contract.md`.

Validation cues:

1. `VER-001` through `VER-006` in `spec_superpowers-adapter-contract.md`.
2. Focused active-surface and generated-template fixtures, template assembly freshness, full harness-policy validation, and policy-boundary review.

Rejected alternatives:

1. Ban Superpowers-specific execution metadata rather than support a conditional merged header.
2. Treat `docs/superpowers` as a second durable source of truth.
3. Copy Superpowers task-sizing or execution-package rules into the harness as permanent durable requirements.
4. Require a named runtime model when Codex does not expose it to the agent.
5. Allow Superpowers to silently inherit a session model or dispatch outside the frozen harness policy envelope.

## Decision Drivers

1. Preserve a reviewable canonical work-item package.
2. Retain Superpowers' useful task sizing, pre-flight, explicit dispatch, and review mechanics.
3. Remove plan-schema duplication and checkbox ambiguity while preserving numbered executable steps.
4. Prevent a gap between a harness model recommendation and Superpowers' actual per-task allocations.
5. Keep the harness usable when Superpowers is unavailable.

## Constraints

1. New durable harness artifacts remain under `docs/work-items/<work-id>/`; the historical-continuity pointer-stub exception remains unchanged.
2. Global constraints are conditional self-containment context, not duplicate specification commitments.
3. Task interfaces describe consumed inputs and produced outputs; dependencies remain ordering or readiness facts.
4. Superpowers execution aids remain ephemeral unless a separate harness evidence rule requires their preservation.
5. `not exposed` is the required runtime-model value unless the platform or operator provides a concrete value.
6. Any material change to lifecycle ownership, artifact canonicality, authorization, concurrency, write authority, or the model-policy envelope requires an amendment and operator approval.

## Future Durable-Doc Boundary

Repository-level durable architecture documents are not needed. This work-item snapshot is the authoritative decision record for the adapter contract; no architecture-summary delta is planned.

## Approval

- Status: Approved
- Superseded by: None
