# <Work Item Name> Plan

Work ID: `<work-id>`
Short ID: `<short-id>`
Status: Draft
Harness release: `<version or unknown>`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`
Execution method: `<approved method, or omit when not selected>`
Current orchestration session: Resolved model profile and Context visibility: `<exposed material facts; omit unless exposed and material>`.

Artifact readability: follow the `module:quality` baseline for final artifact content, resolved decisions, and scannable structure. Load `module:artifact-style` when the plan becomes large or hard to scan.

When Superpowers is the approved execution method, record it in the metadata above. The harness retains scope, model-policy bounds, variance handling, approved commit boundaries, and final integration; do not add a second route.

## Input Artifacts

Read these before finalizing implementation planning:

1. Approved spec: `<spec-filename>`.
2. Architecture input: `<architecture decisions in spec, snapshots/architecture.snapshot.md, or None with reason>`.
3. Required snapshots or deltas: `<paths or None>`.
4. Relevant repository files, tests, docs, logs, or review comments: `<paths or notes>`.
5. Unresolved implementation context to confirm before editing: `<questions, owners, or None identified>`.

If architecture is missing, ambiguous, or changed before freeze, update the draft spec or architecture snapshot before finalizing this plan. If architecture changes after freeze, use variance handling and an amendment when `rule:lifecycle.variance-policy` requires approval. Do not reinterpret architecture decisions in the plan.
