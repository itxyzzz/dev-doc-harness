# Superpowers Stub Continuity Plan

Work ID: `2026-07-12_superpowers-stub-continuity`
Short ID: `superpowers-stub-continuity`
Status: Approved
Harness release: `0.5+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:lifecycle.variance-policy`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Input Artifacts

1. Approved spec: `spec_superpowers-stub-continuity.md`.
2. Architecture input: spec `Architecture Decisions`; no separate snapshot is required.
3. Required snapshots: `snapshots/test-cases.snapshot.md`.
4. Repository inputs: `AGENTS.md`, `README.md`, `.agents/skills/dev-doc-harness/SKILL.md`, `.agents/skills/dev-doc-harness/references/artifact-contract.md`, `.agents/skills/dev-doc-harness/docs/operator-note.md`, `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, `CHANGELOG.md`, current Git status and diff.
5. Unresolved implementation context: None identified.

## Commitment-Disposition Mapping

| Specification Commitment | Disposition | Implementation Tasks |
|---|---|---|
| `SPEC-001` Prohibit directory bootstrapping | implement | `TASK-001`, `TASK-002` |
| `SPEC-002` Preserve pointer-only content | implement | `TASK-001`, `TASK-002` |
| `SPEC-003` Remove repository stubs | implement | `TASK-003`, `TASK-004` |

## Verification-Execution Mapping

| Verification Criterion | Plan Checks | Expected evidence stage |
|---|---|---|
| `VER-001` Live surfaces state the continuity gate | `CHECK-001`, `CHECK-002` | implementation, pre-commit |
| `VER-002` Stub schema remains explicit | `CHECK-001`, `CHECK-002` | implementation, pre-commit |
| `VER-003` Deletions are committed cleanly | `CHECK-003` | pre-commit and post-commit |
| `VER-004` Contract is coherent and regression-protected | `CHECK-002`, `CHECK-003` | pre-commit |

Architecture coverage:

1. Architecture input: spec `Architecture Decisions`.
2. Plan usage: tasks keep the lifecycle owner canonical and summaries concise while validator coverage checks alignment.
3. Drift path: edit the draft package before freeze; after freeze use variance handling and an amendment when required.
4. Reinterpretation guard: implementation may not expand the compatibility exception or alter frozen history.

## Implementation Approach

Update the canonical lifecycle rule first, making the historical-package precondition and anti-seeding prohibition explicit while retaining the current stub schema. Align the live entrypoints and operator guidance to that owner, then strengthen the existing policy validator with high-signal assertions for both halves of the rule. Preserve the operator's six deletions, update changelog records, validate, and commit only intended implementation paths.

## Change Surfaces

Expected edits:

1. `AGENTS.md`, `README.md`, `.agents/skills/dev-doc-harness/SKILL.md`, `.agents/skills/dev-doc-harness/references/artifact-contract.md`, and `.agents/skills/dev-doc-harness/docs/operator-note.md`: aligned live guidance.
2. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: regression assertions.
3. `docs/superpowers/**`: preserve six tracked deletions only.
4. Work-item implementation changelog and root `CHANGELOG.md`: implementation records.

Stable interfaces:

1. Canonical work-item path and minimal stub fields remain unchanged.

Changed interfaces:

1. Superpowers compatibility workflow gains a strict pre-existing historical-package precondition.

Implementation boundaries:

1. Frozen historical work items and external Superpowers plugin files remain unchanged.

## Model and Sub-agent Strategy

Selection dimensions:

1. Model generation: `GPT-5 family; exact generation not exposed`.
2. Capability tier: `flagship`.
3. Reasoning effort: `current runtime value not exposed; medium recommended`.
4. Orchestration mode: `single-agent`.
5. Resolved profile: `not exposed`.
6. Availability/fallback: `current primary agent; fallback is the same task without delegation`.
7. Execution continuity: `same task`.
8. Context visibility: `not exposed`.
9. Artifact rehydration required: `Yes; reread the frozen package and current diff after the freeze stop`.
10. Model-policy source: `AGENTS.md economy-default policy`.
11. Override scope and expiry: `None`.

Fit assessment:

1. Complexity: low; bounded documentation and validator changes.
2. Risk and blast radius: medium; wording controls future artifact creation across copied harness packages.
3. Ambiguity: low after operator approval of the two-rule design.
4. Budget and latency fit: single-agent execution is proportionate.

Recommended selection change:

1. None.

Sub-agents:

1. None; the repository policy does not authorize them for this work and the change is cohesive and bounded.

## Implementation Tasks

### `TASK-001` Implementation Task — Strengthen canonical compatibility rule

Dependencies:

1. Frozen planning package and fresh operator authorization.

Implementation:

1. Update `artifact-contract.md` with the pre-existing historical-package gate, anti-seeding prohibition, and retained pointer-stub schema.
2. Keep canonical artifact ownership and freeze behavior unchanged.

Exit criteria:

1. Canonical wording unambiguously satisfies `SPEC-001` and `SPEC-002`.

### `TASK-002` Implementation Task — Align live guidance and validator

Dependencies:

1. `TASK-001`.

Implementation:

1. Apply concise aligned wording to `AGENTS.md`, `README.md`, the harness router, and operator note.
2. Add high-signal validator assertions covering the continuity gate and pointer-only rule.
3. Avoid unrelated README normalization or historical artifact edits.

Exit criteria:

1. Live surfaces agree and the policy validator passes.

### `TASK-003` Implementation Task — Preserve manual stub deletions

Dependencies:

1. `TASK-001`.

Implementation:

1. Retain all six tracked `docs/superpowers` deletions.
2. Confirm no file or directory is recreated under that path.

Exit criteria:

1. The staged implementation diff includes exactly the intended deletions under `docs/superpowers`.

### `TASK-004` Implementation Task — Validate and commit implementation

Dependencies:

1. `TASK-002`, `TASK-003`.

Implementation:

1. Update the implementation changelog fragment and root changelog.
2. Run all plan checks, review the complete staged diff, and commit with the planned subject.

Exit criteria:

1. Checks pass, intended files are committed, and unrelated operator work remains preserved.

## Plan Checks

### `CHECK-001` Plan Check — Inspect live compatibility language

Covers:

1. `VER-001`.
2. `VER-002`.

Procedure:

1. Run `rg -n "docs/superpowers|pointer stub|previous documentation packages|already exist|must not create|must not seed" AGENTS.md README.md .agents/skills/dev-doc-harness` and manually compare live summaries with the lifecycle owner.

Expected result:

1. Every live surface requires pre-existing historical package content, prohibits bootstrapping, and permits only minimal canonical pointers.

Evidence record:

1. Completion report with command output summary and criterion status.

Stage or environment:

1. Implementation and pre-commit.

Task/check coordination:

1. Requires `TASK-001` and `TASK-002`.

### `CHECK-002` Plan Check — Run harness policy validation

Covers:

1. `VER-001`.
2. `VER-002`.
3. `VER-004`.

Procedure:

1. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Expected result:

1. Exit code `0`, including the strengthened Superpowers compatibility assertions.

Evidence record:

1. Completion report with validator result and criterion status.

Stage or environment:

1. Pre-commit.

Task/check coordination:

1. Gates `TASK-004`.

### `CHECK-003` Plan Check — Review deletion and preservation diff

Covers:

1. `VER-003`.
2. `VER-004`.

Procedure:

1. Inspect `git status --short`, `git diff --check`, the path-specific `docs/superpowers` diff, and the complete staged diff before commit; inspect commit paths after commit.

Expected result:

1. Six stubs are deleted, none are added, frozen historical work items are unchanged, and no unrelated content is staged.

Evidence record:

1. Completion report with staged and committed path summary.

Stage or environment:

1. Pre-commit and post-commit.

Task/check coordination:

1. Requires `TASK-003` and gates completion of `TASK-004`.

## Planned commits

Planning approval commit:

1. Planned subject: `plan: superpowers-stub-continuity -- require historical packages before pointers`.
2. Changelog title or snippet: `2026-07-12_superpowers-stub-continuity -- require historical packages before pointers`.
3. Notes: approval commit for the spec, plan, test-case snapshot, planning fragment, and required root changelog entry.

Implementation commit:

1. Planned subject: `docs: superpowers-stub-continuity -- prohibit bootstrapping compatibility pointers`.
2. Changelog title or snippet: `2026-07-12_superpowers-stub-continuity -- prohibit bootstrapping compatibility pointers`.
3. Notes: live policy, validator, implementation changelogs, and manual deletions.

## Check execution and completion records

Each execution records the check ID, unique execution instance, stage, actual result, evidence summary, and pass/fail/blocker status in the final implementation report or implementation notes if variance arises.

## Plan variance handling

Before freeze, edit this draft for feedback. After freeze, record nontrivial local variance in `implementation-notes/variance-log.md`; obtain approval through an amendment for scope, commitment, criterion, check, policy architecture, or feasibility changes.

## Planning artifact freeze gate

1. Draft review: operator approved the presented design and instructed planning to proceed.
2. Approval commit: this combined package is finalized for the planning freeze commit.
3. Post-freeze implementation authorization: not yet granted; implementation stops after this commit.

## Next-task handoff

1. Planning shape: `combined small/medium plan`.
2. Frozen package: `spec_superpowers-stub-continuity.md`, this plan, and `snapshots/test-cases.snapshot.md`.
3. Next activity: implement `TASK-001` through `TASK-004`.
4. Execution continuity: `same task`.
5. Context visibility: `not exposed`.
6. Artifact rehydration required: `Yes; reread frozen artifacts and current Git diff before implementation`.
7. Exact authoritative artifacts: the three frozen files above.
8. Approved strategy and fallback: single flagship-tier primary agent with medium reasoning; same-task single-agent fallback.
9. First activity: `TASK-001`.
10. Variance stop condition: stop for approval-required variance under the frozen spec and lifecycle rule.

## Plan readiness checklist

- [x] Inputs and repository context are listed.
- [x] Every commitment and criterion is mapped.
- [x] Risks, scope, interfaces, and documentation decisions are covered.
- [x] Tasks are executable without hidden chat context.
- [x] Checks contain procedures, expected results, evidence records, and stages.
- [x] Planned commits and changelog snippets are synchronized.
- [x] Variance handling is explicit.
- [x] Work fits one orchestration thread without sub-agents.
- [x] No unresolved placeholders or decisions remain.

## Completion criteria

1. `VER-001` through `VER-004` have passing evidence.
2. `TASK-001` through `TASK-004` are complete.
3. Required changelogs are current and the planned implementation commit is created.
4. No approval-required variance remains unresolved.

## Approval

- Status: Approved
- Superseded by: None
