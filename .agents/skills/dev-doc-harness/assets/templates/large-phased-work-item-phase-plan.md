# Large or Phased Work Item Phase NN: <Phase Name>

Work ID: `<YYYY-MM-DD-short-kebab-title>` or `<YYYY-MM-DD-ISSUE-short-kebab-title>`
Short ID: `<short-kebab-title>` or `<ISSUE-short-kebab-title>`
Status: Draft

## Objective

Describe the phase outcome.

## Input context

List the approved `spec-<short-id>.md`, prior phase outputs, decisions, and repository areas the implementing agent must read. Preserve all applicable details from the large/phased work item spec; do not narrow, drop, or reinterpret spec decisions in the phase plan.

Follow the repository-root reference `.agents/skills/dev-doc-harness/references/durable-planning-quality.md` so this phase plan is executable by a fresh agent or thread.

## Likely files and areas

List files, directories, APIs, schemas, docs, or workflows expected to change.

## Model and Sub-agent Strategy

Current orchestration: record the model/profile and reasoning effort if known.
Fit assessment: judge complexity, risk, ambiguity, blast radius, budget, and latency.
Recommended change: record `None` or a concrete model/reasoning change with reason.

Sub-agents: assess whether sub-agents are justified for substantial work even when the operator did not explicitly request them. Record `None` with a brief fit reason when no sub-agents are proposed. When proposing sub-agents or nondefault model/reasoning settings, follow the repository-root reference `.agents/skills/dev-doc-harness/references/subagent-model-policy.md` and capture only task-specific choices below.

Context strategy must say how each sub-agent receives context, such as `curated prompt`, `curated artifacts`, `full-history fork`, or `no repo context`. Use full-history forks deliberately because they may carry stale context, increase token load, and inherit or constrain model/reasoning settings on some platforms.

After this phase plan is approved, frozen, and followed by the normal post-freeze operator authorization to begin implementation, the listed sub-agent strategy is authorized without a separate sub-agent-specific confirmation. Fresh confirmation is still required for unplanned sub-agents, stronger unrecorded model/reasoning choices, write-scope escalation, platform-restricted actions, or more than 3 concurrent sub-agents. Long-running phase work may use more than 3 total sub-agents in separate waves when this plan supports those waves and no more than 3 run concurrently.

| Purpose | Context strategy | Input context | Output artifact | Model policy | Model class/profile | Reasoning effort | Reason | Parallel? | Blast radius if wrong |
|---|---|---|---|---|---|---|---|---|---|
| Replace with a bounded explorer/reviewer/worker task, or omit this table when sub-agents are `None` | curated prompt / curated artifacts / full-history fork / no repo context | Files, docs, specs, or decisions to read | Expected deliverable | `economy-default` unless changed by operator | Policy-relative class | low/medium/high | Selection rationale | Yes/No | Low/Medium/High plus consequence |

## Tasks

Write one checkbox per phase step. Include implementation, test, validation, documentation, and handoff work in execution order.

## Tests and validation

| Command | Expected result |
|---|---|
| Record each command before the phase starts | Record the expected signal for success or failure |

## Documentation tasks

List snapshot or delta artifacts this phase must create, update, or mark not applicable.

## Variance reminder

Before approval, operator feedback edits this draft directly and does not require an amendment. After the approval commit or explicit handoff snapshot, approved phase plans are immutable snapshots. Record nontrivial variance in `implementation-notes/variance-log.md`. Create a plan amendment named `plan-amendment-NNN-short-title-<short-id>.md` and request operator approval before proceeding when post-freeze variance affects architecture, APIs, data, security, privacy, compliance, scope, acceptance criteria, or plan feasibility.

## Planning artifact freeze gate

When this phase plan or phase-plan batch is ready for operator review, follow the repository-root reference `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: stage the draft without committing, request approval or feedback, revise directly on feedback, and commit only after explicit approval.

After the approval commit, use the canonical post-freeze prompt to confirm model, reasoning-effort, and sub-agent policy choices and ask whether implementation should begin now.

## Handoff output

Describe what the implementing agent must report at phase completion.

Include assigned scope, files inspected or changed, commands and tests run, assumptions, uncertainty or residual risk, and recommended next step. When sub-agents were authorized or used, include de-facto sub-agent count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.

## Completion criteria

- Phase objective is met.
- Validation commands have been run and recorded.
- Documentation tasks are complete or explicitly deferred with reason.
- `CHANGELOG.md` has a newest-first entry for the phase before each commit.
- Variance log is present and current.
- De-facto sub-agent use is reported when applicable, including count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.
