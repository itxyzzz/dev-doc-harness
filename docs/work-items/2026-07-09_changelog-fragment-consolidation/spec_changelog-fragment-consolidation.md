# Changelog Fragment Consolidation Spec

Work ID: `2026-07-09_changelog-fragment-consolidation`
Short ID: `changelog-fragment-consolidation`
Status: Approved
Harness release: `0.5+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `module:release`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.changelog-before-commit`, `rule:lifecycle.work-item-architecture-decisions`, `rule:release.changelog-source`, `rule:naming.derived-patterns`, `rule:naming.changelog-entries`, `rule:quality.spec-handoff`

## Goal

Replace the root `CHANGELOG.md` as the routine pre-commit write target with work-item-local changelog source fragments, then consolidate those fragments into the root changelog at an explicit operator-owned checkpoint such as after merge, before publication, or before the operator's product/application release.

## Source and Intent

Source input:

1. Operator described parallel work in independent worktrees where the full harness flow is otherwise safe, but every branch must edit `CHANGELOG.md` and therefore predictably conflicts.
2. Investigation found current lifecycle and freeze-gate policy require `CHANGELOG.md` before every commit, including planning approval commits.
3. Investigation found root `CHANGELOG.md` is also source material for this repository's package-local Dev Doc Harness release notes, so the fix must preserve curated root changelog and release-note traceability for harness distribution without implying control over downstream product release processes.

Desired operator outcome:

1. Independent work items can follow the full harness flow in separate worktrees without routine root changelog merge conflicts.
2. Each commit still has durable, reviewable changelog source material synchronized with its planned subject.
3. Root `CHANGELOG.md` remains a curated publication view after an explicit consolidation checkpoint, and harness-distribution release-note traceability remains intact for this repository.

Success summary:

1. Harness policy allows agents to satisfy the pre-commit changelog requirement through work-item-local fragment files under `docs/work-items/<work-id>/changelog/`.
2. A consolidation mechanism validates and copies unreleased fragment entries into root `CHANGELOG.md` idempotently.
3. Freeze-gate, templates, operator guidance, harness-maintainer release guidance, and validator checks all describe the same fragment-first workflow without claiming ownership over application release processes.

## Scope Boundary

### In scope

1. Add a canonical work-item-local changelog fragment location and naming guidance.
2. Update lifecycle and freeze-gate policy so routine planning and implementation commits update changelog source fragments before committing.
3. Preserve root `CHANGELOG.md` as the curated publication view after consolidation, including this repository's role as source material for Dev Doc Harness distribution release notes.
4. Add a consolidation script that validates fragment shape and inserts missing unreleased entries into root `CHANGELOG.md`.
5. Update templates so future specs and plans list changelog source fragments in the documentation matrix and planned commit synchronization prompts.
6. Update this repository's harness-maintainer release branch guidance so Dev Doc Harness release prep consolidates fragments before package-local release-note curation.
7. Add operator-facing guidance that downstream projects can run consolidation after merge, before their own release, or at another project-specific integration checkpoint; the harness owns only its changelog source and consolidation contract, not the application's release process.
7. Add harness validator coverage for the fragment policy, consolidation script, template guidance, and root changelog schema compatibility.
8. Update root `CHANGELOG.md` under the current pre-fragment rules for this planning package and its implementation commit.

### Non-scope

1. Do not remove root `CHANGELOG.md`.
2. Do not make Dev Doc Harness distribution release notes independent of root `CHANGELOG.md`.
3. Do not introduce a custom Git merge driver for `CHANGELOG.md`.
4. Do not rewrite historical work-item artifacts to add fragments.
5. Do not require every downstream repository to adopt generated changelog publication; the harness should support explicit consolidation.
6. Do not change Dev Doc Harness package release versioning, package boundary, or release-note file naming.
7. Do not define or constrain release processes for applications, packages, or agentic systems that use the harness.

### Assumptions

