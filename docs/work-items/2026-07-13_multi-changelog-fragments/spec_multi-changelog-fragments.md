# Multi-entry Changelog Fragments Spec

Work ID: `2026-07-13_multi-changelog-fragments`
Short ID: `multi-changelog-fragments`
Status: Approved
Harness release: `0.6+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

## Goal

Allow a stable work-item changelog fragment to hold multiple independently valid entries, validate fragment grammar before ordinary commits, and preserve root changelog completeness as an explicit release-preparation gate.

## Source and Intent

Source input:

1. Release 0.6 preparation exposed a source fragment containing two valid entries, which the consolidation parser rejected solely because it accepted one entry per file.
2. The same release preparation found that root-changelog completeness is checked too late for ordinary fragment grammar feedback.
3. A manually reflowed README broke narrow assertion patterns despite retaining the protected package-boundary meaning.

Desired operator/user outcome:

1. Maintainers can append a new self-contained entry to an existing fragment without creating artificial files.
2. Ordinary commits receive grammar feedback without being blocked by intentionally unconsolidated root-changelog entries.
3. Release preparation still stops on malformed fragments, duplicate headings, or missing unreleased root entries.

Success summary:

1. The consolidation tool treats a fragment as an ordered collection of entries and exposes a non-mutating `--lint` mode.
2. Existing one-entry fragments, root consolidation, duplicate protection, metadata validation, and release-note curation boundaries remain compatible.

## Scope Boundary

### In scope

1. Change the changelog-fragment parser and its command-line modes so one fragment may contain multiple self-contained entries.
2. Add and enforce `--lint` for ordinary repository commits while retaining `--check` for root-changelog completeness at release preparation.
3. Update the canonical fragment contract, naming guidance, release runbook, and concise operator guidance to distinguish fragment grammar from consolidation completeness.
4. Extend fixture coverage for multi-entry files, per-entry failures, duplicate headings, lint/check separation, and resilient README semantic assertions.

### Non-scope

1. Rewriting frozen historical work-item artifacts or migrating all existing fragments into a new layout.
2. Replacing Markdown source fragments with a structured manifest or changing the root `CHANGELOG.md` schema.
3. Running root consolidation on ordinary commits or requiring `--check` to pass before every commit.
4. Loosening general structural regular-expression assertions outside the reflow-tolerant README semantic checks.

### Assumptions

1. Each entry remains headed by the current date/work-item changelog grammar and owns exactly one `Release target`, `Package impact`, and `Release-note` field.
2. Fragment files remain stable descriptive containers; entries remain newest-first by the existing changelog convention.
3. `--check` continues to validate fragment grammar before assessing root-changelog completeness.

### Open questions

1. None identified after repository-context review.

## Repository Context

### Current state

1. `consolidate_changelog_fragments.py` returns at most one `FragmentEntry` from each path and rejects a file unless it has exactly one recognized entry heading and one set of metadata fields across the whole file.
2. `--check` combines source validation with root `CHANGELOG.md` completeness; the root-local pre-commit hook currently runs only `test_harness_policy.py`.
3. `docs/release-branch-process.md` already runs `--check` before renaming `## Unreleased`, but it does not name a grammar-only ordinary-commit checkpoint.
4. The validator's README package-boundary assertions use line-shape-sensitive regular expressions even though their purpose is semantic prose preservation.

### Evidence read

1. `.agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py`.
2. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
3. `.githooks/pre-commit`.
4. `.agents/skills/dev-doc-harness/references/artifact-contract.md`.
5. `.agents/skills/dev-doc-harness/references/naming-conventions.md`.
6. `docs/release-branch-process.md`, `README.md`, and `.agents/skills/dev-doc-harness/docs/operator-note.md`.
7. `docs/work-items/2026-07-09_changelog-fragment-consolidation/` planning artifacts.

### Constraints and compatibility

1. The active repository policy is `economy-default`.
2. The release branch process must keep `--check` before renaming `## Unreleased` and release-note curation.
3. The root changelog remains a consolidated publication view and ordinary work-item commits must not create routine root-changelog conflicts.
4. Existing valid one-entry fragments and non-`unreleased` downstream release targets must remain accepted.
5. The existing user modification at `docs/work-items/2026-07-12_new-task-handoff-visibility/changelog/implementation.md` is unrelated and must not be edited or staged by this work item.

## Specification Commitments and Local Verification Criteria

### `SPEC-001` Specification Commitment — Parse ordered entry collections

Kind: `Behavior`

