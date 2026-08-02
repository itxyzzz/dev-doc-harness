# Changelog Fragment Clarity Spec

Work ID: `2026-08-01_changelog-fragment-clarity`
Short ID: `changelog-fragment-clarity`
Status: Approved
Harness release: `0.8+`
Schema: `schema:spec.small-medium`
Companion plan: `plan_changelog-fragment-clarity.md`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:implementation-changelog`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

## Goal

Make current implementation changelog files self-describing, move exceptional compatibility operations away from day-to-day guidance, and guarantee readable separation between root changelog entries.

## Source and Intent

Source input:

1. Operator review comments on the newly introduced changelog lifecycle: clarify the names `implementation-fragment.md` and `phase-NN-fragment.md`; move legacy compatibility and root-migration detail to a bottom section; restore missing empty lines between root entries.

Desired operator outcome:

1. Current changelog guidance distinguishes delivered implementation fragments from planning artifacts, while routine authors see only the workflow they need.
2. Root `CHANGELOG.md` remains compact, readable, and deterministically regenerated.

Success summary:

1. Every current contract and generated template names `implementation-fragment.md` or `phase-NN-fragment.md`; frozen historical filenames remain accepted.
2. Compatibility guidance is isolated, root entries have exactly one empty separator line, and repeated migration/consolidation remains byte-for-byte idempotent.

## Scope Boundary

### In scope

1. Current changelog filename examples, layouts, documentation matrices, templates, policy fixtures, and implementation guidance.
2. The root changelog formatter and focused validation for entry separation and idempotency.
3. Normalizing the current root changelog and adding the matching implementation-stage fragment before the implementation commit.

### Non-scope

1. Renaming or rewriting pre-existing work-item changelog fragments, including frozen pre-0.8 fragments.
2. Changing generic `changelog/*.md` discovery, legacy parsing semantics, package-impact values, or release-note curation.
3. Creating a planning changelog fragment or altering release content beyond formatting separators.

### Assumptions

1. The generic Markdown-fragment discovery remains the compatibility boundary for historical filenames.
2. `implementation-fragment.md` is the default name for ordinary implementation work and `phase-NN-fragment.md` is the default for a phase-specific delivery.

### Open questions

1. None identified after repository-context review; the operator selected the `-fragment` convention.

## Repository Context

### Current state

1. `module:implementation-changelog` currently names `implementation.md`; lifecycle layouts and generated templates repeat that example.
2. The consolidator discovers Markdown files below `changelog/` generically, so it does not depend on the current example filename.
3. Current root migration compacts metadata but can leave adjacent level-three entries without an empty separator line.

### Evidence read

1. Review comments supplied by the operator.
2. `references/naming-conventions.md`, `references/implementation-changelog.md`, `references/artifact-contract.md`, `SKILL.md`, small/medium and large/phased templates, `scripts/consolidate_changelog_fragments.py`, and `scripts/test_harness_policy.py`.

### Constraints and compatibility

1. Planning and freeze work must not create changelog entries.
2. Pre-0.8 release notes and changelog fragments remain frozen; historical filenames stay discoverable without a migration.
3. The root migration and default consolidation must remain idempotent.
4. Generated templates are edited through source blocks and `assemble_templates.py`.

## Commitments and verification

### `SPEC-001` Adopt explicit current fragment filenames

Statement:

1. Current implementation guidance, lifecycle layouts, documentation matrices, templates, and current validator fixtures must use `implementation-fragment.md` for ordinary work and `phase-NN-fragment.md` for phase delivery examples, without narrowing generic fragment discovery.

#### `VER-001` Current filename contract is consistent

Covers: `SPEC-001`.

Criterion: Active references and generated templates name the explicit `-fragment` convention; compact-format fixtures exercise the new ordinary filename; frozen legacy fixture paths remain valid.

Expected evidence: Focused repository search, template assembly check, and policy-validator pass.

### `SPEC-002` Separate routine and compatibility guidance

Statement:

1. The implementation changelog reference must keep routine authoring and consolidation instructions near the top, and place frozen legacy metadata support and the `--migrate-root` operation in a final `Compatibility and legacy support` section.

#### `VER-002` Day-to-day guidance remains focused

Covers: `SPEC-002`.

Criterion: A routine implementation author can identify the required fragment, compact metadata, lint, check, and default consolidation workflow before reaching the compatibility section.

Expected evidence: Policy validator assertions and focused document review.

### `SPEC-003` Preserve readable, idempotent root entries

Statement:

1. Root migration and consolidation output must leave exactly one blank line between consecutive changelog entry headings, preserve entry bodies and release headings, and make no change on a second run.

#### `VER-003` Root formatting is deterministic

Covers: `SPEC-003`.

Criterion: Fixtures show spacing normalization without data loss, and rerunning migration or consolidation produces identical bytes.

Expected evidence: Focused validator fixtures, direct migration/consolidation commands, `git diff --check`, and second-run no-op inspection.

## Architecture Decisions

Architecture snapshot status:

1. Not applicable: this is a local documentation contract and formatter-normalization adjustment; no cross-component architecture decision is made.

Decision summary:

1. Drivers: review clarity, reduced routine context, historical compatibility, and root readability.
2. Constraints: generic discovery and frozen historical paths remain unchanged.
3. Selected approach: make `-fragment` the current documented filename convention, retain filename-agnostic discovery, isolate exceptional compatibility prose, and normalize entry separators in the existing deterministic formatter.
4. Affected boundaries: changelog policy, lifecycle documentation, generated templates, consolidator serialization, validation fixtures, and root changelog.
5. Rejected alternatives: enforce filenames in the parser, which would break or burden frozen historical paths; retain `implementation.md`, which does not visibly distinguish the file's role.
6. Validation cues: `VER-001`, `VER-002`, and `VER-003`.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. The documented artifact-path interface changes from current `implementation.md` / `phase-01.md` examples to `implementation-fragment.md` / `phase-01-fragment.md`; generic disk discovery remains unchanged.

### Data, config, and persistence

1. Root `CHANGELOG.md` formatting changes only by inserting required blank separators; no metadata or body content is changed except the new implementation entry created during delivery.

### State and control flow

1. Routine authors follow fragment creation, lint, check, and default consolidation; exceptional legacy support and migration remain separately documented compatibility operations.

### Safety, security, privacy, migration, and rollback

1. No security, privacy, or persistence risk is introduced. The root normalizer is idempotent and can be rolled back by reverting the cohesive implementation commit; frozen fragment paths are not rewritten.

## Risks and Rejected Alternatives

### `RISK-001` Over-enforcing a documentation convention

Decision or mitigation:

1. Keep the consolidator's generic Markdown discovery and retain historical fixtures, so new filenames guide current work without excluding prior paths.

### `RISK-002` Spacing rewrite changes more than intended

Decision or mitigation:

1. Test body and release-heading preservation, review the root diff, and require a second migration/consolidation no-op before committing.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: changelog-fragment-clarity -- approve explicit fragment naming` |
| Implementation | `refactor: changelog-fragment-clarity -- clarify current fragment lifecycle` |

One cohesive implementation commit is required because the naming contract, guidance split, serializer, generated templates, validation, and root formatting must agree.

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Implementation changelog source | Living | Yes | Before implementation commit | `docs/work-items/2026-08-01_changelog-fragment-clarity/changelog/implementation-fragment.md` | Create only after authorization; use the new current convention |
| Root changelog consolidation | Living | Yes | Implementation checkpoint | `CHANGELOG.md` | Normalize after formatter and fixture checks pass |
| Test cases | Snapshot | Yes | Before implementation | `snapshots/test-cases.snapshot.md` | Captures filename, guidance, and spacing cases |
| Testing guide delta | Living delta | No | N/A | N/A | Internal harness validator and script checks provide the evidence |
| Operator manual delta | Living delta | No | N/A | N/A | README remains adequate unless implementation review identifies a current-path example |
| API reference delta | Living delta | No | N/A | N/A | No public API |
| Architecture snapshot | Snapshot | No | N/A | N/A | No work-item architecture decision beyond local mechanics |
| Architecture summary delta | Living delta | No | N/A | N/A | No repository-level architecture update |

## Planning shape and transition ownership

1. Planning shape: `combined small/medium`.
2. Companion plan: `plan_changelog-fragment-clarity.md` is drafted with this spec.
3. Transition owner: `plan_changelog-fragment-clarity.md` owns the `plan execution` transition after the combined package freezes.
4. Next lifecycle stage: `plan execution`.

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Specification Commitments and Verification Criteria are atomic and bounded.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Interfaces, data, control flow, and safety impacts are checked.
- [x] Risks and rejected alternatives are explicit.
- [x] Documentation artifact matrix decisions have paths or reasons.
- [x] Planned implementation commit subject is clear; planning approval has no changelog entry.
- [x] The companion plan owns the implementation handoff.
- [x] No unresolved placeholders, decisions, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
