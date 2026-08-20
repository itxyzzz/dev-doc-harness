# Testing Guide Delta: Superpowers Adapter Contract

Work ID: `2026-07-18_superpowers-adapter-contract`
Short ID: `superpowers-adapter-contract`
Status: Proposed
Harness release: `0.7+`

## Proposed Update

For Superpowers adapter changes, validate source-derived plan templates and the
active policy contract with:

```bash
python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check
python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py
python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --lint
```

Expected results:

1. The assembly check reports that all templates are current.
2. The policy validator reports `PASS compat.superpowers-adapter-contract` in addition to its existing checks.
3. Fragment lint accepts the work-item changelog entries.

The adapter validator checks active guidance, template source blocks, generated
templates, and synthetic positive and negative fixtures. It does not scan or
rewrite frozen historical work-item artifacts merely because their older
wording differs from current policy.
