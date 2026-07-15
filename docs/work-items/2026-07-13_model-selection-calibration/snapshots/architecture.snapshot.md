# Architecture Snapshot

Work ID: `2026-07-13_model-selection-calibration`
Short ID: `model-selection-calibration`
Status: Approved
Harness release: `0.6+`
Schema: `schema:snapshot.architecture`
Policy references: `module:lifecycle`, `module:quality`, `module:models`, `rule:lifecycle.work-item-architecture-decisions`, `rule:lifecycle.immutable-snapshots`, `rule:lifecycle.variance-policy`, `rule:quality.spec-handoff`

## Purpose

Capture the policy-ownership boundary that implementation and review must preserve. This is a work-item decision snapshot, not a repository-wide architecture manual.

## Decision Ledger

### `DEC-001` Architecture Decision — Centralize calibrated selection semantics

Selected approach:

1. Put normative `economy-default` baseline, escalation, de-escalation, variance, and independent-review semantics in `references/subagent-model-policy.md`.
2. Keep `subagent-role-examples.md` advisory, source template blocks limited to one compact decision-recording cue, generated templates derived by assembly, and `test_harness_policy.py` focused on structural presence and ownership boundaries.

Affected boundaries:

1. Repositories: `D:\Code\dev-doc-harness` only.
2. Components or modules: canonical model policy, advisory role examples, shared template blocks and their assemblies, structural validator.
3. Interfaces, schemas, config, or infra: planner-facing Markdown prompts and validation output; no runtime application interface or configuration change.
4. Agentic, process, documentation, or phase boundaries: operator-approved model strategy remains authoritative; a curated independent reviewer advises, while the orchestration thread retains integration and variance judgment.

Source spec sections:

1. `SPEC-001` through `SPEC-004`, `VER-001` through `VER-004`, and `RISK-001` through `RISK-004` in `spec_model-selection-calibration.md`.

Validation cues:

1. `CHECK-001` validates canonical and advisory semantics; `CHECK-002` validates generated output; `CHECK-003` reviews non-duplication and ownership; `CHECK-004` confirms scope.

Rejected alternatives:

1. A policy-only edit was rejected because prompts and checks could drift.
2. A broad README rewrite was rejected because README already routes to the canonical owner.
3. A decision tree copied into templates was rejected because it would compete with canonical policy and become stale.
4. A required concrete model configuration was rejected because runtime availability and operator choice remain authoritative.
5. Broad guidance, README, or template expansion without a distinct operator or regression-protection benefit was rejected as disproportionate to this calibration.

## Decision Drivers

1. Reduce avoidable cost and latency while preserving quality for substantial bounded harness work.
2. Use the research handoff as a compact, evidence-aware calibration without claiming external benchmarks prove a local universal optimum.
3. Make independent review more useful through isolation and a defined evidence lens.

## Constraints

1. Preserve permanent vendor-neutral capability tiers, current provider mapping, authorization layers, `ultra` classification, concurrency policy, and final integration ownership.
2. Do not change `AGENTS.md`, frozen historical artifacts, or root `CHANGELOG.md` during the planning package or implementation unless approved scope changes.
3. Treat an undecided requirement, missing product input, or plan contradiction as variance or approval work, not as an allocation escalation.

## Future Durable-Doc Boundary

1. No repository-level architecture summary update is required. This snapshot is the frozen decision source for the implementation and review pass.

## Approval

- Status: Approved
- Superseded by: None
