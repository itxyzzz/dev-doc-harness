### 2026-07-09_changelog-fragment-consolidation -- add work-item changelog sources

Release target: `unreleased`
Package impact: `distributable`
Release-note: `include`

#### Added

- Added work-item-local changelog fragment policy, template guidance, operator documentation, and a consolidation script for inserting reviewed unreleased fragments into root `CHANGELOG.md`.
- Added harness validation coverage for fragment parsing, duplicate-safe consolidation, check-mode failures, operator-owned checkpoints, and Dev Doc Harness distribution release-source compatibility.

#### Changed

- Changed routine harness commit guidance so independent work items update `docs/work-items/<work-id>/changelog/*.md` before commit and consolidate root `CHANGELOG.md` only at explicit checkpoints.
- Clarified that Dev Doc Harness distribution release policy is separate from release processes for downstream applications, packages, or agentic systems that use the harness.
