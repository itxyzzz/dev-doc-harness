# Architecture Snapshot

Work ID: `2026-08-27_quality-efficiency-policy`
Short ID: `quality-efficiency-policy`
Status: Approved
Harness release: `0.10+`
Schema: `schema:snapshot.architecture`
Policy references: `module:lifecycle`, `module:quality`, `rule:lifecycle.work-item-architecture-decisions`, `rule:lifecycle.immutable-snapshots`, `rule:lifecycle.variance-policy`, `rule:quality.spec-handoff`

## Purpose

Capture the policy-hierarchy and profile-boundary decisions that implementation and review must preserve.

## Decision Ledger

### `DEC-001` Architecture Decision — Nest model selection beside orchestration selection

Selected approach:

1. Keep `## Upcoming-stage selection` as the parent. Retain `### Orchestration selection` and make `### Model selection` its peer.
2. Move Model facets and the profile section beneath Model selection. Rename the latter `#### Model and orchestration selection policies` because profile choice influences both dimensions.

Affected boundaries:

1. Repository: the current Dev Doc Harness repository.
2. Components or modules: `references/subagent-model-policy.md` and `scripts/test_harness_policy.py`.
3. Interfaces, schemas, config, or infra: `rule:models.selection-dimensions` owner references and heading-aware validator extraction.
4. Agentic, process, documentation, or phase boundaries: upcoming-stage planning and execution selection; no lifecycle-stage change.

Source spec sections:

1. `SPEC-001`, `VER-001`, and `RISK-001` in `spec_quality-efficiency-policy.md`.

Validation cues:

1. `CHECK-001`, `CHECK-002`, and `CHECK-004` in `plan_quality-efficiency-policy.md`.

Rejected alternatives:

1. Keep Model selection as a top-level H2. This leaves two coordinated next-stage decisions separated and fails to propagate the agreed structure.

### `DEC-002` Architecture Decision — Replace both profile names without a live alias

Selected approach:

1. Replace `enterprise-default` and `economy-default` with `quality-first` and `efficiency-first` in current policy text, owner IDs, active guidance, prompts, generated templates, and validator fixtures.
2. Preserve old names only in frozen work items and historical release/changelog records; do not add a live alias.

Affected boundaries:

1. Repository: the current Dev Doc Harness repository.
2. Components or modules: canonical policy, root `AGENTS.md`, root README, template source blocks, generated templates, and the policy validator.
3. Interfaces, schemas, config, or infra: textual active-model-policy values and `rule:models.*` owner IDs.
4. Agentic, process, documentation, or phase boundaries: all future work-item strategy records use the new values.

Source spec sections:

1. `SPEC-002` and `VER-002` in `spec_quality-efficiency-policy.md`.

Validation cues:

1. `CHECK-001`, `CHECK-002`, and `CHECK-004` in `plan_quality-efficiency-policy.md`.

Rejected alternatives:

1. Keep `enterprise-default`, which misleadingly describes an organization rather than a selection bias.
2. Retain a live compatibility alias, which would expand the active vocabulary without a current consumer that needs it.

### `DEC-003` Architecture Decision — Keep profiles lightweight across model and delegation choices

Selected approach:

1. Profiles defer to the shared generic rules. Quality-first favors stronger justified allocations and greater independent coverage or fan-out where bounded outputs justify coordination risk.
2. Efficiency-first selects the lowest total expected delivery cost, including coordination and likely rework, while retaining the shared independent-review and isolation floor and using the least fan-out that meets it.
3. The existing conditional non-obvious-selection rationale may name decisive factors only; no numerical estimate, new field, or new approval route is added.

Affected boundaries:

1. Repository: the current Dev Doc Harness repository.
2. Components or modules: `references/subagent-model-policy.md`, templates that name profile choices, and focused validator assertions.
3. Interfaces, schemas, config, or infra: capability-tier/reasoning selection and orchestration-mode interpretation remain independent fields.
4. Agentic, process, documentation, or phase boundaries: generic authorization, context, write authority, concurrency, reviewer, and final integration rules remain unchanged.

Source spec sections:

1. `SPEC-002`, `SPEC-003`, `VER-002`, `VER-003`, and `RISK-003` in `spec_quality-efficiency-policy.md`.

Validation cues:

1. `CHECK-001`, `CHECK-003`, and `CHECK-004` in `plan_quality-efficiency-policy.md`.

Rejected alternatives:

1. Add a cost-estimation worksheet or delegation business case. It adds overhead without improving the current conditional rationale.
2. Treat Ultra as preferred. It is one applicable orchestration mechanism, not a replacement for bounded sub-agents or hybrid work.

## Decision Drivers

1. The operator wants clear, neutral profile names and a single coherent next-stage selection hierarchy.
2. Model choice and delegation topology can both affect quality, latency, and total delivery cost.
3. The harness must keep its current review and authorization protections while avoiding extra planning ceremony.

## Constraints

1. Generic policy stays canonical and must not be duplicated in profile bodies or templates.
2. Current generated templates change through the assembler only.
3. Historical artifacts are immutable.
4. No Pro-mode or release work is part of this package.

## Future Durable-Doc Boundary

Repository-level durable architecture documents are out of scope. `deltas/operator-manual.delta.md` is the required operator-guidance handoff for this work item.

## Approval

- Status: Approved
- Superseded by: None
