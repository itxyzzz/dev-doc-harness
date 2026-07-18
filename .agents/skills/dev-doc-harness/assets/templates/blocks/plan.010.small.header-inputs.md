# <Work Item Name> Plan

Work ID: `<work-id>`
Short ID: `<short-id>`
Status: Draft
Harness release: `<version or unknown>`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:artifact-style`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

Artifact style: small/medium plans must load `module:artifact-style`. Write final artifact content, resolve required decisions, remove authoring scaffolds, and use scannable sections, lists, and tables.

## Superpowers execution meta-header (conditional)

Render this compact meta-header only when the frozen plan records Superpowers as
the approved execution method after the harness freeze and continuity route.
State that the harness retains scope, model-policy bounds, variance handling,
and final integration. Omit the meta-header when another approved method will
execute the plan; it must not create a second approval route.

## Input Artifacts

Read these before finalizing implementation planning:

1. Approved spec: `<spec-filename>`.
2. Architecture input: `<architecture decisions in spec, snapshots/architecture.snapshot.md, or None with reason>`.
3. Required snapshots or deltas: `<paths or None>`.
4. Relevant repository files, tests, docs, logs, or review comments: `<paths or notes>`.
5. Unresolved implementation context to confirm before editing: `<questions, owners, or None identified>`.

If architecture is missing, ambiguous, or changed before freeze, update the draft spec or architecture snapshot before finalizing this plan. If architecture changes after freeze, use variance handling and an amendment when `rule:lifecycle.variance-policy` requires approval. Do not reinterpret architecture decisions in the plan.
