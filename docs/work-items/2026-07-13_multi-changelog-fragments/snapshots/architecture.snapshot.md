# Architecture Snapshot

Work ID: `2026-07-13_multi-changelog-fragments`
Short ID: `multi-changelog-fragments`
Status: Approved
Harness release: `0.6+`
Schema: `schema:snapshot.architecture`
Policy references: `module:lifecycle`, `module:quality`, `rule:lifecycle.work-item-architecture-decisions`, `rule:lifecycle.immutable-snapshots`, `rule:lifecycle.variance-policy`, `rule:quality.spec-handoff`

## Purpose

Preserve the entry-level parser and validation-gate boundaries that make multi-entry fragments safe without moving root consolidation into ordinary commit flow.

## Decision Ledger

### `DEC-001` Architecture Decision — Model fragments as ordered entry collections

Selected approach:

1. Parse each recognized heading-to-next-heading span as one entry, validate its metadata in that span, and flatten all valid entries across fragment paths for duplicate detection and consolidation.
2. Preserve the existing Markdown heading grammar, metadata values, body rendering, heading-based duplicate protection, and one-entry-file compatibility.

Affected boundaries:

1. Repositories: `D:\Code\dev-doc-harness` only.
2. Components or modules: `.agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py` and `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
3. Interfaces, schemas, config, or infra: the `--lint` and `--check` CLI modes; work-item Markdown fragment entry grammar.
4. Agentic, process, documentation, or phase boundaries: `.githooks/pre-commit`, canonical lifecycle/naming guidance, operator guidance, and the release-branch runbook.

Source spec sections:

1. `SPEC-001`, `SPEC-002`, and `SPEC-003` in `spec_multi-changelog-fragments.md`.

Validation cues:

1. `VER-001` through `VER-003`; `CHECK-001` through `CHECK-004` in `plan_multi-changelog-fragments.md`.

Rejected alternatives:

1. One entry per file: rejects valid commit history grouping for a filename-level constraint.
2. Structured manifests: adds migration and authoring burden without solving a demonstrated validation gap better than entry slicing.
3. `--check` in ordinary pre-commit: conflates source validity with intentionally deferred root publication.
4. Broadly loosening regex checks: weakens structural assertions beyond the README reflow problem.

## Decision Drivers

1. Release 0.6 preparation had to repair a valid two-entry fragment before consolidation could proceed.
2. Fragment syntax should fail near the authoring commit, while release completeness must fail before curation and release-group editing.
3. Documentation validation should protect meaning, not incidental Markdown wrapping.

## Constraints

1. Default write mode remains the sole mode that writes root `CHANGELOG.md`.
2. `--check` must retain lint behavior and root completeness semantics for release preparation.
3. Historical fragments remain untouched; source grammar remains Markdown and current metadata values remain valid.
4. The root-local hook is not part of the distributable package, but it must enforce the repository's ordinary-commit lint step.

## Future Durable-Doc Boundary

No repository-level architecture document is needed. This snapshot is the durable decision record for this bounded parser and workflow change.

## Approval

- Status: Approved
- Superseded by: None
