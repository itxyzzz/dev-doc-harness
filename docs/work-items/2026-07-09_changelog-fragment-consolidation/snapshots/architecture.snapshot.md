# Architecture Snapshot

Work ID: `2026-07-09_changelog-fragment-consolidation`
Short ID: `changelog-fragment-consolidation`
Status: Approved
Harness release: `0.5+`
Schema: `schema:snapshot.architecture`
Policy references: `module:lifecycle`, `module:quality`, `module:release`, `rule:lifecycle.work-item-architecture-decisions`, `rule:lifecycle.immutable-snapshots`, `rule:lifecycle.variance-policy`, `rule:quality.spec-handoff`, `rule:release.changelog-source`

## Purpose

Capture the work-item architecture decision that separates branch-local changelog source evidence from the root changelog publication view, while keeping harness distribution release policy separate from downstream product/application release processes. This snapshot is the durable decision record future implementation and review must preserve.

## Decision Ledger

### `DEC-001` Use work-item-local fragments as changelog source evidence

Selected approach:

1. Ordinary harness work-item commits record changelog evidence in `docs/work-items/<work-id>/changelog/*.md`.
2. Root `CHANGELOG.md` remains the curated publication view after explicit consolidation.
3. In this repository, the consolidated root changelog remains the source for Dev Doc Harness distribution release notes.
4. A harness script validates fragment shape and consolidates missing unreleased fragment entries into root `CHANGELOG.md`.
5. This approach removes routine same-file edit pressure during parallel worktree development while preserving pre-commit audit evidence, root publication, and harness distribution release-note traceability.

Affected boundaries:

1. Repositories: this repository and downstream repositories that adopt the harness package.
2. Components or modules: `.agents/skills/dev-doc-harness/references/`, `.agents/skills/dev-doc-harness/assets/templates/`, `.agents/skills/dev-doc-harness/scripts/`, `docs/release-branch-process.md`, `README.md`, `.agents/skills/dev-doc-harness/docs/operator-note.md`, and `CHANGELOG.md`.
3. Interfaces, schemas, config, or infra: changelog entry schema, documentation matrix expectations, freeze-gate staged-file contract, consolidation script command interface, and Dev Doc Harness release-note source workflow.
4. Agentic, process, documentation, or phase boundaries: before-commit changelog source update, planning approval freeze, implementation commit preparation, operator-owned integration or publication consolidation, downstream release-process boundary, and Dev Doc Harness maintainer release branch preparation.

Source spec sections:

1. `REQ-001` Work-item-local changelog source fragments.
2. `REQ-002` Fragment-first commit policy.
3. `REQ-003` Root changelog consolidation mechanism.
4. `REQ-004` Harness distribution release-source compatibility.
5. `AC-001` through `AC-007`.
6. `RISK-001`, `RISK-002`, `RISK-003`, `RISK-005`, and `RISK-006`.

Validation cues:

1. Manual review proves policy, templates, operator docs, and Dev Doc Harness maintainer release guidance describe the same source/publication split.
2. The consolidation script inserts missing unreleased fragments without duplicating existing root headings.
3. Harness validation covers fragment policy discoverability, consolidation behavior, and release-source compatibility.
4. Dev Doc Harness maintainer release branch guidance consolidates before package-local release-note curation.
5. Operator guidance states downstream projects keep their own release process and choose where consolidation belongs.

Rejected alternatives:

1. Custom Git merge driver: rejected because it still makes every branch write root `CHANGELOG.md` and risks hiding semantic conflicts in release metadata or curated text.
2. Root-only manual reconciliation: rejected because it preserves the current bottleneck.
3. Fully generated root changelog: rejected as the first step because this repository uses a curated root changelog and Dev Doc Harness release-note source flow.
4. Dev Doc Harness release notes directly from fragments: rejected because it would create a second feature-history source and weaken the existing root changelog release contract.

## Decision Drivers

1. Parallel worktrees should not conflict when their implementation scopes are independent.
2. Every commit still needs durable changelog evidence synchronized with planned commit subjects.
3. Root `CHANGELOG.md` must remain human-readable and, in this repository, useful as Dev Doc Harness release-note source material.
4. Harness maintainer release preparation should stay explicit and reviewable.
5. Downstream applications, packages, and agentic systems keep their own release processes; the harness should provide a consolidation step that operators can place in those processes.
5. Historical artifacts and root changelog entries should not be rewritten solely for process migration.

## Constraints

1. Current root changelog rules apply until this work is implemented and committed.
2. Fragment entries must keep existing changelog heading and metadata conventions.
3. Consolidation must be deterministic and idempotent.
4. Consolidation must not silently rewrite existing root changelog entries.
5. Dev Doc Harness release notes remain curated from root `CHANGELOG.md` after consolidation.
6. The harness must not prescribe downstream product/application release flow beyond the changelog source and consolidation contract it owns.
6. Planning freeze gates must still stage only intended files and stop before implementation.

## Future Durable-Doc Boundary

Repository-level durable architecture documents such as `ARCHITECTURE.md` are future work for a separate harness extension. Use `deltas/architecture-summary.delta.md` only if implementation creates operator-facing architecture guidance that should later move into long-lived documentation.

## Approval

- Status: Approved
- Superseded by: None
