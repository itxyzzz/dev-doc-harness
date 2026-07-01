# <Work Item Name> Plan

Work ID: `<work-id>`
Short ID: `<short-id>`
Status: Draft
Harness release: `<version or unknown>`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Implementation summary

Describe the implementation approach in a few paragraphs.

## Files and interfaces

List files expected to change and interfaces expected to remain stable or change.

## Model and Sub-agent Strategy

Current orchestration: record the model/profile and reasoning effort if known.
Fit assessment: judge complexity, risk, ambiguity, blast radius, budget, and latency.
Recommended change: record `None` or a concrete model/reasoning change with reason.

Sub-agents: record `None` with rationale, or list bounded task-specific roles in the table. Use canonical model policy rules for strategy requirements, context strategy labels, approved-strategy authorization, and confirmation boundaries.

| Purpose | Context strategy | Input context | Output artifact | Model policy | Model class/profile | Reasoning effort | Reason | Parallel? | Blast radius if wrong |
|---|---|---|---|---|---|---|---|---|---|
| Example bounded explorer/reviewer/worker task; omit this table when sub-agents are `None` | curated prompt / curated artifacts / full-history fork / no repo context | Files, docs, specs, or decisions to read | Expected deliverable | Active repository policy unless changed by operator | Policy-relative class | low/medium/high | Selection rationale | Yes/No | Low/Medium/High plus consequence |

## Tasks

Write one checkbox per implementation, test, validation, or documentation step. Each step should be specific enough for a fresh agent to execute without choosing an approach.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during plan approval, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets. Update this table before committing if implementation changes the subject wording.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `<planning-commit-subject>` | `<changelog-heading>` | Approval commit for this spec and plan, or replace with the artifact set being approved. |
| Implementation | `<commit-subject>` | `<changelog-heading>` | Add one row per expected implementation, validation, release, or maintenance commit. |

## Validation commands

| Command | Expected result |
|---|---|
| Record the exact command before implementation starts | Record the expected signal for success or failure |

## Plan variance handling

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

Record the draft review, approval commit, and post-freeze implementation authorization status for this plan.

## Completion criteria

- Acceptance criteria in `<spec-filename>` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- Commit subjects match the approved planned subjects or recorded variance, and changelog title snippets are synchronized.
- Planned implementation changes are committed, or the completion report names the exact blocker or explicit no-commit instruction plus current worktree status.
- Variance log is present and current.
- De-facto sub-agent use is reported when applicable, including count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.

## Approval

- Status: Draft / Approved / Superseded
- Superseded by: record only when this artifact is superseded
