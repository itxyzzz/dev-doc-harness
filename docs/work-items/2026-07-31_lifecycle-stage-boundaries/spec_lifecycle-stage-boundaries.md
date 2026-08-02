# Lifecycle Stage Boundaries Specification

Work ID: `2026-07-31_lifecycle-stage-boundaries`
Short ID: `lifecycle-stage-boundaries`
Status: Approved
Harness release: `0.8+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:lifecycle.work-sizing`, `rule:lifecycle.planning-shape`, `rule:lifecycle.immutable-snapshots`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Intent and scope

### Goal

Clarify that approval freeze gates separate the harness's major lifecycle stages, remove the redundant task-level transition field, and remove the special explicit-handoff-snapshot path from current harness policy.

### In scope

1. Add a concise canonical lifecycle description immediately after `## Work item folders` in `references/artifact-contract.md`.
2. Make freeze-gate, model, execution-start, router, and template language refer to the documented next lifecycle stage rather than a free-form activity or first implementation task.
3. Remove the formal `explicit handoff snapshot` alternative from current reusable policy and templates. Keep ordinary draft continuation and approved-package cross-task continuity as plain operational behavior, not lifecycle states.
4. Remove the duplicate approval-freeze package-completeness prose.
5. Regenerate affected assembled templates and update the policy validator so it enforces the simplified contract.

### Out of scope

1. Changing the two established lifecycle shapes or their approval-first sequencing.
2. Editing frozen historical work-item artifacts that describe the former handoff-snapshot route.
3. Adding a new handoff artifact, handoff state, emergency-compaction workflow, or context-budget policy.
4. Changing model tiers, `Run in` values, or the approved execution-method cascade, except for the operator-selected Sol High review-only final reviewer recorded for this work item.
5. Editing the pre-existing user modification to `.agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md`.

## Evidence read

1. `README.md`, especially `## Lifecycle at a glance`, which already presents the small/medium and large/phased flows.
2. `.agents/skills/dev-doc-harness/references/artifact-contract.md`, `planning-freeze-gates.md`, `subagent-model-policy.md`, and `context-and-quality-gates.md`.
3. `.agents/skills/dev-doc-harness/SKILL.md`.
4. The small/medium, large-anchor, and phase-plan templates; their source blocks and assembly manifests.
5. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
6. Operator review comments on `planning-freeze-gates.md` lines 38, 46, and 50, plus the agreed design discussion in the current Codex task.

## Constraints and compatibility

1. This is a small/medium documentation-and-validation work item; one orchestration thread owns implementation, with one operator-authorized Sol High review-only final reviewer.
2. Current reusable-policy sources, generated templates, and the validator must agree. Change template source blocks, then regenerate templates through the repository assembler; do not hand-edit generated output as the source of truth.
3. The canonical lifecycle wording belongs in `artifact-contract.md` immediately after `## Work item folders`. Do not edit the intentionally simplified README diagram or explanation; report a real semantic conflict only if one is found.
4. `Next lifecycle stage` must name only the major stage determined by the frozen package, never a Plan Task or an instruction such as `execute task 1`.
5. A draft may be continued in another task by an ordinary operator instruction, and an approved package may be used in another task through existing continuity routing. Neither creates a separate freeze trigger or handoff artifact.
6. Preserve the unrelated modified evidence-reference file and exclude it from every staged change set.

## Commitments and verification

### `SPEC-001` Canonical lifecycle-stage boundary

Statement:

1. `artifact-contract.md` must add the concise lifecycle-stage boundary description immediately after `## Work item folders`, using the two established lifecycle shapes already illustrated by the README.
2. The canonical description must make the frozen package and planning shape determine the next lifecycle stage, including the explicit staged small/medium exception, so a task ID is not a valid transition value.

#### `VER-001` Lifecycle boundaries are canonical and bounded

Covers: `SPEC-001`.