1. Independent worktrees normally create distinct work-item folders, so work-item-local fragment files avoid merge overlap.
2. Root changelog ordering can be reconstructed from fragment headings and metadata at consolidation time.
3. Existing Dev Doc Harness release-note curation can continue once root `CHANGELOG.md` contains the consolidated entries.
4. Downstream projects may have their own changelog, release-note, deployment, or publication conventions; the harness should provide a universal consolidation checkpoint that can fit those conventions.
4. Historical root changelog entries remain valid and do not need to be moved into fragment files.

### Open questions

1. None after operator design approval on 2026-07-09.

## Repository Context

### Current state

1. `references/artifact-contract.md` requires root `CHANGELOG.md` before every commit and lists it as the required living changelog artifact.
2. `references/planning-freeze-gates.md` requires approval freeze commits to update, stage, and commit root `CHANGELOG.md` with finalized planning artifacts.
3. Current templates refer to `CHANGELOG.md` directly in planned commit prompts, readiness checks, documentation matrices, and completion criteria.
4. `references/release-policy.md` defines Dev Doc Harness distribution release identity and says root `CHANGELOG.md` is repository source material for package-local harness release notes; it is not a generic application release policy.
5. `docs/release-branch-process.md` is a maintainer-facing process for cutting Dev Doc Harness release branches in this repository.
6. `scripts/test_harness_policy.py` validates current release-note source entries by checking headings in root `CHANGELOG.md`.
7. Root `CHANGELOG.md` places new unreleased entries at one shared insertion point, making independent worktree merges conflict-prone.

### Evidence read

1. `.agents/skills/dev-doc-harness/SKILL.md`
2. `.agents/skills/dev-doc-harness/references/artifact-contract.md`
3. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
4. `.agents/skills/dev-doc-harness/references/naming-conventions.md`
5. `.agents/skills/dev-doc-harness/references/release-policy.md`
6. `.agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md`
7. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
8. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
9. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
10. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
11. `.agents/skills/dev-doc-harness/assets/templates/architecture-snapshot.md`
12. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`
13. `docs/release-branch-process.md`
14. `CHANGELOG.md`
15. `README.md`
16. `docs/work-items/2026-07-09_plan-task-block-format/spec_plan-task-block-format.md`
17. `docs/work-items/2026-07-09_plan-task-block-format/plan_plan-task-block-format.md`

### Constraints and compatibility

1. Current freeze-gate policy remains in force until this work is implemented; this work item's planning approval commit must still update root `CHANGELOG.md`.
2. The new fragment format must keep the same release metadata fields: `Release target`, `Package impact`, and `Release-note`.
3. Commit subjects and changelog entry title snippets must remain synchronized.
4. Root changelog must remain readable and curated for humans, not only generated output.
5. Dev Doc Harness distribution release-note source traceability must continue to find source headings in root `CHANGELOG.md` after consolidation.
6. Downstream operator guidance must describe when to run consolidation without taking over the downstream product/application release process.
6. Frozen historical artifacts are not rewritten only to match the new fragment workflow.

## Requirements

### `REQ-001` Work-item-local changelog source fragments

Rationale:

1. The bottleneck exists because independent branches all write the same root changelog insertion point.

Acceptance links:

1. Covered by `AC-001`, `AC-002`, and `AC-006`.

Notes:

1. Fragment files live under `docs/work-items/<work-id>/changelog/`.
2. Fragment headings follow existing `rule:naming.changelog-entries` grammar.
3. Fragment bodies use the current root changelog metadata fields and Keep a Changelog subsections.
4. Fragment filenames should be stable and descriptive, such as `planning-approval.md`, `implementation.md`, or `phase-01.md`.

### `REQ-002` Fragment-first commit policy

Rationale:

1. The harness must preserve the pre-commit audit guarantee while changing the write target that causes conflicts.

Acceptance links:

1. Covered by `AC-001`, `AC-003`, `AC-006`, and `AC-007`.

Notes:

1. Before each commit, agents update the work-item-local changelog source fragment for that commit.
2. Planning freeze-gate commits stage approved planning artifacts plus their changelog source fragment; root `CHANGELOG.md` is staged only when the gate is intentionally consolidating.
3. Implementation commits stage implementation files plus their changelog source fragment.

### `REQ-003` Root changelog consolidation mechanism

Rationale:

1. Root `CHANGELOG.md` must remain the curated publication view and release-note source without being the routine branch-local write target.

Acceptance links:

1. Covered by `AC-002`, `AC-004`, `AC-005`, `AC-006`, and `AC-007`.

Notes:

1. Add a script under `.agents/skills/dev-doc-harness/scripts/` to scan fragment files, validate schema, and insert missing unreleased entries into root `CHANGELOG.md`.
2. The script should be idempotent: rerunning it without new fragments leaves root changelog unchanged.
3. The script should support a check mode for validation workflows.
4. Consolidation should preserve existing root changelog entries and avoid duplicating fragment headings already present.

### `REQ-004` Harness distribution release-source compatibility

Rationale:

1. Dev Doc Harness package-local release notes are curated from root changelog entries today, and that harness distribution contract should remain stable.

Acceptance links:

1. Covered by `AC-004`, `AC-005`, and `AC-007`.

Notes:

1. This repository's Dev Doc Harness release branch preparation must consolidate fragments before renaming `## Unreleased` and curating package-local harness release notes.
2. Harness release-note source entry validation may continue to check root `CHANGELOG.md` because consolidation makes the entries present there.
3. This requirement is not a rule for downstream application release notes.

