# Plan Amendment 001: Task Check Conformance

Work ID: `2026-07-30_durable-planning-quality-clarity`
Short ID: `durable-planning-quality-clarity`
Status: Approved
Harness release: `0.8+`
Schema: `schema:plan.amendment`
Policy references: `module:architecture`, `module:lifecycle`, `module:quality`, `module:execution-quality`, `module:models`, `module:freeze-gate`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Original plan reference

- Amendment ID: `AMD-001`
- File: `plan_durable-planning-quality-clarity.md`
- Section or task: `TASK-001` through `TASK-004`, `CHECK-003`, and `CHECK-004`
- Original instruction: clarify a compact `SPEC` → `VER` → `CHECK` evidence model, align reusable templates and validator coverage, and preserve the operator's readability cleanup.

## Discovered issue

The approved implementation defines `SPEC`, `VER`, and `CHECK`, but does not define the equally important `TASK` entity in the canonical quality reference. It also leaves check placement ambiguous: a check proves a verification criterion, while a task may perform the check or produce the input it needs.

The current `## Conformance` section also directs an author to record check evidence and verification-criterion statuses in a planning-quality reference. Those records are implementation-time evidence, not planning-time facts. Keeping that imperative in `module:quality` risks requiring a plan to create results it cannot yet have.

## Proposed change

1. In `module:quality`, add a concise `## Plan Tasks` rule that defines a `TASK-NNN` as a bounded executable unit with a clear outcome and enough dependencies, interfaces, implementation detail, and exit criteria for execution without invented scope.
2. Clarify Plan Check placement: a check always names the `VER-NNN` it supports; place a local check with the task that runs it when that makes execution order clear, and place cross-cutting or end-to-end checks in the shared plan-check section. A task link records operational execution or input production, not conformance.
3. Retain in `module:quality` only the static conformance relationship: checks produce evidence for verification criteria, and completing a task alone does not establish conformance.
4. Move evidence-record and `met` / `not met` / `pending` / `blocked` status-recording requirements to a narrowly scoped `module:execution-quality` section for implementation and completion reporting.
5. Update the policy-architecture catalog, common plan-task/check source block, generated plan templates, and high-signal validator assertions so they express the same entity and stage boundaries.
6. Preserve the operator's existing sentence reordering in `## Baseline artifact readability` exactly; do not revert or rewrite it as part of this amendment.

## Impact assessment

Affected outcome: the quality model becomes complete for the four working entities, `SPEC`, `VER`, `TASK`, and `CHECK`, while preserving the directional evidence relationship `SPEC` → `VER` ← `CHECK` and the operational relation `TASK` → `CHECK`.

Proof impact: plans must continue to link every check to the criterion it supports and now make task/check placement explicit. Implementation evidence and criterion status become an execution record, so plans describe intended evidence rather than claiming results.

Interfaces and data: no runtime interfaces or persisted data change. The documentation interface changes in the quality reference, execution-quality reference, plan source block, generated templates, and validator fixtures.

Risk: duplicating status semantics across quality and execution guidance would create conflicting ownership. The implementation must keep the state vocabulary in one execution-quality owner and leave quality with only the static conformance meaning.

Documentation: update the matching implementation changelog fragment and the testing-guide delta to list the revised validator and template-assembly checks. No root `CHANGELOG.md` consolidation is included.

## Implementation tasks

### `TASK-005` Complete entity and placement guidance

Modify `.agents/skills/dev-doc-harness/references/durable-planning-quality.md` and `.agents/skills/dev-doc-harness/references/policy-architecture.md`.

1. Add `rule:quality.plan-tasks` and a concise `## Plan Tasks` section between Verification Criteria and Plan Checks.
2. Define task scope and required execution detail without duplicating the template's full task schema.
3. State that checks attach semantically to verification criteria and operationally to the task that runs them or produces their required inputs.
4. State when local checks belong beside a task and when cross-cutting checks belong in a shared section.
5. Remove implementation-time status-recording imperatives from `## Conformance`; retain the rule that task completion alone does not establish conformance.
6. Update `module:quality`'s catalog wording to include Plan Tasks and static conformance semantics.

Exit criteria: the quality reference defines all four entities without making a task-to-check relationship substitute for criterion evidence or requiring plans to record implementation results.

### `TASK-006` Create execution-time conformance evidence guidance

Modify `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`.

