# Changelog Lifecycle Simplification Specification

Work ID: `2026-08-01_changelog-lifecycle-simplification`
Short ID: `changelog-lifecycle-simplification`
Status: Approved
Harness release: `0.8+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:release`

## Intent and scope

### Goal

Reduce root changelog size and planning-context noise by recording only implementation-stage delivery, using a compact entry metadata line, and preserving the fragment consolidator's idempotent behavior.

### In scope

1. Remove every root `CHANGELOG.md` entry whose package impact is `planning-only`, regardless of its age.
2. Replace the three-line entry metadata with the tagged two-field form below. Both values must remain in Markdown code tags.

   ```md
   Meta -- `<release-target>` : `<package-impact>`
   ```
3. Move current changelog authoring, fragment, and consolidation rules into a dedicated implementation-stage reference so normal spec, plan, and freeze-gate work does not load them.
4. Stop creating planning-approval changelog fragments and stop requiring a changelog update for a planning approval commit.
5. Update the primary `SKILL.md` router so it loads the dedicated changelog reference only for implementation and changelog-maintenance work, never for routine planning or freeze work.
6. Preserve pre-0.8 release notes and work-item changelog fragments verbatim; retain parser compatibility for their legacy metadata.
7. Update post-0.8 fragments only where migration or validation requires it.
8. Keep fragment linting, root-completeness checks, and insertion idempotent.
9. Remove the obsolete root `TODO.md` statement from the package boundary.

### Out of scope

1. Rewriting frozen release notes or any pre-0.8 fragment.
2. Changing release versioning, package boundaries other than the obsolete `TODO.md` reference, or release-branch flow.
3. Generating release notes automatically.
4. Altering historical Git commits or tags.

### Assumptions

1. Git history is the authoritative audit record for removed historical planning entries.
2. Release-note selection remains manual curation from the compact root changelog; a per-entry `Release-note` field is not needed.
3. Legacy fragments remain valid archival input, but newly authored implementation entries follow the compact schema.

## Repository context

### Current state

1. Root `CHANGELOG.md` is 74 KB and uses separate `Release target`, `Package impact`, and `Release-note` lines for each entry.
2. The consolidator parses those three fields, inserts missing unreleased entries by heading, and treats all valid fragment entries as potential root candidates.
3. Current lifecycle templates and freeze guidance create a `planning-approval.md` fragment and require changelog work during planning approval.
4. `release-policy.md` lists root `TODO.md` as excluded even though it no longer exists.

### Evidence read

