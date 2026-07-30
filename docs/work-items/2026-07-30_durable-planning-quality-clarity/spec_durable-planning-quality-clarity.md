# Durable Planning Quality Clarity Spec

Work ID: `2026-07-30_durable-planning-quality-clarity`
Short ID: `durable-planning-quality-clarity`
Status: Approved
Harness release: `0.8+`
Schema: `schema:spec.small-medium`
Companion plan: `plan_durable-planning-quality-clarity.md`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:quality.spec-handoff`, `rule:quality.phase-plan-fresh-thread`, `rule:quality.conformance-status`

## Goal

Make the durable-planning quality policy internally consistent, self-contained for future planning sessions, and proportionate. It must apply a clear quality bar to both ordinary plans and phase plans while preserving the useful `SPEC` → `VER` → `CHECK` evidence chain without restoring mandatory traceability matrices.

## Source and intent

Source input:

1. The operator's review comments on `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`.
2. The operator's decisions in the planning discussion: remove the unexplained duplicate alternative category; preserve an explicit open-question resolution bar; keep phase size as a quality rule; and use an economical conformance model.
3. Current lifecycle, model-policy, template, and validator behavior inspected during planning.

Desired outcome:

1. An author can tell which quality rules apply to a spec, a small/medium plan, and a phase plan without inferring missing rules from other modules.
2. A fresh executor can treat an approved spec and plan as the source of truth rather than reconstructing material requirements from an earlier chat or attached source.
3. The policy, source templates, generated templates, and validator agree on the minimal evidence relationship.

## Scope boundary

### In scope

1. Clarify the scope, plain-language baseline, spec quality, general plan quality, phase-specific quality, evidence/conformance, and handoff-preservation sections in `references/durable-planning-quality.md`.
2. Retain stable `SPEC-NNN`, `VER-NNN`, `TASK-NNN`, and `CHECK-NNN` identifiers and the default of concise local links.
3. Define the minimal relationship: a commitment is proven by one or more criteria, and a check obtains and records evidence for a criterion. A completed task does not by itself prove conformance.
4. Align the reusable plan/spec source blocks, their generated templates, and focused validator fixtures or assertions with the clarified policy.
5. Preserve the user's current line-break cleanup in the target reference while making the approved content changes.

### Non-scope

1. Do not restore mandatory commitment-disposition or verification-execution mapping tables.
2. Do not turn the harness into a requirements-management system, semantic prose grader, or second approval process.
3. Do not alter frozen historical work-item artifacts.
4. Do not change lifecycle ownership of planning shape, snapshots, freeze gates, variance, execution continuity, or model/sub-agent authorization.
5. Do not change public APIs, application runtime behavior, persistence, releases, or root changelog consolidation policy.

### Assumptions

1. The work remains small/medium: one orchestration thread can integrate the related policy, template, generated-output, and validator changes.
2. Local ID links are sufficient for routine plans; a mapping remains optional only when it has a stated coverage, handoff, or deterministic-validation benefit.
3. A standalone architecture snapshot is not needed because this package records a narrow clarification of existing module boundaries rather than a new work-item architecture.

### Open questions

1. None. The operator selected the economical conformance approach and clarified the desired treatment of open questions, source material, and phase sizing.

## Repository context

1. `module:quality` currently says it applies to all harness-managed specs and plans, but its named quality bar is only for phase plans.
2. `module:lifecycle` owns work sizing, phase sequencing, architecture-snapshot eligibility, immutable snapshots, and variance; `module:quality` must consume those boundaries rather than restate their mechanics.
3. The reusable plan source block already promotes optional local links, but the validator still contains fixtures for an earlier mandatory-mapping, multi-field Plan Check model.
4. `assemble_templates.py` is the supported source-block-to-generated-template workflow and must regenerate both plan outputs after source-block changes.

## Commitments and verification

### `SPEC-001` Apply a coherent quality scope

Statement:

1. `module:quality` must state that it governs durable specs and plans, including phase plans, without a tautological exception for edits that do not invoke the harness.
2. The quality reference must give every plan a general executable, self-contained quality bar and give phase plans only their additional independent-phase requirements.
3. The phase requirement must retain the quality boundary that one phase is safely executable by one orchestration thread with its recorded bounded delegation.

#### `VER-001` Quality rules cover every planning shape

Covers: `SPEC-001`.

Criterion: The reference, policy architecture catalog, plan templates, and phase-plan template use compatible scope language, and no ordinary plan is left without a stated quality bar.

Expected evidence: Focused text checks and generated-template inspection show general plan guidance plus distinct phase-only boundary language.

### `SPEC-002` Keep the readability and open-question bar precise

Statement:

1. The plain-language rule must permit ordinary normative `must` and `should` language while rejecting legalistic authority language and legalistic modal phrasing.
2. Before approval or handoff, an artifact must resolve every question material to its documented next activity.
3. A known unknown may remain only after reasonable checking establishes that it does not affect that activity; later-stage relevance requires a recorded reason and owner or resolving event.
4. The spec-quality list must not duplicate architectural rejected alternatives with an unexplained second category.

#### `VER-002` Readability rules preserve decisions without contradiction

Covers: `SPEC-002`.

Criterion: The quality reference has no literal conflict between its modal convention and its plain-language rule, states the materiality threshold for unresolved questions, and has one clearly owned rejected-alternatives requirement.

Expected evidence: Focused policy assertions and review of the changed section.

### `SPEC-003` Define economical evidence and conformance

Statement:

1. A `VER-NNN` must state the evidence that establishes whether its linked commitment conforms; a `CHECK-NNN` must state the evidence-gathering method, expected result, and evidence record.
2. The reference must define a small, explicit criterion state vocabulary: `met`, `not met`, `pending`, and `blocked`.
3. A commitment must conform only when its applicable criteria are met. Task completion alone must not establish conformance.
4. Full mappings remain optional; local `SPEC`/`VER`/`TASK`/`CHECK` links remain the routine representation.

#### `VER-003` Evidence chain is usable without mandatory matrices

Covers: `SPEC-003`.

Criterion: Current policy, templates, and focused validator behavior accept a plan with local criterion-to-check links and evidence-record fields, reject missing criterion coverage or evidence-record fields where the plan schema requires them, and do not require complete mapping tables.

Expected evidence: Validator fixtures or assertions, generated-template inspection, and the full harness-policy test pass.

### `SPEC-004` Preserve source material in durable handoffs

Statement:

1. Before approval or handoff, authors must compare the draft artifacts with operator-provided source materials, including relevant chat-provided documents, attachments, tickets, and review comments.
2. The spec must capture every material source detail affecting outcome, scope, constraints, decisions, risks, or verification; the plan must capture every remaining material detail affecting its tasks, checks, and handoff.
3. After freeze, a fresh session must be able to use the approved artifacts as the source of truth without reconstructing the original discussion.

#### `VER-004` Handoff rule is durable and proportional

Covers: `SPEC-004`.

Criterion: The quality reference identifies durable source inputs and materiality, covers both ordinary plans and phase plans, and does not demand verbatim preservation of irrelevant source text.

Expected evidence: Focused policy assertion and reviewer inspection of the completed wording.

## Architecture decisions

Architecture snapshot status: `Not applicable`.

Decision summary:

1. `module:quality` owns artifact usability, evidence semantics, and preservation quality; it links to lifecycle for freeze, variance, planning shape, and snapshot mechanics.
2. The four existing entity IDs remain lightweight anchors. `SPEC` expresses delivery, `VER` defines proof, `CHECK` obtains proof, and `TASK` performs work.
3. Keep mappings benefit-based and local links as the default, avoiding reintroduction of mandatory cross-reference matrices.
4. Keep phase size under quality because an oversized phase degrades the usability of the execution plan, while lifecycle remains the owner of phase sequencing.

Rejected alternatives:

1. Only delete disputed sentences from the reference; this would leave ordinary-plan coverage and conformance ownership unresolved.
2. Restore the earlier mandatory mapping/status model; its maintenance and reader cost exceed its value for routine plans.
3. Move all phase freshness and handoff language into lifecycle; this would blur lifecycle sequencing with the usability quality of a single execution plan.

## Interfaces, data, and control flow

Interfaces affected:

1. Current durable-artifact schemas and authoring prompts for small/medium plans and phase plans.
2. Focused validation behavior for the commitment, criterion, task, and check relationship.

Data, config, and persistence: None.

Control flow:

1. Planning authors incorporate material source inputs into the draft spec and plan.
2. A plan links its work and evidence locally unless a justified mapping is useful.
3. Execution records check evidence and derives criterion/commitment conformance from that evidence.
4. Freeze and variance remain lifecycle-controlled transitions.

Safety, security, privacy, migration, and rollback: No runtime or data impact. Rollback is a cohesive revert of the current policy, source-block, generated-template, and validator changes if validation reveals an incompatibility.

## Risks and mitigations

### `RISK-001` The simplification leaves stale mandatory-mapping validation

Decision or mitigation:

1. Locate and replace only fixtures and assertions that still require mandatory mapping tables; keep structural checks that protect IDs, coverage, and generated-template freshness.

### `RISK-002` New wording duplicates lifecycle rules

Decision or mitigation:

1. State only the quality consequence in `module:quality` and cite lifecycle for the governing process and post-freeze handling.

### `RISK-003` Conformance becomes another approval gate

Decision or mitigation:

1. Define conformance as evidence interpretation, not a new transition. The existing freeze gate remains the only approval mechanism.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: durable-planning-quality-clarity -- approve clearer plan quality` |
| Implementation | `docs: durable-planning-quality-clarity -- clarify plans and conformance` |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source | Living | Yes | Before each commit | `changelog/planning-approval.md`, `changelog/implementation.md` | Create at the matching checkpoint; titles match planned subjects. |
| Root changelog consolidation | Living | No | Not applicable | Not applicable | Operator-owned consolidation is outside this package. |
| Test cases | Snapshot | No | Not applicable | Not applicable | Plan checks and focused validator fixtures provide adequate, versioned validation detail. |
| Testing guide delta | Living delta | Yes | Implementation | `deltas/testing-guide.delta.md` | Record the updated validation commands and evidence model. |
| Operator manual delta | Living delta | No | Not applicable | Not applicable | The target policy and templates are the direct operator-facing surfaces. |
| API reference delta | Living delta | No | Not applicable | Not applicable | No public API. |
| Architecture snapshot | Snapshot | No | Not applicable | Not applicable | Existing module boundaries are clarified inline. |
| Architecture summary delta | Living delta | No | Not applicable | Not applicable | No repository-level architecture document changes. |
| Variance log | Execution record | Conditional | Implementation | `implementation-notes/variance-log.md` | Create only for noteworthy allowed drift. |

## Planning shape and transition ownership

Planning shape: `combined small/medium`.

1. This spec and `plan_durable-planning-quality-clarity.md` form one draft package.
2. The plan owns the implementation handoff after an approved freeze.
3. No implementation begins until a fresh post-freeze operator instruction.

## Spec readiness checklist

- [x] Source input, desired outcome, scope, non-scope, assumptions, and open questions are explicit.
- [x] Commitments, criteria, repository context, module boundaries, risks, and validation are specific.
- [x] The package preserves the operator's decisions without requiring later chat reconstruction.
- [x] The companion plan is present and owns the later implementation handoff.
- [x] No placeholders, unresolved required decisions, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