### `REQ-005` Template and operator guidance alignment

Rationale:

1. Future agents will follow templates and README guidance more often than the raw policy modules.

Acceptance links:

1. Covered by `AC-003`, `AC-005`, `AC-006`, and `AC-007`.

Notes:

1. Update spec and plan templates, shared template blocks when applicable, README guidance, and package-local operator note if affected.
2. Documentation matrices should name changelog source fragments as the pre-commit artifact and root `CHANGELOG.md` as the consolidation output.
3. Guidance should tell operators to run consolidation at a project-owned checkpoint, such as after merging work branches, before preparing release notes, before publishing, or before any other process that requires root changelog completeness.
4. Guidance should explicitly say the harness does not own the downstream application's release process beyond its changelog source and consolidation contract.

### `REQ-006` Regression validation

Rationale:

1. The fragment workflow touches multiple process surfaces; validation should catch future drift back to root-only pre-commit language.

Acceptance links:

1. Covered by `AC-005`, `AC-006`, and `AC-007`.

Notes:

1. The validator should check current policy, templates, operator guidance, and Dev Doc Harness maintainer release guidance for the fragment/consolidation contract.
2. The validator should include sample or fixture coverage for fragment parsing, duplicate avoidance, and missing-schema failure paths.

## Acceptance Criteria

### `AC-001` Pre-commit changelog source can be work-item-local

Verifies:

1. `REQ-001`
2. `REQ-002`

Method:

1. Review lifecycle, freeze-gate, and template guidance after implementation.
2. Expected result: routine planning approval and implementation commits can satisfy changelog-before-commit through `docs/work-items/<work-id>/changelog/*.md` without requiring a root `CHANGELOG.md` edit.

### `AC-002` Fragment format preserves current changelog metadata

Verifies:

1. `REQ-001`
2. `REQ-003`

Method:

1. Review policy and test fixture examples.
2. Expected result: each fragment entry contains an existing changelog heading form plus exactly one `Release target`, `Package impact`, and `Release-note` field.

### `AC-003` Planning freeze gate stages fragments instead of root changelog by default

Verifies:

1. `REQ-002`
2. `REQ-005`

Method:

1. Review `references/planning-freeze-gates.md` and generated planning templates.
2. Expected result: the approval freeze checkpoint stages finalized planning artifacts plus the matching changelog source fragment; root `CHANGELOG.md` is not part of ordinary plan-only commits unless the operator is running consolidation.

### `AC-004` Consolidation updates root changelog idempotently

Verifies:

1. `REQ-003`
2. `REQ-004`

