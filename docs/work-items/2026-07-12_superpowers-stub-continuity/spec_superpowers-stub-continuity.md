# Superpowers Stub Continuity Spec

Work ID: `2026-07-12_superpowers-stub-continuity`
Short ID: `superpowers-stub-continuity`
Status: Approved
Harness release: `0.5+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `rule:lifecycle.superpowers-compatibility`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`

## Goal

Prevent harness or Superpowers workflows from creating `docs/superpowers` in repositories that do not already maintain historical Superpowers documentation packages, while preserving pointer-only compatibility in repositories that do.

## Source and Intent

Source input:

1. The operator manually removed the repository's `docs/superpowers` pointer-stub tree after recent wording allowed it to be created without a sufficient continuity reason.
2. The operator approved strengthening the live contract and validator while leaving frozen historical work-item artifacts unchanged.

Desired operator outcome:

1. Current instructions unambiguously prohibit bootstrapping `docs/superpowers`.
2. Existing repositories with prior Superpowers documentation packages may add only the already-defined minimal pointer stubs for continuity.
3. The manual deletion is committed with the implementation.

Success summary:

1. Every live compatibility surface expresses both the pre-existing-package gate and the pointer-stub content restriction.
2. Structural validation protects the contract from later softening.

## Scope Boundary

### In scope

1. Align `AGENTS.md`, `README.md`, `.agents/skills/dev-doc-harness/SKILL.md`, the lifecycle owner, and the package-local operator note.
2. Add or strengthen validator coverage for both rules.
3. Preserve and commit deletion of the six tracked `docs/superpowers` stubs.
4. Update the implementation changelog fragment and root `CHANGELOG.md` as required before implementation commit.

### Non-scope

1. Rewriting frozen historical work-item specs, plans, snapshots, or changelog fragments.
2. Modifying the installed Superpowers plugin.
3. Changing canonical harness artifact locations or stub field definitions.
4. Removing or overwriting unrelated operator changes, including the pre-existing `README.md` worktree state.

### Assumptions

1. "Already exists and contains previous documentation packages" means the directory and prior package content predate the current work; an agent may not create placeholder history to satisfy the gate.
2. Git history and the pre-edit worktree provide sufficient evidence for continuity when needed.

### Open questions

1. None identified after repository-context review.

## Repository Context

### Current state

1. The lifecycle owner currently says `docs/superpowers` files may exist only as stubs, but does not prohibit creating the directory.
2. Entry points repeat similarly permissive wording.
3. Six tracked pointer stubs are manually deleted in the worktree.
4. `README.md` is already marked modified, although its textual diff is empty; implementation must avoid broad normalization.

### Evidence read

1. `AGENTS.md` and the operator-provided global instructions.
2. `.agents/skills/dev-doc-harness/SKILL.md`.
3. `.agents/skills/dev-doc-harness/references/artifact-contract.md`.
4. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`.
5. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`.
6. `.agents/skills/dev-doc-harness/references/naming-conventions.md`.
7. `.agents/skills/dev-doc-harness/docs/operator-note.md`, `README.md`, and `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` search results.
8. Recent Git history and current worktree status.

### Constraints and compatibility

1. Repository-local harness rules override Superpowers' default `docs/superpowers` output path.
2. Canonical durable artifacts remain under `docs/work-items/<work-id>/`.
3. The planning package must freeze before live contract or validator edits begin.
4. Frozen historical artifacts remain truthful records and are not retroactively edited.

## Specification Commitments and Local Verification Criteria

### `SPEC-001` Specification Commitment — Prohibit directory bootstrapping

Kind: `Constraint`

Intent: `Prevent`

Concerns: `compatibility, artifact lifecycle`

Statement:

1. Live harness guidance must permit new `docs/superpowers` documents only when that directory already existed before the current work and contains previous Superpowers documentation packages needed for backward compatibility and continuity.
2. Live guidance must prohibit an agent from creating or seeding the directory to satisfy this condition.

Rationale:

1. Absence of the directory is an intentional repository state and should not be reversed by an external workflow's default path.

#### `VER-001` Verification Criterion — Live surfaces state the continuity gate

Covers:

1. `SPEC-001`.

Criterion:

1. Canonical and operator-facing live surfaces consistently require pre-existing historical package content and forbid bootstrapping the directory.

Expected evidence:

1. Focused text search, diff review, and passing harness policy validation.

### `SPEC-002` Specification Commitment — Preserve pointer-only content

Kind: `Constraint`

Intent: `Maintain`

Concerns: `single source of truth`

Statement:

1. When the continuity gate is satisfied, each newly added `docs/superpowers` document must be a minimal pointer stub containing the existing required title, status, and canonical `docs/work-items/...` link, with no duplicate full spec or plan.

Rationale:

1. Backward compatibility must not create a second durable source of truth.

#### `VER-002` Verification Criterion — Stub schema remains explicit

Covers:

1. `SPEC-002`.

Criterion:

1. The canonical rule and live summaries retain the pointer-only restriction and canonical stub fields.

Expected evidence:

1. Canonical policy inspection and passing harness policy validation.

### `SPEC-003` Specification Commitment — Remove repository stubs

Kind: `Deliverable`

Intent: `Change`

Concerns: `repository cleanup`

Statement:

1. The six operator-deleted tracked files under `docs/superpowers` must be included in the implementation commit without recreating the directory.

