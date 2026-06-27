# <Work Item Name> Large or Phased Work Spec

Work ID: `<YYYY-MM-DD-short-kebab-title>` or `<YYYY-MM-DD-ISSUE-short-kebab-title>`
Short ID: `<short-kebab-title>` or `<ISSUE-short-kebab-title>`
Status: Draft
Harness release: `<version or unknown>`
Schema: `schema:spec.large-phased`
Policy references: `module:lifecycle`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:lifecycle.large-anchor-spec`, `rule:lifecycle.large-phase-orchestration`, `rule:lifecycle.commit-message-format`, `rule:quality.spec-handoff`, `rule:models.strategy-required`, `rule:freeze.multi-gate-flow`

## Goal

Describe the outcome and why this work needs phase planning.

## Planning handoff quality bar

This spec is the central handoff from the initial large-scale planning session to later planning sessions that produce the phase plans. Preserve work-item-specific decisions, constraints, assumptions, risks, acceptance criteria, known unknowns, and rejected alternatives here before writing phase plans.

The initial planning package is anchor-spec-only by default under `rule:lifecycle.large-phase-orchestration`. Do not create concrete phase-plan files during this package unless the operator explicitly requests combined planning.

Phase plans must derive from this spec. If later planning discovers missing context before this spec is frozen, update the draft spec directly. If missing context is discovered after freeze, create an amendment.

Follow the repository-root reference `.agents/skills/dev-doc-harness/references/durable-planning-quality.md` before asking for approval to freeze this spec.

## Scope

List included systems, modules, workflows, APIs, data, and documentation.

## Non-scope

List deferred or intentionally excluded work.

## Current state

Summarize the relevant baseline before implementation.

## Proposed behavior

Describe the intended post-implementation behavior and operator-visible outcomes.

## Interfaces and data

Record affected APIs, internal interfaces, config, schemas, persistence, files, CLI flags, services, or data contracts. State `None` when not applicable.

## State flow and control flow

Describe affected lifecycle, state transitions, orchestration, request flow, jobs, concurrency, retries, or other control flow. State `None` when not applicable.

## Safety, security, privacy, compliance, migration, and rollback

Record auth, data exposure, privacy, compliance, migration, rollout, rollback, destructive-operation, and operator-safety considerations. State `None identified` only after checking the relevant code and docs.

## Validation strategy

Describe tests, manual checks, review gates, fixtures, environment assumptions, and expected validation signals.

## Triage, debugging, and operations

Record logs, metrics, diagnostics, runbooks, failure modes, recovery steps, or support workflows. State `None` when not applicable.

## Assumptions

Write one bullet per assumption that affects scope, sequencing, interfaces, data, risk, or validation.

## Risks

Record integration, migration, compatibility, security, privacy, compliance, rollout, and operational risks.

## Known unknowns

List unresolved facts or decisions that affect planning, implementation, validation, rollout, or risk. State `None` only when the spec has no known unknowns.

## Rejected alternatives

List important alternatives considered and why they are not part of this plan. State `None` when no meaningful alternatives were rejected.

## Acceptance criteria

Write one bullet per observable outcome. Each criterion should be testable by a command, manual check, review finding, or documented operator acceptance.

## Phase decomposition

Use actual phases for this work item.

The output filenames below are future phase-plan outputs, not files to create during the anchor-spec planning package unless combined planning was explicitly requested.

| Phase | Objective | Future phase-plan output |
|---|---|---|
| 01 | Discovery or preparation | `plan-phase-01-discovery-<short-id>.md` |
| 02 | Core implementation | `plan-phase-02-core-implementation-<short-id>.md` |
| 03 | Hardening and review | `plan-phase-03-hardening-<short-id>.md` |

## Planning artifact freeze gates

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.multi-gate-flow`. Record the draft review, approval commit or handoff snapshot, and pause before implementation, later phase-plan drafting, or later phase execution.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during spec and phase-plan review, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Anchor spec approval | `<short-id> spec: <title snippet>` | `<work-id>: <title snippet>` | Approval commit for this anchor spec. |
| Phase plan approval pattern | `<short-id> phase N plan: <title snippet>` | `<work-id>: <title snippet>` | Replace or refine in each concrete phase plan. |
| Implementation pattern | `<short-id> <type>: <expanded title snippet>` | `<work-id>: <expanded title snippet>` | Replace with concrete rows in phase plans. |

## Model and Sub-agent Strategy

Current orchestration: record the model/profile and reasoning effort if known.
Fit assessment: judge complexity, risk, ambiguity, blast radius, budget, and latency.
Recommended change: record `None` or a concrete model/reasoning change with reason.

Sub-agents: record `None` with rationale, or list bounded phase-level roles in the table. Prefer curated-artifact sub-agent phase-plan drafting after anchor-spec freeze when phases are independently plannable and platform support is available. Use canonical model policy rules for strategy requirements, context strategy labels, approved-strategy authorization, and confirmation boundaries.

| Phase | Purpose | Context strategy | Input context | Output artifact | Model policy | Model class/profile | Reasoning effort | Reason | Parallel? | Blast radius if wrong |
|---|---|---|---|---|---|---|---|---|---|---|
| Example phase number; omit this table when sub-agents are `None` | Bounded explorer/reviewer/worker task | curated prompt / curated artifacts / full-history fork / no repo context | Files, docs, specs, or decisions to read | Expected deliverable | Active repository policy unless changed by operator | Policy-relative class | low/medium/high | Selection rationale | Yes/No | Low/Medium/High plus consequence |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Newest-first entries grouped by change type; title snippets synchronized with planned commit subjects |
| Test cases | Snapshot | Yes/No | Before implementation | snapshots/test-cases.snapshot.md | Capture expected behavior before code changes |
| Testing guide delta | Living delta | Yes/No | During or after implementation | deltas/testing-guide.delta.md | Update if operator or test flow changes |
| Operator manual delta | Living delta | Yes/No | After implementation | deltas/operator-manual.delta.md | Update if runtime or operator behavior changes |
| API reference delta | Living delta | Yes/No | During or after API work | deltas/api-reference.delta.md | Required for public API changes |
| Architecture snapshot | Snapshot | Yes/No | Before or after design stabilization | snapshots/architecture.snapshot.md | Work-item-bound decision snapshot |
| Architecture summary delta | Living delta | Yes/No | After review | deltas/architecture-summary.delta.md | Update if long-lived architecture docs change |

## Approval

- Status: Draft / Approved / Superseded
- Superseded by: record only when this artifact is superseded
