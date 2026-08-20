# Changelog Fragment Clarity Plan

Work ID: `2026-08-01_changelog-fragment-clarity`
Short ID: `changelog-fragment-clarity`
Status: Approved
Harness release: `0.8+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:implementation-changelog`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`
Execution method: `superpowers:executing-plans`
Current planning Codex task: Model/profile, reasoning, and context visibility: `not exposed`.

## Input Artifacts

1. Approved spec: `spec_changelog-fragment-clarity.md`.
2. Architecture input: architecture decisions in the approved spec; no dedicated snapshot is required.
3. Required snapshots or deltas: `snapshots/test-cases.snapshot.md`.
4. Relevant repository files: `references/naming-conventions.md`, `references/implementation-changelog.md`, `references/artifact-contract.md`, template source blocks and assemblies, `scripts/consolidate_changelog_fragments.py`, `scripts/test_harness_policy.py`, and `CHANGELOG.md`.
5. Unresolved implementation context to confirm before editing: None identified.

## Traceability approach

`SPEC-*` to `VER-*` links and one nested `CHECK-*` per task provide direct implementation coverage without a separate mapping.

## Global Constraints

Current `-fragment` names are documentation defaults only. Preserve generic Markdown discovery, frozen historical fragment paths, legacy parser compatibility, root entry body text, and release headings.

## Change surfaces

1. `references/naming-conventions.md`, `references/artifact-contract.md`, and `references/implementation-changelog.md`: make current names explicit and split routine versus compatibility guidance.
2. `assets/templates/blocks/`, assemblies, and generated templates: use the new ordinary and phase-specific fragment filenames.
3. `scripts/consolidate_changelog_fragments.py`: serialize one blank line between consecutive root entries while retaining idempotency and heading/body preservation.
4. `scripts/test_harness_policy.py`: cover the new current filename fixture, legacy filename compatibility, compatibility-section routing, root spacing, and no-op reruns.
5. `CHANGELOG.md`: normalize root-entry separators only after the formatter is verified.
6. `docs/work-items/2026-08-01_changelog-fragment-clarity/changelog/implementation-fragment.md`: create after authorization, before the implementation commit.

## Implementation approach

First change the current contract and source templates without narrowing discovery. Then add a failing fixture for adjacent root entries and implement the smallest serializer normalization that passes it. Regenerate templates, normalize the root once, prove a second run is a no-op, and commit the cohesive compatible result.

## Model and Sub-agent Strategy

Upcoming-stage sub-agent assessment:

1. Sub-agents: None.
2. Fit reason: current policy, serializer, fixture, template, and root-diff review are tightly coupled but bounded; one controller can make and validate the compatible change more safely than partitioned editing.
3. Authorization state: Not needed.

## Implementation tasks

### `TASK-001` Establish the explicit current fragment convention

Dependencies: Fresh post-freeze authorization.

Interfaces:

1. Consumes: approved spec, naming/lifecycle/changelog policy, and template source blocks.
2. Produces: current `implementation-fragment.md` and `phase-NN-fragment.md` documentation convention with unchanged generic discovery.

Implementation:

1. Replace only current ordinary and phase filename examples in naming, lifecycle layouts, documentation matrices, implementation guidance, template source blocks, assemblies, and generated templates.
2. Keep historical compatibility wording filename-agnostic; do not rename existing work-item fragments or add parser filename enforcement.
3. Refactor `implementation-changelog.md` so its routine lifecycle and standard consolidation instructions remain first; move frozen legacy parsing and `--migrate-root` prose into a final `## Compatibility and legacy support` section.
4. Regenerate templates with `assemble_templates.py` and inspect the generated diff for source/assembly consistency.

Exit criteria: Current authors encounter explicit `-fragment` defaults and compact routine workflow before exceptional compatibility guidance; historical paths remain supported.

#### `CHECK-001` Validate current contract routing

Covers: `VER-001`, `VER-002`.

Method: Search active policy/template surfaces for retired current examples, inspect the final guidance-section order, run template assembly verification, and run focused harness-policy checks.

Expected result: Current surfaces use `implementation-fragment.md` or `phase-NN-fragment.md`; legacy filename references occur only as fixtures or historical compatibility; assembled templates are current.

Evidence record: Search results, assembly output, and validator output in the completion report.

### `TASK-002` Normalize root entry separation without altering content

Dependencies: `TASK-001`.

Interfaces:

1. Consumes: existing root-entry parser/serializer and the frozen-compatibility behavior.
2. Produces: root output with exactly one blank line before each subsequent entry heading and unchanged body/release-heading boundaries.

