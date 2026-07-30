# Testing Guide Delta: Durable Planning Quality Clarity

Status: Proposed for implementation integration

## Proposed update

Use the current harness validator and template assembler when changing durable planning quality, plan-template prompts, or their evidence model:

1. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` after a focused policy or validator change.
2. When source blocks change, run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write`, then confirm `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` is current.
3. Plan Check prompts must record criterion coverage, method, expected result, and an evidence record. Routine plans may use local links; they do not need complete mapping tables unless a named benefit justifies one.
4. Plan Checks always identify `Covers: VER-NNN`. A local check appears after the task that runs it and must identify `Related task(s)`; cross-cutting checks belong in the shared Plan Checks section. The task relation is operational and does not establish conformance.
5. Record Plan Check results and `VER` conformance states during implementation, not in a plan. Plans define expected evidence; execution-quality guidance owns `met`, `not met`, `pending`, and `blocked` records.
6. Review `git diff --check` and the complete diff before committing, especially when a policy cleanup removes old validation code.

## Evidence from this work item

1. The new policy/template assertions failed before the quality and source-block changes, then passed after regeneration.
2. The local-link Plan Check fixture failed under the former mapping-heavy validator and passed after its focused replacement.
3. The task-local and shared Plan Check fixtures both pass while retaining required `VER` coverage and evidence-record fields.
