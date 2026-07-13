# Operator Manual Delta

Work ID: `2026-07-13_multi-changelog-fragments`
Short ID: `multi-changelog-fragments`
Status: Approved
Harness release: `0.6+`

## Proposed update

Changelog fragment files are stable containers and may contain multiple independently valid, newest-first entries. Each entry has its own heading, exactly one release-target/package-impact/release-note metadata set, and change body.

Before an ordinary commit, update the matching fragment with a new entry and run the grammar-only lint gate. Do not require the root changelog to be complete at that point. Before preparing a release, run lint and the root-completeness check; if valid unreleased entries are missing, run the explicit write consolidation and review the root-changelog diff before renaming the release group.

## Integration target

1. Apply concise operator wording to `README.md` and the package-local operator note, and authoritative lifecycle/naming wording to their canonical references.