Method:

1. Run the planned consolidation validation.
2. Expected result: missing unreleased fragment entries are inserted under `## Unreleased`; existing root entries are not duplicated; a second run has no changes.

### `AC-005` Harness-maintainer release branch process consolidates before curation

Verifies:

1. `REQ-003`
2. `REQ-004`
3. `REQ-005`

Method:

1. Review `docs/release-branch-process.md` after implementation.
2. Expected result: Dev Doc Harness release prep explicitly runs or verifies changelog fragment consolidation before renaming `## Unreleased` and curating package-local harness release notes.

### `AC-006` Templates and docs guide agents to the fragment workflow

Verifies:

1. `REQ-001`
2. `REQ-002`
3. `REQ-005`
4. `REQ-006`

Method:

1. Review current generated templates, README guidance, and package-local operator guidance after implementation.
2. Expected result: future work-item specs and plans list changelog source fragments as the before-commit artifact and mention root `CHANGELOG.md` consolidation at operator-owned checkpoints such as after merge, before release notes, or before product/application release.

### `AC-007` Harness validation passes and protects the contract

Verifies:

1. All requirements.

Method:

1. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
2. Expected result: the validator exits successfully and includes checks for fragment policy discoverability, consolidation behavior, and release-source compatibility.

## Architecture Decisions

Architecture snapshot status:

1. Required: `snapshots/architecture.snapshot.md`.

Decision summary:

1. Drivers: parallel worktree throughput, audit trail preservation, release-note source compatibility, and reduced manual conflict resolution.
2. Constraints: root changelog remains the curated publication view and, for this repository, the Dev Doc Harness release-note source; commit/changelog synchronization remains mandatory; current freeze-gate behavior applies until implementation lands.
3. Selected approach: make work-item-local changelog fragments the pre-commit source artifact and consolidate them into root `CHANGELOG.md` at explicit operator-owned integration or publication checkpoints.
4. Affected boundaries: lifecycle policy, freeze-gate policy, naming guidance, templates, harness distribution release policy wording, harness maintainer release branch runbook, validator, root changelog workflow, and agent planning behavior.
5. Rejected alternatives: custom Git merge driver, root-only manual conflict resolution, generated-only changelog with no curated root view, and Dev Doc Harness package-local release notes as an independent history.
6. Validation cues: fragment parser tests, idempotent consolidation check, policy/template validator checks, downstream release-boundary review, and Dev Doc Harness maintainer release-flow review.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. Harness policy interface for the changelog-before-commit requirement.
2. Planning freeze-gate operator workflow and staged file expectations.
3. Template prompts for planned commits, documentation matrices, readiness checks, and completion criteria.
4. Script interface for changelog consolidation and check mode.
5. Dev Doc Harness maintainer release branch process steps for changelog and package-local release-note preparation.

### Data, config, and persistence

1. New work-item-local fragment files under `docs/work-items/<work-id>/changelog/`.
2. Root `CHANGELOG.md` remains the consolidated durable publication file.
3. No runtime data store, application config, or persistence migration is introduced.

### State and control flow

1. Before commit: update the work-item-local fragment matching the planned commit.
2. During ordinary branch work: leave root `CHANGELOG.md` unchanged unless the work intentionally consolidates.
3. During operator-owned integration, publication, or product/application release preparation: run consolidation to copy missing unreleased fragments into root changelog when that process requires a complete root changelog.
4. During this repository's Dev Doc Harness release prep: curate package-local harness release notes from the consolidated root changelog as today.

### Safety, security, privacy, migration, and rollback

1. No security or privacy impact is expected.
2. Migration is process-only: new work items use fragments; historical root changelog entries remain in place.
3. Rollback reverts the policy, template, script, validator, and documentation changes; existing fragment files remain review artifacts under their work-item folders and can be manually copied into root changelog if needed.

## Risks and Rejected Alternatives

### `RISK-001` Root changelog becomes stale

Decision or mitigation:

