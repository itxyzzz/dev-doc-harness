# Testing Guide Delta: Planning Template Clarity

Work ID: `2026-07-18_planning-template-clarity`
Short ID: `planning-template-clarity`
Status: Approved
Harness release: `0.7+`

## Proposed Update

For planning-template clarity changes, validate source blocks, generated
templates, lifecycle routing, and changelog grammar with:

```powershell
python .agents\skills\dev-doc-harness\scripts\assemble_templates.py --check
python .agents\skills\dev-doc-harness\scripts\test_harness_policy.py
python .agents\skills\dev-doc-harness\scripts\consolidate_changelog_fragments.py --lint
git diff --check
```

Expected results:

1. Template assembly reports that every generated template matches its source blocks and manifest.
2. Policy validation reports all checks as `PASS`, including the focused planning-template-clarity contract.
3. Fragment lint accepts the planning and implementation source entries and their synchronized planned subjects.
4. Diff checking reports no whitespace errors.

Focused fixtures cover literal completion checklists, complete repeated
commitment structure, absence of undefined classification, concise planned
commits, observed-versus-recommended model fields, conservative continuity,
single handoff ownership, rolling phase order, actual Superpowers metadata, and
history-safe structural enforcement. They also cover mandatory upcoming-stage
sub-agent assessment, a useful pending strategy that requests approval, an
approved in-envelope dispatch without repeated confirmation, a no-use rationale,
an unavailable-tool fallback, and out-of-envelope reapproval.
