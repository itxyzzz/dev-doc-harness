# Specification Block Consolidation Small Spec

Work ID: `2026-08-26_spec-block-consolidation`
Short ID: `spec-block-consolidation`
Status: Approved
Harness release: `0.9+`
Schema: `schema:spec.small`
Companion plan: `plan_spec-block-consolidation.md`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:freeze-gate`, `rule:lifecycle.documentation-assessment`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`

## Goal

Consolidate reusable specification blocks and replace `middle-and-large` block filenames with `medium-and-large`, while preserving rendered template content except for the approved commit/freeze placement and readiness normalization.

## Scope

### In scope

1. Rename `spec.080.common.documentation-assessment.md` to `spec.070.common.documentation-assessment.md` and move its assembled documentation section before the merged `075` commit/handoff blocks.
2. Merge the medium planned-commit and handoff sections into `spec.075.medium.commits-handoff.md`, and the large planned-commit/freeze and handoff sections into `spec.075.large.commits-handoff.md`.
3. Extract the identical specification Approval section into `spec.095.common.approval.md`; remove it from small, medium, and large source blocks.
4. Rename the small tail to `spec.080.small.handoff-readiness.md` after removing only Approval.
5. Create `spec.080.medium-and-large.readiness.md` with the seven shared or normalized medium/large readiness checks, and retain large-only checks in `spec.085.large.readiness-extension.md`.
6. Rename all spec and plan block filenames containing `middle-and-large` to `medium-and-large`; update manifests and current validator references.
7. Regenerate templates only through `assemble_templates.py` and update static validation to protect the new composition and permitted readiness wording.

### Non-scope

1. Changing lifecycle, documentation-assessment, approval, planned-commit, handoff, model, or freeze policy.
2. Changing plan-template rendered bodies; their source filenames and manifests change only.
3. Adding a medium readiness-extension block or changing small readiness content beyond Approval extraction.
4. Updating frozen historical work items.

## Material context, decisions, and risks

### Context and constraints

1. Source blocks and manifests are authoritative; assembled templates are generated and must not be hand-edited.
2. Block order is validated from numeric prefixes, so `070` documentation precedes `075` commit/handoff and `095` Approval remains final.
3. Current block filename grammar, duplicate-block detection, expected assembly lists, and source-path assertions in `test_harness_policy.py` hard-code the old names.
4. The current spec-block inventory has 19 files. The two requested commits/handoff merges reduce it to 18; no additional block files are introduced.

### Decisions

1. The medium-and-large readiness core has seven checks: the first three identical checks, the medium wording of the verification-completeness check, one normalized self-containment check, documentation assessment, and no-unresolved-items.
2. The normalized self-containment check states that a specification and its architecture snapshot are self-contained so a fresh session can draft the next actionable plan without reconstructing original session context.
3. The large extension retains cross-phase verification ownership as a separate check, followed by phase decomposition, next-stage, and impact-surface checks.
4. The only rendered wording changes are the normalized self-containment check and splitting the large verification check to retain its cross-phase ownership requirement. The only rendered ordering changes are documentation before the merged `075` blocks and the large readiness checklist structure.

### Risks

1. A missed old filename or validator path can make template assembly or static policy validation fail. Mitigation: test-first validator updates, a repository-scoped old-name scan, and full assembler validation.
2. Recombining readiness can silently remove a large-only requirement. Mitigation: require the extension's cross-phase, phase-decomposition, next-stage, and impact-surface checks in static validation and generated-template review.
3. Generated-output changes can exceed the approved order and wording changes. Mitigation: inspect the final word diff against the pre-change baseline and accept only the decisions recorded above.

## Commitments and verification

### `SPEC-001` Consolidated specification block composition

Statement:

1. Small, medium, and large specification assemblies must use the approved `070`, `075`, `080`, `085`, and `095` block structure, with one common Approval block and no medium readiness extension.

#### `VER-001` Assembly composition is exact

Covers: `SPEC-001`.

Criterion: Static validation requires the exact ordered manifest lists and source paths for all three specification templates, and the assembler reports current outputs.

Expected evidence: harness-policy validator and assembler freshness output.

### `SPEC-002` Rendered content is preserved within approved exceptions

Statement:

1. The consolidation must preserve all rendered template sections except documentation moving before the merged `075` commit/handoff blocks, the approved medium/large readiness normalization, and the large readiness reorder.

#### `VER-002` Generated templates retain required sections

Covers: `SPEC-002`.

Criterion: Generated-template review shows every existing planned-commit, handoff, documentation, readiness, and approval obligation exactly once, with only the recorded ordering and readiness wording changes.

Expected evidence: scoped word diff and generated-template heading/checklist inspection.

### `SPEC-003` Medium-and-large naming is canonical

Statement:

1. Current spec and plan source-block filenames, manifests, and validator references must use `medium-and-large` rather than `middle-and-large`.

#### `VER-003` No old current block name remains

Covers: `SPEC-003`.

Criterion: Active template and validator sources contain no `middle-and-large` block filename or path; the filename grammar accepts `medium-and-large` and rejects retired names.

Expected evidence: focused validator and repository-scoped search output.

## Documentation assessment

- `DOC-TEST-CASE`: Not required — the existing static validator and planned command checks provide durable rerunnable evidence for this bounded template refactor.
- `DOC-TEST-GUIDE`: Not required — contributor testing instructions do not change.
- `DOC-OPS-GUIDE`: Not required — operator or runtime guidance does not change.
- `DOC-API-GUIDE`: Not required — no public API changes.
- `DOC-ARCH-SUMMARY`: Not required — this is local template composition, not a work-item architecture decision.

## Planning shape and readiness

1. Planning shape: `combined small`.
2. Companion plan: `plan_spec-block-consolidation.md` is drafted and reviewed with this spec.
3. Transition owner: `plan_spec-block-consolidation.md` owns `Stage: plan execution` after freeze.
4. The scope remains eligible for small because all changes are local template composition, renames, generated output, and deterministic static validation.

- [x] All relevant input is preserved in this specification file and it is self-contained so a fresh session can execute the actionable plan without reconstructing original session context.
- [x] Goal, scope, material context, decisions, commitments, and verification are mutually consistent.
- [x] Every `SPEC-*` has applicable `VER-*` evidence.
- [x] Documentation assessment assigns every relevant prompt.
- [x] No placeholders, undecided required items, missing sections, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
