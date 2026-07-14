# Testing Guide Delta

Work ID: `2026-07-14_plain-language-artifacts`

## Current policy checks

Run the focused harness-policy validator after changes to current authoring
guidance, modal-language routing, or commitment-template source blocks:

```powershell
python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py
```

The validator checks the canonical plain-language rule, the required
small/medium route, the shared prompt and generated specification templates,
every reusable template source block and generated template, and the declared
active authoring Markdown paths with their controlled exclusions.

After changing a template source block, regenerate and check assembled output:

```powershell
python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write
python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check
```

Before committing, inspect the declared authoring scope and the diff:

```powershell
rg -n -i '\bshall\b' AGENTS.md .agents/skills/dev-doc-harness
git diff --check
```
