# Specification Block Consolidation Small Plan

Work ID: `2026-08-26_spec-block-consolidation`
Short ID: `spec-block-consolidation`
Status: Approved
Harness release: `0.9+`
Schema: `schema:plan.small`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:freeze-gate`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:quality.plan-executable`

## Exact inputs

1. Draft spec: `spec_spec-block-consolidation.md`.
2. Relevant repository surfaces: all six assembly manifests; spec blocks numbered `070`, `080`, `085`, `090`, and `095`; every spec and plan block whose filename contains `middle-and-large`; the six generated templates; `assemble_templates.py`; and `test_harness_policy.py` filename, manifest, handoff, readiness, duplicate-block, and source-path assertions.
3. Required documentation outputs from the specification: None.

## Change surfaces

1. Spec block inventory: rename the common documentation, small tail, and every `middle-and-large` source block; merge the two medium and two large commit/handoff inputs; extract common Approval; replace the two medium/large readiness sources with one core and one large extension.
2. All six assembly manifests: reference renamed source blocks and preserve their numeric semantic order.
3. `test_harness_policy.py`: change filename grammar and allowed scopes to `medium-and-large`, update source-path and exact-manifest assertions, and protect the seven-check core, large extension, and common Approval arrangement.
4. Generated templates: regenerate with the assembler only; plan-template bodies remain byte-for-byte unchanged.

## Approach

First make the validator expect the new file names, manifests, and readiness composition, then run it against the unchanged source tree to establish an expected red failure. Next rename/recompose the source blocks and manifests, regenerate outputs, and run the validator green. Finally inspect generated word diffs against `HEAD` to verify that only the approved order and readiness wording changes appear.

## Implementation tasks

### `TASK-001` Define the post-consolidation static contract

Dependencies: None.

Implementation:

1. Update validator filename grammar, allowed scopes, duplicate-block glob, exact small assembly list, hard-coded source paths, and planned-commit/handoff/readiness assertions to expect `medium-and-large` and the new `070` through `095` spec structure.
2. Add focused assertions that the common Approval block has exactly `## Approval`, `Status: Draft`, and `Superseded by: None`; the readiness core has seven expected checks; and the large extension retains cross-phase ownership, phase decomposition, next-stage, and impact checks.
3. Run the validator before changing block sources or manifests and confirm it fails because the old block inventory and assemblies do not satisfy the new contract.

Exit criteria: The static contract fully names the approved target structure and fails only for the old source tree's expected filename, path, or assembly mismatch.

#### `CHECK-001` Red validation evidence

Covers: `VER-001`, `VER-003`.

Method: Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` immediately after the validator edit and before renaming or recomposing source blocks.

Expected result: exits nonzero with expected old-name, missing-target-block, or manifest-order failures; it must not fail from syntax, import, or unrelated policy errors.

Evidence record: command output recorded in the implementation completion report.

### `TASK-002` Recompose specification sources and rename shared blocks

Dependencies: `TASK-001`.

Implementation:

1. Rename `spec.080.common.documentation-assessment.md` to `spec.070.common.documentation-assessment.md` without altering its body.
2. Create the `075` medium and large commit/handoff blocks by concatenating their current source sections verbatim in their current internal order; remove the merged input blocks.
3. Move the identical three-line Approval section into `spec.095.common.approval.md`; remove it from the small tail and medium/large readiness sources.
4. Rename the remaining small tail to `spec.080.small.handoff-readiness.md` without changing its planning-shape or readiness content.
5. Replace medium/large readiness sources with `spec.080.medium-and-large.readiness.md` and `spec.085.large.readiness-extension.md` using exactly the core and extension decisions in the draft spec.
6. Rename every spec and plan `middle-and-large` source block to `medium-and-large`, and update all six manifests to the approved assembly order.
7. Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` to regenerate templates and run integrated validation.

Exit criteria: The source-block inventory decreases from 19 to 18 specification blocks; all manifests resolve; every plan block uses `medium-and-large`; and generated outputs are assembled only by the assembler.

#### `CHECK-002` Green structure and assembly evidence

Covers: `VER-001`, `VER-003`.

Method: Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, then `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`.

Expected result: both commands exit `0`; the freshness check prints `All assembled templates are current.`

Evidence record: command output recorded in the implementation completion report.

### `TASK-003` Review rendered-template preservation

Dependencies: `TASK-002`.

Implementation:

1. Inspect the small, medium, and large generated specifications for one documentation section, the required commit/handoff sections, one final Approval section, and the approved readiness composition.
2. Confirm both generated plan templates are content-identical to their `HEAD` versions despite source filename migration.
3. Review `git diff --word-diff=plain HEAD` for generated specifications. Accept only documentation moving before `075`, the common Approval extraction with no body change, the normalized self-containment check, the split large cross-phase verification check, and large readiness ordering.
4. Search active template and validator sources for `middle-and-large`; retain no current source or path occurrence.
5. Run `git diff --check` and inspect the complete planned diff for unrelated changes.

Exit criteria: Required content appears exactly once in each applicable output, plan output bodies are unchanged, only documented rendered changes remain, and no retired filename remains in active sources.

#### `CHECK-003` Preservation and diff evidence

Covers: `VER-002`.

Method: Run `git diff --check`, `git diff --word-diff=plain HEAD -- .agents/skills/dev-doc-harness/assets/templates`, and `rg -n "middle-and-large" .agents/skills/dev-doc-harness/assets/templates .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Expected result: no whitespace errors; the word diff contains only the recorded generated-specification changes; the search returns no active source or validator occurrence.

Evidence record: reviewed command output recorded in the implementation completion report.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: spec-block-consolidation -- approve shared readiness structure` |
| Implementation | `refactor: spec-block-consolidation -- consolidate specification blocks` |

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
