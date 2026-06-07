# Operator Manual Delta

Work ID: `2026-06-07-release-versioning`
Phase: Phase 02 release package implementation

## Package Boundary

The copyable Dev Doc Harness package is root `AGENTS.md` plus `.agents/`.

Do not copy this repository's `docs/work-items/`, root `README.md`, root `CHANGELOG.md`, root `TODO.md`, `.git/`, or local development files into downstream projects.

## Team Adoption

1. Copy root `AGENTS.md` and `.agents/` from the release into the target repository.
2. Merge project-specific `AGENTS.md` instructions carefully when the target already has them.
3. Confirm `.agents/skills/dev-doc-harness/VERSION` records the adopted release.
4. Run the harness validation command when practical.
5. Commit or open a PR for the harness update separately from product work.

## Rollback

Rollback is by reverting the dedicated harness update commit or PR. Preserve the target repository's own `docs/work-items/` unless a project-specific cleanup plan says otherwise.

## Release Notes Source

Package-local release notes live under `.agents/skills/dev-doc-harness/docs/releases/` and are curated from root `CHANGELOG.md`. Planning changelog entries are source evidence; release notes summarize delivered package-facing changes once.
