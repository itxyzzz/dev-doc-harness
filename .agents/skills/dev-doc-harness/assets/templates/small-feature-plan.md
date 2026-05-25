# <Feature Name> Plan

Feature ID: `<YYYY-MM-DD-short-kebab-title>` or `<YYYY-MM-DD-ISSUE-short-kebab-title>`
Status: Draft

## Implementation summary

Describe the implementation approach in a few paragraphs.

## Files and interfaces

List files expected to change and interfaces expected to remain stable or change.

## Tasks

Write one checkbox per implementation, test, validation, or documentation step. Each step should be specific enough for a fresh agent to execute without choosing an approach.

## Validation commands

| Command | Expected result |
|---|---|
| Record each command before implementation starts | Record the expected signal for success or failure |

## Plan variance handling

Approved plans are immutable snapshots. Record nontrivial implementation variance in `implementation-notes/variance-log.md`. Create a plan amendment and request operator approval before proceeding when variance affects architecture, APIs, data, security, privacy, compliance, scope, acceptance criteria, or plan feasibility.

## Planning artifact freeze gate

When this plan is finalized, update `CHANGELOG.md`, commit `spec.md`, `plan.md`, required documentation artifacts, variance log, and changelog together, then stop before implementation. Report the commit hash and remind the operator that they may push and create a draft plan-only PR. Implementation requires a fresh explicit instruction after the operator has had a chance to change model, reasoning-effort, or sub-agent policy.

## Completion criteria

- Acceptance criteria in `spec.md` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- Variance log is present and current.

## Approval

- Status: Draft / Approved / Superseded
- Superseded by: blank unless superseded
