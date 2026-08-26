# Shared Documentation Assessment Block Small Spec

Work ID: `2026-08-25_shared-documentation-assessment-block`
Short ID: `shared-documentation-assessment-block`
Status: Approved
Harness release: `0.9+`
Schema: `schema:spec.small`
Companion plan: `plan_shared-documentation-assessment-block.md`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:freeze-gate`, `rule:lifecycle.documentation-assessment`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`

## Goal

Use one documentation-assessment source block in small, medium, and large specification templates, while retaining the small template's planning-shape, readiness, and approval content as its local tail.

## Scope

### In scope

1. Rename the current medium-and-large `spec.080` documentation-assessment block to a common block without changing its five `DOC-*` prompts or status syntax.
2. Add that common block to the small specification assembly immediately after commitments and before the small-only `080` tail.
3. Move the small-only tail to `spec.085.small.handoff-readiness-approval.md` and retain its planning shape, readiness checklist, and approval section after removing the duplicated documentation assessment.
4. Update medium and large assemblies to use the renamed common block, regenerate the three affected assembled specification templates, and update focused validator assertions.

### Non-scope

1. Changing the five documentation-assessment IDs, their lifecycle policy, or medium/large output wording.
2. Consolidating commitment, header, scope/context, handoff, or readiness blocks.
3. Changing plan templates, frozen historical work items, release/version policy, or implementation-changelog behavior.

## Material context, decisions, and risks

### Context and constraints

1. Source blocks and their assembly manifests are authoritative; generated templates must be regenerated with `assemble_templates.py` and never hand-edited.
2. The existing small manifest and validator currently require every listed block to be small-specific, so the validator must explicitly permit this one common documentation block.
3. The block count must not increase. Renaming the existing medium-and-large block and reducing the existing small tail preserves the two-file `080` source-block count.

### Decisions

1. Name the reused source block `spec.080.common.documentation-assessment.md` to accurately state that it is used by all three specification sizes.
2. Keep the common block's current contents as the canonical five-prompt assessment; do not create a third `080` file.
3. Rename the small tail to `spec.085.small.handoff-readiness-approval.md`; its first heading is `## Planning shape and readiness`.

### Risks

1. A stale manifest or generated template could hide the new composition. Mitigation: regenerate through the assembler and run both its freshness check and the full harness-policy validator.
2. A permissive validator change could allow unrelated common blocks in the small template. Mitigation: assert the complete ordered small specification block list, including only the named shared `080` block and `085` small tail.

## Commitments and verification

### `SPEC-001` Common documentation assessment source

Statement:

1. The small, medium, and large specification assemblies must use one common `spec.080` documentation-assessment source block containing the current five prompts and status syntax.

#### `VER-001` Common source is assembled everywhere

Covers: `SPEC-001`.

Criterion: The three manifests reference the same common `spec.080` block, and each regenerated specification template contains one `## Documentation assessment` section with the five current `DOC-*` prompts.

Expected evidence: focused harness-policy validation and assembler freshness output.

### `SPEC-002` Small-only tail remains intact

Statement:

1. The small `spec.080` block must retain only its planning-shape, readiness, and approval content after the common assessment is extracted.

#### `VER-002` Small output preserves its local tail

Covers: `SPEC-002`.

Criterion: The regenerated small specification places the common assessment before the planning-shape section and contains no second copy of the five documentation prompts.

Expected evidence: focused harness-policy validation and review of the regenerated small template.

### `SPEC-003` Validator protects the intended exception

Statement:

1. Static validation must require the exact compact small-specification block order and permit only `spec.080.common.documentation-assessment.md` as its shared block.

#### `VER-003` Validator rejects the old composition

Covers: `SPEC-003`.

Criterion: Before source-manifest edits, the updated validator fails because the small assembly lacks the required common block; after implementation it passes with the exact intended list.

Expected evidence: captured red/green validator output from `test_harness_policy.py`.

## Documentation assessment

- `DOC-TEST-CASE`: Not required — the existing validator script and plan checks provide rerunnable evidence; no separate test-case snapshot is needed for this bounded source-block reorganization.
- `DOC-TEST-GUIDE`: Not required — contributor testing instructions do not change.
- `DOC-OPS-GUIDE`: Not required — operator or runtime guidance does not change.
- `DOC-API-GUIDE`: Not required — no public API changes.
- `DOC-ARCH-SUMMARY`: Not required — the work makes no architecture decision beyond local template composition.

## Planning shape and readiness

1. Planning shape: `combined small`.
2. Companion plan: `plan_shared-documentation-assessment-block.md` is drafted and reviewed with this spec.
3. Transition owner: `plan_shared-documentation-assessment-block.md` owns `Stage: plan execution` after freeze.
4. The scope remains eligible for small because it changes one named template concept, a bounded assembly list, generated outputs, and focused validation only.

- [x] All relevant input is preserved in this specification file and it is self-contained so a fresh session can execute the actionable plan without reconstructing original session context.
- [x] Goal, scope, material context, decisions, commitments, and verification are mutually consistent.
- [x] Every `SPEC-*` has applicable `VER-*` evidence.
- [x] Documentation assessment assigns every relevant prompt.
- [x] No placeholders, undecided required items, missing sections, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
