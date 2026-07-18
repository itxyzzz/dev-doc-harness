# Lifecycle Documentation Clarity Spec

Work ID: `2026-07-18_lifecycle-doc-clarity`
Short ID: `lifecycle-doc-clarity`
Status: Approved
Harness release: `0.7+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:artifact-style`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:quality.spec-handoff`

## Goal

Correct the user-facing lifecycle guidance so it presents every required approval
and fresh-instruction boundary, while replacing the overly formal planning and
conformance graph with concise operator language.

## Source and Intent

Source input:

1. Review findings against `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md` after local `master` / 0.7.
2. The operator accepted the four findings and constrained the diagram change to its missing post-freeze gates and approval-feedback loops.

Desired operator/user outcome:

1. An operator can see when a package freezes, when feedback returns to drafting, and when a fresh instruction is required without learning the harness's internal trace-ID vocabulary.

Success summary:

1. The README diagram accurately depicts the combined and phased approval paths.
2. The README and operator note use the same concise, accurate explanation of planning artifacts and execution selection.

## Scope Boundary

### In scope

1. `README.md`: repair the lifecycle diagram and its immediate explanation; replace the `SPEC`/`VER`/`DEC`/`TASK`/`CHECK` graph with plain-language planning and verification guidance; state that the applicable planning artifact, including a large anchor spec, records the execution selection.
2. `.agents/skills/dev-doc-harness/docs/operator-note.md`: correct the timing and location of execution-selection metadata and describe each freeze boundary in the large/phased path.
3. This work item's planning package, changelog source, and operator-manual delta.

### Non-scope

1. Changes to canonical lifecycle, freeze-gate, model, template, validator, or release policy.
2. New lifecycle states, amendment paths, model-policy rules, or diagram redesign beyond the missing gates and feedback loops.
3. Changes to frozen historical work items, root `CHANGELOG.md`, or the distributable package boundary.

### Assumptions

1. Existing canonical references remain the source of truth; this work only corrects summaries that diverged from them.
2. The Mermaid renderer supports the existing flowchart syntax and class styling.

### Open questions

1. None identified after review feedback and repository-context inspection.

## Repository Context

### Current state

1. The README's simplified diagram sends the combined freeze directly to implementation, the anchor freeze directly to phase-plan drafting, and the phase-plan freeze directly to implementation; it omits feedback loops for the large and phase-plan approvals.
2. `artifact-contract.md` and `planning-freeze-gates.md` require a fresh instruction after an anchor freeze and fresh post-freeze authorization before implementation.
3. The operator note says execution selection appears only after freeze and fresh authorization and says the normal flow freezes "once". Both statements conflict with the current gate rules.
4. The README presents the trace IDs as a user-facing graph even though current policy makes full mapping proportional and optional.

### Evidence read

1. `README.md`.
2. `.agents/skills/dev-doc-harness/docs/operator-note.md`.
3. `AGENTS.md` and `.agents/skills/dev-doc-harness/SKILL.md`.
4. `.agents/skills/dev-doc-harness/references/artifact-contract.md`, `planning-freeze-gates.md`, `subagent-model-policy.md`, `durable-planning-quality.md`, and `artifact-style.md`.
5. `git diff master...HEAD -- README.md .agents/skills/dev-doc-harness/docs/operator-note.md` and the post-0.7 documentation commits.

### Constraints and compatibility

1. Preserve the current diagram's overall layout, terminology, Mermaid styling, and small/medium versus large/phased split.
2. Add only fresh-instruction/authorization gates and approval-feedback loops needed to depict existing policy.
3. Keep operator copy plain-language and non-normative; canonical references remain authoritative.
4. Do not leave a generic claim that execution selection exists only in a plan or only after authorization.

## Commitments and verification

### `SPEC-001` Repair the lifecycle diagram

Statement:

1. The README must show a fresh-instruction or start-authorization node after every freeze boundary before the next planning or implementation activity, and must restore feedback loops for both the large-anchor and phase-plan approval decisions.

#### `VER-001` Diagram preserves approval boundaries

Covers: `SPEC-001`.

Criterion: The rendered Mermaid source has no direct freeze-to-work arrow and shows feedback routes for all three approval decisions.

Expected evidence: Manual inspection of the diagram source and rendered README, plus a targeted search of its labels and arrows.

### `SPEC-002` Use proportional operator guidance

Statement:

1. The README must replace the trace-ID relationship graph with short plain-language text explaining that plans define outcomes and boundaries, tasks perform the work, and checks supply verification evidence; it must state that exact IDs and mappings are proportional to the work.

#### `VER-002` README is concise and accurate

Covers: `SPEC-002`.

Criterion: The README retains the useful planning/conformance explanation without presenting `SPEC`, `VER`, `DEC`, `TASK`, and `CHECK` as an operator workflow.

Expected evidence: Diff review and targeted search confirm the removed graph is absent and the replacement wording is present.

### `SPEC-003` Correct operator-note execution wording

Statement:

1. The operator note must say that the approved execution selection is recorded in the applicable planning artifact before freeze, including a large anchor spec where applicable, and that large/phased work freezes each current package before its documented next activity.

#### `VER-003` Operator note matches canonical gates

Covers: `SPEC-003`.

Criterion: The note no longer suggests post-authorization creation of plan metadata or a single freeze for all large/phased work.

Expected evidence: Diff review cross-checked against `planning-freeze-gates.md` and `subagent-model-policy.md`.

## Cross-cutting verification

None. Each commitment has local evidence.

## Architecture Decisions

Architecture snapshot status:

1. Not applicable: the work changes summary prose and a documentation diagram but makes no work-item architecture decision.

Decision summary:

1. Drivers: remove operator confusion created by post-0.7 summary drift.
2. Constraints: preserve existing lifecycle policy and diagram style.
3. Selected approach: make narrow corrections in the two user-facing documents rather than changing canonical rules.
4. Affected boundaries: README and distributable operator note only.
5. Rejected alternatives: redesigning the entire diagram or expanding the README with canonical-policy detail would exceed the accepted scope.
6. Validation cues: `VER-001` through `VER-003` and the harness validator.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. User-facing Markdown and Mermaid documentation only; no APIs or generated interfaces change.

### Data, config, and persistence

1. None.

### State and control flow

1. The Mermaid lifecycle depiction changes only to accurately show existing approval and fresh-instruction control flow.

### Safety, security, privacy, migration, and rollback

1. No safety, security, privacy, migration, or rollout impact. A documentation-only commit is recoverable by normal revert.

## Risks and Rejected Alternatives

### `RISK-001` Diagram introduces a new policy

Decision or mitigation:

1. Add only nodes and arrows already required by the canonical freeze-gate rules; do not add amendment or task-creation flow.

### `RISK-002` Concision removes a necessary distinction

Decision or mitigation:

1. Keep the distinction between plans/tasks/checks in everyday language and retain links to canonical references through existing README structure.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: lifecycle-doc-clarity -- approve user-facing documentation corrections` |
| Implementation | `docs: lifecycle-doc-clarity -- clarify lifecycle gates and planning guidance` |

