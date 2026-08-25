# Shared Documentation Assessment Block Small Plan

Work ID: `2026-08-25_shared-documentation-assessment-block`
Short ID: `shared-documentation-assessment-block`
Status: Approved
Harness release: `0.9+`
Schema: `schema:plan.small`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:freeze-gate`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:quality.plan-executable`

## Exact inputs

1. Draft spec: `spec_shared-documentation-assessment-block.md`.
2. Relevant repository surfaces: `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.080.middle-and-large.documentation-assessment.md`, `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.080.small.documentation-readiness-approval.md`, the three specification assembly manifests, the three generated specification templates, `assemble_templates.py`, and the focused `test_harness_policy.py` assertions.
3. Required documentation outputs from the specification: None.

## Change surfaces

1. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.080.middle-and-large.documentation-assessment.md`: rename to `spec.080.common.documentation-assessment.md` without changing its assessment body.
2. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.080.small.documentation-readiness-approval.md`: rename to `spec.085.small.handoff-readiness-approval.md`, remove the duplicated assessment heading, status instruction, and five `DOC-*` bullets, and retain the local tail.
3. `.agents/skills/dev-doc-harness/assets/templates/assemblies/small-work-item-spec.json`: add the common block between commitments and the small tail.
4. `.agents/skills/dev-doc-harness/assets/templates/assemblies/medium-work-item-spec.json` and `large-phased-work-item-spec.json`: replace the renamed block path.
5. `.agents/skills/dev-doc-harness/assets/templates/small-work-item-spec.md`, `medium-work-item-spec.md`, and `large-phased-work-item-spec.md`: regenerated only through the assembler.
6. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: require the exact small-specification composition and allow only the named common `080` block as an exception to dedicated small blocks; point documentation-assessment assertions at the renamed common source.

## Approach

First change the focused validator to describe the intended shared-small composition and run it to establish the expected failure against the still-old manifest. Then rename and compose the source blocks, regenerate the templates, and run the focused validator and assembler freshness check. Do not hand-edit generated files.

## Implementation tasks

### `TASK-001` Specify the shared-small composition in static validation

Dependencies: None.

Implementation:

1. In `test_harness_policy.py`, change the expected small specification manifest list to include `blocks/spec.080.common.documentation-assessment.md` before `blocks/spec.085.small.handoff-readiness-approval.md`.
2. Replace the all-`.small.` assertion with a narrow allowlist that permits this exact common block and rejects any other non-small block in the small specification manifest; retain the exact `085` small-tail path in the expected order.
3. Change the documentation-assessment source path constant to `spec.080.common.documentation-assessment.md`.
4. Run the validator before changing source blocks or manifests; confirm it fails because the current small manifest does not yet include the required common block.

Exit criteria: The focused static contract expresses the desired assembly and fails for the expected missing-common-block reason while production template sources remain unchanged.

#### `CHECK-001` Red validation evidence

Covers: `VER-003`.

Method: Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` immediately after the validator edit and before source-block or manifest edits.

Expected result: exits nonzero and reports the small-specification manifest composition mismatch or the forbidden non-small-block rule; it must not fail from an import, syntax, or unrelated harness error.

Evidence record: command output recorded in the implementation handoff or completion report.

### `TASK-002` Assemble one common `080` block and retain the small tail

Dependencies: `TASK-001`.

Implementation:

1. Rename `spec.080.middle-and-large.documentation-assessment.md` to `spec.080.common.documentation-assessment.md` without changing its five documentation prompts or status syntax.
2. Rename `spec.080.small.documentation-readiness-approval.md` to `spec.085.small.handoff-readiness-approval.md` and remove its documentation-assessment section so its first heading is `## Planning shape and readiness`.
3. Update the three specification manifests: small inserts the common block immediately before its renamed `085` small tail; medium and large replace their old path with the common one.
4. Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` to regenerate outputs and execute integrated validation.

Exit criteria: All three source assemblies reference the common `080` block; the small tail has no `DOC-*` prompt; generated specification templates are rebuilt only by the assembler.

#### `CHECK-002` Green policy and assembly evidence

Covers: `VER-001`, `VER-002`, `VER-003`.

Method: Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, then `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`.

Expected result: both commands exit `0`; the second prints `All assembled templates are current.`

Evidence record: command output recorded in the implementation handoff or completion report.

### `TASK-003` Inspect the generated contract and scoped diff

Dependencies: `TASK-002`.

Implementation:

1. Inspect the regenerated small template to confirm it contains one documentation assessment before `## Planning shape and readiness` and no duplicate `DOC-*` list in the tail.
2. Inspect the medium and large templates to confirm their documentation-assessment content is unchanged apart from its source-block provenance.
3. Run `git diff --check` and review the scoped diff for only the named source blocks, manifests, generated specification templates, and policy validator.

Exit criteria: Generated text has one assessment per specification template, the small local tail remains intact, and no unrelated files or whitespace errors remain.

#### `CHECK-003` Generated-output and diff inspection

Covers: `VER-001`, `VER-002`.

Method: Run `git diff --check`; inspect the three generated specification templates and `git diff --` limited to the change surfaces named above.

Expected result: no whitespace errors; the small template has one five-prompt assessment followed by its unchanged planning/readiness/approval tail; medium and large retain one assessment each.

Evidence record: reviewed diff and command output recorded in the implementation handoff or completion report.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: shared-documentation-assessment-block -- approve common spec assessment` |
| Implementation | `refactor: shared-documentation-assessment-block -- share spec documentation assessment` |

## Validation and variance

1. Run each nested `CHECK-*` and record its evidence.
2. Regenerate templates only through `assemble_templates.py --write`; verify freshness with `--check`.
3. Record a useful routine variance; stop for an amendment and operator approval when a change materially affects the outcome, architecture, API, data, security, privacy, compliance, scope, or required evidence.

## Plan readiness

- [x] Exact inputs are sufficient for the bounded tasks.
- [x] Each `TASK-*` has executable steps, exit criteria, and nested `CHECK-*` evidence.
- [x] Checks cover every applicable `VER-*`.
- [x] Required documentation outputs: None.
- [x] No placeholders, unresolved implementation decisions, missing owners, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