Criterion: The lifecycle owner contains the concise two-shape description and its document-type-to-stage mapping without adding a third handoff lifecycle; the README remains unchanged unless implementation finds a real semantic conflict.

Expected evidence: Targeted inspection and a passing harness-policy validation assertion for the lifecycle-stage boundary contract.

### `SPEC-002` Approval freeze remains the only formal freeze path

Statement:

1. Current reusable policy must make explicit operator approval plus its planning approval commit the formal planning-freeze path.
2. Current policy and generated templates must not define `explicit handoff snapshot` as an alternative freeze trigger, immutable state, or input artifact.
3. The ordinary approved-package handoff remains available through post-freeze continuity routing, while a pre-approval draft continuation remains an ad-hoc operator instruction outside the lifecycle contract.

#### `VER-002` No special handoff-snapshot lifecycle remains

Covers: `SPEC-002`.

Criterion: The current reusable-policy sources, source blocks, generated templates, and validator use approved frozen packages for continuity and do not expose the removed special handoff-snapshot route.

Expected evidence: Targeted searches of current policy/template surfaces and a passing full harness-policy validator. Historical work-item matches are explicitly excluded from this check.

### `SPEC-003` Next-stage summary contains stages, not tasks

Statement:

1. The existing `Activity` group in next-stage summaries must be renamed to `Next lifecycle stage`.
2. The group must record the applicable stage value and must not contain `First Plan Task`.
3. Freeze-gate, model-policy, execution-start, and template language must use the same terminology.
4. The duplicate package-completeness wording in the approval-freeze checkpoint must be replaced by a concise recheck reference to the draft-review completeness requirement.

#### `VER-003` Transition presentation is consistent and nonredundant

Covers: `SPEC-003`.

Criterion: The rendered next-stage summaries retain Orchestration, Model, and Fallbacks and limits, while replacing Activity/First Plan Task with Next lifecycle stage; approval freeze contains one detailed completeness rule and one non-duplicated recheck.

Expected evidence: Rendered-template inspection, targeted validator assertions and fixtures, and a passing full harness-policy validator.

### `SPEC-004` Generated policy surfaces and checks remain synchronized

Statement:

1. Template source blocks and their assembled outputs must stay synchronized after the terminology and handoff-route changes.
2. The validator must reject the retired summary shape and accept the canonical lifecycle-stage presentation while retaining existing freeze-stop, fresh authorization, and variance boundaries.

#### `VER-004` Policy conformance remains green

Covers: `SPEC-004`.

Criterion: The template assembler check, harness-policy validator, targeted searches, and whitespace check pass after the implementation.

Expected evidence: Recorded command output in the implementation completion report and matching work-item changelog source fragment.

## Architecture decisions

Architecture snapshot status: Not applicable.

Decision summary:

1. Drivers: Review feedback found that free-form Activity values encouraged task-level entries, that approval-freeze completeness prose was repeated, and that the special handoff snapshot conflated lifecycle freeze with ordinary cross-task continuity.
2. Constraints: Preserve the existing two lifecycle shapes and intentionally simplified README presentation; keep lifecycle ownership in `module:lifecycle`, freeze mechanics in `module:freeze-gate`, and continuity/model behavior in `module:models`.
3. Selected approach: Add a concise lifecycle-stage-boundary description near work-item layout; rename the summary group to `Next lifecycle stage`; remove the special handoff-snapshot state and consume only approved frozen packages at formal transitions.
4. Affected boundaries: Lifecycle, freeze-gate, execution-start, model-policy, router, generated planning templates, and static policy validation.
5. Rejected alternatives: Do not define a third formal handoff lifecycle or a new handoff artifact. Do not retain `First Plan Task` as optional metadata because it recreates the task-level ambiguity.
6. Validation cues: The validator must check stage-boundary ownership, the new summary group, removal of retired handoff wording, and regenerated template conformance.

## Interfaces, data, and control flow

