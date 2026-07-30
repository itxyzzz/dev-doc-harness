# Testing Guide Delta: Durable Planning Quality Clarity

Status: Proposed for implementation integration

## Proposed update

Use the current harness validator and template assembler when changing durable planning quality, plan-template prompts, or their evidence model:

1. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` after a focused policy or validator change.
2. When source blocks change, run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write`, then confirm `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` is current.
3. Plan Check prompts must record criterion coverage, method, expected result, and an evidence record. Routine plans may use local links; they do not need complete mapping tables unless a named benefit justifies one.
4. Review `git diff --check` and the complete diff before committing, especially when a policy cleanup removes old validation code.

## Evidence from this work item

1. The new policy/template assertions failed before the quality and source-block changes, then passed after regeneration.
2. The local-link Plan Check fixture failed under the former mapping-heavy validator and passed after its focused replacement.
