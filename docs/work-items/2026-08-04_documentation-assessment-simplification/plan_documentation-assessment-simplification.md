# Documentation Assessment Simplification Plan

Work ID: `2026-08-04_documentation-assessment-simplification`
Short ID: `documentation-assessment-simplification`
Status: Approved
Harness release: `0.8+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:architecture`, `rule:lifecycle.documentation-assessment`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.execution-review-contract`
Execution method: `superpowers:executing-plans`

## Input artifacts

1. Draft spec: `spec_documentation-assessment-simplification.md`.
2. Architecture input: Architecture Decisions in the draft spec; no architecture snapshot is required.
3. Required snapshots or deltas: `snapshots/test-cases.snapshot.md`.
4. Relevant repository inputs: `AGENTS.md`; `.agents/skills/dev-doc-harness/SKILL.md`; lifecycle, naming, planning-freeze, implementation-changelog, quality, maintenance-architecture, release, and model-policy references; README and operator guidance; affected template blocks/manifests; assembled templates; `assemble_templates.py`; and `test_harness_policy.py`.
5. Unresolved implementation context to confirm before editing: None. The operator approved the design boundaries and exact documentation IDs.

## Traceability approach

Local `SPEC-*`, `VER-*`, `TASK-*`, and `CHECK-*` links provide complete coverage without a separate traceability matrix. `TASK-001` records the required `DOC-TEST-CASE` snapshot; `TASK-002` through `TASK-004` implement the policy, template, and static-check commitments.

## Change surfaces

1. `references/artifact-contract.md`: replace the documentation-matrix rule and matrix with compact assessment policy, five readable IDs, statuses, and architecture/changelog exclusions.
2. `references/naming-conventions.md`: retain generic commit-subject grammar but remove fragment-path, filename, entry-heading, and changelog-synchronization rules.
3. `references/implementation-changelog.md`: become the sole owner of current fragment path/name, entry-heading and commit synchronization, metadata, lint, consolidation, compatibility, and root-cleanup instructions.
4. `references/maintenance-architecture.md`, `durable-planning-quality.md`, and `SKILL.md`: rename documentation-matrix ownership and retain only the correct planning, execution, and release routing boundaries.
5. `assets/templates/blocks/spec.080.common.documentation-matrix.md`: remove this legacy source block and replace it with a new shared documentation-assessment block.
6. `assets/templates/assemblies/small-medium-work-item-spec.json` and `large-phased-work-item-spec.json`: reference the new shared block.
7. Small and large spec headers and readiness blocks: cite the renamed rule and include one generic assessment-completeness check without duplicating the five IDs or policy trigger text.
8. Small and phase plan planned-commit/readiness blocks, `plan.080.phase.documentation-tasks.md`, and `plan-amendment.md`: remove copied changelog/catalog procedure; preserve only the concise pre-implementation changelog reminder in plans and phase plans.
9. `README.md` and `docs/operator-note.md`: replace operational changelog commands or detailed claims with a high-level implementation-only handoff to `module:implementation-changelog`.
10. Generated small/medium spec and plan plus large/phased spec and phase-plan templates: regenerated outputs only.
11. `scripts/test_harness_policy.py`: replace matrix assertions/discoverability expectations with static policy/template/readiness and changelog-ownership checks; preserve implementation and release route checks.
12. `snapshots/test-cases.snapshot.md`: required pre-implementation test-case record for static policy/template and changelog-ownership cases.

## Implementation tasks

### `TASK-001` Define assessment cases before changing policy

Implements: `SPEC-003`; supports `VER-003` and `VER-005`.

Files:

1. Create `docs/work-items/2026-08-04_documentation-assessment-simplification/snapshots/test-cases.snapshot.md`.

Steps:

1. Record a positive case that lifecycle policy has exactly the five approved IDs in order and uses no changelog or architecture-snapshot assessment entry.
2. Record a positive case that both generated specification templates contain five status bullets, and that `Required` requires a path plus Plan Task while `Deferred` requires an owner plus resolution point.
3. Record a positive case that readiness checks are generic, and a negative case that restoring a full matrix, a copied ID list in readiness, or detailed changelog rows fails the static contract.
4. Record a phase-plan case: phase documentation prompts inherit the approved assessment and list only phase-owned required/deferred output, without a complete catalog or changelog procedure.
5. Record an ownership case: generic commit-subject grammar stays in naming; current fragment path/name, entry-heading/synchronization, lint, and consolidation instructions live in the implementation-changelog reference; planning freeze has no changelog action.
6. Record an audience case: plan/phase-plan have only a concise before-commit handoff, README/operator note have only an implementation-stage summary/link, and release sources retain release-stage consolidation context.

Exit criteria:

1. The snapshot gives an implementer concrete positive and negative assertions that map to `test_harness_policy.py` changes.
2. It contains no implementation placeholders and does not prescribe a new validator for arbitrary work-item artifacts.

### `TASK-002` Establish compact assessment and complete changelog ownership

Implements: `SPEC-001`, `SPEC-004`; supports `VER-001`, `VER-004`, and `VER-005`.

Files:

1. Modify `.agents/skills/dev-doc-harness/references/artifact-contract.md`.
2. Modify `.agents/skills/dev-doc-harness/references/naming-conventions.md`.
3. Modify `.agents/skills/dev-doc-harness/references/implementation-changelog.md`.
4. Modify `.agents/skills/dev-doc-harness/references/maintenance-architecture.md`, `durable-planning-quality.md`, and `.agents/skills/dev-doc-harness/SKILL.md`.

Steps:

1. Rename the lifecycle rule from `rule:lifecycle.documentation-matrix` to `rule:lifecycle.documentation-assessment` in its owner list and all active references.
2. Replace the matrix section with a compact five-row `ID | Consider when` list, status meanings, and the rule that every new substantial specification assesses every ID.
3. State that the assessment contains no changelog entry and no architecture-snapshot entry; point readers to the implementation module and Architecture Decisions respectively.
4. Remove changelog-entry synchronization requirements from lifecycle commit-message prose. Retain planned generic commit subjects, but make the implementation module the owner of current entry synchronization.
5. Move `<changelog-fragment-path>`, `<changelog-heading>`, fragment filename variants, and `## Changelog entries` guidance out of naming. Retain work IDs, artifact filenames, and generic commit-subject grammar there.
6. Add the moved fragment location, filename variants, heading grammar, and commit-subject synchronization details to `implementation-changelog.md`, alongside its existing metadata, lint, consolidation, compatibility, and cleanup instructions.
7. Update maintenance architecture, quality wording, and skill checklist/router language to name documentation assessment and distinguish plan, implementation, and release responsibilities without duplicating detailed changelog procedure.
8. Search active current-policy files for retired matrix and misplaced current-changelog rules; correct active owners or consumers only, and do not alter frozen historical work items.

