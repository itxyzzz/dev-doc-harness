# Changelog Lifecycle Simplification Plan

Work ID: `2026-08-01_changelog-lifecycle-simplification`
Short ID: `changelog-lifecycle-simplification`
Status: Approved
Harness release: `0.8+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:release`, `rule:lifecycle.variance-policy`
Execution method: `superpowers:executing-plans`
Current planning Codex task: Model/profile, reasoning, and context visibility: `not exposed`.

## Input artifacts

1. Approved spec: `spec_changelog-lifecycle-simplification.md`.
2. Architecture input: `snapshots/architecture.snapshot.md`.
3. Required snapshots: `snapshots/test-cases.snapshot.md`.
4. Relevant repository files: `CHANGELOG.md`, `.agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py`, `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, current policy references, `.agents/skills/dev-doc-harness/references/maintenance-architecture.md`, template source blocks, assemblies, generated templates, and `README.md`.
5. Unresolved implementation context to confirm before editing: None identified.

## Traceability approach

Local `SPEC-*`, `VER-*`, `TASK-*`, and `CHECK-*` links provide complete coverage without a separate mapping.

## Change surfaces

1. `.agents/skills/dev-doc-harness/references/implementation-changelog.md`: new sole owner for current implementation-stage changelog lifecycle, compact schema, compatibility, and consolidation.
2. `.agents/skills/dev-doc-harness/references/artifact-contract.md`: remove planning-stage changelog ownership and route implementation work to the dedicated module.
3. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: remove planning changelog fragment and root-update requirements.
4. `.agents/skills/dev-doc-harness/SKILL.md`: update the primary operation router so execution and changelog-maintenance routes load the dedicated implementation-changelog reference, while spec/plan drafting and freeze routes do not load it.
5. `.agents/skills/dev-doc-harness/references/naming-conventions.md`, `release-policy.md`, and `README.md`: align naming, package-boundary, and release-source wording with the new route.
6. `.agents/skills/dev-doc-harness/references/maintenance-architecture.md`: update `## Lifecycle Decomposition Direction` to establish the implementation-changelog module as the selected lifecycle split and to keep work sizing, layouts, orchestration, immutability, and variance under lifecycle ownership.
7. `.agents/skills/dev-doc-harness/assets/templates/blocks/`, assemblies, and generated templates: remove planning fragment requirements and place compact implementation guidance only where an implementation handoff needs it.
8. `.agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py`: parse compact current metadata and legacy frozen metadata, select only eligible implementation entries, and preserve idempotency.
9. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: add schema, lifecycle, frozen-boundary, and idempotency regression coverage.
10. `CHANGELOG.md`: remove all planning-only sections and rewrite surviving metadata to one compact tagged line.
11. `docs/work-items/2026-08-01_changelog-lifecycle-simplification/changelog/implementation.md`: create after authorization, before the implementation commit.

## Implementation approach

First establish one current ownership module and remove changelog work from planning authoring and freeze flow. Then update the parser and validator with fixture-driven compatibility checks. Finally run a deterministic root migration, update only allowed current fragments if required for end-to-end coverage, execute all validation, write the single implementation fragment, and commit the cohesive result.

## Model and Sub-agent Strategy

Upcoming-stage sub-agent assessment:

1. Sub-agents: One final independent reviewer after implementation validation.
2. Fit reason: the policy, parser, validator, and root migration are tightly coupled and stay with one controller, while an isolated final reviewer can challenge compatibility, frozen-boundary, and idempotency assumptions without shared write authority.
3. Authorization state: Approved by operator direction.

Sub-agent `final-reviewer`:

1. Purpose: Review the completed uncommitted change against the frozen spec and plan with a requirements-traceability, legacy-compatibility, and root-migration lens.
2. Context strategy: curated artifacts.
3. Input context: Frozen spec, plan, architecture snapshot, test-case snapshot, changed diff, final validator output, fragment lint/check output, and frozen-path comparison.
4. Output artifact: Evidence-backed review findings with severity, affected path, and reproduction or validation path.
5. Model policy: `economy-default` with explicit operator override.
6. Model generation: `gpt-5.6`.
7. Capability tier: `flagship`.
8. Resolved profile: `gpt-5.6-sol`.
9. Availability/fallback: If Sol High is unavailable, stop and request operator direction; do not silently downgrade the final reviewer.
10. Reasoning effort: `high`.
11. Selection reason: The schema migration and frozen-history boundary have high review sensitivity despite a bounded implementation scope.
12. Parallel execution: No; requires completed implementation diff and validation evidence.
13. Blast radius if wrong: High; a missed compatibility or cleanup defect could corrupt release-source history or invalidate frozen-boundary guarantees.

## Implementation tasks

### `TASK-001` Establish implementation-only policy ownership

Dependencies: Fresh post-freeze authorization.

Interfaces:

1. Consumes: approved spec, architecture snapshot, current lifecycle/release/naming/freeze references, template source blocks, manifests, generated templates, `SKILL.md`, and `README.md`.
2. Produces: `module:implementation-changelog` and planning routes that have no changelog authoring obligation.

