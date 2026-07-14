# Plain-language Policy Review

Work ID: `2026-07-14_plain-language-artifacts`
Review role: `review-001`
Review mode: `read-only post-diff review`

## Scope

Reviewed the frozen specification, plan, architecture snapshot, test-case
snapshot, changed policy and template surfaces, current diff, policy-validator
output, assembler check, modal-scope scan, and whitespace check.

## Findings

### `REV-001` — P1: Current templates are not fully covered

Evidence: The active-path list excludes the current small/medium plan,
large/phased phase-plan, architecture snapshot, amendment, and variance-log
templates. Existing small/medium templates also retain an optional
style-loading cue that conflicts with the required router entry.

Reproduction or validation path: Add the prohibited modal to the small/medium
plan template and run the policy validator; the current focused check does not
report it.

Resolution: Blocked pending amendment approval because correcting this finding
expands the approved template-consumer and validation-scope boundaries.

### `REV-002` — P1: Delivery-evidence files must be staged for the full validator

Evidence: The validator reports the new implementation changelog, testing
delta, and variance log as untracked work-item Markdown artifacts.

Reproduction or validation path: Stage the planned delivery-evidence files and
rerun the full policy validator.

Resolution: Pending the amended implementation checkpoint; no repair occurs
while the amendment is proposed.

### `REV-003` — P2: The canonical definition exception needs an exact assertion

Evidence: The validator allows the canonical definition if encountered, but it
does not require the exact definition-only sentence to exist.

Reproduction or validation path: Remove that sentence from the style rule and
run the focused policy validator; the current check continues to pass.

Resolution: Included in the proposed amendment because the change affects the
controlled-exception validation boundary.

### `REV-004` — P2: The fixture boundary needs a narrow documented check

Evidence: The validator-fixture example is outside the Markdown allowlist by
file type, rather than being represented as a narrow documented exception.

Reproduction or validation path: Separate or explicitly identify fixture data,
then verify that the active Markdown scan remains limited to declared paths.

Resolution: Included in the proposed amendment with the active-path boundary.

## Amendment follow-up review

Review role: `review-002`
Review mode: `read-only post-amendment review`

### Result

No blocking findings remain.

Evidence:

1. The active-path validator covers every current generated template and every
   reusable template source block.
2. The mandatory small/medium cues originate in source blocks, and the
   assembler regenerated matching output templates.
3. The validator requires the exact canonical definition-only exception once,
   while the narrowly named fixture, frozen work items, and `LICENSE` remain
   outside the active Markdown set.
4. The staged full policy validator, assembler freshness check, modal-scope
   scan, and whitespace check passed.

Reproduction or validation path:

```powershell
python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py
python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check
git diff --cached --check
```

## Gate status

Pass. Amendment 001 resolves the earlier blocking findings, and the staged
implementation package is ready for its planned commit.
