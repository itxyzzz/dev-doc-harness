# Plan Task Block Format Spec

Work ID: `2026-07-09_plan-task-block-format`
Short ID: `plan-task-block-format`
Status: Approved
Harness release: `0.5+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:artifact-style`, `module:models`, `module:freeze-gate`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:quality.spec-handoff`, `rule:style.template-prompts`

## Goal

Replace checklist-shaped plan task prompts with sectioned task blocks that preserve implementation detail in the plan itself, while keeping traceability review centralized in one compact `REQ` and `AC` matrix.

## Source and Intent

Source input:

1. Operator reported that harness release `0.5.0` regularly produces specs and plans with the right sections, but the plan itself reads like a checklist instead of a detailed implementation plan.
2. Investigation compared `D:\Backup\2026-07-06_cv-style-gate\` and `D:\Backup\2026-07-09_candidate-ingestion-fact-carry-forward\`.
3. Investigation found the missing detail was present in specs, evidence reports, and snapshots, but compressed away in the plan task rows.
4. Operator approved replacing checkbox task rows with the same sectioned style used by `REQ`, `AC`, and `RISK` lists, and requested a centralized traceability matrix in the plan.

Desired operator outcome:

1. Future harness-generated plans use detailed task blocks instead of checklist rows.
2. Reviewers can inspect requirement and acceptance coverage from one matrix.
3. Implementing agents can follow each task without reconstructing mechanics from scattered sections or hidden chat context.

Success summary:

1. The shared plan task template block renders numbered task sections with `Dependencies`, `Implementation`, `Exit criteria`, and optional `Notes`.
2. `Spec Traceability` becomes a compact matrix mapping each requirement or acceptance criterion to primary tasks and validation.
3. Risks are not included in the main traceability matrix; risk handling stays in task notes, scope/boundary text, or a separate section only when a concrete plan needs it.
4. Harness validation catches regressions that reintroduce checkbox examples or omit the required task-block fields.

## Scope Boundary

### In scope

1. Update the shared plan task block under `.agents/skills/dev-doc-harness/assets/templates/blocks/`.
2. Regenerate the assembled small/medium and phase-plan templates from the updated block.
3. Update plan readiness prompts or quality wording only where needed to align with task blocks and centralized traceability.
4. Add a focused policy validation check that current plan templates use the sectioned task-block shape and no longer use checkbox task examples.
5. Update release or operator-facing notes only if the implementation changes current harness guidance that users need to see.
6. Update `CHANGELOG.md` before the planning approval commit and before the implementation commit.

### Non-scope

1. Do not redesign spec templates beyond references needed for consistency.
2. Do not add semantic validators that attempt to judge arbitrary plan quality beyond the explicit template contract.
3. Do not include risk rows in the main `Spec Traceability` matrix.
4. Do not change Superpowers' upstream plan format; this repository harness owns the canonical artifact format here.
5. Do not rewrite historical work-item artifacts.

### Assumptions

1. The current assembled templates are generated from block files and assembly manifests.
2. A lightweight validator can check template contract markers without becoming a semantic plan-quality parser.
3. `Exit criteria` should be required in task blocks because it gives the implementing agent a local done signal before global validation.
4. Per-task trace IDs are optional; the main matrix is the default review surface.

### Open questions

1. None after operator design approval.

## Repository Context

### Current state

1. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.050.common.task-plan.md` currently prompts checklist rows with task IDs, dependencies, task text, and traces.
2. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md` and `large-phased-work-item-phase-plan.md` contain the generated checklist task prompt.
3. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md` requires plans to be executable by a fresh agent or thread, but the current task prompt does not force a sectioned execution shape.
4. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` validates structural harness contracts and can host a focused check for the explicit task-block template shape.

### Evidence read

1. `.agents/skills/dev-doc-harness/SKILL.md`
2. `.agents/skills/dev-doc-harness/references/artifact-contract.md`
3. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
4. `.agents/skills/dev-doc-harness/references/artifact-style.md`
5. `.agents/skills/dev-doc-harness/references/policy-architecture.md`
6. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
7. `.agents/skills/dev-doc-harness/references/naming-conventions.md`
8. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
9. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
10. `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
11. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.050.common.task-plan.md`
12. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`
13. `D:\Backup\2026-07-06_cv-style-gate\plan_cv-style-gate.md`
14. `D:\Backup\2026-07-09_candidate-ingestion-fact-carry-forward\plan_candidate-ingestion-fact-carry-forward.md`

### Constraints and compatibility

1. The validator change must stay graph- or contract-oriented and avoid parsing arbitrary historical plans for subjective quality.
2. The template should remain readable in both small/medium plans and phase plans.
3. The task-block prompt must not create excessive duplication with the central traceability matrix.
4. Existing frozen historical plans remain valid historical artifacts.

## Requirements

### `REQ-001` Sectioned task-block format

Rationale:

1. Checklist rows encouraged agents to produce task labels rather than implementation plans.

Acceptance links:

1. Covered by `AC-001`, `AC-002`, and `AC-005`.

Notes:

1. Each task should be a third-level section such as ``### `T-001` Short imperative title``.
2. Each task should include `Dependencies`, `Implementation`, and `Exit criteria`.
3. `Notes` should be optional for boundaries, gotchas, or risk-specific guidance.

### `REQ-002` Centralized spec traceability matrix

Rationale:

1. Requirement and acceptance coverage is easier to review in one compact table than repeated across every task.

Acceptance links:

1. Covered by `AC-003` and `AC-005`.

Notes:

1. The plan matrix should use columns `Requirement or acceptance criterion`, `Primary tasks`, and `Validation`.
2. Matrix rows should cover requirements and acceptance criteria.
3. Risk rows should not be part of the default matrix.

