# TASK-001 Red-Phase Record

Work ID: `2026-07-13_model-selection-calibration`
Task: `TASK-001` — Add focused calibration regression checks
Execution instance: `2026-07-14` fresh task with curated-artifact handoff
Status: Expected pre-change failure recorded

## Command

```powershell
python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py
```

## Result

Exit code: `1` (expected before `TASK-002` and `TASK-003`).

The validator passed all pre-existing checks outside
`models.selection-dimensions`. The new focused calibration assertions failed
only because the current surfaces do not yet contain the approved calibration:

1. Terra-medium bounded-work baseline and effort-versus-tier escalation
   classifications.
2. Late-escalation residual-uncertainty or variance requirement,
   bounded-work de-escalation, and missing-decision approval boundary.
3. Separate curated-artifact reviewer shape, named lens, severity, and
   reproduction-or-validation-path evidence requirements in canonical policy
   and advisory examples.
4. Baseline and late-escalation decision cues in both shared model-strategy
   source blocks.

The failure labels identify the required semantic boundaries. Existing
permanent-tier, authorization, `ultra`, template-assembly, and historical
compatibility assertions remained passing.

## Scope and variance

Only `scripts/test_harness_policy.py` and this execution record changed.
No approval-required variance occurred. The next authorized activity remains
`TASK-002`.