Rationale:

1. This repository no longer requires backward-compatible continuity at that path.

#### `VER-003` Verification Criterion — Deletions are committed cleanly

Covers:

1. `SPEC-003`.

Criterion:

1. The implementation commit records all six deletions and contains no added file under `docs/superpowers`.

Expected evidence:

1. Pre-commit staged diff and post-commit path/status inspection.

## Cross-cutting Verification Criteria

### `VER-004` Verification Criterion — Contract is coherent and regression-protected

Covers:

1. `SPEC-001`.
2. `SPEC-002`.
3. `SPEC-003`.

Criterion:

1. The complete live policy, validator, and repository state enforce one coherent compatibility rule without altering frozen history or unrelated operator work.

Expected evidence:

1. Passing policy tests, focused search results, and final diff review.

Applicability:

1. Pre-implementation-commit review.

## Architecture Decisions

Architecture snapshot status:

1. `Not applicable`: the operator selected a bounded policy invariant with no new system, interface, data, or multi-phase architecture.

Decision summary:

1. Drivers: prevent unjustified compatibility artifacts and preserve a single source of truth.
2. Constraints: allow continuity only for repositories already carrying historical Superpowers packages.
3. Selected approach: align all live contract surfaces and add structural regression coverage.
4. Affected boundaries: repository instructions, harness lifecycle policy, package operator guidance, README, and validator.
5. Rejected alternatives: canonical-only wording is insufficiently discoverable; validator-only enforcement is insufficient for copied packages and pre-validation agent behavior.
6. Validation cues: `VER-001` through `VER-004` and the plan checks.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. Agent-facing documentation lifecycle contract and validator expectations.

### Data, config, and persistence

1. None.

### State and control flow

1. Artifact creation gains a precondition: check for a pre-existing directory containing prior documentation packages; otherwise keep all durable planning under the canonical work-item path and create no stub.

### Safety, security, privacy, migration, and rollback

1. No security, privacy, or data migration impact.
2. Rollback is a normal revert; historical frozen artifacts remain unchanged throughout.

## Risks and Rejected Alternatives

### `RISK-001` Ambiguous meaning of pre-existing content

Decision or mitigation:

1. State that the directory and prior package content must predate the current work and cannot be seeded to satisfy the gate.

### `RISK-002` Policy drift across duplicated summaries

Decision or mitigation:

1. Keep detailed ownership in `artifact-contract.md`, align concise entrypoint summaries, and test high-signal required phrases/semantics.

### `RISK-003` Accidental unrelated README normalization

Decision or mitigation:

1. Use a focused patch, inspect the path-specific diff, and stage only intended hunks/files.

## Planned commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `plan: superpowers-stub-continuity -- require historical packages before pointers` | `2026-07-12_superpowers-stub-continuity -- require historical packages before pointers` | Freeze the combined planning package. |
| Implementation | `docs: superpowers-stub-continuity -- prohibit bootstrapping compatibility pointers` | `2026-07-12_superpowers-stub-continuity -- prohibit bootstrapping compatibility pointers` | Align live policy and tests; commit the manual deletions. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source | Living | Yes | Before each commit | `docs/work-items/2026-07-12_superpowers-stub-continuity/changelog/*.md` | Planning and implementation fragments. |
| Root changelog consolidation | Living | Yes | Planning freeze and implementation commit | `CHANGELOG.md` | Required by the applicable top-level freeze instruction. |
| Test cases | Snapshot | Yes | Before implementation | `snapshots/test-cases.snapshot.md` | Captures continuity, pointer-only, deletion, and preservation cases. |
| Testing guide delta | Living delta | No | Not applicable | None | No operator test workflow changes. |
| Operator manual delta | Living delta | No | Not applicable | None | Live package operator note is edited directly as an implementation target. |
| API reference delta | Living delta | No | Not applicable | None | No API change. |
| Architecture snapshot | Snapshot | No | Not applicable | None | No architecture decision beyond the bounded policy rule. |
| Architecture summary delta | Living delta | No | Not applicable | None | No repository architecture change. |

## Next-task handoff

1. Planning shape: `combined small/medium`.
2. Frozen package: this spec, `plan_superpowers-stub-continuity.md`, and `snapshots/test-cases.snapshot.md`.
3. Next activity: implement the live contract, validator, changelog, and manual stub deletions.
4. Execution continuity: `same task`.
5. Context visibility: `not exposed`.
6. Artifact rehydration required: `Yes; reread the frozen package and current worktree before editing because implementation starts only after a fresh operator instruction.`
7. Exact authoritative artifacts: this spec, the plan, and test-case snapshot.
8. Approved strategy and fallback: plan section `Model and Sub-agent Strategy`.
9. First activity: `TASK-001`.
10. Variance stop condition: approval is required for changes to scope, commitments, verification criteria, plan checks, policy architecture, or deletion set.

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Specification Commitments contain the normative obligations.
- [x] Verification Criteria are pass/fail and evidence-backed.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Interfaces, control flow, and safety impacts are checked.
- [x] Risks and rejected alternatives are recorded.
- [x] Documentation artifact decisions have paths or reasons.
- [x] Planned commit subjects and changelog snippets are synchronized.
- [x] No unresolved placeholders or decisions remain.

## Approval

- Status: Approved
- Superseded by: None