1. `.agents/skills/dev-doc-harness/references/artifact-contract.md`
2. `.agents/skills/dev-doc-harness/references/release-policy.md`
3. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
4. `.agents/skills/dev-doc-harness/references/naming-conventions.md`
5. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
6. `.agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py`
7. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`
8. `CHANGELOG.md`

### Constraints and compatibility

1. The current planning package is subject to the freeze gate, but it must not add a new plan-only changelog record because the approved scope removes that lifecycle behavior.
2. The canonical planning package stays under `docs/work-items/`; no `docs/superpowers` copy is created.
3. Current policy and templates must direct implementation work to the dedicated changelog reference, while planning routes avoid loading it.
4. Consolidation must remain safe to run repeatedly: after a successful run, a second run must not modify `CHANGELOG.md`.

## Commitments and verification

### `SPEC-001` Implementation-only changelog lifecycle

Statement:

1. The harness must not create or require changelog entries for spec, plan, amendment, or planning-approval work; it must require an implementation-stage fragment before each implementation commit that changes a harness-managed repository.
2. A dedicated current reference must own the implementation fragment schema, migration compatibility, consolidation timing, and root cleanup rule.
3. The primary router must load that reference for implementation and changelog-maintenance routes only, so routine planning and freeze context does not include it.

#### `VER-001` Implementation-only lifecycle routing

Covers: `SPEC-001`.

Criterion: Current router, lifecycle, freeze, template, and README surfaces describe changelog work only at the implementation stage and route implementation authors to one dedicated reference.

Expected evidence: Focused policy-validator checks and repository searches show no active planning-stage changelog obligation or planning-approval fragment template.

### `SPEC-002` Compact tagged metadata schema

Statement:

1. New implementation fragment and root changelog entries must use exactly one metadata line in the compact tagged form defined in the Scope section above.
2. Valid current package-impact values are `distributable` and `repository-only`; `planning-only` is historical compatibility input only and must not appear in the root changelog.
3. Release-note relevance must not be stored as entry metadata.

#### `VER-002` Compact schema validation

Covers: `SPEC-002`.

Criterion: The consolidator and policy tests accept the compact tagged form, reject malformed current values, accept frozen legacy syntax only for compatibility, and reject or remove root planning-only entries.

Expected evidence: Targeted parser fixtures and the full harness-policy validator pass.

### `SPEC-003` Safe historical cleanup

Statement:

1. The root changelog cleanup must remove every planning-only entry and compact every remaining entry without changing release notes or pre-0.8 fragments.
2. Post-0.8 fragment changes must be limited to the schema or behavior necessary for the new current lifecycle.

#### `VER-003` Cleanup boundary

Covers: `SPEC-003`.

Criterion: The root changelog contains no `planning-only`, `Release-note:`, `Release target:`, or legacy three-line metadata; pre-0.8 release-note and fragment files are unchanged.

Expected evidence: Deterministic content checks, `git diff --check`, and a scoped diff review.

### `SPEC-004` Idempotent consolidation

Statement:

1. Fragment linting, missing-root detection, and insertion must support both preserved legacy fragments and compact current implementation fragments.
2. After consolidation has inserted all eligible compact entries, repeating the command must make no further change.

#### `VER-004` Idempotency and compatibility

Covers: `SPEC-004`.

Criterion: Test fixtures demonstrate legacy lint compatibility, compact-entry insertion, planning-only exclusion, duplicate-heading rejection, and a no-op second consolidation run.

Expected evidence: Focused script tests run by the policy validator and direct `--lint` / `--check` command output.

### `SPEC-005` Accurate distribution boundary

Statement:

1. The release policy must no longer claim that root `TODO.md` is part of the excluded repository-local material.

#### `VER-005` Package-boundary accuracy

Covers: `SPEC-005`.

Criterion: The current release policy and its validator expectation no longer reference root `TODO.md`.

Expected evidence: Focused text search and the release-policy validator pass.

## Architecture decisions

Architecture snapshot status: Required. The change creates an explicit ownership boundary between planning artifacts and implementation changelog operations, and preserves a compatibility parser at that boundary.

Decision summary:

1. Drivers: reduce active planning context, constrain root changelog growth, and preserve release-source and fragment-consolidation behavior.
2. Constraints: historical pre-0.8 release notes and fragments are immutable; root history can be curated because Git preserves prior content.
3. Selected approach: create a dedicated `module:implementation-changelog` reference; use a compact tagged two-field line; allow legacy parsing without generating or consolidating plan-only content.
4. Affected boundaries: lifecycle and freeze guidance, templates and assembly manifests, naming guidance, release policy, consolidator, validator, root changelog, current fragments, and README routing.
5. Rejected alternatives: retain the `Release-note` field (unnecessary noise); eliminate metadata entirely (weakens validation); rewrite frozen fragments (violates the release boundary); retain planning fragments but hide them (does not reduce planning context or maintenance burden).
6. Validation cues: `VER-001` through `VER-005`, direct consolidation idempotency checks, and scoped frozen-file review.

## Interfaces, data, and control flow

### Interfaces affected

1. Fragment entry parser input changes from three separate metadata lines to one tagged compact metadata line for current entries.
2. CLI behavior continues to expose `--lint` and `--check`; any migration or cleanup mode must be explicit and documented.

### Data, config, and persistence

1. `CHANGELOG.md` is migrated in place by removing plan-only sections and normalizing remaining metadata.
2. Work-item fragments are archival text records; only post-0.8 files may change.

### State and control flow

1. Planning flow: draft, review, and freeze without changelog source creation.
2. Implementation flow: read the dedicated changelog reference, update one implementation fragment before its commit, then consolidate at an operator-owned checkpoint.
3. Consolidation flow: parse compatible fragments, consider only eligible implementation entries, reject duplicates, insert absent eligible entries newest-first, and make a second run a no-op.

### Safety, security, privacy, migration, and rollback

1. No security, privacy, or personal-data impact is identified.
2. Migration risk is accidental alteration of frozen material; implementation must use an allowlisted post-0.8 scope and review the diff against frozen release and fragment paths.
3. Rollback is a normal Git revert of the implementation commit, restoring the previous policy, script, and root changelog content.

## Risks and rejected alternatives

### `RISK-001` Legacy compatibility permits newly authored obsolete fragments

Decision or mitigation:

1. Document compact metadata as the sole current authoring schema and add validator checks for active templates and current policy. Keep legacy parsing only as a read compatibility path for frozen historical files.

### `RISK-002` Root cleanup changes a large historical file

Decision or mitigation:

1. Use deterministic entry parsing or a narrowly tested rewrite path, verify no planning-only section remains, normalize remaining metadata, and review the resulting count and diff before commit.

### `RISK-003` Release-note curation loses a hint

Decision or mitigation:

1. Treat release-note inclusion as release-maintainer curation from implementation-facing root entries. `distributable` remains the useful package-impact signal, and no automatic release-note generation depends on the removed field.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: changelog-lifecycle-simplification -- approve implementation-only changelog flow` |
| Implementation | `refactor: changelog-lifecycle-simplification -- retain only implementation delivery records` |

