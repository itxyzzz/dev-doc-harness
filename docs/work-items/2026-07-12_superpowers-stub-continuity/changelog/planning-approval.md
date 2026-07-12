# Changelog Source

## 2026-07-12_superpowers-stub-continuity -- require historical packages before pointers

Release target: `unreleased`
Package impact: `planning-only`
Release-note: `source-only`

### Added

- Approved the combined spec, plan, and test cases for prohibiting creation of `docs/superpowers` unless the directory already contains earlier documentation packages needed for continuity.
- Preserved the existing pointer-only schema when that backward-compatibility condition is satisfied.

### Changed

- Planned aligned live policy wording, structural validator coverage, and inclusion of the operator's six manual stub deletions in the later implementation commit.
