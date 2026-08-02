# Router and Maintenance Architecture Spec

Work ID: `2026-08-01_router-maintenance-architecture`
Short ID: `router-maintenance-architecture`
Status: Approved
Harness release: `0.8+`
Schema: `schema:spec.small-medium`
Companion plan: `plan_router-maintenance-architecture.md`
Policy references: `module:architecture`, `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:release`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

## Goal

Make `SKILL.md` the harness's sole operational router, isolate maintenance-only architecture guidance, and defer freeze-gate loading until a planning package reaches review or approval.

## Source and Intent

Source input:

1. Operator review comments on the former `references/policy-architecture.md`, including its external work-item provenance, unused content-type rows, duplicated routing table, stale route coverage, and "next activity" wording.
2. Operator decision on 2026-08-01 to keep the sole operational router in `SKILL.md`, rename the architecture reference, retain only used content types without a "Reusable policy source?" column, and defer `module:freeze-gate` until it is used.

Desired operator outcome:

1. Normal harness invocation reads the operation router and only its route-required modules; maintenance guidance, approval-gate mechanics, and duplicated operational summaries do not consume ordinary planning context.

## Scope Boundary

### In scope

1. Rewrite the opening orientation in `.agents/skills/dev-doc-harness/SKILL.md` so work sizing and the operation router are the first normal guidance, and maintenance architecture is linked only from maintenance routes.
2. Rename `references/policy-architecture.md` to `references/maintenance-architecture.md` while retaining `module:architecture` as its stable module ID.
3. Remove the external `docs/work-items/` provenance sentence and delete the duplicate `## Router Inputs` table from the renamed reference.
4. Keep the content-type taxonomy only for `Normative policy`, `Advisory guidance`, and `Example`; remove unused rows and the `Reusable policy source?` column.
5. Reconcile `SKILL.md` operation routes with templates and current policy: normal planning explicitly obtains naming, model/sub-agent, lifecycle, and quality inputs; maintenance and release work remain conditional routes; `module:freeze-gate` remains a separate review/freeze route.
6. Remove draft-time plan-template policy references and instructions that require loading `module:freeze-gate`; keep only the compact draft/frozen presentation state needed by the plan artifact, with approval procedure owned by the gate when invoked.
7. Update structural validator paths, route expectations, and assertions for the rename, the single operational router, the retained taxonomy, and deferred freeze-gate loading.
8. Regenerate template outputs from their source blocks and retain full harness validation coverage.

### Non-scope

1. Changing approval, commit, immutable-snapshot, or post-freeze continuation behavior owned by `planning-freeze-gates.md`.
2. Changing lifecycle meanings, model/sub-agent policy, release-policy semantics, durable planning schema, or the current economy-default policy.
3. Rewriting frozen historical work items solely to reflect the new reference filename or current route model.
4. Introducing a generated manifest or a second operational routing document.

### Assumptions

1. A normal combined small/medium planning package needs naming grammar in addition to lifecycle, quality, and models because it creates work IDs, filenames, planned commits, and changelog headings.
2. The freeze gate's detailed draft-review, approval, commit, and handoff procedure is not required to design a plan; it is required only when the package is presented for review or frozen.
3. The plan's existing current-task and next-stage fields remain useful artifacts; their formal approval-state projection remains gate-owned and is not a reason to load the full gate while drafting.

### Open questions

1. None identified after repository-context review.

## Repository Context

### Current state

1. `SKILL.md` already contains the complete live operation router, while `policy-architecture.md` repeats an incomplete module-only router table.
2. The duplicate table omits several `SKILL.md` routes and lags current execution-model and routing behavior.
3. The policy-architecture opening places a maintenance-oriented reference before normal operational guidance and links to a non-distributable work-item snapshot.
4. The plan templates cite `module:freeze-gate` and freeze rules even though `SKILL.md` defers freezing to its own operation; the gate document itself owns review, approval, commit, pause, and continuation mechanics.
5. `test_harness_policy.py` hard-codes the former reference path in required-file, catalog, discoverability, and maintenance assertions.

### Evidence read

1. `AGENTS.md` and `.agents/skills/dev-doc-harness/SKILL.md`.
2. `.agents/skills/dev-doc-harness/references/policy-architecture.md`, `artifact-contract.md`, `planning-freeze-gates.md`, `subagent-model-policy.md`, `durable-planning-quality.md`, `naming-conventions.md`, and `release-policy.md`.
3. Small/medium and large/phase template source blocks plus generated templates.
4. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
5. Operator review comments and decisions in this Codex task.

### Constraints and compatibility

1. `module:architecture` remains the stable route token so current maintenance references do not need a module-ID migration.
2. Current templates are generated; source blocks are authoritative and generated templates must not be edited independently.
3. A single authoritative operation router must avoid duplicate, independently maintained operation tables.
4. Historical planning artifacts are frozen records and must not be modified solely to remove old filename references.

## Commitments and verification

### `SPEC-001` One operational router

Statement:

1. `SKILL.md` must be the only current operational operation router; its initial orientation must not direct ordinary invocation to maintenance architecture, and the renamed maintenance reference must not contain a duplicate operational routing table.

#### `VER-001` Router ownership evidence

Covers: `SPEC-001`.

Criterion: Current harness surfaces present `SKILL.md` as the sole operational route map and load `module:architecture` only for maintenance operations.

Expected evidence: Focused route inspection, structural validator assertions, and a search confirming the duplicate table and former reference path are absent from current reusable surfaces.

### `SPEC-002` Focused maintenance architecture

Statement:

1. `maintenance-architecture.md` must contain only the used content types—Normative policy, Advisory guidance, and Example—without the "Reusable policy source?" column; it must retain the module catalog, rule-ID conventions, dependency constraints, validation contract, route-budget maintenance constraints, and lifecycle-decomposition guidance needed for harness maintenance.

