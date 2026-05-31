# <Work Item Name> Large or Phased Work Spec

Work ID: `<YYYY-MM-DD-short-kebab-title>` or `<YYYY-MM-DD-ISSUE-short-kebab-title>`
Short ID: `<short-kebab-title>` or `<ISSUE-short-kebab-title>`
Status: Draft

## Goal

Describe the outcome and why this work needs phase planning.

## Planning handoff quality bar

This spec is the central handoff from the initial large-scale planning session to later planning sessions that produce the phase plans. Preserve work-item-specific decisions, constraints, assumptions, risks, acceptance criteria, known unknowns, and rejected alternatives here before writing phase plans.

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

Replace these example rows with the actual phases for this work item.

| Phase | Objective | Output |
|---|---|---|
| 01 | Discovery or preparation | `plan-phase-01-discovery-<short-id>.md` |
| 02 | Core implementation | `plan-phase-02-core-implementation-<short-id>.md` |
| 03 | Hardening and review | `plan-phase-03-hardening-<short-id>.md` |

## Planning artifact freeze gates

When this spec, later phase-plan batches, or high-impact amendments are ready for operator review, follow the repository-root reference `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: stage the draft without committing, request approval or feedback, revise directly on feedback, and commit only after explicit approval or explicit handoff.

## Model and Sub-agent Strategy

Current orchestration: record the model/profile and reasoning effort if known.
Fit assessment: judge complexity, risk, ambiguity, blast radius, budget, and latency.
Recommended change: record `None` or a concrete model/reasoning change with reason.

Sub-agents: record `None` when no sub-agents are proposed. When proposing sub-agents or nondefault model/reasoning settings, follow the repository-root reference `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`, capture only task-specific choices below, and get explicit operator confirmation before applying those choices.

| Phase | Purpose | Input context | Output artifact | Model policy | Model class/profile | Reasoning effort | Reason | Parallel? | Blast radius if wrong |
|---|---|---|---|---|---|---|---|---|---|
| Replace with phase number or omit this table when sub-agents are `None` | Bounded explorer/reviewer/worker task | Files, docs, specs, or decisions to read | Expected deliverable | `economy-default` unless changed by operator | Policy-relative class | low/medium/high | Selection rationale | Yes/No | Low/Medium/High plus consequence |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Newest-first entries grouped by change type |
| Test cases | Snapshot | Yes/No | Before implementation | snapshots/test-cases.snapshot.md | Capture expected behavior before code changes |
| Testing guide delta | Living delta | Yes/No | During or after implementation | deltas/testing-guide.delta.md | Update if operator or test flow changes |
| Operator manual delta | Living delta | Yes/No | After implementation | deltas/operator-manual.delta.md | Update if runtime or operator behavior changes |
| API reference delta | Living delta | Yes/No | During or after API work | deltas/api-reference.delta.md | Required for public API changes |
| Architecture snapshot | Snapshot | Yes/No | Before or after design stabilization | snapshots/architecture.snapshot.md | Work-item-bound decision snapshot |
| Architecture summary delta | Living delta | Yes/No | After review | deltas/architecture-summary.delta.md | Update if long-lived architecture docs change |

## Approval

- Status: Draft / Approved / Superseded
- Superseded by: blank unless superseded
