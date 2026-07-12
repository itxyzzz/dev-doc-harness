# Testing Guide Delta

Work ID: `2026-07-09_changelog-fragment-consolidation`
Short ID: `changelog-fragment-consolidation`
Status: Implemented
Harness release: `0.5+`
Schema: `schema:delta.testing-guide`

## Delta

Harness maintenance checks now include changelog fragment consolidation behavior.

Run the full harness validator after changing lifecycle policy, freeze gates,
templates, operator guidance, release guidance, or consolidation behavior:

```bash
python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py
```

Run the consolidation script in check mode when the workflow needs to verify
that reviewed unreleased fragments are already present in root `CHANGELOG.md`:

```bash
python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --check
```

Run consolidation without `--check` at an operator-owned checkpoint when root
changelog completeness is required:

```bash
python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py
```

Expected signals:

1. `--check` exits nonzero when a valid unreleased fragment is missing from root
   `CHANGELOG.md` or when a fragment is malformed.
2. Write mode inserts missing unreleased fragment entries under `## Unreleased`
   and skips headings already present in root `CHANGELOG.md`.
3. `test_harness_policy.py` exercises valid insertion, duplicate skip,
   malformed metadata failure, and missing-fragment check failure with temporary
   fixtures.
