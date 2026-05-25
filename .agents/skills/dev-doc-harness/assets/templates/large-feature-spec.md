# <Feature Name> Large Feature Spec

Feature ID: `<YYYY-MM-DD-short-kebab-title>`
Status: Draft

## Goal

Describe the outcome and why this work needs phase planning.

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

| Phase | Objective | Output |
|---|---|---|
| 01 | Discovery or preparation | `phases/01-discovery-plan.md` |
| 02 | Core implementation | `phases/02-core-implementation-plan.md` |
| 03 | Hardening and review | `phases/03-hardening-plan.md` |

## Sub-agent orchestration

| Phase | Sub-agent task | Model policy | Model class | Effort | Reason | Output |
|---|---|---|---|---|---|---|
| 01 | Repository or API discovery | economy-default | smaller/faster | medium | Bounded exploration | Discovery notes |
| 02 | Architecture or integration review | economy-default | latest strongest | high | High blast radius | Review memo |
| 03 | Final implementation review | economy-default | latest strongest | high | Subtle integration risk | Review findings |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Test cases | Snapshot | Yes/No | Before implementation | docs/snapshots/test-cases.snapshot.md | Capture expected behavior before code changes |
| Testing guide delta | Living delta | Yes/No | During or after implementation | docs/living/testing-guide.delta.md | Update if operator or test flow changes |
| Operator manual delta | Living delta | Yes/No | After implementation | docs/living/operator-manual.delta.md | Update if runtime or operator behavior changes |
| API reference delta | Living delta | Yes/No | During or after API work | docs/living/api-reference.delta.md | Required for public API changes |
| Architecture snapshot | Snapshot | Yes/No | Before or after design stabilization | docs/snapshots/architecture.snapshot.md | Feature-bound decision snapshot |
| Architecture summary delta | Living delta | Yes/No | After review | docs/living/architecture-summary.delta.md | Update if long-lived architecture docs change |

## Approval

- Status: Draft / Approved / Superseded
- Approved by: blank until approved
- Approval date: blank until approved
