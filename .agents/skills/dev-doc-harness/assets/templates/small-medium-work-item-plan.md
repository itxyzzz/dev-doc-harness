# <Work Item Name> Plan

Work ID: `<work-id>`
Short ID: `<short-id>`
Status: Draft
Harness release: `<version or unknown>`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Input Artifacts

Read these before finalizing implementation planning:

- Approved spec: `<spec-filename>`
- Required snapshots or deltas: `<paths or None>`
- Relevant repository files, tests, docs, logs, or review comments: `<paths or notes>`
- Unresolved implementation context to confirm before editing: `<questions, owners, or None identified>`

## Spec Traceability

Map the approved spec to execution without restating the spec. Use compact bullets or short blocks; avoid wide tables when cells need more than a few words.

Requirement coverage:

- `REQ-001`: implemented by `<task ids>`; verified by `<validation ids or acceptance criteria>`.

Acceptance coverage:

- `AC-001`: implemented by `<task ids>`; verified by `<validation ids, manual check, review finding, or operator acceptance path>`.

Risk and boundary coverage:

- `RISK-001` or scope boundary: handled by `<task ids, validation ids, or explicit no-op rationale>`.

## Implementation Approach

Describe the implementation approach in a few paragraphs. Focus on sequencing, dependencies, technical shape, and review strategy. Do not repeat the spec's source intent, requirements, or acceptance criteria except to explain implementation tradeoffs.

## Change Surfaces

Expected edits:

- `<file or directory>`: `<kind of change and boundary>`

Stable interfaces:

- `<API, schema, config, template, workflow, or None>`: `<what must remain compatible>`

Changed interfaces:

- `<API, schema, config, template, workflow, or None>`: `<what changes and who consumes it>`

Implementation boundaries:

- `<nearby file, behavior, cleanup, or follow-up>` stays out of scope because `<reason>`.

## Model and Sub-agent Strategy

Use `module:models`, including `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, and `rule:models.fresh-confirmation`. Record only the compact strategy needed for this work item.

Current orchestration:

- Model/profile and reasoning effort if known: `<value or not exposed>`

Fit assessment:

- Complexity: `<low/medium/high plus reason>`
- Risk and blast radius: `<low/medium/high plus consequence>`
- Ambiguity: `<low/medium/high plus reason>`
- Budget and latency fit: `<acceptable constraints or tradeoff>`

Recommended orchestration change:

- `<None, or concrete model/profile/reasoning change with reason>`

Sub-agents:

- `<None with rationale, or bounded strategy below>`

Use sub-agents only when they improve isolation, review quality, parallel exploration, specialized execution, or risk reduction enough to justify the coordination cost. Small/medium plans may use a bounded number of sub-agents, but if the work needs many sub-agents, multiple waves, or additional planning hierarchy to stay understandable, split, re-scope, or escalate to large/phased handling.

For each proposed sub-agent, record a short block:

Sub-agent `<role or task id>`:

- Purpose: `<bounded task-specific purpose>`
- Context strategy: `<curated prompt / curated artifacts / full-history fork / no repo context>`
- Input context: `<files, specs, docs, diffs, decisions, or supplied text>`
- Output artifact: `<notes, review findings, patch scope, test list, or other deliverable>`
- Model policy: `<active repository policy unless changed by operator>`
- Model class/profile: `<policy-relative class or concrete profile if required>`
- Reasoning effort: `<low/medium/high plus reason>`
- Selection reason: `<why this delegation is useful>`
- Parallel execution: `<Yes/No and dependency>`
- Blast radius if wrong: `<Low/Medium/High plus consequence>`

## Task Plan

Write one checkbox per implementation, test, validation, or documentation step. Tasks should be SMART:

- Specific enough that a fresh implementation agent or delegated sub-agent knows which files, behavior, tests, docs, or decisions are in scope.
- Measurable through a linked acceptance criterion, validation command, review finding, or explicit artifact update.
- Achievable within the approved small/medium scope and one orchestration thread with bounded delegation.
- Relevant to a spec requirement, acceptance criterion, risk, interface, documentation need, or commit boundary.
- Time-bounded by lifecycle checkpoint, such as before editing, before validation, before commit, or during final review.

Order tasks by implementation dependency and reviewability. Label dependencies explicitly as `Dependencies: <None, task ids, artifacts, or external event>`. Do not force vertical slices when shared setup, tests, refactors, or interface updates need to happen first.

- [ ] `<T-001>` Dependencies: `<None or task/artifact ids>`; `<specific task with files/scope>`; Traces: `<REQ/AC/risk ids>`.
- [ ] `<T-002>` Dependencies: `<T-001 or None>`; `<specific validation, documentation, changelog, or review task>`; Traces: `<AC/risk ids>`.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during plan approval, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets. Update this table before committing if implementation changes the subject wording.

Planning approval commit:

- Planned subject: `<planning-commit-subject>`
- Changelog title or snippet: `<changelog-heading>`
- Notes: `<approval commit for this spec and plan, or replace with the artifact set being approved>`

Implementation commit:

- Planned subject: `<commit-subject>`
- Changelog title or snippet: `<changelog-heading>`
- Notes: `<add one block per expected implementation, validation, release, or maintenance commit>`

## Validation Plan

| Command | Expected result |
|---|---|
| `<exact command, manual check, review finding, or operator acceptance path>` | `<expected signal and linked AC/risk coverage>` |

Every validation entry must state the expected signal before implementation starts. Include command exit behavior, important output text, manual observation, review criterion, or operator acceptance condition as applicable.

## Plan variance handling

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

Record the draft review, approval commit, and post-freeze implementation authorization status for this plan.

## Plan readiness checklist

- [ ] Input artifacts and relevant repository context have been read and listed.
- [ ] Every spec requirement and acceptance criterion has at least one task and one validation path.
- [ ] Risks, scope boundaries, interfaces, and documentation decisions are either covered by tasks or explicitly marked as no-op with a reason.
- [ ] Task detail is sufficient for a fresh implementation agent or delegated sub-agent to execute its assigned part without inventing task order, file scope, validation, or documentation steps.
- [ ] Validation entries have exact commands, manual checks, review findings, or operator acceptance paths with expected signals.
- [ ] Planned commits and changelog title snippets are synchronized.
- [ ] Variance handling is clear for likely implementation drift.
- [ ] The work still fits one orchestration thread with a bounded sub-agent strategy. If it does not, split, re-scope, or escalate to large/phased handling before freeze.
- [ ] Sub-agent strategy follows `module:models`, or `Sub-agents: None` has a brief fit rationale.
- [ ] No unresolved placeholders remain before approval or handoff.

## Completion criteria

- Acceptance criteria in `<spec-filename>` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- The frozen plan had enough detail for each assigned execution part or delegated sub-agent to proceed safely.
- Execution remained within one orchestration thread with a bounded sub-agent strategy; otherwise the work was split, re-scoped, or escalated before implementation.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- Commit subjects match the approved planned subjects or recorded variance, and changelog title snippets are synchronized.
- Planned implementation changes are committed, or the completion report names the exact blocker or explicit no-commit instruction plus current worktree status.
- Variance log is present and current.
- De-facto sub-agent use is reported when applicable, including count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.

## Approval

- Status: Draft / Approved / Superseded
- Superseded by: record only when this artifact is superseded
