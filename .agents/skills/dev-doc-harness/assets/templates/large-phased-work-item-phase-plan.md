# Large or Phased Work Item Phase NN: <Phase Name>

Work ID: `<YYYY-MM-DD[_ISSUE-123]_short-kebab-title>`
Short ID: `<[ISSUE-123_]short-kebab-title>`
Status: Draft
Harness release: `<version or unknown>`
Schema: `schema:plan.phase`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:lifecycle.large-phase-orchestration`, `rule:quality.phase-plan-fresh-thread`, `rule:models.strategy-required`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.work-item-paths`, `rule:naming.artifact-filenames`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Objective

Describe the phase outcome.

## Input context

List the approved anchor spec or handoff snapshot, approved amendments, prior phase outputs, decisions, repository areas, and recorded context strategy the implementing agent must read. Confirm this phase plan follows `rule:lifecycle.large-phase-orchestration`. Preserve all applicable details from the large/phased work item spec; do not narrow, drop, or reinterpret spec decisions in the phase plan.

Follow the repository-root reference `.agents/skills/dev-doc-harness/references/durable-planning-quality.md` so this phase plan is executable by a fresh agent or thread.

## Likely files and areas

List files, directories, APIs, schemas, docs, or workflows expected to change.

## Model and Sub-agent Strategy

Current orchestration: record the model/profile and reasoning effort if known.
Fit assessment: judge complexity, risk, ambiguity, blast radius, budget, and latency.
Recommended change: record `None` or a concrete model/reasoning change with reason.

Sub-agents: record `None` with rationale, or list bounded phase-specific roles in the table. When this phase plan was drafted with a curated-artifact sub-agent, name the approved spec, amendments, prior phase outputs, and handoff artifacts used as input context. Use canonical model policy rules for strategy requirements, context strategy labels, approved-strategy authorization, and confirmation boundaries.

| Purpose | Context strategy | Input context | Output artifact | Model policy | Model class/profile | Reasoning effort | Reason | Parallel? | Blast radius if wrong |
|---|---|---|---|---|---|---|---|---|---|
| Example bounded explorer/reviewer/worker task; omit this table when sub-agents are `None` | curated prompt / curated artifacts / full-history fork / no repo context | Files, docs, specs, or decisions to read | Expected deliverable | Active repository policy unless changed by operator | Policy-relative class | low/medium/high | Selection rationale | Yes/No | Low/Medium/High plus consequence |

## Tasks

Write one checkbox per phase step. Include implementation, test, validation, documentation, and handoff work in execution order.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during phase-plan approval, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets. Update this table before committing if implementation changes the subject wording.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Phase plan approval | `[<issue-key> ]phase N plan: <title>[ -- <elaboration>]` | `<work-id>[ -- <elaboration>]` | Approval commit for this phase plan. |
| Phase implementation | `[<issue-key> ]<type>: <title>[ -- <elaboration>]` | `<work-id>[ -- <elaboration>]` | Add one row per expected phase implementation, validation, release, or maintenance commit. |

## Tests and validation

| Command | Expected result |
|---|---|
| Record the exact command before the phase starts | Record the expected signal for success or failure |

## Documentation tasks

List snapshot or delta artifacts this phase must create, update, or mark not applicable.

## Variance reminder

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

Record the draft review, approval commit, and post-freeze implementation authorization status for this phase plan.

## Handoff output

Describe what the implementing agent must report at phase completion.

Include assigned scope, files inspected or changed, commands and tests run, assumptions, uncertainty or residual risk, and recommended next step. When sub-agents were authorized or used, include de-facto sub-agent count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.

If planned implementation changes remain uncommitted, name the exact blocker or explicit no-commit instruction and include the current worktree status.

## Completion criteria

- Phase objective is met.
- Validation commands have been run and recorded.
- Documentation tasks are complete or explicitly deferred with reason.
- `CHANGELOG.md` has a newest-first entry for the phase before each commit.
- Commit subjects match the approved planned subjects or recorded variance, and changelog title snippets are synchronized.
- Planned implementation changes are committed, or the completion report names the exact blocker or explicit no-commit instruction plus current worktree status.
- Variance log is present and current.
- De-facto sub-agent use is reported when applicable, including count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.