### Interfaces affected

1. Harness text interface: `Next-stage recommendation` and `Approved next stage` retain their outer headings but replace their first group with `Next lifecycle stage`.
2. Lifecycle interface: the new lifecycle-stage-boundary section is the canonical source for the stage selected by each frozen package.

### Data, config, and persistence

None. The work changes repository Markdown and a local validation script only.

### State and control flow

1. The two approval-first flows stay unchanged.
2. Draft continuation before approval is not a freeze state.
3. Approved-package continuity may run in the same or a new Codex task only after the existing fresh authorization route.

### Safety, security, privacy, migration, and rollback

None identified after repository-context review. The main operational risk is silently changing policy semantics; targeted conformance tests and review of the rendered templates mitigate it.

## Risks and rejected alternatives

### `RISK-001` Terminology migration leaves stale generated or validator wording

Decision or mitigation:

1. Update source blocks before assembling generated templates, then update every validator assertion and fixture that intentionally tests the presentation contract.
2. Search current reusable policy and template surfaces for `First Plan Task`, `explicit handoff snapshot`, and the old group heading before final validation.

### `RISK-002` Removing handoff snapshots removes necessary continuity behavior

Decision or mitigation:

1. Preserve normal post-freeze same-task/new-task continuity and fresh authorization.
2. State that an unapproved draft may be continued by an operator-directed ordinary task handoff, but avoid elevating that recovery action into an immutable lifecycle route.

### `RISK-003` The implementation stages unrelated user work

Decision or mitigation:

1. Treat `.agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md` as pre-existing unrelated work and do not modify or stage it.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: lifecycle-stage-boundaries -- approve lifecycle transition clarification` |
| Implementation | `docs: lifecycle-stage-boundaries -- clarify freeze lifecycle stages` |

One cohesive implementation commit is planned: the textual policy, template-source/generated output, validator, and matching implementation changelog fragment change together as one reviewable contract update.

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source | Living | Yes | Before planning and implementation commits | `changelog/planning-approval.md`, `changelog/implementation.md` | One entry per commit; do not edit root `CHANGELOG.md` for ordinary work-item commits. |
| Root changelog consolidation | Living | No | Operator-owned checkpoint | `CHANGELOG.md` | Not part of this work item. |
| Test cases | Snapshot | No | Before implementation | — | Static policy-validator checks cover this documentation contract. |
| Testing guide delta | Living delta | No | During implementation | — | The validation command remains the existing harness-policy test. |
| Operator manual delta | Living delta | No | After implementation | — | No operator-facing documentation change is planned. |
| API reference delta | Living delta | No | During implementation | — | No API change. |
| Architecture snapshot | Snapshot | No | Before implementation | — | No work-item architecture decision beyond local policy wording. |
| Architecture summary delta | Living delta | No | After review | — | No separate long-lived architecture documentation is needed. |

## Planning shape and transition ownership

1. Planning shape: `combined small/medium`.
2. Companion plan: `plan_lifecycle-stage-boundaries.md` is drafted and presented with this specification.
3. Transition owner: `plan_lifecycle-stage-boundaries.md` owns the implementation handoff after the combined package freezes.
4. Next lifecycle stage: `plan execution`.

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Specification Commitments are atomic, bounded, and contain every implementation obligation in their Statements.
- [x] Verification Criteria have valid Covers sets and expected evidence.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Interfaces, data, control flow, and safety/privacy/migration impacts are checked.
- [x] Risks and rejected alternatives are listed.
- [x] Documentation artifact matrix decisions have paths or reasons.
- [x] Planned commit subjects and changelog title snippets are synchronized.
- [x] The companion plan is present in the combined package and owns its implementation handoff.
- [x] The upcoming-stage sub-agent assessment records the authorized Sol High review-only final reviewer and its no-write boundary.
- [x] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain before approval.

## Approval

- Status: Approved
- Superseded by: None
