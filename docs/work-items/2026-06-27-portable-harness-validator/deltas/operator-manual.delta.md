# Operator Manual Delta: Portable Harness Validator

Work ID: `2026-06-27-portable-harness-validator`
Short ID: `portable-harness-validator`
Status: Proposed
Harness release: `0.3.0`

## Proposed Update

The active harness maintenance validation command is now cross-platform Python:

```bash
python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py
```

The previous PowerShell command is no longer supported as an active validator surface. Frozen historical work-item artifacts may still mention the old command as review history.

Operators adopting the harness should continue copying root `AGENTS.md` plus `.agents/` as the distributable package and should run validation when practical after merging local instructions.
