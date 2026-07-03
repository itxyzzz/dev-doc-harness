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

1. Approved anchor spec: `<spec-filename or handoff snapshot>`.
2. Approved amendments: `<paths or None>`.
3. Prior phase outputs or handoffs: `<paths, commit hashes, notes, or None>`.
4. Architecture input: `<architecture decisions in approved spec, snapshots/architecture.snapshot.md, amendments, or None with reason>`.
5. Required snapshots or deltas: `<paths or None>`.
6. Relevant repository files, tests, docs, logs, or review comments: `<paths or notes>`.
7. Recorded context strategy from the anchor spec: `<curated artifacts / curated prompt / full-history fork / no repo context / not applicable>`.
8. Unresolved phase context to confirm before editing: `<questions, owners, or None identified>`.

Confirm this phase plan follows `rule:lifecycle.large-phase-orchestration`, preserves applicable details from the large/phased work item spec, and does not narrow, drop, or reinterpret spec decisions.
If architecture is missing, ambiguous, or changed before phase-plan freeze, update the draft spec or architecture snapshot when still draftable. After freeze, route architecture drift through variance handling and an amendment when `rule:lifecycle.variance-policy` requires approval.