1. Add an owned execution-quality rule and section for conformance evidence after a task's checks run and before completion is reported.
2. Require the implementation record to retain the check result/evidence and record each affected `VER-NNN` as `met`, `not met`, `pending`, or `blocked` using the existing meanings.
3. State that completed work is conformant only when all applicable verification criteria are met; non-met, pending, or blocked criteria must be reported rather than represented as planning results.
4. Cite `module:quality` for the entity relationship and preserve lifecycle ownership of variance, amendment, approval, and freeze mechanics.

Exit criteria: the mutable evidence/status record is clearly execution-time guidance, has one owner, and does not create a new planning gate.

### `TASK-007` Align authoring surfaces and validation

Modify `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.050.common.task-plan.md`, the generated small/medium and phase-plan templates, `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, and `docs/work-items/2026-07-30_durable-planning-quality-clarity/deltas/testing-guide.delta.md`.

1. Add a compact task/check-placement prompt that requires `Covers: VER-NNN` and distinguishes the check's supported criterion from related task execution.
2. Regenerate plan templates with `.agents/skills/dev-doc-harness/scripts/assemble_templates.py --write`; do not hand-edit generated outputs.
3. First add high-signal validator assertions and fixtures for the `TASK` rule, local/cross-cutting check placement, quality/execution ownership split, and preserved readability reordering; run the validator to confirm the assertions fail before the policy/template changes satisfy them.
4. Run the template assembler check, the full policy validator, whitespace validation, and a focused complete-diff review.
5. Update the testing-guide delta and implementation changelog fragment before the implementation commit.

Exit criteria: source block, generated templates, policy owners, and regression checks agree; no mandatory traceability matrix or planning-time evidence status is reintroduced.

## Plan checks

### `CHECK-006` Verify entity and placement semantics

Covers: `VER-003` and `VER-004` from the approved plan.

Method: Inspect the quality reference, plan source block, and generated plans; run focused validator fixtures that distinguish `Covers: VER-NNN` from an optional related task link and local versus shared check placement.

Expected result: `TASK` has a canonical definition, every check still identifies its supported verification criterion, and task links only describe execution order or inputs.

Evidence record: Validator output and focused requirements-traceability review notes.

### `CHECK-007` Verify execution-time conformance recording

Covers: `VER-003`.

Method: Inspect the quality and execution-quality references and run validator assertions for their ownership boundaries and state vocabulary.

Expected result: quality defines conformance without directing a plan to record evidence/status; execution quality owns check evidence and `VER` status recording after implementation.

Evidence record: Validator output and complete-diff review notes.

### `CHECK-008` Verify preservation and repository hygiene

Covers: `VER-001`, `VER-002`, `VER-003`, and `VER-004`.

Method: Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`, `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, `git diff --check`, `git diff --stat`, and inspect the complete diff against the approved plan and this amendment.

Expected result: generated templates are current, the policy validator exits `0`, no whitespace or unrelated changes appear, and the operator's readability sentence reordering remains present.

Evidence record: Command output, changed-path list, and independent-review findings.

## Model and sub-agent strategy

Model policy: active repository `economy-default`.

1. Execution method: `superpowers:executing-plans`; the policy ownership, source-block generation, and validator assertions require ordered integration.
2. Continuity: `same Codex task`; the approved package, existing user change, and prior evidence are available here.
3. Writer delegation: `Sub-agents: None`; all affected policy, template, and validator surfaces are coupled and share file ownership.
4. Independent review: rerun one read-only reviewer after deterministic validation with curated artifacts, the changed diff, and the entity-ownership/requirements-traceability lens.
5. Reviewer profile: `gpt-5.6-sol`, high reasoning, retained from the operator-approved task policy because the review must assess cross-document normative ownership. Write authority: none. Fallback: report reviewer unavailability rather than silently downgrading the agreed review boundary.
6. Final integration: the execution Codex task owns implementation, validation, variance judgment, and the user-facing completion report.

## Approval

- Required: Yes
- Status: Approved
- Approval evidence: Operator approved the staged amendment on 2026-07-30.
- Superseded by: None

## Planned commits

| Stage | Planned subject |
|---|---|
| Amendment approval | `plan: task-check-conformance -- approve quality amendment` |
| Amended implementation | `docs: task-check-conformance -- clarify execution evidence` |

## Planning artifact freeze gate

This proposed amendment adds the `TASK` entity and moves mutable conformance records to execution-quality ownership. It must pass `module:freeze-gate` before implementation. After approval and the amendment-approval commit, implementation remains paused until a fresh explicit operator instruction.
