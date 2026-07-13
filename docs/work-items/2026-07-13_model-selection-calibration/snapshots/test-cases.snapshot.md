# Model-Selection Calibration Test Cases Snapshot

Work ID: `2026-07-13_model-selection-calibration`
Short ID: `model-selection-calibration`
Status: Approved
Harness release: `0.6+`
Schema: `schema:snapshot.test-cases`

## Purpose

Define the policy and generated-template cases that implementation must demonstrate before changing current harness surfaces.

## Cases

### `CASE-001` Suggested bounded-work baseline

1. Given the active `economy-default` policy, the canonical text names Terra medium as the suggested baseline for substantial bounded work with explicit outputs and validation.
2. The text preserves operator override authority and permanent `balanced` tier vocabulary.
3. Expected evidence: targeted `test_harness_policy.py` assertions pass.

### `CASE-002` Effort and tier changes are not conflated

1. Given a suitable bounded task that needs more dependency or edge-case traversal, the policy identifies Terra high as an effort escalation.
2. Given unresolved ambiguity, competing interpretations, an unclear causal chain, or difficult judgment, the policy identifies Sol medium as a tier escalation.
3. Given a high-impact unresolved conflict or evidence gap after Sol medium, the policy limits Sol high to an exceptional escalation with a written reason.
4. Expected evidence: targeted validator assertions pass and manual review confirms the distinctions.

### `CASE-003` Lifecycle reduces allocation pressure

1. Given a frozen spec or plan, deterministic checks, or a fixed review lens that makes remaining work bounded, the policy permits return to Terra medium or high rather than retaining a stronger allocation.
2. Given missing product input, an undecided requirement, or a plan contradiction, the policy routes the issue to variance or approval rather than stronger model use.
3. Expected evidence: targeted validator assertions pass.

### `CASE-004` Independent review is evidence-led and bounded

1. Given an important multi-file change with a clear plan, reviewer guidance uses a separate task or thread with curated artifacts, one named lens, evidence-backed findings with severity, and a reproduction or validation path.
2. A stronger reviewer allocation is permitted when missed defects cost more than the clear-plan executor allocation, but the guidance does not create a new mandatory gate or transfer integration ownership.
3. Expected evidence: canonical-policy and advisory-example review plus targeted validator assertions pass.

### `CASE-005` Prompts support the policy without duplicating it

1. Shared source strategy blocks prompt a planner to name a suggested baseline, distinguish effort from tier changes, and name residual uncertainty or variance for a later-stage escalation.
2. Generated templates are current and retain their existing selection-dimension fields.
3. The templates route detailed reusable semantics to `module:models` and do not reproduce the complete allocation ladder.
4. Expected evidence: `assemble_templates.py --check` returns `All assembled templates are current.` and the policy validator passes.

### `CASE-006` Scope remains limited

1. The implementation diff does not change `AGENTS.md`, `README.md`, permanent tier names, authorization layers, frozen historical artifacts, or root `CHANGELOG.md` without an approved variance.
2. Expected evidence: `git diff --check` succeeds and scoped diff review records no unapproved file.

### `CASE-007` Each supporting edit earns its maintenance cost

1. Given the completed implementation diff, every changed supporting surface has one distinct purpose: policy semantics, advisory role illustration, decision-recording prompt, generated mirror, or concrete regression assertion.
2. A second allocation ladder, new mandatory review gate, generic model-selection feature, or supporting edit with no distinct purpose is absent from the final diff.
3. Expected evidence: independent policy-boundary review records the purpose of each changed supporting surface and finds no disproportionate expansion.

## Approval

- Status: Approved
- Superseded by: None
