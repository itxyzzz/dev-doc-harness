# Large or Phased Work Item Phase NN: <Phase Name>

Work ID: `<work-id>`
Short ID: `<short-id>`
Status: Draft
Harness release: `<version or unknown>`
Schema: `schema:plan.phase`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:lifecycle.large-phase-orchestration`, `rule:quality.phase-plan-fresh-thread`, `rule:models.strategy-required`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Objective

Describe the phase outcome and how this phase advances the approved anchor spec without reinterpreting it.

## Input Artifacts

Read these before finalizing phase implementation planning:

- Approved anchor spec: `<spec-filename or handoff snapshot>`.
- Approved amendments: `<paths or None>`.
- Prior phase outputs or handoffs: `<paths, commit hashes, notes, or None>`.
- Required snapshots or deltas: `<paths or None>`.
- Relevant repository files, tests, docs, logs, or review comments: `<paths or notes>`.
- Recorded context strategy from the anchor spec: `<curated artifacts / curated prompt / full-history fork / no repo context / not applicable>`.
- Unresolved phase context to confirm before editing: `<questions, owners, or None identified>`.

Confirm this phase plan follows `rule:lifecycle.large-phase-orchestration`, preserves applicable details from the large/phased work item spec, and does not narrow, drop, or reinterpret spec decisions.

## Spec Traceability

Map the approved anchor spec to this phase without restating the whole spec. Use compact bullets or short blocks; avoid wide tables when cells need more than a few words.

Phase objective coverage:

- Anchor phase `<phase id or objective>`: implemented by `<task ids>`; verified by `<validation ids or acceptance criteria>`.

Requirement coverage:

- `REQ-001`: implemented by `<task ids or deferred to phase ids>`; verified by `<validation ids or acceptance criteria>`.

Acceptance coverage:

- `AC-001`: implemented by `<task ids or later phase ids>`; verified by `<validation ids, manual check, review finding, or operator acceptance path>`.

Risk and boundary coverage:

- `RISK-001` or scope boundary: handled by `<task ids, validation ids, later phase ids, or explicit no-op rationale>`.

## Implementation Approach

Describe the phase implementation approach in a few paragraphs. Focus on sequencing, dependencies, technical shape, integration points, and review strategy. Do not repeat the anchor spec except to explain phase-specific tradeoffs.

## Change Surfaces

Expected edits:

- `<file or directory>`: `<kind of change and boundary>`.

Stable interfaces:

- `<API, schema, config, template, workflow, or None>`: `<what must remain compatible>`.

Changed interfaces:

- `<API, schema, config, template, workflow, or None>`: `<what changes and who consumes it>`.

Implementation boundaries:

- `<nearby file, behavior, cleanup, later phase, or follow-up>` stays out of scope because `<reason>`.

Fresh-thread readiness:

- This phase should be safely executable by one orchestration thread with bounded delegation.
- If the phase still needs hidden chat context, split the phase, update the anchor spec before freeze, or create an amendment after freeze.

## Model and Sub-agent Strategy

Use `module:models`, including `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, and `rule:models.fresh-confirmation`. Record only the compact strategy needed for this phase.

Current orchestration:

- Model/profile and reasoning effort if known: `<value or not exposed>`.

Fit assessment:

- Complexity: `<low/medium/high plus reason>`.
- Risk and blast radius: `<low/medium/high plus consequence>`.
- Ambiguity: `<low/medium/high plus reason>`.
- Budget and latency fit: `<acceptable constraints or tradeoff>`.

Recommended orchestration change:

- `<None, or concrete model/profile/reasoning change with reason>`.

Sub-agents:

- `<None with rationale, or bounded strategy below>`.

When this phase plan was drafted with a curated-artifact sub-agent, name the approved spec, amendments, prior phase outputs, and handoff artifacts used as input context. For each proposed phase-specific sub-agent, record a short block:

Sub-agent `<role or task id>`:

- Purpose: `<bounded task-specific purpose>`.
- Context strategy: `<curated prompt / curated artifacts / full-history fork / no repo context>`.
- Input context: `<files, specs, docs, diffs, decisions, or supplied text>`.
- Output artifact: `<notes, review findings, patch scope, test list, or other deliverable>`.
- Model policy: `<active repository policy unless changed by operator>`.
- Model class/profile: `<policy-relative class or concrete profile if required>`.
- Reasoning effort: `<low/medium/high plus reason>`.
- Selection reason: `<why this delegation is useful>`.
- Parallel execution: `<Yes/No and dependency>`.
- Blast radius if wrong: `<Low/Medium/High plus consequence>`.

## Task Plan

Write one checkbox per implementation, test, validation, documentation, or handoff step. Tasks should be SMART:

