# Testing Guide Delta

Work ID: `2026-07-14_harness-simplification`

## Added coverage

- `scenarios.harness-simplification` checks optional mappings, uninterrupted
  approved execution, equivalent-evidence variance, material amendments, and
  README bootstrap ownership.

## Evidence

1. Before policy edits, the fixed manifest measured 2,135 nonblank lines and
   24,255 words. The new scenario check failed for all five missing behaviors.
2. After implementation, `python -X utf8
   .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` passed all
   checks, including `scenarios.harness-simplification`.
3. The same manifest measured 1,823 nonblank lines and 18,722 words: reductions
   of 312 lines and 5,533 words.

## Notes

Run the policy validator after changing current harness policy, templates,
README bootstrap, or generated templates. Run the assembler with `--check` to
confirm generated templates are current.