Exit criteria:

1. Lifecycle policy contains the exact approved IDs and no full documentation matrix.
2. Naming contains no current fragment/entry procedure; implementation-changelog contains the complete current procedure.
3. Planning/freeze policy contains no changelog procedure beyond the concise plan handoff, and release sources retain only release-stage context.
4. Current policy references use the new rule name and ownership boundaries consistently.

### `TASK-003` Replace repeated template content with assessment and handoff prompts

Implements: `SPEC-002`, `SPEC-003`, `SPEC-004`; supports `VER-002`, `VER-003`, `VER-004`, and `VER-005`.

Files:

1. Remove `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.080.common.documentation-matrix.md`.
2. Create `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.080.common.documentation-assessment.md`.
3. Modify `.agents/skills/dev-doc-harness/assets/templates/assemblies/small-medium-work-item-spec.json` and `large-phased-work-item-spec.json`.
4. Modify affected spec header and readiness blocks.
5. Modify `plan.060.small.planned-commits.md`, `plan.060.phase.planned-commits.md`, `plan.080.phase.documentation-tasks.md`, `plan.090.small.readiness-completion-approval.md`, `plan.090.phase.readiness-completion-approval.md`, and `plan-amendment.md`.
6. Modify `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md`.

Steps:

1. Write the shared assessment block with exactly five readable status bullets, one short instruction for `Required`, one for `Deferred`, and no catalog trigger prose, changelog rows, or architecture-snapshot row.
2. Change both spec manifests to consume the new block; update policy references and generic spec readiness language to use `rule:lifecycle.documentation-assessment` without reproducing the IDs.
3. Remove changelog behavior from spec planned-commit prompts and the amendment template. Replace small and phase plan wording that describes a matching changelog entry with one concise reminder to follow `module:implementation-changelog` before implementation commits.
4. Replace phase Documentation Tasks with a short prompt that consumes the approved assessment and records only documentation outputs owned by that phase; it must neither repeat the five-item list nor describe changelog operations.
5. Make small and phase plan readiness lines generic: required documentation outputs are assigned to tasks, deferred items have owner/resolution, and detailed changelog mechanics are not a plan artifact.
6. Reduce README and operator-note wording to an implementation-only summary and reference; remove command, fragment filename, metadata, lint, and consolidation procedure from planning-facing/operator orientation text.

