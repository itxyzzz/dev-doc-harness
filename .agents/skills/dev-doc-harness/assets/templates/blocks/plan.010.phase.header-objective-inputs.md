# Large or Phased Work Item Phase NN: <Phase Name>

Work ID: `<work-id>`
Short ID: `<short-id>`
Status: Draft
Harness release: `<version or unknown>`
Schema: `schema:plan.phase`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `rule:lifecycle.large-phase-orchestration`, `rule:quality.phase-plan-fresh-thread`, `rule:models.strategy-required`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`
Execution method: `<approved method, or omit when not selected>`
Current orchestration session: Generation, capability tier, reasoning, resolved profile, and context visibility: `<exposed facts, or omit when not exposed or material>`.

Artifact style baseline: write final artifact content, resolve required decisions, remove authoring scaffolds, and use scannable sections, lists, and tables. Load `module:artifact-style` when the phase plan becomes large or hard to scan.

When Superpowers is the approved execution method, record it in the metadata
above. The harness retains scope, model-policy bounds, variance handling,
approved commit boundaries, and final integration; do not add a second route.

## Objective

State the phase outcome and how this phase advances the approved anchor spec without reinterpreting it.

## Input Artifacts

Read these before finalizing phase implementation planning:

1. Approved anchor spec: `<spec-filename>`.
2. Approved amendments: `<paths or None>`.
3. Prior phase outputs or handoffs: `<paths, commit hashes, notes, or None>`.
4. Architecture input: `<architecture decisions in approved spec, snapshots/architecture.snapshot.md, amendments, or None with reason>`.
5. Required snapshots or deltas: `<paths or None>`.
6. Relevant repository files, tests, docs, logs, or review comments: `<paths or notes>`.
7. Recorded context strategy from the anchor spec: `<curated artifacts / curated prompt / full-history fork / no repo context / not applicable>`.
8. Unresolved phase context to confirm before editing: `<questions, owners, or None identified>`.

Confirm this phase plan follows `rule:lifecycle.large-phase-orchestration`, preserves applicable details from the large/phased work item spec, and does not narrow, drop, or reinterpret spec decisions.
If architecture is missing, ambiguous, or changed before phase-plan freeze, update the draft spec or architecture snapshot when still draftable. After freeze, route architecture drift through variance handling and an amendment when `rule:lifecycle.variance-policy` requires approval.
