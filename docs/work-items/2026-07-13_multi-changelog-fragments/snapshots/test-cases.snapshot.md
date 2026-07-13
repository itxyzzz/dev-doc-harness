# Test Cases Snapshot

Work ID: `2026-07-13_multi-changelog-fragments`
Short ID: `multi-changelog-fragments`
Status: Approved
Harness release: `0.6+`

## Cases

### `TC-001` Two valid entries in one fragment

1. Given a fragment with two valid newest-first entries and an otherwise valid root changelog, `--lint` exits `0` even before root consolidation.
2. `--check` exits nonzero and names both missing headings without modifying the root changelog.
3. Default write mode inserts each entry exactly once under `## Unreleased`; a repeat write makes no duplicate insertion; `--check` then exits `0`.

### `TC-002` Metadata errors stay local to their entry

1. Given a valid first entry and a second entry with duplicate `Release target` plus missing `Release-note`, `--lint` exits nonzero.
2. Error output identifies the fragment path, the affected entry heading or ordinal context, and the violated metadata fields.

### `TC-003` Duplicate headings are rejected across entry locations

1. Given duplicate valid headings in two entries within one fragment, `--lint` and `--check` exit nonzero.
2. Error output identifies the duplicate heading and both occurrence contexts in the shared path.

### `TC-004` Lint remains independent of root completeness

1. Given a valid fragment and no root `CHANGELOG.md`, `--lint` exits `0` because it only checks fragment grammar and duplicates.
2. `--check` and write mode retain their existing root-changelog requirement.

### `TC-005` README prose reflow does not weaken semantic checks

1. The current README's package-boundary, work-item-exclusion, and rollback statements pass through a dedicated normalization helper that collapses whitespace and ignores case.
2. Structural policy checks continue to call the existing regular-expression helper.
