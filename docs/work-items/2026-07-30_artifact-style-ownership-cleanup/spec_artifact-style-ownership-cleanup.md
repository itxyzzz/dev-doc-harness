# Artifact Style Ownership Cleanup Spec

Work ID: `2026-07-30_artifact-style-ownership-cleanup`
Short ID: `artifact-style-ownership-cleanup`
Status: Approved
Harness release: `0.8+`
Schema: `schema:spec.small-medium`
Companion plan: `plan_artifact-style-ownership-cleanup.md`
Policy references: `module:architecture`, `module:lifecycle`, `module:quality`, `module:artifact-style`, `module:models`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

## Goal

Make the Artifact Style reference a focused conditional readability module, while moving universal plain-language guidance and already-owned verification semantics to their correct canonical owners.

## Source and Intent

Source input:

1. Operator review of `.agents/skills/dev-doc-harness/references/artifact-style.md` on 2026-07-30.
2. Agreement to move Plain language into `## Baseline artifact readability` of `durable-planning-quality.md` after removing the validator implementation detail.

Desired operator outcome:

1. Routine planning uses one baseline plain-language owner without loading Artifact Style, Artifact Style retains only readability guidance that benefits large or hard-to-scan artifacts, and templates and validator checks agree with the ownership graph.

Success summary:

1. Plain language is quality-owned; Verification Criterion placement is not duplicated outside Quality; traceability guidance is consolidated; the user’s source reflow is preserved; and the full harness validator passes.

## Scope Boundary

### In scope

1. Move the author-facing `must`/`should` and concise-wording guidance from Artifact Style into Quality baseline readability under a quality-owned rule.
2. Remove the `shall` definition-only exception from author-facing policy and update validator logic so its enforcement remains covered without that prose exception.
3. Condense Artifact Style's ownership-boundary paragraph, remove Verification Criterion placement as a duplicate Quality rule, and consolidate entity presentation, proportional traceability, traceability density, and blank-line guidance into a coherent readability structure.
4. Align policy architecture, template source blocks and generated templates, and focused validator assertions with the revised owner set.
5. Preserve the operator's current one-line source reflow in `artifact-style.md`; correct only the accidental doubled space in `validation  signals` while making the scoped content changes.

### Non-scope

1. Changing the semantics of Specification Commitments, Verification Criteria, Plan Checks, or the default small/medium versus large artifact-style routing.
2. Broadly reformatting current references, templates, historical work items, or changelog history.
3. Changing the validator's Markdown scan scope, frozen-artifact exclusions, or legal-text exclusions except as necessary to remove the obsolete definition-only exception.

### Assumptions

1. `module:quality` remains the owner of Verification Criterion semantics because it already requires local criteria near commitments and cross-cutting criteria in one shared section.
2. `rule:style.trace-density` can remain the stable Artifact Style traceability rule ID while its heading and content are consolidated; obsolete duplicate style rule IDs can be retired from current reusable surfaces.
3. The current user-authored source reflow is intentional and must not be reverted.

### Open questions

1. None identified after repository-context review.

## Repository Context

### Current state

1. `artifact-style.md` is conditionally loaded for large or hard-to-scan artifacts, but it currently owns Plain language even though routine small/medium spec templates cite that rule without loading the conditional module.
2. `durable-planning-quality.md` already owns the substantive local and cross-cutting Verification Criterion placement rule.
3. Artifact Style splits closely related traceability guidance across Entity presentation, Proportional traceability, and Traceability density, and places blank-line guidance under traceability rather than structure.
4. `test_harness_policy.py` asserts the old style owner, templates cite the old style rule ID, and generated templates are assembled from source blocks.

### Evidence read

1. `.agents/skills/dev-doc-harness/references/artifact-style.md`.
2. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`.
3. `.agents/skills/dev-doc-harness/references/policy-architecture.md`.
4. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.030.common.commitments-verification.md` and generated spec templates.
5. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
6. Applicable repository `AGENTS.md`, harness router, templates, and model policy.

### Constraints and compatibility

1. Templates are guidance surfaces and do not own long reusable policy.
2. Current reusable policy, template sources, generated templates, and validator expectations must change atomically.
3. Historical frozen work-item artifacts remain immutable records and must not be normalized to the new ownership graph.

## Commitments and verification

### `SPEC-001` Baseline plain-language ownership

Statement:

1. Quality policy must own the author-facing `must`/`should` and concise-wording guidance within Baseline artifact readability; Artifact Style and all current templates must no longer cite `rule:style.plain-language`.

#### `VER-001` Plain-language owner evidence

Covers: `SPEC-001`.

Criterion: Current policy, template source blocks, generated templates, and validator checks identify the Quality rule as the sole plain-language owner.

Expected evidence: Focused search, template assembly check, and full harness-validator output.

