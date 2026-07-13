# Testing Guide Delta

Work ID: `2026-07-13_model-selection-calibration`
Short ID: `model-selection-calibration`
Status: Approved
Harness release: `0.6+`

## Proposed update

After changing current model-policy text, role examples, source template blocks, generated templates, or structural policy validation, run:

```powershell
python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check
python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py
git diff --check
```

The assembly check must report `All assembled templates are current.`. The policy validator must exit successfully after confirming the calibrated baseline, escalation/de-escalation boundary, independent-review shape, and non-duplicative template ownership. Diff review must confirm that policy semantics remain canonical and that no unrelated root instruction, README, frozen historical artifact, or root changelog edit was added without approved variance.

## Integration target

1. Keep this as work-item implementation evidence unless a later operator-owned testing-guide surface needs the command set; do not create a repository-wide testing guide solely for this delta.
