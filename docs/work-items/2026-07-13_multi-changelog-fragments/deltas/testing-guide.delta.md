# Testing Guide Delta

Work ID: `2026-07-13_multi-changelog-fragments`
Short ID: `multi-changelog-fragments`
Status: Approved
Harness release: `0.6+`

## Proposed update

For ordinary work-item commits, validate source-fragment grammar without requiring root consolidation:

```powershell
python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --lint
```

For release preparation and other root-completeness checkpoints, run lint followed by:

```powershell
python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --check
```

`--lint` must exit `0` for valid fragments even when their unreleased entries have not yet been consolidated. `--check` must exit nonzero for malformed fragments, duplicate headings, or valid unreleased entries missing from root `CHANGELOG.md`. Default mode remains the explicit write operation that inserts missing entries.

## Integration target

1. Apply this guidance to the release runbook and concise maintainer/operator guidance during implementation; do not create a repository-wide testing guide solely for this delta.