Exit criteria:

1. Each planning surface owns only its expected detail: policy list, spec decision bullets, or generic readiness/task handoff.
2. No planning template, amendment template, README, or operator note carries a matrix or detailed changelog procedure.
3. Architecture snapshot remains in its existing Architecture Decisions prompt.

### `TASK-004` Regenerate and protect the compact contract

Implements: `SPEC-001`, `SPEC-002`, `SPEC-003`, `SPEC-004`; verifies `VER-001` through `VER-005`.

Files:

1. Modify `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
2. Regenerate `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`, `large-phased-work-item-spec.md`, `small-medium-work-item-plan.md`, and `large-phased-work-item-phase-plan.md` through the assembler.

Steps:

1. Replace static assertions and discoverability wording that require `Documentation artifact matrix` with assertions for the renamed rule, five canonical IDs, shared spec assessment heading/bullets, and generic readiness wording.
2. Change changelog assertions so naming no longer owns fragment path/heading grammar, implementation-changelog owns complete current authoring rules, plan/phase plan have one concise handoff, planning freeze has no action, and release references retain their release-specific checks.
3. Add a narrow current-surface allowlist or equivalent assertions for permitted high-level changelog mentions in README/operator note; reject fragment path, filename, metadata, lint, or consolidation procedure outside implementation/release owners.
4. Do not add command-line modes, parsing fixtures, or semantic validation for created work-item specs/plans.
5. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` to regenerate affected outputs and execute its integrated validator.
6. Run the explicit validation checks below, then review the scoped diff for generated-file freshness, correct changelog ownership, unexpected current-policy changes, and untouched frozen history.

Exit criteria:

1. Generated templates are current and show the new compact contract.
2. Static validation protects policy, template body, readiness, and changelog-ownership boundaries without becoming a second work-item framework.
3. All checks pass with no unrelated diff.

## Plan checks

### `CHECK-001` Policy and template contract

Covers: `VER-001`, `VER-002`, `VER-003`, `VER-004`.

Run: `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`

Expected result: exits `0`; reports harness policy checks as passed, including the updated documentation-assessment, implementation-only changelog ownership, and release contracts.

### `CHECK-002` Assembly freshness

Covers: `VER-002`, `VER-005`.

Run: `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`

Expected result: exits `0` and prints `All assembled templates are current.`

### `CHECK-003` Retired-matrix and changelog-leak scan

Covers: `VER-001`, `VER-004`.

Run: `rg -n "Documentation artifact matrix|rule:lifecycle\.documentation-matrix|matching compact changelog entry|matching changelog fragment" .agents/skills/dev-doc-harness README.md`

Expected result: no active current policy, template, README, or validator occurrence; immutable historical work items are outside this command's target.

### `CHECK-004` Diff hygiene

Covers: `VER-005`.

Run: `git diff --check`, then review the diff limited to `README.md`, `.agents/skills/dev-doc-harness`, and this work-item folder.