Implementation:

1. Create `references/implementation-changelog.md` as the sole current owner of the implementation fragment lifecycle, the compact tagged line, allowed values, legacy compatibility, root cleanup rule, consolidation checkpoint, and release-note curation boundary.
2. Remove `planning-approval.md` from current small/medium and large/phased layouts, templates, freeze instructions, and router outcomes; require an implementation fragment only after fresh implementation authorization.
3. Replace current three-field schema prose with the exact compact tagged grammar specified by `SPEC-002`, and identify `planning-only` as historical compatibility input rather than a current value.
4. Update `maintenance-architecture.md` under `## Lifecycle Decomposition Direction` to name the implementation-changelog module as the justified split and describe its limited ownership boundary.
5. Update the primary `SKILL.md` operation router: add the dedicated reference to execution and changelog-maintenance routes; remove changelog loading from spec/plan drafting and planning-freeze routes; keep the router's route-budget and required-route checks current.
6. Update naming, release, README, and validator owner maps to point to the new module without duplicating its schema.
7. Remove root `TODO.md` from the release-policy package-boundary exclusion list and any matching validation expectation.
8. Update template source blocks and manifests, regenerate generated templates with `assemble_templates.py`, and review the generated diff for source/assembly consistency.

Exit criteria: Current planning guidance does not create, require, or route a changelog fragment; current implementation guidance has one unambiguous changelog owner.

#### `CHECK-001` Validate lifecycle routing

Covers: `VER-001`, `VER-005`.

Method: Run focused repository searches for `planning-approval.md`, `planning-only`, `Release-note:`, root `TODO.md`, and the old planning-stage changelog requirement across active policy, template, and README surfaces; then run the relevant harness policy-validator checks.

Expected result: Only explicitly retained legacy compatibility or historical documents match; active current surfaces route implementation work to the dedicated module and contain no obsolete root `TODO.md` claim.

Evidence record: Validator command output and scoped diff review in the implementation completion report.

### `TASK-002` Implement compatible compact consolidation

Dependencies: `TASK-001`.

Interfaces:

1. Consumes: the compact schema and compatibility boundary from `references/implementation-changelog.md` plus the existing fragment parser CLI.
2. Produces: compatible parsed-entry representation, eligibility selection, deterministic root rewrite or migration operation, and unchanged `--lint` / `--check` contracts.

Implementation:

1. Refactor fragment parsing so one entry may use either the frozen legacy three-field metadata or the compact tagged metadata; normalize both forms into release target, package impact, and eligibility data.
2. Treat only `distributable` and `repository-only` implementation entries as current consolidation candidates. Parse legacy `planning-only` fragments for frozen compatibility but never insert them into root output.
3. Add an explicit, documented root migration/rewrite operation that removes root planning-only sections and rewrites each remaining entry to the compact tagged form while preserving heading order and body content.
4. Keep duplicate-heading detection and newest-first missing-entry insertion behavior. Ensure root presence detection prevents duplicate insertion after a successful first run.
5. Update error messages so malformed compact metadata and invalid current package impact identify the fragment path, entry ordinal, and offending value.

Exit criteria: The script preserves its supported lint/check/consolidate workflows, accepts frozen legacy fragments, and supports compact current entries without reinserting anything on a second run.

#### `CHECK-002` Exercise parser and idempotency fixtures

Covers: `VER-002`, `VER-004`.

Method: Add or update validator fixtures for compact parsing, malformed metadata, legacy compatibility, plan-only exclusion, duplicate headings, first insertion, and second-run no-op. Run the focused validator checks and direct `consolidate_changelog_fragments.py --lint` and `--check` commands.

Expected result: Valid compact and frozen legacy inputs pass where intended; invalid inputs fail precisely; one insertion occurs once only; duplicate headings fail.

Evidence record: Fixture names, commands, and passing output in the implementation completion report.

### `TASK-003` Migrate and verify the root changelog

Dependencies: `TASK-002`.

Interfaces:

1. Consumes: verified migration operation and current `CHANGELOG.md`.
2. Produces: compact root changelog without planning-only sections or legacy metadata.

Implementation:

1. Run the explicit migration operation against `CHANGELOG.md`.
2. Verify that every root planning-only entry is removed, every surviving root entry has exactly one compact tagged meta line, and no `Release target:`, `Package impact:`, or `Release-note:` line remains in root history.
3. Confirm pre-0.8 release-note files and pre-0.8 changelog fragment paths have no diff. Migrate post-0.8 fragments only when the script or fixtures need current-schema coverage.
4. Run the migration a second time and verify `git diff --exit-code -- CHANGELOG.md` is clean after the first migrated state.

Exit criteria: Root history is materially smaller and compact, frozen artifacts are unchanged, and rerunning migration is a no-op.

#### `CHECK-003` Verify cleanup boundaries

Covers: `VER-003`, `VER-004`.

Method: Use deterministic searches/counts for forbidden legacy metadata and planning-only root sections; compare the frozen release-note and pre-0.8 fragment paths to the baseline; run the migration twice; run `git diff --check`.