#### `VER-002` Maintenance reference evidence

Covers: `SPEC-002`.

Criterion: The renamed reference contains no non-distributable work-item provenance, no obsolete content-type rows, and no duplicate router; its catalog remains usable by maintenance routes and validator checks.

Expected evidence: Targeted content assertions, full harness-validator output, and scoped diff review.

### `SPEC-003` Deferred freeze-gate loading

Statement:

1. Drafting routes and draft plan-template policy references must not require `module:freeze-gate` or `rule:freeze.*`; the gate must remain discoverable and mandatory when the planning package enters review, approval, or freeze.

#### `VER-003` Deferred-gate evidence

Covers: `SPEC-003`.

Criterion: A normal plan can be drafted from its explicit planning inputs without opening the gate, while the `Freeze planning packages` route and the gate's package-completeness checks remain intact.

Expected evidence: Route and template-policy-reference assertions, template assembly, gate content inspection, and full harness-validator output.

### `SPEC-004` Validator and generated-template continuity

Statement:

1. The validator, template source blocks, generated templates, and canonical-file lists must be updated atomically so the renamed file and revised route ownership are structurally enforced without weakening current freeze-gate validation.

#### `VER-004` Continuity evidence

Covers: `SPEC-004`.

Criterion: Template assembly, changelog-fragment lint, the full harness-policy validator, whitespace validation, and scoped-diff review all pass after the change.

Expected evidence: Command output recorded by the implementation plan and no unrelated or historical-artifact edits in the name-only diff.

## Architecture Decisions

Architecture snapshot status: Required; `snapshots/architecture.snapshot.md` records the durable routing and module-loading boundary selected for this work.

Decision summary:

1. Drivers: reduce ordinary context load, remove router drift, and make the approval gate a just-in-time operation.
2. Constraints: preserve stable module IDs, generated-template ownership, historical immutability, and the current freeze behavior.
3. Selected approach: retain one operational router in `SKILL.md`, rename the architecture reference as maintenance-only, and remove freeze-gate dependencies from planning inputs rather than duplicating gate procedure elsewhere.
4. Affected boundaries: entrypoint orientation, maintenance reference, template source blocks and outputs, validator path/route assertions, and freeze-gate discoverability.
5. Rejected alternatives: a minimal wording-only cleanup, a second operational router reference, and a new generated routing manifest.
6. Validation cues: `VER-001` through `VER-004` and their linked Plan Checks.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. Harness module file paths, operation-router loading contract, template policy-reference metadata, and structural validator assertions; no product runtime API changes.

### Data, config, and persistence

1. None.

### State and control flow

1. Planning route selection loads planning modules only; review/approval route selection later loads `module:freeze-gate` and projects the draft package into frozen state.

### Safety, security, privacy, migration, and rollback

1. None identified after repository-context review. A revert restores documentation-routing and validator behavior without data migration.

## Risks and Rejected Alternatives

### `RISK-001` Deferred gate leaves a drafting requirement undefined

Decision or mitigation:

1. Trace every current template and validator use of `module:freeze-gate`; retain necessary lifecycle, quality, and model-owned draft information in their owners or artifact fields, and prove the gate remains required at review/freeze.

### `RISK-002` Route table simplification hides necessary naming input

Decision or mitigation:

1. Treat `module:naming` as a normal planning input where a new work item or planned commit/changelog subject is produced, and revise route-budget wording rather than implying it is optional.

### `RISK-003` Rename leaves stale package references

Decision or mitigation:

1. Use targeted searches and the full validator to update all current maintenance surfaces; do not rewrite frozen historical records.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: router-maintenance-architecture -- approve routing cleanup` |
| Implementation | `refactor: router-maintenance-architecture -- isolate maintenance and freeze context` |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source | Living | Yes | Before each commit | `changelog/planning-approval.md`, `changelog/implementation.md` | Fragment headings match planned subjects. |
| Root changelog consolidation | Living | No | Operator-owned checkpoint | `CHANGELOG.md` | Ordinary plan-only and implementation commits use source fragments; root consolidation is not part of this work. |
| Test cases | Snapshot | Yes | Before implementation | `snapshots/test-cases.snapshot.md` | Covers router ownership, reference content, gate deferral, and validator continuity. |
| Testing guide delta | Living delta | No | N/A | N/A | No end-user test workflow changes. |
| Operator manual delta | Living delta | No | N/A | N/A | No product runtime or operator workflow changes. |
| API reference delta | Living delta | No | N/A | N/A | No API change. |
| Architecture snapshot | Snapshot | Yes | Before implementation | `snapshots/architecture.snapshot.md` | Preserves the selected operational-versus-maintenance loading boundary. |
| Architecture summary delta | Living delta | No | N/A | N/A | The work does not update a repository-level system architecture document. |

## Planning shape and transition ownership

1. Planning shape: `combined small/medium`.
2. Companion plan: `plan_router-maintenance-architecture.md` is drafted with this spec.
3. Transition owner: the companion plan owns the `plan execution` transition after the combined package freezes.
4. Next lifecycle stage: `plan execution`.

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Specification Commitments and Verification Criteria are atomic and testable.
- [x] Repository evidence, compatibility constraints, and the routing boundary are recorded.
- [x] Architecture, interface, data, and safety impacts are explicitly assessed.
- [x] Documentation artifacts and planned commits are explicit.
- [x] The companion plan, architecture snapshot, and test-case snapshot are present in the combined package.
- [x] The upcoming-stage sub-agent assessment records one operator-approved, read-only independent final reviewer using Sol at high reasoning after implementation validation.
- [x] No unresolved placeholders, required decisions, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
