# Router and Maintenance Architecture Snapshot

Work ID: `2026-08-01_router-maintenance-architecture`
Short ID: `router-maintenance-architecture`
Status: Approved
Harness release: `0.8+`
Schema: `schema:snapshot.architecture`
Policy references: `module:lifecycle`, `module:quality`, `rule:lifecycle.work-item-architecture-decisions`, `rule:lifecycle.immutable-snapshots`, `rule:lifecycle.variance-policy`, `rule:quality.spec-handoff`

## Purpose

Capture the harness loading boundary selected for this work: operational routing is loaded from `SKILL.md`, while the module catalog and validator-architecture constraints are loaded only for maintenance work.

## Decision Ledger

### `DEC-001` Single operational router

Selected approach:

1. Keep the complete operation router exclusively in `.agents/skills/dev-doc-harness/SKILL.md`.
2. Rename the former policy-architecture reference to `references/maintenance-architecture.md` and remove its duplicate router table.

Affected boundaries:

1. Repositories: this repository only.
2. Components or modules: `SKILL.md`, `module:architecture`, canonical-reference catalog, and validator route assertions.
3. Interfaces, schemas, config, or infra: module file path and route-loading contract; no runtime API.
4. Agentic, process, documentation, or phase boundaries: normal harness invocation does not load maintenance architecture unless it is maintaining routes, module ownership, templates, or the policy validator.

Source spec sections:

1. `SPEC-001`, `SPEC-002`, and `RISK-003` in `spec_router-maintenance-architecture.md`.

Validation cues:

1. `VER-001`, `VER-002`, `CHECK-001`, `CHECK-002`, and the full harness validator.

Rejected alternatives:

1. Keep a second router table: rejected because it has already drifted from the live router and creates unnecessary context load.
2. Create a new operational routing reference: rejected because it would add another file to ordinary invocation without eliminating the duplicate source.

### `DEC-002` Just-in-time freeze-gate loading

Selected approach:

1. Normal drafting routes omit `module:freeze-gate` from their required inputs and draft-template policy references.
2. The gate remains the mandatory owner when a package is presented for review, approval, or freeze; it owns the approval commit, pause, and post-freeze transition projection.

Affected boundaries:

1. Repositories: this repository only.
2. Components or modules: operation router, plan and phase-plan source blocks, generated templates, freeze-gate reference, and validator route assertions.
3. Interfaces, schemas, config, or infra: planning artifact metadata and policy-reference declarations; no runtime API.
4. Agentic, process, documentation, or phase boundaries: drafting uses lifecycle, quality, naming, and model policy; review/freeze adds gate mechanics at the actual lifecycle boundary.

Source spec sections:

1. `SPEC-003`, `SPEC-004`, and `RISK-001` in `spec_router-maintenance-architecture.md`.

Validation cues:

1. `VER-003`, `VER-004`, `CHECK-003`, gate-content inspection, template assembly, and full-validator output.

Rejected alternatives:

1. Keep gate citations in draft templates: rejected because they imply that a detailed approval procedure must stay in context during active design work.
2. Copy gate procedure into lifecycle or templates: rejected because it duplicates the gate owner and makes later maintenance drift more likely.

## Decision Drivers

1. Ordinary agents need a compact, correct route to task-specific policy.
2. Maintenance policy needs stable ownership, dependency, and validation constraints without being mistaken for normal task guidance.
3. Approval gates need discoverability and strict enforcement at their lifecycle boundary, not eager loading.

## Constraints

1. `module:architecture` remains a stable retrieval token.
2. `SKILL.md` is the only operational route map after this change.
3. Generated template outputs follow source blocks.
4. Existing freeze behavior and historical artifacts remain unchanged except for current-surface references required by the rename.

## Future Durable-Doc Boundary

This snapshot governs only the frozen work-item decision. A future, separately authorized harness change may adopt a machine-readable generated route manifest if maintenance evidence shows that one router table still cannot remain coherent.

## Approval

- Status: Approved
- Superseded by: None
