# Quality and Efficiency Policy Test Cases

Work ID: `2026-08-27_quality-efficiency-policy`
Short ID: `quality-efficiency-policy`
Status: Approved
Harness release: `0.10+`
Schema: `schema:snapshot.test-cases`
Source spec: `spec_quality-efficiency-policy.md`

## Purpose

Define the policy-validator scenarios that prove the renamed profiles, nested hierarchy, and lightweight delegation biases without weakening the generic policy foundation.

## Cases

### `TC-001` Nested Model selection remains discoverable

Covers: `VER-001`.

Given the canonical policy nests `### Model selection` below `## Upcoming-stage selection`, when the focused model-selection validator reads its section, then it finds Generation, Capability tier, Reasoning effort, Model facets, and Model and orchestration selection policies without changing unrelated H2 extraction behavior.

Expected evidence: the focused model-selection check passes and the H2 helper remains available for Current-session diagnostics and Required notation.

### `TC-002` Live profile vocabulary is fully migrated

Covers: `VER-002`, `VER-004`.

Given current canonical policy, root guidance, template source blocks, generated templates, and validator fixtures, when a scoped search examines those live surfaces, then they use `quality-first` and `efficiency-first` and do not use the retired profile names.

Expected evidence: the scoped search has no live old-name match; any retained old-name match is inspected as immutable history.

### `TC-003` Quality-first increases optional coverage without replacing safeguards

Covers: `VER-002`, `VER-003`.

Given multiple valid model or orchestration choices under shared rules, when quality-first is selected, then its text favors stronger justified allocation and additional independently bounded coverage through applicable bounded sub-agents, platform multi-agent/Ultra, or hybrid work; it still defers to shared review, authorization, context, write-authority, concurrency, and integration rules.

Expected evidence: focused canonical-text assertions and independent review findings.

### `TC-004` Efficiency-first accounts for total delivery cost without new ceremony

Covers: `VER-002`, `VER-003`.

Given multiple valid choices under shared rules, when efficiency-first is selected, then it favors the least total expected delivery cost, including coordination and likely rework, preserves required independent review and isolation, and uses the least fan-out that meets those requirements.

Expected evidence: focused canonical-text assertions; no new required model, cost, or delegation field appears in templates.

### `TC-005` Existing escalation and authority boundaries remain narrow

Covers: `VER-003`.

Given efficiency-first allocation, when work is bounded supporting work, then fast/economy remains non-authoritative. When a high-blast-radius task already requires both difficult judgment and broad traversal, direct flagship/high remains a documented exceptional path; missing product input or a plan contradiction remains an approval issue rather than a spending trigger.

Expected evidence: focused assertions and canonical policy review.

### `TC-006` Source/generated outputs and full harness policy agree

Covers: `VER-004`.

Given the two changed model-strategy source blocks, when the assembler writes then checks generated templates and the full validator runs, then all three consuming generated templates are current and all harness policy checks pass.

Expected evidence: successful `assemble_templates.py --write`, `assemble_templates.py --check`, and `test_harness_policy.py` output.

## Approval

- Status: Approved
- Superseded by: None
