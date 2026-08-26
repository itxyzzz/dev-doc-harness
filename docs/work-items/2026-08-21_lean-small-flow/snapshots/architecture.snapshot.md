# Lean/Small Flow Architecture Snapshot

Work ID: `2026-08-21_lean-small-flow`
Short ID: `lean-small-flow`
Status: Approved
Harness release: `0.9+ development`
Schema: `schema:snapshot.architecture`
Policy references: `module:lifecycle`, `module:quality`, `rule:lifecycle.work-item-architecture-decisions`, `rule:lifecycle.immutable-snapshots`, `rule:lifecycle.variance-policy`, `rule:quality.spec-handoff`

## Purpose

Preserve the routing and policy-ownership boundaries needed to add lean/small work-item planning without changing established flow behavior.

## Decision ledger

### `DEC-001` Isolate lean/small policy and assets

Selected approach:

1. Add a distinct `lean/small` router path, dedicated lean source blocks, two manifests, and two generated templates.
2. Keep existing small/medium templates and source blocks untouched; a conditional-template branch would retain unwanted prompts and create regression risk.

Affected boundaries:

1. Repositories: `D:/Code/dev-doc-harness`.
2. Components or modules: skill router, lifecycle/freeze/execution references, assembler, and policy validator.
3. Interfaces, schemas, config, or infra: `schema:spec.lean-small`, `schema:plan.lean-small`, assembly manifests, and router labels.
4. Agentic, process, documentation, or phase boundaries: lean packages retain the approval/freeze sequence but do not freeze orchestration/model strategy.

Source spec sections:

1. `SPEC-001`, `SPEC-002`, `SPEC-003` in `spec_lean-small-flow.md`.

Validation cues:

1. `VER-001` through `VER-003`, template assembly freshness, and targeted negative validator assertions.

Rejected alternatives:

1. Conditional reuse of current small/medium blocks — rejected because omitted semantics can remain in generated output and shared-block changes would risk established flows.

### `DEC-002` Split large-only lifecycle details from the core

Selected approach:

1. Move the detailed large layout and the bodies of the two existing large rule IDs to `references/large-phased-lifecycle.md`.
2. Retain the IDs and leave a concise dispatch in the core lifecycle reference.

Affected boundaries:

1. Components or modules: `artifact-contract.md`, new large lifecycle reference, router, large templates, maintenance architecture, and validator rule-owner assertions.
2. Agentic/process boundaries: small/medium and lean planning no longer need to load detailed large-flow guidance.

Source spec sections:

1. `SPEC-004`, `SPEC-005` in `spec_lean-small-flow.md`.

Validation cues:

1. `VER-004`, `VER-005`, full validator, and name-only diff review.

Rejected alternatives:

1. Rename the rule IDs during extraction — rejected because it increases compatibility and validator risk without reducing context further.

## Decision drivers

1. Reduce planning artifact and reference load for bounded work.
2. Preserve approval safety and existing route compatibility.
3. Avoid a broad terminology migration or historical-document rewrite.

## Constraints

1. Lean/small must not require or load the model policy, role examples, artifact style, or implementation changelog while drafting or freezing.
2. Existing small/medium and large/phased behavior must be preserved.
3. Historical documents are immutable and outside this work item's change scope.

## Future durable-doc boundary

No repository-level architecture documentation change is required.

## Approval

- Status: Approved
- Superseded by: None