Intent: `Change`

Concerns: `changelog grammar`, `compatibility`

Statement:

1. The consolidation tool shall parse every recognized entry in a fragment independently, require exactly one valid metadata set for each entry, preserve each entry body for consolidation, and continue rejecting duplicate headings across all discovered entries.

Rationale:

1. A fragment is a stable commit-oriented container, not a one-entry record; validation safety belongs to entries rather than filenames.

#### `VER-001` Verification Criterion — Multi-entry source files remain independently valid

Covers:

1. `SPEC-001`.

Criterion:

1. Fixture evidence shows two valid entries in one fragment pass grammar validation and are each consolidated once, while malformed metadata or a duplicate heading in any entry fails with the affected path and entry context.

Expected evidence:

1. Passing multi-entry, malformed-entry, and duplicate-within-file fixture assertions in `test_harness_policy.py`.

### `SPEC-002` Specification Commitment — Separate ordinary lint from release completeness

Kind: `Behavior`

Intent: `Establish`

Concerns: `commit workflow`, `release preparation`

Statement:

1. The consolidation tool shall provide a non-mutating `--lint` mode that validates source fragment grammar and duplicate headings without reading or requiring root-changelog completeness; `--check` shall retain grammar validation plus missing-unreleased-entry detection, and the root-local pre-commit hook shall run `--lint`.
2. The release runbook shall explicitly treat successful lint and successful `--check` as release-preparation prerequisites before release-group editing.

Rationale:

1. Fragment source validity is actionable at ordinary commit time, whereas root completeness is intentionally checkpoint-owned and must be enforced before release curation.

#### `VER-002` Verification Criterion — Lint and completeness gates have distinct outcomes

Covers:

1. `SPEC-002`.

Criterion:

1. A valid unconsolidated fixture passes `--lint` and fails `--check` without modifying `CHANGELOG.md`; after write consolidation, `--check` passes, and the hook and release documentation invoke their assigned gates.

Expected evidence:

1. Passing command-mode fixture assertions and policy assertions in `test_harness_policy.py`.
2. Reviewable `.githooks/pre-commit` and `docs/release-branch-process.md` diff.

### `SPEC-003` Specification Commitment — Preserve semantic README release assertions through reflow

Kind: `Quality`

Intent: `Preserve`

Concerns: `validator resilience`, `documentation`

Statement:

1. README assertions for the package boundary, work-item exclusion, and rollback statement shall compare normalized prose that ignores case and whitespace-only reflow while retaining the complete expected semantic phrases; general regex assertion behavior shall remain unchanged for structural contracts.

Rationale:

1. Editorial line wrapping must not produce false failures, but policy checks must not become broad keyword searches.

#### `VER-003` Verification Criterion — README reflow tolerance is narrowly scoped

Covers:

1. `SPEC-003`.

Criterion:

1. The harness validator passes against the current reflowed README through the normalized semantic assertions, and non-README structural checks continue to use the existing regex helper.

Expected evidence:

1. Passing `test_harness_policy.py` output and review of the dedicated normalized-prose helper call sites.

## Architecture Decisions

Architecture snapshot status:

1. `Required`: parser cardinality, command-mode boundaries, and release process ownership are consequential work-item decisions and are captured in `snapshots/architecture.snapshot.md`.

Decision summary:

1. Drivers: remove accidental file-cardinality friction while detecting malformed entries before release preparation.
2. Constraints: preserve the Markdown entry schema, root publication role, one-entry-fragment compatibility, and release-runbook ordering.
3. Selected approach: parse fragments into ordered entry lists; make `--lint` grammar-only and keep `--check` as lint plus root completeness.
4. Affected boundaries: consolidation script, validator fixtures, root-local hook, lifecycle/naming/operator/release documentation.
5. Rejected alternatives: retain one entry per file; make `--check` the ordinary pre-commit gate; replace fragments with a structured manifest; globally loosen regex matching.
6. Validation cues: `VER-001` through `VER-003` and `CHECK-001` through `CHECK-004`.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. CLI: add `--lint`; preserve default write mode and `--check` behavior for existing callers.
2. Internal parser: change `parse_fragment` from one optional entry to a collection of entries plus errors; `discover_fragments` flattens those collections.

### Data, config, and persistence

1. No persisted schema, migration, configuration, or release identity change. Markdown fragment grammar remains the source data format, with metadata scoped per entry.

### State and control flow

