# <Feature Name> Large Feature Spec

Feature ID: `<YYYY-MM-DD-short-kebab-title>` or `<YYYY-MM-DD-ISSUE-short-kebab-title>`
Status: Draft

## Goal

Describe the outcome and why this work needs phase planning.

## Planning handoff quality bar

This spec is the central handoff from the initial large-scale planning session to later planning sessions that produce the phase plans. Preserve all important decisions, constraints, assumptions, risks, data/interface choices, acceptance criteria, known unknowns, and rejected alternatives here before writing phase plans.

Phase plans must derive from this spec. If later planning discovers missing context, update the draft spec before approval or create an amendment after approval.

## Scope

List included systems, modules, workflows, APIs, data, and documentation.

## Non-scope

List deferred or intentionally excluded work.

## Assumptions

Write one bullet per assumption that affects scope, sequencing, interfaces, data, risk, or validation.

## Risks

Record integration, migration, compatibility, security, privacy, compliance, rollout, and operational risks.

## Acceptance criteria

Write one bullet per observable outcome. Each criterion should be testable by a command, manual check, review finding, or documented operator acceptance.

## Phase decomposition

Replace these example rows with the actual phases for this feature.

| Phase | Objective | Output |
|---|---|---|
| 01 | Discovery or preparation | `plan-phase-01-discovery.md` |
| 02 | Core implementation | `plan-phase-02-core-implementation.md` |
| 03 | Hardening and review | `plan-phase-03-hardening.md` |

## Sub-agent orchestration

Replace these example rows with the actual sub-agent choices for this feature. Omit this table when no sub-agents are proposed.

| Phase | Sub-agent task | Model policy | Model class | Effort | Reason | Output |
|---|---|---|---|---|---|---|
| 01 | Repository or API discovery | economy-default | smaller/faster | medium | Bounded exploration | Discovery notes |
| 02 | Architecture or integration review | economy-default | latest strongest | high | High blast radius | Review memo |
| 03 | Final implementation review | economy-default | latest strongest | high | Subtle integration risk | Review findings |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Newest-first entries grouped by change type |
| Test cases | Snapshot | Yes/No | Before implementation | docs/snapshots/test-cases.snapshot.md | Capture expected behavior before code changes |
| Testing guide delta | Living delta | Yes/No | During or after implementation | docs/living/testing-guide.delta.md | Update if operator or test flow changes |
| Operator manual delta | Living delta | Yes/No | After implementation | docs/living/operator-manual.delta.md | Update if runtime or operator behavior changes |
| API reference delta | Living delta | Yes/No | During or after API work | docs/living/api-reference.delta.md | Required for public API changes |
| Architecture snapshot | Snapshot | Yes/No | Before or after design stabilization | docs/snapshots/architecture.snapshot.md | Feature-bound decision snapshot |
| Architecture summary delta | Living delta | Yes/No | After review | docs/living/architecture-summary.delta.md | Update if long-lived architecture docs change |

## Approval

- Status: Draft / Approved / Superseded
- Superseded by: blank unless superseded
