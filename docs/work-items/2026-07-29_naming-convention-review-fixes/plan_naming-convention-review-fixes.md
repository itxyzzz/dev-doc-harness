# Naming Convention Review Fixes Plan

Work ID: `2026-07-29_naming-convention-review-fixes`
Short ID: `naming-convention-review-fixes`
Status: Approved
Harness release: `0.8+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`
Execution method: `superpowers:executing-plans`
Current planning Codex task: Model/profile, reasoning, and context visibility: `not exposed`.

## Input Artifacts

1. Draft spec: `spec_naming-convention-review-fixes.md`.
2. Architecture input: None; the spec records architecture snapshot status as not applicable.
3. Required snapshots or deltas: None.
4. Relevant repository files: `.agents/skills/dev-doc-harness/references/naming-conventions.md`, `.agents/skills/dev-doc-harness/references/artifact-contract.md`, `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, and `CHANGELOG.md`.
5. Unresolved implementation context to confirm before editing: None identified.

## Traceability approach

Local links connect `SPEC-001` to `TASK-001` and `CHECK-001`, and `SPEC-002` to `TASK-002` and `CHECK-002`; this is sufficient for deterministic validation of the narrow policy change.

## Change surfaces

1. `.agents/skills/dev-doc-harness/references/naming-conventions.md`: canonical grammar and duplicate-removal edits.
2. `.agents/skills/dev-doc-harness/references/artifact-contract.md`: replace the direct consumer's obsolete full-commit-message heading alternative with a reference to `<changelog-heading>`.
3. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: update the focused naming assertion from `NNN` to `NN` and add or adjust focused text assertions only as needed to protect the revised canonical rules.
4. `changelog/planning-approval.md`: required planning-freeze source entry.
5. `CHANGELOG.md`: one planning-freeze entry, then one implementation entry only when the implementation commit is authorized.

## Implementation approach

Update the single canonical reference first, then its direct consumer and validation guard. Do not rename or edit historical work-item artifacts; validate active policy surfaces with focused searches and the full harness test.

## Model and Sub-agent Strategy

Upcoming-stage sub-agent assessment:

1. Sub-agents: None.
2. Fit reason: the work is a small, sequential documentation-policy edit with one direct validator; delegation would add coordination cost without improving isolation or coverage.
3. Authorization state: Not needed.

## Implementation tasks

### `TASK-001` Reconcile canonical naming policy

Dependencies: Approved combined planning package and fresh operator authorization.

Interfaces:

1. Consumes: `SPEC-001`, review comments, and the existing uncommitted `<changelog-heading>` table-row edit.
2. Produces: a single internally consistent naming grammar in the active reference and direct lifecycle consumer.

Implementation:

1. In `naming-conventions.md`, replace spaced artifact-type labels with `phase-NN-plan` and `amendment-NN`; change the amendment filename placeholder and example from three to two digits.
2. Express `<work-id>` as `<date>_[<issue-key>_]<short-title>` and remove the repeated local work-ID grammar block from Work item paths.
3. Replace the repeated planning-artifact-type list in Commit messages with a reference to `<artifact-type>`. Remove the repeated local work-ID, changelog-fragment-path, and commit-subject grammar blocks that merely restate Fields or Derived patterns. Retain the filename-kind list because it provides a local index without restating expansions, and retain concrete filename examples because they demonstrate the patterns.
4. Set `<changelog-heading>` to `## <date> <commit-subject>` and have the Changelog entries section point to that derived pattern rather than repeat another grammar. Reconcile the existing uncommitted table-row edit with that form.
5. Update `artifact-contract.md` to refer to `<changelog-heading>` rather than a full commit message or work-ID alternative.

Exit criteria: `SPEC-001` is satisfied with no conflicting active grammar or review-identified duplication.

### `TASK-002` Align validation and inspect scope

Dependencies: `TASK-001`.

Interfaces:

1. Consumes: revised active naming policy.
2. Produces: validator coverage and evidence that historical artifacts were not rewritten.

Implementation:

1. Change the current harness-policy assertion from `plan_amendment-NNN` to `plan_amendment-NN`; add focused assertions for `<date> <commit-subject>` only if the existing validator structure supports them without broad text linting.
2. Run focused searches across current reusable harness surfaces for `amendment-NNN`, `phase N plan`, `amendment NNN`, and full-commit-message or work-ID-alternative changelog heading guidance; treat historical work-item records and changelog history as intentionally out of scope.
3. Review the implementation diff to ensure only the planned current-policy, validator, changelog, and work-item-package files changed.

Exit criteria: `SPEC-002` is satisfied and no historical artifact changed solely because it records a prior naming convention.

## Plan checks

### `CHECK-001` Canonical naming inspection

Covers: `VER-001`.

Method: Run targeted `rg` searches over `.agents/skills/dev-doc-harness` for the new grammar and excluded obsolete active forms, then manually inspect the naming reference and its direct lifecycle consumer.

Expected result: active policy contains the approved two-digit, kebab-case, optional-issue-key, and single `<date> <commit-subject>` heading grammar without duplicated local grammar blocks.

### `CHECK-002` Harness policy validation

Covers: `VER-002`.

Method: Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Expected result: exit code 0 and all focused naming-policy checks pass.

### `CHECK-003` Diff integrity

Covers: `VER-002`.

Method: Run `git diff --check`, `git status --short`, and inspect the name-only diff against the Change surfaces list.

Expected result: no whitespace errors and no unplanned rewrite of historical work-item artifacts.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: naming-convention-review-fixes -- approve naming cleanup` |
| Implementation | `docs: naming-convention-review-fixes -- reconcile review feedback` |

## Validation and variance

1. `CHECK-001` through `CHECK-003` are all required.
2. Equivalent wording may vary when it preserves the approved canonical grammar and removes the identified duplicate guidance.
3. Stop for an amendment and operator approval before changing historical artifact names, semantic field separators, the scope beyond active reusable surfaces, or the planned commit boundary.

## Approved next stage

### Activity

1. Next activity: implement `TASK-001` followed by `TASK-002`.
2. First Plan Task: `TASK-001`.

### Orchestration

1. Method: `superpowers:executing-plans`.
2. Run in: `new Codex task`, because the current planning profile and context suitability are not exposed and a fresh task can load the small frozen package directly.
3. Plan Task reviewers: disclose an independent reviewer when available; otherwise record the execution controller's self-review limitation before implementation.

### Model

1. Model: balanced tier.
2. Reasoning: medium.

### Fallbacks and limits

1. Default fallback: native Codex in a new task only if Superpowers is unavailable; the execution task must follow the applicable independent-review policy before proceeding.
2. Artifact loading: load applicable `AGENTS.md`, the repository-local harness, this frozen package, the user review comments, the existing worktree diff, and the variance stop condition before edits.
3. Variance stop condition: request approval for any material scope or naming-boundary change named in Validation and variance.

## Readiness

- [x] Inputs, scope, tasks, checks, documentation, and planned commits are clear.
- [x] The existing uncommitted naming-reference edit is explicitly accounted for and will not be discarded.
- [x] Historical artifact preservation is an implementation boundary.
- [x] The upcoming-stage sub-agent assessment records `Sub-agents: None` with a fit reason.
- [x] No required decision, placeholder, or ownerless deferral remains.

## Approval

- Status: Approved
- Superseded by: None