### `SPEC-002` Focused Artifact Style ownership

Statement:

1. Artifact Style must retain only conditional readability guidance: a concise ownership boundary, final content, scannable structure, placeholder control, one consolidated traceability rule, and template-prompt guidance. Verification Criterion placement must remain Quality-owned.

#### `VER-002` Ownership and structure evidence

Covers: `SPEC-002`.

Criterion: The architecture catalog and validator owner sets match the simplified Artifact Style rule set, and no active reusable policy duplicates Quality's Verification Criterion placement rule.

Expected evidence: Focused policy inspection and full harness-validator output.

### `SPEC-003` Validator continuity and source preservation

Statement:

1. The plain-language validator must enforce the same active-authoring rule without relying on a definition-only exception in Artifact Style, and the scoped edit must preserve the operator's intentional source reflow while correcting the doubled space in `validation  signals`.

#### `VER-003` Enforcement and diff evidence

Covers: `SPEC-003`.

Criterion: The synthetic active-surface modal failure remains detected, controlled exclusions remain outside the active scan, and the final diff contains no unrelated reformatting or historical artifact rewrites.

Expected evidence: Full harness-validator output, focused validator inspection, and `git diff --check` plus scoped diff review.

## Architecture Decisions

Architecture snapshot status: Not applicable; this is a local policy-ownership and validator-alignment change with no component, interface, or runtime architecture change.

Decision summary:

1. Drivers: reduce uneven and duplicated guidance while keeping routine planning lightweight.
2. Constraints: retain stable, current rule references where useful; avoid template-owned policy; preserve historical records and user-authored reflow.
3. Selected approach: move baseline language to Quality, keep Verification Criterion semantics in Quality, and reduce Artifact Style to conditional presentation concerns.
4. Affected boundaries: Quality policy, Artifact Style policy, policy architecture, template sources and generated outputs, and validator owner checks.
5. Rejected alternatives: leaving Plain language in an optional module, making templates the sole owner of Verification Criterion placement, and retaining three overlapping traceability sections.
6. Validation cues: `VER-001`, `VER-002`, `VER-003`, and the plan checks.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. Harness rule IDs and template policy references; no public runtime interface changes.

### Data, config, and persistence

1. None.

### State and control flow

1. None.

### Safety, security, privacy, migration, and rollback

1. None identified after repository-context review. The work modifies documentation policy and validator expectations only; a revert restores the prior owner graph without data migration.

## Risks and Rejected Alternatives

### `RISK-001` Owner drift between references and generated templates

Decision or mitigation:

1. Update source blocks before running the template assembler, then run the full policy validator and focused ownership searches.

Notes:

1. Generated output must not be hand-edited independently of its source block.

### `RISK-002` Overbroad formatting churn

Decision or mitigation:

1. Preserve the current one-line reflow and limit whitespace correction to the identified doubled space while reviewing the scoped diff before commit.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: artifact-style-ownership-cleanup -- approve policy consolidation` |
| Implementation | `refactor: artifact-style-ownership-cleanup -- consolidate readability policy` |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source | Living | Yes | Before each commit | `changelog/planning-approval.md`, `changelog/implementation.md` | Entries use the canonical changelog-heading grammar and match planned subjects. |
| Root changelog | Living | Yes | Planning freeze | `CHANGELOG.md` | Required by repository-local freeze-gate instructions. |
| Test cases | Snapshot | Yes | Before implementation | `snapshots/test-cases.snapshot.md` | Captures owner-graph, template, and modal-enforcement cases. |
| Testing guide delta | Living delta | No | N/A | N/A | No user-facing testing-flow change. |
| Operator manual delta | Living delta | No | N/A | N/A | No runtime/operator behavior change. |
| API reference delta | Living delta | No | N/A | N/A | No API change. |
| Architecture snapshot | Snapshot | No | N/A | N/A | No architecture decision beyond local policy ownership. |
| Architecture summary delta | Living delta | No | N/A | N/A | No durable system architecture change. |

## Planning shape and transition ownership

1. Planning shape: `combined small/medium`.
2. Companion plan: `plan_artifact-style-ownership-cleanup.md` is drafted with this spec.
3. Transition owner: the companion plan owns the implementation handoff after the combined package freezes.
4. Next activity: implement policy-owner consolidation, template regeneration, validator alignment, and validation.

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Commitments and verification criteria are bounded and testable.
- [x] Repository evidence, compatibility constraints, and source-reflow boundary are recorded.
- [x] Architecture, interfaces, data, and safety impacts are explicitly assessed.
- [x] Documentation artifact decisions and planned commits are explicit.
- [x] The companion plan is present and owns the implementation handoff.
- [x] An operator-approved independent reviewer sub-agent will assess the completed implementation with curated artifacts and validation evidence.
- [x] No unresolved placeholders, required decisions, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
