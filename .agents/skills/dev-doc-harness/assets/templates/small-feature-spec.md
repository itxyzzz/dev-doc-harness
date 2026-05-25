# <Feature Name> Spec

Feature ID: `<YYYY-MM-DD-short-kebab-title>`
Status: Draft

## Goal

Describe the user-visible or operator-visible outcome.

## Scope

List the behavior, files, interfaces, or workflows included in this change.

## Non-scope

List nearby work intentionally excluded from this change.

## Current state

Summarize the relevant repository behavior before implementation.

## Proposed behavior

Describe the intended behavior after implementation.

## Interfaces and data

Record public APIs, config, schemas, persistence, CLI flags, files, or other interfaces affected by the change. State `None` when the change does not affect interfaces or data.

## Risks

Record behavioral, migration, compatibility, security, privacy, or operational risks. State `None identified` only after checking the relevant code and docs.

## Acceptance criteria

Write one bullet per observable outcome. Each criterion should be testable by a command, manual check, review finding, or documented operator acceptance.

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
