# Plan Block Consolidation Small Spec

Work ID: `2026-08-26_plan-block-consolidation`
Short ID: `plan-block-consolidation`
Status: Approved
Harness release: `0.9+`
Schema: `schema:spec.small`
Companion plan: `plan_plan-block-consolidation.md`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:freeze-gate`, `rule:lifecycle.documentation-assessment`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`

## Goal

Make the plan templates use one shared Approval block, consistent `medium-and-large` naming, and aligned small-plan block numbering while preserving the compact small-plan route.

## Scope

### In scope

1. Create `plan.095.common.approval.md` and remove the identical Approval section from the small, medium, and phase plan tails.
2. Rename the medium and phase tails after Approval extraction so their names describe readiness and completion only.
3. Rename `plan.020.medium-and-large.traceability-approach-surfaces.md` to `plan.020.medium-and-large.traceability-constraints-surfaces.md` and update its references.
4. Rename `plan.030.small.tasks-checks.md` to `plan.050.small.tasks-checks.md`.
5. Replace `plan.040.small.validation-variance-approval.md` with `plan.060.small.planned-commits.md` and `plan.070.small.validation-variance.md`.
6. Update the three plan assemblies, regenerate their derived templates, and update static validation for the new block inventory and exact assembly order.

### Non-scope

1. Changing policy requirements, lifecycle routing, task/check semantics, model strategy, handoff content, or phase-plan scope.
2. Consolidating readiness, completion, handoff, or planned-commit blocks beyond the requested Approval extraction.
3. Changing specification blocks or frozen historical work-item artifacts.

## Material context, decisions, and risks

### Context and constraints

1. Source blocks and assembly manifests are authoritative; generated templates are updated only through `assemble_templates.py`.
2. `assemble_templates.py` concatenates direct block paths without parameters or conditional rendering.
3. `test_harness_policy.py` currently fixes plan block names, small manifest composition, shared-block behavior, and expected source paths.

### Decisions

1. The common Approval block contains only `## Approval`, `Status: Draft`, and `Superseded by: None`, matching the approved specification-block pattern.
2. `plan.060.small.planned-commits.md` introduces the small plan's approval and implementation commit-subject table; `plan.070.small.validation-variance.md` retains the former validation-and-variance guidance without Approval.
3. Small remains a compact route: it consumes the shared Approval block but does not consume `module:models` or medium/phase planning blocks.

### Risks

1. A stale block path or expected-manifest assertion can break assembly or validation. Mitigation: update the contract first, confirm the expected red failure, then regenerate and run the full validator.
2. Removing Approval from a tail could omit it from a generated template. Mitigation: assert the common block's exact content and require it as the final manifest block for every plan.
3. The new small planned-commit section could unintentionally change the compact route beyond the requested scope. Mitigation: use the existing planned-commit table shape and restrict the generated change to that new section plus the shared Approval placement.

## Commitments and verification

### `SPEC-001` Shared plan Approval composition

Statement:

1. Small, medium, and phase plan assemblies must each end with one `plan.095.common.approval.md` block, and no preceding plan block may render a second Approval section.

#### `VER-001` Assembly and rendered approval are exact

Covers: `SPEC-001`.

Criterion: Static validation requires the exact ordered plan manifests and the common Approval block contains only the shared Draft status and supersession fields.

Expected evidence: harness-policy validator and assembler freshness output.

### `SPEC-002` Plan block names and small-plan structure are aligned

Statement:

1. Current plan sources, manifests, and static validation must use the requested `020`, `050`, `060`, `070`, `090`, and `095` names, with the small planned-commit and validation blocks in their intended order.

#### `VER-002` Current plan block inventory is resolvable

Covers: `SPEC-002`.

Criterion: The assembler resolves all three manifests, static validation rejects retired source paths, and the generated small plan has Tasks, Planned commits, Validation and variance, and Approval sections in that order.

Expected evidence: harness-policy validator, assembler freshness output, and scoped generated-template inspection.

## Documentation assessment

- `DOC-TEST-CASE`: Not required — the static validator and assembler provide durable rerunnable evidence.
- `DOC-TEST-GUIDE`: Not required — contributor testing instructions do not change.
- `DOC-OPS-GUIDE`: Not required — operator or runtime guidance does not change.
- `DOC-API-GUIDE`: Not required — no public API changes.
- `DOC-ARCH-SUMMARY`: Not required — this is local template composition, not a work-item architecture decision.

## Planning shape and readiness

1. Planning shape: `combined small`.
2. Companion plan: `plan_plan-block-consolidation.md` is drafted and reviewed with this spec.
3. Transition owner: `plan_plan-block-consolidation.md` owns `Stage: plan execution` after freeze.
4. The scope remains eligible for small because it is limited to local source-block composition, generated templates, and deterministic validation.

- [x] All relevant input is preserved in this specification file and it is self-contained so a fresh session can execute the actionable plan without reconstructing original session context.
- [x] Goal, scope, material context, decisions, commitments, and verification are mutually consistent.
- [x] Every `SPEC-*` has applicable `VER-*` evidence.
- [x] Documentation assessment assigns every relevant prompt.
- [x] No placeholders, undecided required items, missing sections, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