Implementation:

1. Add a focused failing fixture containing adjacent root entries, a release heading, and preserved body content; assert the first migration normalizes separators and the second run is byte-identical.
2. Modify only the root serialization/normalization path required to make the fixture pass; do not change generic fragment discovery or legacy parse acceptance.
3. Extend fixtures to use `implementation-fragment.md` for current compact input while retaining an old filename for legacy compatibility input.
4. Run the root migration against `CHANGELOG.md`, inspect its diff for separator-only historical changes, and rerun migration and default consolidation to prove no change.

Exit criteria: Root entries have readable separators, release headings and entry bodies survive, and repeat operations are idempotent.

#### `CHECK-002` Exercise compatibility and idempotency

Covers: `VER-001`, `VER-003`.

Method: Run focused fixture coverage through `test_harness_policy.py`, then direct `--lint`, `--check`, `--migrate-root`, a second `--migrate-root`, default consolidation, and `git diff --exit-code` after the stable output.

Expected result: Compact current names and frozen legacy paths both pass where valid; output has one blank separator line between entries; release headings/bodies are preserved; all repeat runs are no-ops.

Evidence record: Fixture names and command outputs in the completion report.

### `TASK-999` Verify delivery and record the implementation change

Dependencies: `TASK-001`, `TASK-002`.

Interfaces:

1. Consumes: completed policy, template, serializer, fixture, and root changes.
2. Produces: validation evidence and the implementation fragment using the new convention.

Implementation:

1. Run the full harness policy suite, fragment lint/check, template assembly check, and `git diff --check`.
2. Review changed paths for frozen-fragment rewrites, stale filename examples, legacy-guidance ordering, unexpected root content changes, and generated-template drift.
3. Create `changelog/implementation-fragment.md` with compact metadata and the synchronized implementation subject before committing.
4. Consolidate the eligible entry at the implementation checkpoint and commit only the authorized cohesive implementation surfaces.

Exit criteria: All checks pass, the root and fragment are idempotent, frozen historical paths are unchanged, and the implementation commit exists.

#### `CHECK-999` Complete end-to-end verification

Covers: `VER-001`, `VER-002`, `VER-003`.

Method: Run the full policy validator, template assembly check, fragment lint/check, migration/default-consolidation no-op checks, `git diff --check`, and final frozen-path diff inspection.

Expected result: Every command succeeds; routine naming and guidance are clear, root formatting is deterministic, and historical inputs remain preserved.

Evidence record: Final command outputs and scoped diff summary.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: changelog-fragment-clarity -- approve explicit fragment naming` |
| Implementation | `refactor: changelog-fragment-clarity -- clarify current fragment lifecycle` |

One cohesive implementation commit is required because the contract, serializer, generated templates, tests, root formatting, and implementation record must stay compatible.

## Validation and variance

1. Run every nested Plan Check before the implementation commit.
2. A need to rename frozen fragments, reject generic discovery, alter legacy parse semantics, remove release history, or change root content beyond separator formatting is material variance and requires an amendment and operator approval.
3. A narrow test-fixture rename from a current filename example to the explicit `-fragment` convention is expected.

## Implementation handoff

### Approved next stage

#### Next lifecycle stage

Stage: `plan execution`.

#### Orchestration

Method: `superpowers:executing-plans`; Run in: `same Codex task`; Plan Task reviewers: `execution-controller self-review and full validation; no independent reviewer is proposed because this bounded documentation and formatter change has deterministic fixture coverage`.

#### Model

Model: `economy-default balanced tier`; Reasoning: `medium`.

#### Fallbacks and limits

`Load the frozen package before editing. Stop for an amendment if frozen fragments must change, generic discovery must narrow, or root content must change beyond the approved spacing normalization.`

1. Frozen package: `spec_changelog-fragment-clarity.md`, this plan, and `snapshots/test-cases.snapshot.md`.
2. Artifact rehydration: Read all frozen package files, current naming/changelog references, and the consolidator before editing.
3. Variance stop condition: Any scope change described in Validation and variance requires approval before implementation continues.

## Readiness

- [x] Current planning facts are separate from the next-stage recommendation.
- [x] Inputs, scope, tasks, checks, documentation, and implementation changelog requirement are clear.
- [x] The execution selection, handoff, and upcoming-stage sub-agent assessment are explicit.
- [x] No required decision or ownerless deferral remains.

## Completion

Required work and evidence are pending fresh implementation authorization.

## Approval

- Status: Approved
- Superseded by: None