1. Ordinary commit flow becomes fragment update, `--lint`, then the existing policy validator.
2. Release preparation becomes `--lint`, `--check`, optional write consolidation, then release-group editing; `--check` remains the final non-mutating completeness test before that decision.

### Safety, security, privacy, migration, and rollback

1. No security, privacy, or migration impact. Parser errors must remain non-mutating and path-specific; write mode remains the only mode that edits root `CHANGELOG.md`.
2. Rollback is a normal revert of the feature commit; existing one-entry fragments remain compatible during and after rollback.

## Risks and Rejected Alternatives

### `RISK-001` Metadata from adjacent entries is accidentally attributed to the wrong entry

Decision or mitigation:

1. Bound each parsed entry at the next recognized changelog heading and match metadata only inside that slice; add a malformed-second-entry fixture.

### `RISK-002` Ordinary commits are incorrectly blocked on root consolidation

Decision or mitigation:

1. Make `--lint` independent of root changelog access and test a valid-but-unconsolidated fixture that passes lint and fails `--check`.

### `RISK-003` Relaxed prose checks hide policy removal

Decision or mitigation:

1. Introduce a dedicated normalized-prose helper only for complete README semantic phrases; preserve `assert_text_contains` and its regex call sites for all structural policy checks.

### `RISK-004` Historical artifacts are silently rewritten

Decision or mitigation:

1. Update only live canonical policy, tooling, operator documentation, hook, and this work-item package; do not edit frozen historical packages or the unrelated modified fragment.

## Planned commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `plan: multi-changelog-fragments -- approve entry-level lint and release gates` | `2026-07-13_multi-changelog-fragments -- approve entry-level lint and release gates` | Approval commit for this combined planning package and its source fragment. |
| Implementation | `feat: multi-changelog-fragments -- validate multiple fragment entries` | `2026-07-13_multi-changelog-fragments -- validate multiple fragment entries` | Parser, command modes, fixtures, hook, and live guidance. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source | Living | Yes | Before each commit | `docs/work-items/2026-07-13_multi-changelog-fragments/changelog/*.md` | Planning approval and implementation entries may share stable fragments after this work. |
| Root changelog consolidation | Living | As needed | Release preparation | `CHANGELOG.md` | Not edited in the plan-only freeze; release uses `--check` and write mode when required. |
| Test cases | Snapshot | Yes | Before implementation | `snapshots/test-cases.snapshot.md` | Captures multi-entry, error-isolation, lint/check, and README reflow cases. |
| Testing guide delta | Living delta | Yes | During implementation | `deltas/testing-guide.delta.md` | Records ordinary `--lint` and release `--check` validation guidance. |
| Operator manual delta | Living delta | Yes | During implementation | `deltas/operator-manual.delta.md` | Records fragment-entry and release-preparation workflow changes. |
| API reference delta | Living delta | No | N/A | N/A | No public API. |
| Architecture snapshot | Snapshot | Yes | Before implementation | `snapshots/architecture.snapshot.md` | Freezes parser and lifecycle decision boundaries. |
| Architecture summary delta | Living delta | No | N/A | N/A | No repository-level architecture document is being introduced. |

## Next-task handoff

1. Planning shape: `combined small/medium`.
2. Frozen package: this spec, `plan_multi-changelog-fragments.md`, `snapshots/architecture.snapshot.md`, `snapshots/test-cases.snapshot.md`, and the two documentation deltas.
3. Next activity: implement `TASK-001` through `TASK-004` in the approved plan.
4. Execution continuity: `same task`; the scope is bounded and the current orchestration thread owns integration.
5. Context visibility: `not exposed`.
6. Artifact rehydration required: `Yes`; re-read the frozen spec, plan, snapshots, and `AGENTS.md` before edits.
7. Exact authoritative artifacts: the frozen package named above and `changelog/planning-approval.md`.
8. Approved strategy and fallback: `plan_multi-changelog-fragments.md` Model and Sub-agent Strategy.
9. First activity: `TASK-001` — add failing multi-entry and mode-separation fixtures.
10. Variance stop condition: stop for an amendment if parser grammar, root consolidation ownership, release-preparation ordering, or verification criteria must change.

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Specification Commitments are atomic, classified, bounded, and contain every implementation obligation in their Statements.
- [x] Verification Criteria have valid Covers sets and expected evidence.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Interfaces, data, control flow, and safety impacts are checked.
- [x] Risks and rejected alternatives are listed.
- [x] Documentation artifact matrix decisions have paths or reasons.
- [x] Planned commit subjects and changelog title snippets are synchronized.
- [x] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