The implementation is one cohesive change because policy, parser, validation, and the root migration must agree atomically.

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source | Living | No | Planning | None | Planning-only records are retired by this work. |
| Implementation changelog source | Living | Yes | Before the implementation commit | `docs/work-items/2026-08-01_changelog-lifecycle-simplification/changelog/implementation.md` | Create only after fresh implementation authorization, using the compact tagged schema. |
| Root changelog consolidation | Living | Yes | Implementation migration and later operator-owned checkpoints | `CHANGELOG.md` | Cleanup is a direct implementation deliverable; later consolidation remains checkpoint-owned. |
| Test cases | Snapshot | Yes | Before implementation | `snapshots/test-cases.snapshot.md` | Covers parser compatibility, cleanup, and idempotency. |
| Architecture snapshot | Snapshot | Yes | Before implementation | `snapshots/architecture.snapshot.md` | Captures ownership and compatibility boundary. |
| Testing guide delta | Living delta | No | N/A | None | Harness validation commands remain in the current guidance. |
| Operator manual delta | Living delta | No | N/A | None | Current operator note and README will be updated directly if routing language changes. |
| API reference delta | Living delta | No | N/A | None | No public application API. |
| Architecture summary delta | Living delta | No | N/A | None | Architecture decision is work-item-local. |

## Planning shape and transition ownership

1. Planning shape: `combined small/medium`.
2. Companion plan: `plan_changelog-lifecycle-simplification.md` is drafted with this spec.
3. Transition owner: the companion plan owns the `plan execution` transition after the package freezes.
4. Next lifecycle stage: `plan execution`.

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Specification Commitments and Verification Criteria are atomic and linked.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Interfaces, data, control flow, and migration impacts are checked.
- [x] Risks and rejected alternatives are explicit.
- [x] Documentation artifact decisions have paths or reasons.
- [x] Planned commit subjects are defined without a planning-only changelog entry.
- [x] The companion plan is present and owns implementation handoff.
- [x] The upcoming-stage sub-agent assessment is recorded in the companion plan.
- [x] No unresolved placeholders, unresolved required decisions, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
