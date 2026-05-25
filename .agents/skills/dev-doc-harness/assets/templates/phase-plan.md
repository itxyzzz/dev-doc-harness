# Phase NN: <Phase Name>

Feature ID: `<YYYY-MM-DD-short-kebab-title>`
Status: Draft

## Objective

Describe the phase outcome.

## Input context

List approved specs, prior phase outputs, decisions, and repository areas the implementing agent must read.

## Likely files and areas

List files, directories, APIs, schemas, docs, or workflows expected to change.

## Tasks

Write one checkbox per phase step. Include implementation, test, validation, documentation, and handoff work in execution order.

## Tests and validation

| Command | Expected result |
|---|---|
| Record each command before the phase starts | Record the expected signal for success or failure |

## Documentation tasks

List snapshot or living-delta artifacts this phase must create, update, or mark not applicable.

## Variance reminder

Approved phase plans are immutable snapshots. Record nontrivial variance in `implementation-notes/variance-log.md`. Create a plan amendment and request operator approval before proceeding when variance affects architecture, APIs, data, security, privacy, compliance, scope, acceptance criteria, or plan feasibility.

## Handoff output

Describe what the implementing agent must report at phase completion.

## Completion criteria

- Phase objective is met.
- Validation commands have been run and recorded.
- Documentation tasks are complete or explicitly deferred with reason.
- Variance log is present and current.
