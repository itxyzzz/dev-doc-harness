# Multi-entry Changelog Fragments Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

Work ID: `2026-07-13_multi-changelog-fragments`
Short ID: `multi-changelog-fragments`
Status: Approved
Harness release: `0.6+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Input Artifacts

1. Approved spec: `spec_multi-changelog-fragments.md`.
2. Architecture input: `snapshots/architecture.snapshot.md` (`DEC-001`).
3. Required snapshots or deltas: `snapshots/test-cases.snapshot.md`, `deltas/testing-guide.delta.md`, and `deltas/operator-manual.delta.md`.
4. Relevant repository files: `.agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py`, `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, `.githooks/pre-commit`, `README.md`, `.agents/skills/dev-doc-harness/docs/operator-note.md`, `.agents/skills/dev-doc-harness/references/artifact-contract.md`, `.agents/skills/dev-doc-harness/references/naming-conventions.md`, and `docs/release-branch-process.md`.
5. Unresolved implementation context to confirm before editing: None identified; preserve the unrelated modified `2026-07-12_new-task-handoff-visibility` fragment.

## Commitment-Disposition Mapping

| Specification Commitment | Disposition | Implementation Tasks |
|---|---|---|
| `SPEC-001` Parse ordered entry collections | implement | `TASK-001`, `TASK-002` |
| `SPEC-002` Separate ordinary lint from release completeness | implement | `TASK-001`, `TASK-002`, `TASK-003` |
| `SPEC-003` Preserve semantic README release assertions through reflow | implement | `TASK-001`, `TASK-003` |

## Verification-Execution Mapping

| Verification Criterion | Plan Checks | Expected evidence stage |
|---|---|---|
| `VER-001` Multi-entry source files remain independently valid | `CHECK-001`, `CHECK-003` | implementation, pre-commit |
| `VER-002` Lint and completeness gates have distinct outcomes | `CHECK-001`, `CHECK-002`, `CHECK-003` | implementation, review, pre-commit |
| `VER-003` README reflow tolerance is narrowly scoped | `CHECK-001`, `CHECK-003`, `CHECK-004` | implementation, pre-commit, review |

Architecture coverage:

1. Architecture input: `DEC-001` in `snapshots/architecture.snapshot.md`.
2. Plan usage: parser tasks enforce entry-scoped metadata and mode separation; documentation tasks keep ordinary lint distinct from release completeness.
3. Drift path: update draft artifacts before freeze; after freeze, use variance and amendment handling for parser grammar, CLI semantics, or release-order changes.
4. Reinterpretation guard: implement the frozen entry-list and mode-boundary decision without introducing a manifest format, root schema change, or global regex relaxation.

## Implementation Approach

Make the validator demonstrate entry-list parsing and lint/check separation before changing code. Change `parse_fragment` to return entry collections, flatten them in discovery, and add `--lint` as grammar/duplicate validation that never opens root `CHANGELOG.md`. Preserve default write mode and `--check` after validation.

Then put lint in the root-local hook and document the two checkpoints: `--lint` before ordinary commits; `--lint` plus `--check` before release-group editing. Replace only the three README semantic regex calls with a dedicated whitespace-and-case normalized prose helper; leave the general regex helper unchanged.

## Change Surfaces

Expected edits:

1. `.agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py`: entry-slice parser, flattened discovery, `--lint`, and duplicate occurrence diagnostics.
2. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: multi-entry/mode fixtures, policy/hook assertions, and narrow README normalization helper.
3. `.githooks/pre-commit`: add source-fragment `--lint` to the existing policy validator.
4. `artifact-contract.md`, `naming-conventions.md`, `README.md`, package operator note, and `docs/release-branch-process.md`: explain entry-level metadata and ordinary/release gate ownership.
5. This work item's testing/operator deltas and implementation source fragment.

Stable interfaces:

1. Default invocation remains write consolidation; `--check` remains non-mutating validation plus root missing-entry detection.
2. Heading grammar, metadata names/value sets, root insertion location, and downstream non-`unreleased` targets remain compatible.

Changed interfaces:

1. CLI adds a grammar/duplicate-only `--lint` mode.
2. Internal `parse_fragment` returns a list of `FragmentEntry` values plus errors; same-file duplicate diagnostics identify both occurrences.

Implementation boundaries:

1. Frozen historical packages, templates, root changelog content, and the existing user-modified historical fragment stay out of scope.

## Model and Sub-agent Strategy

1. Model generation: `not exposed`.
2. Capability tier: `balanced`.
3. Reasoning effort: `medium`.
4. Orchestration mode: `single-agent`.
5. Resolved profile: `not exposed`.
6. Availability/fallback: current compatible balanced profile; fallback `fast/economy` at medium reasoning if balanced is unavailable.
7. Execution continuity: `same task` after fresh post-freeze authorization.
8. Context visibility: `not exposed`.
9. Artifact rehydration required: `Yes`; re-read frozen artifacts and `AGENTS.md` before edits.
10. Model-policy source: repository `AGENTS.md` active `economy-default` policy.
11. Override scope and expiry: `None`.

Fit assessment:

