# Changelog Fragment Consolidation Plan

Work ID: `2026-07-09_changelog-fragment-consolidation`
Short ID: `changelog-fragment-consolidation`
Status: Approved
Harness release: `0.5+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `module:release`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:lifecycle.changelog-before-commit`, `rule:release.changelog-source`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Input Artifacts

Read these before implementation:

1. Approved spec: `docs/work-items/2026-07-09_changelog-fragment-consolidation/spec_changelog-fragment-consolidation.md`.
2. Architecture input: `docs/work-items/2026-07-09_changelog-fragment-consolidation/snapshots/architecture.snapshot.md`.
3. Required snapshots or deltas:
   1. `docs/work-items/2026-07-09_changelog-fragment-consolidation/snapshots/test-cases.snapshot.md`
   2. `docs/work-items/2026-07-09_changelog-fragment-consolidation/deltas/testing-guide.delta.md`, to be created during or after implementation if validation guidance changes.
   3. `docs/work-items/2026-07-09_changelog-fragment-consolidation/deltas/operator-manual.delta.md`, to be created after implementation.
4. Relevant repository files:
   1. `.agents/skills/dev-doc-harness/SKILL.md`
   2. `.agents/skills/dev-doc-harness/references/artifact-contract.md`
   3. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
   4. `.agents/skills/dev-doc-harness/references/naming-conventions.md`
   5. `.agents/skills/dev-doc-harness/references/release-policy.md`
   6. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
   7. `.agents/skills/dev-doc-harness/assets/templates/blocks/`
   8. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
   9. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
   10. `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
   11. `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
   12. `.agents/skills/dev-doc-harness/scripts/assemble_templates.py`
   13. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`
   14. `docs/release-branch-process.md`
   15. `README.md`
   16. `CHANGELOG.md`
5. Unresolved implementation context to confirm before editing: none identified.

## Spec Traceability

| Requirement or acceptance criterion | Primary tasks | Validation |
|---|---|---|
| `REQ-001` Work-item-local changelog source fragments | `T-001`, `T-003`, `T-004`, `T-006`, `T-007` | `V-001`, `V-002`, `V-005`, `V-006`, `V-009` |
| `REQ-002` Fragment-first commit policy | `T-001`, `T-002`, `T-004`, `T-006`, `T-007` | `V-001`, `V-003`, `V-005`, `V-006`, `V-009` |
| `REQ-003` Root changelog consolidation mechanism | `T-002`, `T-005`, `T-006`, `T-007` | `V-002`, `V-004`, `V-007`, `V-009` |
| `REQ-004` Harness distribution release-source compatibility | `T-002`, `T-003`, `T-006`, `T-007` | `V-004`, `V-005`, `V-006`, `V-009` |
| `REQ-005` Template and operator guidance alignment | `T-001`, `T-003`, `T-004`, `T-006`, `T-007` | `V-001`, `V-003`, `V-005`, `V-006`, `V-009` |
| `REQ-006` Regression validation | `T-005`, `T-006`, `T-007` | `V-007`, `V-008`, `V-009`, `V-010` |
| `AC-001` Pre-commit changelog source can be work-item-local | `T-001`, `T-003`, `T-004`, `T-007` | `V-001`, `V-003`, `V-005`, `V-009` |
| `AC-002` Fragment format preserves current changelog metadata | `T-001`, `T-002`, `T-005` | `V-001`, `V-002`, `V-007`, `V-009` |
| `AC-003` Planning freeze gate stages fragments by default | `T-001`, `T-004`, `T-006` | `V-001`, `V-003`, `V-006`, `V-009` |
| `AC-004` Consolidation updates root changelog idempotently | `T-002`, `T-005`, `T-007` | `V-002`, `V-004`, `V-007`, `V-009` |
| `AC-005` Harness-maintainer release branch process consolidates before curation | `T-003`, `T-006`, `T-007` | `V-004`, `V-005`, `V-009` |
| `AC-006` Templates and docs guide fragment workflow | `T-004`, `T-006`, `T-007` | `V-003`, `V-006`, `V-009` |
| `AC-007` Harness validation passes and protects contract | `T-005`, `T-006`, `T-007` | `V-007`, `V-008`, `V-009`, `V-010` |

Architecture coverage:

1. Architecture input: `snapshots/architecture.snapshot.md`.
2. Plan usage: tasks preserve the selected fragment-source plus root-publication architecture across policy, templates, tooling, operator guidance, and harness-maintainer release flow.
3. Drift path: before freeze, edit this draft spec, plan, or architecture snapshot directly; after freeze, use the variance log or amendment process for changes that alter the fragment-first workflow, root publication role, harness distribution release-note source contract, or downstream release-process boundary.
4. Reinterpretation guard: implementation must not silently change the root changelog into a fully generated artifact, make Dev Doc Harness release notes depend directly on fragments, or claim ownership over downstream application release processes without an amendment.

## Implementation Approach

Update policy first so the new contract is explicit, then add tooling that makes the contract operational. The policy change should use careful wording: routine work-item commits update changelog source fragments, while root `CHANGELOG.md` remains the curated publication view after consolidation. In this repository, the consolidated root changelog also remains the source for Dev Doc Harness distribution release notes; downstream applications keep their own release process.

Add a small consolidation script with two responsibilities: validate fragment entries and copy missing unreleased fragment entries into root `CHANGELOG.md`. The script should be deterministic, idempotent, and conservative: it should not rewrite existing root entries or try to semantically merge edited text.

After policy and tooling exist, update templates and operator-facing docs so future agents naturally use the fragment workflow. Finish by extending the harness validator to protect policy discoverability, template language, script behavior, generic operator checkpoint guidance, and the harness-maintainer release-branch ordering used by this repository.

## Change Surfaces

Expected edits:

1. `.agents/skills/dev-doc-harness/references/artifact-contract.md`: define changelog source fragments and update changelog-before-commit semantics.
2. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: stage changelog source fragments by default during approval freeze; root changelog only when consolidating.
3. `.agents/skills/dev-doc-harness/references/naming-conventions.md`: add fragment path and filename guidance if needed for reusable naming.
4. `.agents/skills/dev-doc-harness/references/release-policy.md`: clarify this file is about Dev Doc Harness distribution release identity and release notes; evaluate whether to rename it to a more explicit harness-distribution release-policy name or update its title and router labels if a rename would create unnecessary churn.
5. `.agents/skills/dev-doc-harness/SKILL.md`: update router outcomes and checklist wording that currently names only root `CHANGELOG.md`.
6. `.agents/skills/dev-doc-harness/assets/templates/blocks/` and generated templates: update documentation matrix, planned commit, readiness, and completion wording.
7. `.agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py`: create fragment validation and root changelog consolidation script.
8. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: add policy/template/script validation checks and any script fixture checks.
9. `docs/release-branch-process.md`: for harness maintainers, consolidate fragments before Dev Doc Harness release changelog and package-local release-note curation.
10. `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md`: describe fragment-first workflow at the operator level, including consolidation after merge, before product/application release, or at another project-owned checkpoint.
11. `docs/work-items/2026-07-09_changelog-fragment-consolidation/deltas/testing-guide.delta.md`: record new validation command guidance if implementation changes testing docs.
12. `docs/work-items/2026-07-09_changelog-fragment-consolidation/deltas/operator-manual.delta.md`: record operator workflow delta.
13. `CHANGELOG.md`: update under current rules for this implementation commit.

Stable interfaces:

1. Root `CHANGELOG.md` remains the human-readable publication view.
2. Dev Doc Harness distribution release notes remain curated from root `CHANGELOG.md` in this repository.
3. Existing changelog entry heading grammar and release metadata fields remain valid.
4. Historical work-item artifacts and historical root changelog entries remain unchanged except normal new entries.
5. Planning freeze still requires an approval commit and stop-before-implementation boundary.

Changed interfaces:

1. The pre-commit changelog artifact becomes a work-item-local source fragment for ordinary work.
2. The approval freeze checkpoint stages changelog source fragments by default instead of root `CHANGELOG.md`.
3. Integration and publication preparation gain an explicit consolidation step; downstream product/application release preparation may include that step when the operator chooses.
4. The harness exposes a consolidation/check script for root changelog publication.

Implementation boundaries:

1. Do not implement a custom Git merge driver.
2. Do not make root changelog fully generated or disposable.
3. Do not change Dev Doc Harness distribution version identity or package boundary.
4. Do not define downstream product/application release processes.
4. Do not migrate old changelog entries into fragments.
5. Do not make the validator parse arbitrary old work-item artifacts for fragment compliance.

## Model and Sub-agent Strategy

Current orchestration:

1. Model/profile and reasoning effort if known: not exposed.
2. Model-policy source: active repository policy from `AGENTS.md`, using `economy-default`.
3. Override scope and expiry: none.

Fit assessment:

1. Complexity: medium-high because lifecycle, harness distribution release wording, templates, operator guidance, and tooling must change together.
2. Risk and blast radius: high for harness users because a wrong freeze-gate instruction can break commit discipline or release-note traceability.
3. Ambiguity: low after operator selected the fragment/consolidation approach.
4. Budget and latency fit: acceptable with one read-only review sub-agent after implementation because main-thread integration remains important.

Recommended orchestration change:

1. Use the current main-thread orchestration for implementation and final integration.
2. Use a single read-only reviewer sub-agent after implementation if available and authorized by the frozen plan.

Sub-agents:

Sub-agent `reviewer-01`:

1. Purpose: review the completed policy, template, tooling, and validator diff for contradictions in the new fragment workflow.
2. Context strategy: curated artifacts.
3. Input context: approved spec, approved plan, architecture snapshot, test-case snapshot, implementation diff, validator output, operator guidance diff, and harness-maintainer release-process diff.
4. Output artifact: review findings in the implementation completion notes or variance log if nontrivial issues are found.
5. Model policy: active repository policy, `economy-default`.
6. Model class/profile: latest strongest available class if exposed; otherwise default review-capable profile.
7. Reasoning effort: high because this is final review of lifecycle, operator-boundary, and harness distribution release-policy behavior.
8. Selection reason: cross-surface contradictions are subtle and high-blast-radius.
9. Parallel execution: No; run after implementation validation.
10. Blast radius if wrong: Medium, because the orchestration thread owns final integration and can reject weak findings.

## Task Plan

### `T-001` Define fragment-first lifecycle policy

Dependencies:

1. Approved planning artifacts.

Implementation:

1. Modify `.agents/skills/dev-doc-harness/references/artifact-contract.md`.
2. Add a changelog source fragment location under `docs/work-items/<work-id>/changelog/`.
3. Update `rule:lifecycle.changelog-before-commit` so before-commit evidence is the matching changelog source fragment for ordinary work.
4. Preserve root `CHANGELOG.md` as the consolidated publication view and explain when it is updated.
5. Update documentation matrix wording to distinguish changelog source fragments from root changelog consolidation.
6. Modify `.agents/skills/dev-doc-harness/references/naming-conventions.md` only if reusable fragment path or filename grammar is needed.

Exit criteria:

1. Lifecycle policy no longer requires ordinary independent worktree commits to edit root `CHANGELOG.md`.
2. Policy still requires every planned commit to have synchronized changelog source material before commit.
3. Root changelog consolidation remains mandatory before Dev Doc Harness package-local release-note curation in this repository.
4. Operator guidance clearly says downstream projects run consolidation at a project-owned checkpoint and keep their own release process.

Notes:

1. Keep this work item's own approval and implementation commits under the current root changelog rule until the implementation commit lands.

### `T-002` Add conservative changelog consolidation script

Dependencies:

1. `T-001`

Implementation:

1. Create `.agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py`.
2. Implement fragment discovery for `docs/work-items/*/changelog/*.md`.
3. Validate each fragment entry heading and metadata fields: exactly one `Release target`, `Package impact`, and `Release-note`.
4. Reject malformed fragments with clear file-path and heading errors.
5. Insert missing unreleased fragment entries under root `CHANGELOG.md` `## Unreleased`.
6. Skip entries whose heading already exists in root changelog.
7. Preserve existing root changelog content and historical release sections.
8. Add a `--check` mode that exits nonzero when valid fragments are missing from root changelog or malformed.

Exit criteria:

1. The script can consolidate missing fragments without duplicating existing headings.
2. The script can report check-mode failures without modifying files.
3. The script is deterministic enough for review and validation.

Notes:

1. Prefer standard-library Python only.
2. Keep semantic curation out of the script; release notes remain manually curated.

### `T-003` Preserve harness distribution release-source compatibility

Dependencies:

1. `T-001`
2. `T-002`

Implementation:

1. Modify `.agents/skills/dev-doc-harness/references/release-policy.md`.
2. State that the file describes Dev Doc Harness distribution release identity, package-local release notes, package boundary, adoption, and rollback.
3. Evaluate a low-risk rename to a more explicit file name such as `harness-release-policy.md`; if route churn is too high for this work item, keep the path and clarify the title, introductory paragraph, router labels, and references instead.
4. State that root `CHANGELOG.md` remains the Dev Doc Harness release-note source after fragment consolidation.
5. Clarify that fragments are pre-publication source evidence, not independent Dev Doc Harness release notes.
6. Modify `docs/release-branch-process.md` so Dev Doc Harness release prep runs or verifies consolidation before renaming `## Unreleased`.
7. Keep current Dev Doc Harness release-note curation and source-entry requirements unchanged after consolidation.
8. Add explicit wording that downstream applications, packages, or agentic systems using the harness have their own release processes outside this policy.

Exit criteria:

1. Harness distribution release policy preserves the root changelog source contract.
2. Harness maintainer release branch process includes consolidation before package-local release-note curation.
3. No Dev Doc Harness release versioning or package boundary rule changes are introduced.
4. The docs distinguish harness distribution release flow from downstream product/application release flow.

### `T-004` Update templates and operator-facing guidance

Dependencies:

1. `T-001`
2. `T-003`

Implementation:

1. Update relevant template source blocks under `.agents/skills/dev-doc-harness/assets/templates/blocks/` so planned commit prompts, documentation matrices, readiness checks, and completion criteria refer to changelog source fragments before ordinary commits.
2. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py`.
3. Review generated small/medium and large/phased templates for consistent fragment guidance.
4. Update `.agents/skills/dev-doc-harness/SKILL.md` workflow and completion checklist wording.
5. Update `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md` with concise operator guidance for fragment-first work and consolidation gates, including after merging work branches, before preparing project release notes, before product/application release, or at another checkpoint selected by the operator.
6. Create or update `docs/work-items/2026-07-09_changelog-fragment-consolidation/deltas/operator-manual.delta.md`.

Exit criteria:

1. Future generated specs and plans point agents to `docs/work-items/<work-id>/changelog/*.md` as the routine pre-commit changelog source.
2. Operator-facing docs explain when root `CHANGELOG.md` is consolidated without prescribing the downstream product/application release process.
3. Generated templates are regenerated from source blocks rather than hand-edited.

### `T-005` Add validation and script fixtures

Dependencies:

1. `T-002`
2. `T-004`

Implementation:

1. Modify `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
2. Add checks that current policy, templates, operator docs, and this repository's harness-maintainer release process mention changelog fragments and consolidation.
3. Add fixture-style validation for the consolidation script using temporary files or a contained test helper pattern consistent with the existing script.
4. Cover these cases: valid fragment insertion, duplicate heading skip, malformed fragment metadata failure, and `--check` failure when root changelog is missing a valid fragment.
5. Ensure existing Dev Doc Harness release-note source validation continues to check root `CHANGELOG.md`.
6. Create or update `docs/work-items/2026-07-09_changelog-fragment-consolidation/deltas/testing-guide.delta.md` if new commands or expected outputs should be preserved.

Exit criteria:

1. Validator protects the fragment/consolidation contract without rewriting historical artifacts.
2. Script behavior is exercised enough to catch the core merge-conflict bottleneck regression.
3. Existing Dev Doc Harness distribution release validation remains compatible after consolidation.

### `T-006` Validate policy consistency and run harness checks

Dependencies:

1. `T-001`
2. `T-002`
3. `T-003`
4. `T-004`
5. `T-005`

Implementation:

1. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
2. Run the consolidation script in `--check` mode if the command is separate from the harness validator.
3. Use `rg` to inspect remaining root-only pre-commit wording in current harness policy and templates.
4. Review the diff for accidental historical artifact rewrites.
5. Run the planned read-only reviewer sub-agent if available and authorized after implementation validation.

Exit criteria:

1. Harness validator exits successfully.
2. Consolidation check exits successfully or reports only expected current-rule planning-package state documented in the implementation notes.
3. Remaining root `CHANGELOG.md` references clearly describe publication, consolidation, operator-selected checkpoints, Dev Doc Harness release prep, or this work item's current-rule transition.
4. Reviewer findings are resolved, recorded as variance, or reported as residual risk.

### `T-007` Update current-rule root changelog and prepare implementation commit

Dependencies:

1. `T-006`

Implementation:

1. Add a newest-first root `CHANGELOG.md` entry for `2026-07-09_changelog-fragment-consolidation -- add work-item changelog sources` under the current pre-fragment rules.
2. Verify planned subject and changelog title snippet stay synchronized.
3. Stage only planned implementation files, work-item deltas created during implementation, and root `CHANGELOG.md`.
4. Commit with `docs: changelog-fragment-consolidation -- add work-item changelog sources`.

Exit criteria:

1. Implementation commit contains only planned files or recorded variance.
2. Root changelog entry exists for this implementation under the old rule.
3. Final report includes validation output, reviewer use if any, commit hash, and variance.

Notes:

1. After this implementation commit lands, later work items should use fragments for routine commits.

## Planned Commits

Planning approval commit:

1. Planned subject: `plan: changelog-fragment-consolidation -- plan merge-friendly changelog sources`.
2. Changelog title or snippet: `2026-07-09_changelog-fragment-consolidation -- plan merge-friendly changelog sources`.
3. Notes: approval commit for this spec, plan, architecture snapshot, test-case snapshot, and current-rule root changelog entry.

Implementation commit:

1. Planned subject: `docs: changelog-fragment-consolidation -- add work-item changelog sources`.
2. Changelog title or snippet: `2026-07-09_changelog-fragment-consolidation -- add work-item changelog sources`.
3. Notes: policy, template, consolidation script, validator, harness release guidance, operator docs, deltas, and current-rule root changelog update.

## Validation Plan

| ID | Command | Expected result |
|---|---|---|
| `V-001` | Manual review of `.agents/skills/dev-doc-harness/references/artifact-contract.md` | Changelog-before-commit rule names work-item-local fragments as routine source evidence and root changelog as consolidated publication view. |
| `V-002` | Manual review of `.agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py` | Script discovers `docs/work-items/*/changelog/*.md`, validates required metadata, inserts missing unreleased entries, skips duplicates, and supports `--check`. |
| `V-003` | Manual review of `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md` | Approval freeze stages approved planning artifacts plus matching changelog source fragment by default, not root changelog. |
| `V-004` | Manual review of `.agents/skills/dev-doc-harness/references/release-policy.md` | File scope is clearly Dev Doc Harness distribution release identity and release notes; root `CHANGELOG.md` remains harness release-note source after consolidation; fragments are source evidence and not independent release notes. |
| `V-005` | Manual review of `docs/release-branch-process.md` | Harness maintainer release branch flow consolidates fragments before renaming `## Unreleased` and curating Dev Doc Harness package-local release notes. |
| `V-006` | Manual review of current generated templates and README/operator note | Templates and operator docs describe fragment-first commits and root changelog consolidation at operator-owned checkpoints without prescribing downstream application release processes. |
| `V-007` | `python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --check` | Exits successfully after consolidation or reports only expected missing consolidation before the implementation's final consolidation step, with no malformed fragment errors. |
| `V-008` | `rg -n "CHANGELOG.md.+before each commit|Update `CHANGELOG.md` before every commit|stage only .*CHANGELOG.md" .agents/skills/dev-doc-harness README.md docs/release-branch-process.md` | Remaining matches either refer to current historical artifacts, root publication/consolidation, operator checkpoints, Dev Doc Harness release prep, or this work item's transition note; no current root-only routine pre-commit instruction remains. |
| `V-009` | `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | Exits successfully with fragment policy, consolidation behavior, template guidance, operator-boundary guidance, and harness release-source compatibility checks passing. |
| `V-010` | `git diff --name-only` before implementation staging | Contains only planned policy, template, script, validator, docs, deltas, work-item files, and root `CHANGELOG.md`, unless variance is recorded. |

## Plan Variance Handling

Before implementation begins, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `docs/work-items/2026-07-09_changelog-fragment-consolidation/implementation-notes/variance-log.md`; use a plan amendment for changes that alter the selected fragment-first workflow, root changelog publication role, Dev Doc Harness release-note source contract, downstream release-process boundary, consolidation script scope, acceptance criteria, or feasibility.

## Planning Artifact Freeze Gate

Draft review state: approved by operator on 2026-07-10.
Approval commit: this planning freeze gate commit.
Post-freeze implementation authorization: not requested.

## Plan Readiness Checklist

- [x] Input artifacts and relevant repository context have been read and listed.
- [x] Every spec requirement and acceptance criterion has at least one task and one validation path.
- [x] Risks, scope boundaries, interfaces, and documentation decisions are either covered by tasks or explicitly marked as no-op with a reason.
- [x] Task detail is sufficient for a fresh implementation agent or delegated reviewer to execute its assigned part without inventing task order, file scope, validation, or documentation steps.
- [x] Validation entries have exact commands, manual checks, review findings, or operator acceptance paths with expected signals.
- [x] Planned commits and changelog title snippets are synchronized.
- [x] Variance handling is clear for likely implementation drift.
- [x] The work still fits one orchestration thread with a bounded review sub-agent strategy.
- [x] Sub-agent strategy follows `module:models`.
- [x] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain before approval or handoff.

## Completion Criteria

1. Acceptance criteria in `spec_changelog-fragment-consolidation.md` are met.
2. Required validation commands have been run and recorded.
3. Required documentation artifacts have been created or updated.
4. The frozen plan had enough detail for implementation to proceed safely.
5. Root `CHANGELOG.md` has a newest-first entry before this work item's planning and implementation commits under current rules.
6. After implementation lands, future routine work-item commits can use changelog source fragments instead of root `CHANGELOG.md`.
7. Commit subjects match approved planned subjects or recorded variance.
8. Variance log is current if variance occurs.
9. De-facto sub-agent use is reported if the reviewer sub-agent is used.

## Approval

- Status: Approved
- Superseded by: None
