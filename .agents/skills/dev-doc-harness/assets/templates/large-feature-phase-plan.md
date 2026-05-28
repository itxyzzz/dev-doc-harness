# Large or Phased Work Item Phase NN: <Phase Name>

Work ID: `<YYYY-MM-DD-short-kebab-title>` or `<YYYY-MM-DD-ISSUE-short-kebab-title>`
Status: Draft

## Objective

Describe the phase outcome.

## Input context

List the approved `spec.md`, prior phase outputs, decisions, and repository areas the implementing agent must read. Preserve all applicable details from the large/phased work item spec; do not narrow, drop, or reinterpret spec decisions in the phase plan.

Follow the repository-root reference `.agents/skills/dev-doc-harness/references/durable-planning-quality.md` so this phase plan is executable by a fresh agent or thread.

## Likely files and areas

List files, directories, APIs, schemas, docs, or workflows expected to change.

## Model and Sub-agent Strategy

Current orchestration: record the model/profile and reasoning effort if known.
Fit assessment: judge complexity, risk, ambiguity, blast radius, budget, and latency.
Recommended change: record `None` or a concrete model/reasoning change with reason.

Sub-agents: record `None` when no sub-agents are proposed. When proposing sub-agents or nondefault model/reasoning settings, follow the repository-root reference `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`, capture only task-specific choices below, and get explicit operator confirmation before applying those choices.

| Purpose | Input context | Output artifact | Model policy | Model class/profile | Reasoning effort | Reason | Parallel? | Blast radius if wrong |
|---|---|---|---|---|---|---|---|---|
| Replace with a bounded explorer/reviewer/worker task, or omit this table when sub-agents are `None` | Files, docs, specs, or decisions to read | Expected deliverable | `economy-default` unless changed by operator | Policy-relative class | low/medium/high | Selection rationale | Yes/No | Low/Medium/High plus consequence |

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

## Planning artifact freeze gate

When this phase plan or phase-plan batch is finalized, follow the repository-root reference `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md` before implementation.

## Handoff output

Describe what the implementing agent must report at phase completion.

Include assigned scope, files inspected or changed, commands and tests run, assumptions, uncertainty or residual risk, and recommended next step.

## Completion criteria

- Phase objective is met.
- Validation commands have been run and recorded.
- Documentation tasks are complete or explicitly deferred with reason.
- `CHANGELOG.md` has a newest-first entry for the phase before each commit.
- Variance log is present and current.