1. Complexity: medium because parser cardinality, mode boundaries, docs, and fixtures must agree.
2. Risk and blast radius: medium; an error can block release preparation or permit malformed source, but no external data or service is affected.
3. Ambiguity: low after the approved design decision.
4. Budget and latency fit: one coherent implementation and validation pass is cheaper and safer than delegating coupled files.

Recommended selection change:

1. None.

Sub-agents:

1. None; the small coupled code surface gains no isolation benefit from delegation.

## Implementation Tasks

### `TASK-001` Implementation Task — Add failing entry-list and mode-separation fixtures

Dependencies:

1. Frozen spec, architecture snapshot, and test-case snapshot.

Implementation:

1. In `assert_changelog_fragment_contract`, replace the single-entry happy-path fixture with two valid entries in one `implementation.md` file.
2. Assert `--lint` returns `0` before consolidation; `--check` reports both missing headings without root mutation; write mode inserts each once; repeat write is idempotent; post-write `--check` passes.
3. Add fixtures for malformed metadata in only the second entry, duplicate headings inside one file, and valid lint with no root changelog.
4. Add policy assertions for `--lint` in the hook, ordinary guidance, and release process alongside existing `--check` ordering.
5. Add normalized-prose expectations for the three README semantic facts while preserving structural regex-helper use.

Exit criteria:

1. New assertions fail before parser and CLI changes for the intended missing behavior.
2. Existing unrelated validator scenarios are untouched.

### `TASK-002` Implementation Task — Implement entry-scoped parsing and lint mode

Dependencies:

1. `TASK-001` failing fixtures.

Implementation:

1. Locate every recognized heading, slice from each heading to the next heading or end of normalized text, and validate metadata only in that entry slice.
2. Preserve the `FragmentEntry` body format per slice; return entry lists plus accumulated errors from `parse_fragment`; make discovery flatten those lists.
3. Retain heading-based duplicate detection and report repository-relative occurrence context for duplicate entries, including same-file cases.
4. Add mutually exclusive `--lint`; it performs discovery and duplicate validation only. Default and `--check` lint first and then keep their existing root-changelog write/completeness behavior.

Exit criteria:

1. Every `TASK-001` fixture passes, including downstream target compatibility and idempotent write behavior.
2. Existing one-entry fragments retain behavior.

### `TASK-003` Implementation Task — Wire gates and document ownership

Dependencies:

1. `TASK-002` passing parser and modes.

Implementation:

1. Update `.githooks/pre-commit` under `set -eu` to run `consolidate_changelog_fragments.py --lint` and `test_harness_policy.py`, never `--check`.
2. Update lifecycle and naming references to state that stable fragments may contain multiple newest-first entries and required metadata belongs to each entry.
3. Update README and package operator note: ordinary commits use lint; root consolidation remains checkpoint-owned; release preparation uses lint plus check.
4. Update release-process step 4 to run lint and check before renaming `## Unreleased`, retain explicit write consolidation, and stop on either grammar or completeness failure.
5. Add `normalize_prose(text)` and `assert_normalized_text_contains(...)` in `test_harness_policy.py`; use them only for the README's package-boundary, work-item-exclusion, and rollback phrases. Do not change `assert_text_contains`.
6. Align this work item's testing and operator deltas with the implementation wording.

Exit criteria:

1. Hook, canonical policy, concise guidance, and release runbook distinguish lint from completeness consistently.
2. README reflow tolerance stays limited to complete semantic phrases.

### `TASK-004` Implementation Task — Verify behavior and commit the scoped change

Dependencies:

1. `TASK-001`, `TASK-002`, and `TASK-003`.

Implementation:

1. Run `CHECK-001` through `CHECK-004`, record distinct execution instances and outcomes in the implementation completion report, and review the listed diff surfaces.
2. Update `changelog/implementation.md` with the planned implementation heading before committing; do not consolidate root `CHANGELOG.md` during this ordinary feature work.
3. Stage only implementation targets and the implementation fragment; verify the unrelated modified `2026-07-12_new-task-handoff-visibility` fragment is excluded.
4. Commit using the planned implementation subject, or record approved variance if it changes.

Exit criteria:

1. Plan checks support passing `VER-001` through `VER-003`.
2. No unrelated user work or root-changelog consolidation is included.

## Plan Checks

### `CHECK-001` Plan Check — Run harness policy and changelog fixture suite

Covers:

1. `VER-001`.
2. `VER-002`.
3. `VER-003`.

Procedure:

1. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Expected result:

1. Exit code `0`; `changelog.fragments` passes multi-entry, error-isolation, duplicate, lint/check, policy/hook, and README-normalization assertions.

Evidence record:

1. Completion report execution instance `CHECK-001-final` with output summary.

Stage or environment:

1. Implementation and pre-commit, repository-root Windows PowerShell.

Task/check coordination:

1. `TASK-001` creates the assertions; `TASK-002` and `TASK-003` make them pass.

### `CHECK-002` Plan Check — Exercise grammar-only lint

Covers:

1. `VER-001`.
2. `VER-002`.

Procedure:

1. Run `python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --lint`.

Expected result:

1. Exit code `0` with no root-changelog mutation or missing-entry report.