One cohesive documentation commit is planned.

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source | Living | Yes | Before each commit | `docs/work-items/2026-07-18_lifecycle-doc-clarity/changelog/*.md` | Planning and implementation entries synchronize with commit subjects. |
| Root changelog consolidation | Living | No | Operator-owned checkpoint | `CHANGELOG.md` | No consolidation is part of this documentation-only work. |
| Test cases | Snapshot | No | Before implementation | Not applicable | No runtime behavior changes. |
| Testing guide delta | Living delta | No | During implementation | Not applicable | Validation workflow is unchanged. |
| Operator manual delta | Living delta | Yes | During implementation | `deltas/operator-manual.delta.md` | Captures the corrected operator-facing lifecycle guidance. |
| API reference delta | Living delta | No | During implementation | Not applicable | No API change. |
| Architecture snapshot | Snapshot | No | Before implementation | Not applicable | No architecture decision beyond local documentation mechanics. |
| Architecture summary delta | Living delta | No | After review | Not applicable | No repository architecture change. |

## Planning shape and transition ownership

1. Planning shape: `combined small/medium`.
2. Transition owner: `plan_lifecycle-doc-clarity.md` owns the implementation handoff after the combined planning package freezes.
3. Next activity: update `README.md` and the operator note according to `TASK-001` through `TASK-003`.

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Specification Commitments and Verification Criteria define the bounded documentation outcome.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Documentation artifact decisions have paths or reasons.
- [x] Planned commit subjects are synchronized with the planned changelog title snippets.
- [x] The plan owns the combined package's implementation handoff.
- [x] The upcoming-stage sub-agent assessment is recorded in the plan.
- [x] No unresolved placeholders, required decisions, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