1. Make consolidation an explicit operator-owned integration or publication gate, and include it in this repository's Dev Doc Harness release-prep gate.
2. Add validator or script check mode to detect fragments not present in root changelog when consolidation is expected.

### `RISK-002` Release notes miss fragment-only changes

Decision or mitigation:

1. Update this repository's Dev Doc Harness release branch process to consolidate before package-local harness release-note curation.
2. Keep harness release-note source validation tied to root changelog after consolidation.

### `RISK-003` Fragment and root entries drift after consolidation

Decision or mitigation:

1. Treat fragment files as pre-commit source evidence and root changelog as publication view.
2. The consolidation script should skip duplicate headings and not rewrite existing root content silently.

### `RISK-004` Process change is larger than a local doc edit

Decision or mitigation:

1. Use a required architecture snapshot and test-case snapshot.
2. Keep implementation in one small/medium work item with focused script and validator changes.

### `RISK-005` Custom merge driver alternative hides semantic conflicts

Decision or mitigation:

1. Reject the merge-driver approach because it still writes the same file from every branch and cannot reliably preserve release metadata, ordering, and curated human edits.

### `RISK-006` Generated-only changelog alternative removes useful curation

Decision or mitigation:

1. Reject generated-only root changelog as the first step because this repository already uses curated release notes and human-readable root changelog sections.

## Planned Commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `plan: changelog-fragment-consolidation -- plan merge-friendly changelog sources` | `2026-07-09_changelog-fragment-consolidation -- plan merge-friendly changelog sources` | Approval commit for this spec, plan, architecture snapshot, test-case snapshot, and current-rule root changelog entry. |
| Implementation | `docs: changelog-fragment-consolidation -- add work-item changelog sources` | `2026-07-09_changelog-fragment-consolidation -- add work-item changelog sources` | Update policy, templates, consolidation script, validator, harness release guidance, README/operator guidance, and current-rule root changelog entry. |

## Documentation Artifact Matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` for this work item under current rules; future work items use `docs/work-items/<work-id>/changelog/*.md` before commit and consolidate to `CHANGELOG.md` at operator-owned checkpoints | This work must follow current root changelog rules until implementation changes them. |
| Test cases | Snapshot | Yes | Before implementation | `docs/work-items/2026-07-09_changelog-fragment-consolidation/snapshots/test-cases.snapshot.md` | Captures fragment parsing, consolidation, validation, operator checkpoint, and harness-maintainer release scenarios. |
| Testing guide delta | Living delta | Yes | During or after implementation | `docs/work-items/2026-07-09_changelog-fragment-consolidation/deltas/testing-guide.delta.md` | Record new consolidation/check validation commands if implementation changes operator testing guidance. |
| Operator manual delta | Living delta | Yes | After implementation | `docs/work-items/2026-07-09_changelog-fragment-consolidation/deltas/operator-manual.delta.md` | Record the new fragment-first workflow for later operator docs. |
| API reference delta | Living delta | No | Not applicable | N/A | No public API surface. |
| Architecture snapshot | Snapshot | Yes | Before implementation | `docs/work-items/2026-07-09_changelog-fragment-consolidation/snapshots/architecture.snapshot.md` | Required because lifecycle, release-source, and integration workflow boundaries change. |
| Architecture summary delta | Living delta | Deferred | After implementation review | `docs/work-items/2026-07-09_changelog-fragment-consolidation/deltas/architecture-summary.delta.md` | Create only if implementation changes long-lived architecture-summary guidance beyond this work-item snapshot. |

## Spec Readiness Checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Requirements are specific, relevant, bounded, and linked to acceptance criteria.
- [x] Acceptance criteria are observable, testable, and tied to requirements or scope items.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Interfaces, data, control flow, and safety/privacy/migration impacts are checked.
- [x] Risks and rejected alternatives are listed.
- [x] Documentation artifact matrix decisions have paths or reasons.
- [x] Planned commit subjects and changelog title snippets are synchronized.
- [x] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain before approval or handoff.

## Approval

- Status: Approved
- Superseded by: None
