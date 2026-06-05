# <Work Item Name> Plan

Work ID: `<YYYY-MM-DD-short-kebab-title>` or `<YYYY-MM-DD-ISSUE-short-kebab-title>`
Short ID: `<short-kebab-title>` or `<ISSUE-short-kebab-title>`
Status: Draft

## Implementation summary

Describe the implementation approach in a few paragraphs.

## Files and interfaces

List files expected to change and interfaces expected to remain stable or change.

## Model and Sub-agent Strategy

Current orchestration: record the model/profile and reasoning effort if known.
Fit assessment: judge complexity, risk, ambiguity, blast radius, budget, and latency.
Recommended change: record `None` or a concrete model/reasoning change with reason.

Sub-agents: assess whether sub-agents are justified for substantial work even when the operator did not explicitly request them. Record `None` with a brief fit reason when no sub-agents are proposed. When proposing sub-agents or nondefault model/reasoning settings, follow the repository-root reference `.agents/skills/dev-doc-harness/references/subagent-model-policy.md` and capture only task-specific choices below.

After this plan is approved, frozen, and followed by the normal post-freeze operator authorization to begin implementation, the listed sub-agent strategy is authorized without a separate sub-agent-specific confirmation. Fresh confirmation is still required for unplanned sub-agents, stronger unrecorded model/reasoning choices, write-scope escalation, platform-restricted actions, or more than 3 concurrent sub-agents. Long-running work may use more than 3 total sub-agents in separate waves when this plan supports those waves and no more than 3 run concurrently.

| Purpose | Input context | Output artifact | Model policy | Model class/profile | Reasoning effort | Reason | Parallel? | Blast radius if wrong |
|---|---|---|---|---|---|---|---|---|
| Replace with a bounded explorer/reviewer/worker task, or omit this table when sub-agents are `None` | Files, docs, specs, or decisions to read | Expected deliverable | `economy-default` unless changed by operator | Policy-relative class | low/medium/high | Selection rationale | Yes/No | Low/Medium/High plus consequence |

## Tasks

Write one checkbox per implementation, test, validation, or documentation step. Each step should be specific enough for a fresh agent to execute without choosing an approach.

## Validation commands

| Command | Expected result |
|---|---|
| Record each command before implementation starts | Record the expected signal for success or failure |

## Plan variance handling

Before approval, operator feedback edits this draft directly and does not require an amendment. After the approval commit or explicit handoff snapshot, approved plans are immutable snapshots. Record nontrivial implementation variance in `implementation-notes/variance-log.md`. Create a plan amendment named `plan-amendment-NNN-short-title-<short-id>.md` and request operator approval before proceeding when post-freeze variance affects architecture, APIs, data, security, privacy, compliance, scope, acceptance criteria, or plan feasibility.

## Planning artifact freeze gate

When this plan is ready for operator review, follow the repository-root reference `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: stage the draft without committing, request approval or feedback, revise directly on feedback, and commit only after explicit approval.

After the approval commit, use the canonical post-freeze prompt to confirm model, reasoning-effort, and sub-agent policy choices and ask whether implementation should begin now.

## Completion criteria

- Acceptance criteria in `spec-<short-id>.md` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- Variance log is present and current.
- De-facto sub-agent use is reported when applicable, including count, roles/scopes, concurrency or waves, and de-facto model/model class/profile when known.

## Approval

- Status: Draft / Approved / Superseded
- Superseded by: blank unless superseded