- Specific enough that a fresh implementation agent or delegated sub-agent knows which files, behavior, tests, docs, or decisions are in scope.
- Measurable through a linked acceptance criterion, validation command, review finding, or explicit artifact update.
- Achievable within this phase and one orchestration thread with bounded delegation.
- Relevant to the approved anchor spec, phase objective, acceptance criterion, risk, interface, documentation need, or commit boundary.
- Time-bounded by lifecycle checkpoint, such as before editing, before validation, before commit, or during final review.

Order tasks by implementation dependency and reviewability. Label dependencies explicitly as `Dependencies: <None, task ids, artifacts, prior phase, or external event>`. Do not force vertical slices when shared setup, tests, refactors, or interface updates need to happen first.

- [ ] `<T-001>` Dependencies: `<None or task/artifact ids>`; `<specific task with files/scope>`; Traces: `<REQ/AC/risk/phase ids>`.
- [ ] `<T-002>` Dependencies: `<T-001 or None>`; `<specific validation, documentation, changelog, or review task>`; Traces: `<AC/risk/phase ids>`.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during phase-plan approval, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets. Update this section before committing if implementation changes the subject wording.

Phase plan approval:

- Planned subject: `<planning-commit-subject>`.
- Changelog title or snippet: `<changelog-heading>`.
- Notes: `Approval commit for this phase plan.`

Phase implementation:

- Planned subject: `<commit-subject>`.
- Changelog title or snippet: `<changelog-heading>`.
- Notes: `<add one block per expected phase implementation, validation, release, or maintenance commit>`.

## Validation Plan

| Command | Expected result |
|---|---|
| `<exact command, manual check, review finding, or operator acceptance path>` | `<expected signal and linked AC/risk/phase coverage>` |

Every validation entry must state the expected signal before phase implementation starts. Include command exit behavior, important output text, manual observation, review criterion, or operator acceptance condition as applicable.

## Documentation Tasks

List snapshot or delta artifacts this phase must create, update, or mark not applicable.

- Changelog: `CHANGELOG.md` before each commit.
- Test cases: `<snapshot path or not applicable with reason>`.
- Testing guide delta: `<delta path or not applicable with reason>`.
- Operator manual delta: `<delta path or not applicable with reason>`.
- API reference delta: `<delta path or not applicable with reason>`.
- Architecture snapshot or summary delta: `<path or not applicable with reason>`.

## Plan variance handling

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

Record the draft review, approval commit, and post-freeze implementation authorization status for this phase plan.

## Handoff output

Describe what the implementing agent must report at phase completion.

Include assigned scope, files inspected or changed, commands and tests run, assumptions, uncertainty or residual risk, and recommended next step. When sub-agents were authorized or used, include de-facto sub-agent count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.

If planned implementation changes remain uncommitted, name the exact blocker or explicit no-commit instruction and include the current worktree status.

## Plan readiness checklist

- [ ] Input artifacts and relevant repository context have been read and listed.
- [ ] The phase preserves the approved anchor spec, amendments, and prior phase outputs without silent reinterpretation.
- [ ] Every in-phase requirement and acceptance criterion has at least one task and one validation path.
- [ ] Deferred requirements, risks, boundaries, interfaces, and documentation decisions are covered by later phase references or explicit no-op rationale.
- [ ] Task detail is sufficient for a fresh implementation agent or delegated sub-agent to execute its assigned part without inventing task order, file scope, validation, or documentation steps.
- [ ] Validation entries have exact commands, manual checks, review findings, or operator acceptance paths with expected signals.
- [ ] Planned commits and changelog title snippets are synchronized.
- [ ] Variance handling is clear for likely implementation drift.
- [ ] This phase fits one orchestration thread with bounded delegation. If it does not, split the phase, re-scope it, or amend the anchor before freeze.
- [ ] Sub-agent strategy follows `module:models`, or `Sub-agents: None` has a brief fit rationale.
- [ ] No unresolved placeholders remain before approval or handoff.

## Completion criteria

- Phase objective is met.
- Acceptance criteria assigned to this phase are met or explicitly deferred to named later phases.
- Validation commands have been run and recorded.
- Documentation tasks are complete or explicitly deferred with reason.
- The frozen phase plan had enough detail for each assigned execution part or delegated sub-agent to proceed safely.
- Execution remained within one orchestration thread with a bounded sub-agent strategy; otherwise the phase was split, re-scoped, or amended before implementation.
- `CHANGELOG.md` has a newest-first entry for the phase before each commit.
- Commit subjects match the approved planned subjects or recorded variance, and changelog title snippets are synchronized.
- Planned implementation changes are committed, or the completion report names the exact blocker or explicit no-commit instruction plus current worktree status.
- Variance log is present and current.
- De-facto sub-agent use is reported when applicable, including count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.

## Approval

- Status: Draft / Approved / Superseded
- Superseded by: record only when this artifact is superseded
