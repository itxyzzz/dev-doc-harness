# Test Cases Snapshot

Work ID: `2026-07-09_changelog-fragment-consolidation`
Short ID: `changelog-fragment-consolidation`
Status: Approved
Harness release: `0.5+`
Schema: `schema:snapshot.test-cases`
Policy references: `module:lifecycle`, `module:quality`, `rule:lifecycle.immutable-snapshots`, `rule:quality.spec-handoff`

## Purpose

Capture the expected validation scenarios for work-item-local changelog fragments and root changelog consolidation before implementation begins.

## Test Cases

### `TC-001` Valid fragment is accepted

Verifies:

1. `REQ-001`
2. `REQ-003`
3. `AC-002`

Scenario:

1. A file under `docs/work-items/2026-07-09_example/changelog/implementation.md` contains one changelog heading plus exactly one `Release target`, `Package impact`, and `Release-note` field.
2. The fragment has a Keep a Changelog subsection such as `#### Changed`.

Expected result:

1. Fragment validation succeeds.
2. The parsed heading and body are available for consolidation.

### `TC-002` Missing metadata is rejected

Verifies:

1. `REQ-001`
2. `REQ-006`
3. `AC-002`
4. `AC-007`

Scenario:

1. A fragment lacks `Release-note`, or contains duplicate `Release target` fields.

Expected result:

1. Validation fails.
2. Error output names the fragment path and the missing or duplicated metadata field.

### `TC-003` Consolidation inserts missing unreleased entries

Verifies:

1. `REQ-003`
2. `AC-004`

Scenario:

1. Root `CHANGELOG.md` has a `## Unreleased` section.
2. A valid fragment heading is absent from root changelog.
3. Consolidation runs in write mode.

Expected result:

1. The fragment entry appears under `## Unreleased`.
2. Existing root changelog content outside the insertion location is preserved.

### `TC-004` Consolidation skips duplicate headings

Verifies:

1. `REQ-003`
2. `AC-004`

Scenario:

1. Root `CHANGELOG.md` already contains a heading matching a valid fragment.
2. Consolidation runs in write mode.

Expected result:

1. The root changelog is not given a duplicate entry.
2. Existing root entry text is preserved.

### `TC-005` Check mode reports unconsolidated fragments

Verifies:

1. `REQ-003`
2. `REQ-006`
3. `AC-004`
4. `AC-007`

Scenario:

1. A valid fragment exists.
2. Root `CHANGELOG.md` lacks the fragment heading.
3. Consolidation runs with `--check`.

Expected result:

1. The command exits nonzero.
2. Output identifies the fragment heading missing from root changelog.
3. Root `CHANGELOG.md` is not modified.

### `TC-006` Check mode passes after idempotent consolidation

Verifies:

1. `REQ-003`
2. `REQ-006`
3. `AC-004`
4. `AC-007`

Scenario:

1. A valid fragment has already been consolidated into root `CHANGELOG.md`.
2. Consolidation runs with `--check`.

Expected result:

1. The command exits successfully.
2. No file changes are produced.

### `TC-007` Harness maintainer release process consolidates before curation

Verifies:

1. `REQ-004`
2. `REQ-005`
3. `AC-005`

Scenario:

1. A Dev Doc Harness release branch is being prepared in this repository.
2. There are valid unreleased fragment entries not present in root `CHANGELOG.md`.

Expected result:

1. `docs/release-branch-process.md` instructs the agent to run or verify consolidation before renaming `## Unreleased`.
2. Package-local Dev Doc Harness release notes are curated from the consolidated root changelog.

### `TC-008` Downstream operator guidance keeps product release process out of scope

Verifies:

1. `REQ-005`
2. `AC-006`

Scenario:

1. A downstream project uses the harness to manage work-item artifacts while the project has its own release, deployment, or publication process.

Expected result:

1. Operator-facing guidance tells the project to run changelog consolidation at a project-owned checkpoint such as after merge, before preparing release notes, before product/application release, or wherever root changelog completeness is needed.
2. The guidance does not require the downstream project to follow the Dev Doc Harness maintainer release branch process.

### `TC-009` Templates no longer require root changelog for ordinary commits

Verifies:

1. `REQ-002`
2. `REQ-005`
3. `AC-001`
4. `AC-006`

Scenario:

1. A future small/medium or phase plan is created from current templates after implementation.

Expected result:

1. The documentation matrix names `docs/work-items/<work-id>/changelog/*.md` as the routine before-commit changelog source.
2. The template mentions root `CHANGELOG.md` consolidation at operator-owned checkpoints such as after merge, before release-note preparation, or before product/application release.

### `TC-010` Remaining root changelog references are intentional

Verifies:

1. `REQ-005`
2. `REQ-006`
3. `AC-006`
4. `AC-007`

Scenario:

1. A repository search finds references to `CHANGELOG.md` in current harness docs and templates.

Expected result:

1. Remaining current references describe root publication, consolidation, operator-owned checkpoints, Dev Doc Harness release prep, historical context, or this work item's transition.
2. No current policy or template says ordinary independent work-item commits must update root `CHANGELOG.md` directly after implementation.

## Approval

- Status: Approved
- Superseded by: None
