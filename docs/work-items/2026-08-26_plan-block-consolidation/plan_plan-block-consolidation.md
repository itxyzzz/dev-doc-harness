# Plan Block Consolidation Small Plan

Work ID: `2026-08-26_plan-block-consolidation`
Short ID: `plan-block-consolidation`
Status: Approved
Harness release: `0.9+`
Schema: `schema:plan.small`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:freeze-gate`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:quality.plan-executable`

## Exact inputs

1. Draft spec: `spec_plan-block-consolidation.md`.
2. Relevant repository surfaces: the three plan assembly manifests; all `plan.*` source blocks; the three generated plan templates; `assemble_templates.py`; and `test_harness_policy.py` assembly, small-contract, duplicate-block, and plan source-path assertions.
3. Required documentation outputs from the specification: None.

## Change surfaces

1. Plan source blocks: create the shared Approval block, rename the requested `020`, `050`, and `090` blocks, and split the small `040` tail into `060` planned commits and `070` validation/variance.
2. Plan assembly manifests: use the revised block paths in numeric semantic order and append the common Approval block.
3. Static policy validator: protect the revised block inventory, common Approval contract, small plan order, and retired-path absence.
4. Generated plan templates: regenerate with the assembler only.

## Approach

First update static validation so it specifies the desired manifests and common Approval source, then run it against the current source tree to establish an expected red failure. Next rename and split the source blocks, update manifests, and regenerate the three templates. Finally run the full validator, check template freshness, inspect the generated small-plan section order, and scan for retired paths.

## Implementation tasks

### `TASK-001` Define the revised plan-block contract

Dependencies: None.

Implementation:

1. Update static validator expectations for the three plan manifests, the renamed `020` and `050` paths, the split small `060` and `070` blocks, renamed `090` tails, and the final shared `095` Approval block.
2. Add an exact assertion that `plan.095.common.approval.md` contains only the shared Approval fields and appears once at the end of every generated plan.
3. Run the validator before changing the source blocks or manifests.

Exit criteria: The validator fails because the old source inventory does not satisfy the target composition, rather than from syntax or unrelated policy failures.

#### `CHECK-001` Red plan-block contract

Covers: `VER-001`, `VER-002`.

Method: Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` after the validator edit and before source-block changes.

Expected result: nonzero exit with expected missing target paths, retired path, or manifest-composition failures.

Evidence record: command output in the implementation completion report.

### `TASK-002` Recompose source blocks and assemblies

Dependencies: `TASK-001`.

Implementation:

1. Create `plan.095.common.approval.md` from the identical existing Approval content, remove Approval from the three current tail blocks, and rename the medium and phase tails to `readiness-completion`.
2. Rename the `020` medium-and-large traceability block and the small `030` tasks/checks block to their approved target paths.
3. Replace the small `040` tail with a `060` planned-commit table and a `070` validation-and-variance block.
4. Update all three plan manifests and run `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write`.

Exit criteria: All source paths resolve, all generated plans contain exactly one final Approval section, and the small plan has the approved `050`, `060`, `070`, and `095` sequence.

#### `CHECK-002` Green plan composition

Covers: `VER-001`, `VER-002`.

Method: Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` followed by `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`.

Expected result: both commands exit `0`; the freshness check prints `All assembled templates are current.`

Evidence record: command output in the implementation completion report.

### `TASK-003` Review generated-template preservation

Dependencies: `TASK-002`.

Implementation:

1. Inspect each generated plan for one final Approval section and the expected plan-specific tail content.
2. Confirm the small generated plan orders Implementation tasks, Planned commits, Validation and variance, Plan readiness, and Approval.
3. Search active template and validator paths for every retired filename and inspect the complete diff for unrelated changes.

Exit criteria: No retired source path remains active, generated template changes match the approved structure, and no unrelated changes are present.

#### `CHECK-003` Preservation and diff review

Covers: `VER-001`, `VER-002`.

Method: Run `git diff --check`, then `rg -n "plan.020.medium-and-large.traceability-approach-surfaces|plan.030.small.tasks-checks|plan.040.small.validation-variance-approval|plan.090.medium.readiness-completion-approval|plan.090.phase.readiness-completion-approval" .agents/skills/dev-doc-harness/assets/templates .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Expected result: no whitespace errors and no active occurrence of a retired path.

Evidence record: command output in the implementation completion report.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: plan-block-consolidation -- approve initial plan blocks` |
| Implementation | `refactor: plan-block-consolidation -- extract shared plan approval` |

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