Evidence record:

1. Completion report execution instance `CHECK-002-final` and `git diff -- CHANGELOG.md` confirmation.

Stage or environment:

1. Pre-commit, repository-root Windows PowerShell.

Task/check coordination:

1. `TASK-002` supplies the mode; `TASK-003` places it in the hook.

### `CHECK-003` Plan Check — Validate configured pre-commit commands

Covers:

1. `VER-001`.
2. `VER-002`.
3. `VER-003`.

Procedure:

1. Run the lint command and `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
2. Inspect `.githooks/pre-commit` for those commands under `set -eu` and no root-completeness `--check` call.

Expected result:

1. Both commands exit `0`; the hook matches the ordinary-commit ownership boundary.

Evidence record:

1. Completion report execution instance `CHECK-003-final` with hook diff.

Stage or environment:

1. Pre-commit review, repository-root Windows PowerShell.

Task/check coordination:

1. `TASK-003` completes hook integration.

### `CHECK-004` Plan Check — Review release and prose-assertion boundaries

Covers:

1. `VER-002`.
2. `VER-003`.

Procedure:

1. Inspect the diff for the release runbook, README, operator note, lifecycle/naming references, and README assertion helper call sites.
2. Run `git diff --check`.

Expected result:

1. Release prep names lint plus check before renaming `## Unreleased`; ordinary guidance names lint only; normalized prose is limited to the three README phrases; `git diff --check` exits `0`.

Evidence record:

1. Completion report execution instance `CHECK-004-final` with review notes.

Stage or environment:

1. Review and pre-commit, repository-root Windows PowerShell.

Task/check coordination:

1. `TASK-003` produces reviewed surfaces; `TASK-004` records the result.

## Planned commits

Planning approval commit:

1. Planned subject: `plan: multi-changelog-fragments -- approve entry-level lint and release gates`.
2. Changelog title or snippet: `2026-07-13_multi-changelog-fragments -- approve entry-level lint and release gates`.
3. Notes: approval commit for the spec, plan, architecture snapshot, test-case snapshot, two deltas, and planning-approval fragment.

Implementation commit:

1. Planned subject: `feat: multi-changelog-fragments -- validate multiple fragment entries`.
2. Changelog title or snippet: `2026-07-13_multi-changelog-fragments -- validate multiple fragment entries`.
3. Notes: parser, fixtures, hook, guidance, and implementation fragment; root consolidation remains release-owned.

## Check execution and completion records

For every Plan Check execution, record the `CHECK` ID, a unique execution instance, stage or environment, actual result, evidence location or inline evidence, and `pass`, `fail`, or `blocker` status. Repeated executions of an unchanged procedure produce distinct records.

## Plan variance handling

Before freeze, edit this draft directly for feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use an amendment for parser grammar, CLI semantics, root ownership, release ordering, Specification Commitment, Verification Criterion, Plan Check, or feasibility changes.

## Planning artifact freeze gate

Draft review status: approved by the operator on 2026-07-13.

Approval commit status: pending the planned approval commit.

Post-freeze implementation authorization: not granted; implementation waits for a fresh operator instruction after the approval commit.

## Next-task handoff

1. Planning shape: `combined small/medium plan`.
2. Frozen package: this spec, this plan, the architecture and test-case snapshots, and the two deltas.
3. Next activity: implement `TASK-001` through `TASK-004`.
4. Execution continuity: `same task` after fresh post-freeze authorization.
5. Context visibility: `not exposed`.
6. Artifact rehydration required: `Yes`; re-read frozen artifacts and `AGENTS.md` before `TASK-001`.
7. Exact authoritative artifacts: the frozen package plus `changelog/planning-approval.md` and any approved amendment.
8. Approved strategy and fallback: single-agent balanced/medium under `economy-default`; fallback fast/economy/medium if balanced is unavailable.
9. First activity: `TASK-001` — add failing entry-list and mode-separation fixtures.
10. Variance stop condition: stop for approval-required variance if parser grammar, release order, source/root ownership, or any mapped commitment, criterion, or check changes.

## Plan readiness checklist

- [x] Input artifacts and repository context are listed.
- [x] Every commitment has a disposition and every criterion has Plan Check coverage.
- [x] Risks, scope, interfaces, and documentation are covered or marked no-op with reasons.
- [x] Tasks are executable by a fresh implementation agent without invented order or scope.
- [x] Plan Checks have procedure, result, evidence record, and stage.
- [x] Commit subjects and changelog snippets are synchronized.
- [x] Variance handling is clear.
- [x] The work fits one orchestration thread; sub-agents are intentionally not used.
- [x] No unresolved placeholders, decisions, sections, or ownerless deferrals remain.

## Completion criteria

1. `VER-001` through `VER-003` have evidence-backed passing status.
2. `CHECK-001` through `CHECK-004` have recorded results.
3. Required live documentation and this work item's deltas are updated.
4. The implementation fragment exists before the implementation commit.
5. The implementation commit excludes unrelated user work and root `CHANGELOG.md` unless later explicitly owned consolidation requires it.

## Approval

- Status: Approved
- Superseded by: None