Expected result: Forbidden root patterns have zero matches, frozen paths have zero changes, the second migration has no diff, and whitespace validation passes.

Evidence record: Command output plus final scoped diff summary.

### `TASK-004` Run full validation and record implementation delivery

Dependencies: `TASK-001`, `TASK-002`, `TASK-003`.

Interfaces:

1. Consumes: completed policy, parser, validator, template, and root migration changes.
2. Produces: passing validation evidence and one compact implementation-stage changelog fragment.

Implementation:

1. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` and the fragment consolidator's repository `--lint` and `--check` modes.
2. Re-run template assembly and verify generated template files are current.
3. Review the whole diff for frozen boundary violations, unrelated files, duplicate policy, stale references, and root migration completeness.
4. Create `changelog/implementation.md` with the exact compact tagged metadata and an implementation subject synchronized with this work item's implementation commit.

Exit criteria: All checks pass, the implementation fragment is compact and synchronized, the freeze boundary is preserved, and an uncommitted review-ready diff exists.

#### `CHECK-004` Complete end-to-end verification

Covers: `VER-001`, `VER-002`, `VER-003`, `VER-004`, `VER-005`.

Method: Run the full policy validator, fragment lint/check, template assembly verification, `git diff --check`, and a final frozen-path diff inspection.

Expected result: Every command succeeds; current policy has one changelog owner, root cleanup is complete, consolidation is idempotent, and frozen artifacts remain unchanged.

Evidence record: Final command output and completion summary.

### `TASK-005` Obtain and integrate the Sol High final review

Dependencies: `TASK-004`.

Interfaces:

1. Consumes: the complete uncommitted diff, frozen planning package, compact implementation fragment, and all validation evidence.
2. Produces: an independent review report, resolved substantiated findings, rerun affected validation, and the final implementation commit.

Implementation:

1. Dispatch the operator-approved final reviewer on Sol High with curated artifacts and the named requirements-traceability, legacy-compatibility, and root-migration lens.
2. Require each finding to provide severity, affected path, rationale, and a reproduction or validation path; treat unsupported preferences as non-blocking suggestions.
3. Resolve every substantiated finding, rerun every affected Plan Check, and update the implementation fragment if the implementation commit subject or delivered behavior changes.
4. Review the final diff once more for frozen-boundary violations and commit only the authorized implementation surfaces using the planned implementation subject.

Exit criteria: The independent Sol High review has no unresolved substantiated finding, affected checks pass, and the cohesive implementation commit exists.

#### `CHECK-005` Review final migration safety

Covers: `VER-001`, `VER-002`, `VER-003`, `VER-004`, `VER-005`.

Method: Provide the reviewer the exact curated inputs listed in the strategy, inspect the evidence-backed report, resolve substantiated findings, and rerun affected checks.

Expected result: The report confirms or challenges requirements traceability, legacy compatibility, frozen-path preservation, compact root syntax, and second-run idempotency with concrete evidence; no substantiated issue remains at commit.

Evidence record: Final-review report, resolution summary, and rerun command output in the implementation completion report.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: changelog-lifecycle-simplification -- approve implementation-only changelog flow` |
| Implementation | `refactor: changelog-lifecycle-simplification -- retain only implementation delivery records` |

One implementation commit is required because the schema, parser, validator, policies, templates, and root data migration form one compatibility boundary.

## Validation and variance

1. The implementing task must run every nested Plan Check before commit.
2. A discovery that pre-0.8 parsing cannot remain compatible, a need to rewrite frozen material, a new release-note automation requirement, or an incompatible CLI change is a material variance and requires an amendment and operator approval.
3. A narrow post-0.8 fragment migration needed to achieve current-schema coverage is expected and must be included in the scoped diff review.

## Implementation handoff

### Approved next stage

#### Next lifecycle stage

Stage: `plan execution`.

#### Orchestration

Method: `superpowers:executing-plans`; Run in: `same Codex task`; Plan Task reviewers: `execution-controller self-review and full validation, followed by one independent Sol High final reviewer with curated artifacts`.

#### Model

Model: `economy-default balanced tier`; Reasoning: `medium`.

#### Fallbacks and limits

`Load the frozen package before editing. Use only the operator-approved Sol High final reviewer with curated artifacts. Stop for an amendment if frozen legacy artifacts must change or a material CLI/release-process boundary appears.`

1. Frozen package: `spec_changelog-lifecycle-simplification.md`, this plan, `snapshots/architecture.snapshot.md`, and `snapshots/test-cases.snapshot.md`.
2. Artifact rehydration: Read all frozen package files, current `implementation-changelog.md`, and the affected script before editing.
3. Variance stop condition: Any scope change described in Validation and variance requires approval before implementation continues.

## Readiness

- [x] Current planning facts are separate from the Approved next stage.
- [x] Inputs, scope, tasks, checks, documentation, and implementation changelog requirement are clear.
- [x] The execution selection, handoff, and upcoming-stage sub-agent assessment are explicit.
- [x] No required decision or ownerless deferral remains.

## Completion

Required work and evidence are pending fresh implementation authorization.

## Approval

- Status: Approved
- Superseded by: None