### `REQ-003` Template regeneration and consistency

Rationale:

1. The harness source block and generated templates must stay synchronized so downstream adopters receive the same behavior.

Acceptance links:

1. Covered by `AC-001`, `AC-004`, and `AC-005`.

Notes:

1. The implementation should update the source block first, then regenerate assembled plan templates.

### `REQ-004` Regression validation

Rationale:

1. The old checklist shape should not return during future template edits.

Acceptance links:

1. Covered by `AC-004` and `AC-005`.

Notes:

1. The validator should check explicit template contract markers, not semantic quality in arbitrary work-item artifacts.

## Acceptance Criteria

### `AC-001` Small/medium plan template uses task blocks

Verifies:

1. `REQ-001`
2. `REQ-003`

Method:

1. Review `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`.
2. Expected result: `## Task Plan` shows sectioned `T-001` and `T-002` task examples with `Dependencies`, `Implementation`, `Exit criteria`, and optional `Notes`; it does not use checkbox task examples.

### `AC-002` Phase-plan template uses task blocks

Verifies:

1. `REQ-001`

Method:

1. Review `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`.
2. Expected result: the phase-plan task prompt uses the same sectioned task-block shape and remains compatible with fresh-thread phase execution.

### `AC-003` Plan traceability is centralized

Verifies:

1. `REQ-002`

Method:

1. Review the plan templates' `Spec Traceability` section.
2. Expected result: the section includes a matrix with `Requirement or acceptance criterion`, `Primary tasks`, and `Validation`, and it does not instruct agents to put risk rows in that default matrix.

### `AC-004` Harness validator protects the task-block contract

Verifies:

1. `REQ-003`
2. `REQ-004`

Method:

1. Run `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
2. Expected result: validation passes when plan templates use task blocks and would fail if current plan templates reintroduced checkbox task examples or omitted required task-block field labels.

### `AC-005` Harness policy validation passes

Verifies:

1. All requirements.

Method:

1. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
2. Expected result: the full harness policy validator exits successfully after template regeneration and validator updates.

## Architecture Decisions

Architecture snapshot status:

1. Not applicable. This is a template and policy-surface change with no new runtime architecture, data model, public API, persistence, security, or migration boundary.

Decision summary:

1. Drivers: plan readability, fresh-agent executability, and reduced checklist-shaped outputs.
2. Selected approach: keep traceability centralized in a matrix, and make task detail live in sectioned task blocks.
3. Affected boundaries: shared plan template block, generated plan templates, template-style policy prompts, and harness policy validation.
4. Rejected alternatives: keep checkbox rows with stronger wording; require per-task trace and validation fields everywhere; include risks in the default traceability matrix.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. Harness plan templates change their authoring interface for future work-item plans.
2. The harness validator gains a current-template contract check.

### Data, config, and persistence

1. No runtime data, config, database, or API persistence changes.

### State and control flow

1. Template source block changes are assembled into generated plan templates through `.agents/skills/dev-doc-harness/scripts/assemble_templates.py`.
2. Harness validation then checks the generated current surfaces.

### Safety, security, privacy, migration, and rollback

1. No security, privacy, or migration impact is expected.
2. Rollback reverts the template block, generated templates, validator check, and changelog entry.

## Risks and Rejected Alternatives

### `RISK-001` Task blocks become too verbose

Decision or mitigation:

1. Keep the required fields short and practical: `Dependencies`, `Implementation`, and `Exit criteria`; keep `Notes` optional.

### `RISK-002` Traceability becomes duplicated noise

Decision or mitigation:

1. Put `REQ` and `AC` coverage in one matrix. Do not require trace rows inside every task unless useful.

### `RISK-003` Validator overreaches into subjective quality

Decision or mitigation:

1. Validate explicit current-template markers only. Do not parse historical or arbitrary work-item plans for semantic completeness.

### `RISK-004` Risk coverage disappears from plans

Decision or mitigation:

1. Keep risk handling available in task `Notes`, implementation boundaries, or a plan-specific section when needed, but do not include risks in the default matrix.

## Planned Commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `plan: plan-task-block-format` | `2026-07-09_plan-task-block-format -- plan sectioned task blocks` | Approval commit for this spec and plan. |
| Implementation | `docs: plan-task-block-format -- replace checklist task rows` | `2026-07-09_plan-task-block-format -- replace checklist task rows` | Update task-plan template block, generated templates, validator coverage, and changelog. |

## Documentation Artifact Matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Required for planning approval and implementation commits. |
| Test cases | Snapshot | No | Not applicable | N/A | Acceptance criteria and validator coverage are enough for this template-policy change. |
| Testing guide delta | Living delta | No | Not applicable | N/A | Harness validator command already exists and remains the testing surface. |
| Operator manual delta | Living delta | No | Not applicable | N/A | No separate operator workflow change beyond template behavior. |
| API reference delta | Living delta | No | Not applicable | N/A | No API changes. |
| Architecture snapshot | Snapshot | No | Not applicable | N/A | No runtime or work-item architecture decision beyond local template format. |
| Architecture summary delta | Living delta | No | Not applicable | N/A | No long-lived architecture documentation change. |

## Spec Readiness Checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Requirements are specific, relevant, bounded, and linked to acceptance criteria.
- [x] Acceptance criteria are observable, testable, and tied to requirements or scope items.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Interfaces, data, control flow, and safety/privacy/migration impacts are checked.
- [x] Risks and rejected alternatives are listed.
- [x] Documentation artifact matrix decisions have paths or reasons.
- [x] Planned commit subjects and changelog title snippets are synchronized.
- [x] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain before approval or handoff.

## Approval

- Status: Approved
- Superseded by: None