Expected result: no whitespace errors; changes are limited to planned policy, implementation-reference, template, operator/README, generated-output, validator, and planning-package paths.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: documentation-assessment-simplification -- approve compact documentation prompts` |
| Implementation | `docs: documentation-assessment-simplification -- simplify documentation assessment` |

The implementation commit is cohesive because policy ownership, implementation-reference rules, source blocks, operator guidance, generated outputs, test contract, and test-case snapshot form one maintained lifecycle/template contract.

Implementation changelog: before an implementation commit, follow `module:implementation-changelog`.

## Model and Sub-agent Strategy

### Upcoming-stage sub-agent assessment

1. Method: `superpowers:executing-plans`.
2. Orchestration mode: bounded delegated sub-agents; the execution controller is the only writer and the sole delegate is the final reviewer.
3. Run in: new orchestration session.
4. Working location: the existing local repository checkout; do not create or use a worktree.
5. Review: one independent final implementation reviewer sub-agent after all planned changes and checks, using Sol with high reasoning; it receives a curated frozen package, final diff, and validation evidence, then reports evidence-backed findings to the execution controller.
6. Execution generation: latest available.
7. Execution capability tier: balanced.
8. Execution reasoning: medium.
9. Context strategy: the new session loads the frozen spec, plan, test-case snapshot, changed source blocks/manifests, current generated outputs, and focused validator assertions; it does not load frozen historical work items except as scoped evidence.
10. Sub-agents: one final independent reviewer only; it uses Sol high, has read-only review scope, and does not implement or modify files. No executor sub-agent is planned because the policy/template/validator changes share generated outputs and must be integrated by one controller.
11. Authorization boundary: do not edit implementation targets until this package is approved, committed, frozen, and a fresh operator instruction starts the new orchestration session.
12. Fallback: if the selected execution method is unavailable, use the harness-approved host-native route in the existing local checkout. If the final independent reviewer is unavailable, stop and report the blocker rather than silently replacing the required Sol-high review.

## Next-stage recommendation

### Stage

Stage: `plan execution`.

### Orchestration

Method: `superpowers:executing-plans`.

Orchestration mode: `bounded delegated sub-agents (final reviewer only)`.

Run in: `new orchestration session`.

Working location: `existing local repository checkout; no worktree`.

Review: `one final independent reviewer sub-agent using Sol high; curated frozen package, final diff, and validation evidence; read-only report to the execution controller`.

### Model

Generation: `latest available for execution controller`.

Capability tier: `balanced for execution controller`.

Reasoning: `medium for execution controller; Sol high for final reviewer`.

### Execution requirements and contingencies

1. A fresh operator instruction starts the approved work in a new orchestration session using the existing local checkout; it must not create a worktree.
2. Run the four Plan Checks, preserve frozen historical work items, and stop for a variance/amendment if scope expands beyond the approved policy/template contract.
3. After implementation and checks, run the required Sol-high final review. The execution controller integrates fixes, reruns affected checks, and reports the review findings and disposition.

## Readiness

- [x] This plan is self-sufficient: inputs, change surfaces, task boundaries, expected outputs, and checks let a fresh executor implement it without reconstructing hidden context.
- [x] Every task has a bounded outcome, exact source surfaces, executable steps, and observable exit criteria.
- [x] Plan Checks cover every Verification Criterion, including generated-template and static-policy validation.
- [x] Required documentation output is assigned to `TASK-001`; no deferred documentation item remains.
- [x] The implementation-changelog handoff is concise and detailed mechanics remain implementation-stage only.
- [x] The next-stage strategy records new-session continuity, existing-local-checkout location, balanced/medium execution, one read-only Sol-high final reviewer, and the authorization boundary.
- [x] No placeholder, unresolved implementation decision, missing owner, or ownerless deferral remains.

## Completion

- Required work and evidence are complete; any noteworthy variance is recorded.
- Planned changes are committed, or the blocker is stated.

## Approval

- Status: Approved
- Superseded by: None
