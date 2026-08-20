# Lifecycle Documentation Clarity Plan

Work ID: `2026-07-18_lifecycle-doc-clarity`
Short ID: `lifecycle-doc-clarity`
Status: Approved
Harness release: `0.7+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:artifact-style`, `module:freeze-gate`, `module:execution-quality`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:models.strategy-required`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`
Execution method: `Superpowers executing-plans` after harness freeze and fresh implementation authorization

## Input Artifacts

1. Draft spec: `docs/work-items/2026-07-18_lifecycle-doc-clarity/spec_lifecycle-doc-clarity.md`.
2. Canonical rules: `.agents/skills/dev-doc-harness/references/artifact-contract.md`, `planning-freeze-gates.md`, `subagent-model-policy.md`, `durable-planning-quality.md`, and `artifact-style.md`.
3. Current user-facing files: `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md`.
4. User review feedback that accepted the four identified corrections and limited diagram work to missing gates and feedback loops.
5. Unresolved implementation context: none.

## Traceability approach

Local links are sufficient: `SPEC-001` maps to `TASK-001`; `SPEC-002` maps to `TASK-002`; `SPEC-003` maps to `TASK-003`; all tasks are checked by `CHECK-001` through `CHECK-003`.

## Change surfaces

1. `README.md`: lifecycle Mermaid diagram, its explanatory paragraph, planning-and-conformance prose, and execution-selection wording.
2. `.agents/skills/dev-doc-harness/docs/operator-note.md`: execution-selection and multi-freeze wording.
3. `docs/work-items/2026-07-18_lifecycle-doc-clarity/deltas/operator-manual.delta.md`: direct operator guidance change record.
4. `docs/work-items/2026-07-18_lifecycle-doc-clarity/changelog/implementation.md`: implementation commit source.

## Implementation approach

Make the smallest textual and diagram changes that satisfy the three
commitments. Preserve the existing diagram structure and visual classes. Do not
edit canonical policy or expand the lifecycle beyond the missing post-freeze
authorization nodes and the three approval feedback loops.

## Model and Sub-agent Strategy

### Planning-task observations

1. Model generation: `not exposed`.
2. Resolved profile: `not exposed`.
3. Reasoning effort: `not exposed`.
4. Context visibility: `not exposed`.

### Approved execution selection

1. Target model/profile: active `economy-default` balanced-tier selection (`Terra` when available).
2. Capability tier: `balanced`.
3. Reasoning effort: `medium`.
4. Orchestration mode: `single-agent`.
5. Availability/fallback: use the same policy-relative balanced selection when available; otherwise stop for an operator decision rather than silently changing tier or effort.
6. Execution continuity: `same task`.
7. Artifact rehydration required: `Yes`; re-read the frozen spec, plan, operator feedback, applicable instructions, and current worktree before editing.
8. Model-policy source: repository `AGENTS.md` active `economy-default` policy.
9. Override scope and expiry: none.

### Upcoming-stage sub-agent assessment

1. Sub-agents: `None`.
2. Fit reason: the two documents and the diagram/prose corrections are tightly coupled, do not have independent file ownership, and are low-risk enough for focused orchestration-thread review.
3. Authorization state: `Not needed`.

## Implementation tasks

### `TASK-001` Repair README lifecycle gates

Dependencies: frozen combined planning package and fresh implementation authorization.

Interfaces:

1. Consumes: `SPEC-001`, current Mermaid graph, and canonical freeze-gate rules.
2. Produces: a Mermaid graph whose paths expose required pauses and feedback.

Implementation:

1. Add an explicit fresh-start-authorization node between the combined-package freeze and its implementation node.
2. Add an explicit fresh-instruction node between the anchor freeze and phase-plan drafting, and add an explicit fresh-start-authorization node between each phase-plan freeze and phase implementation.
3. Restore a `Feedback` arrow from each large-anchor and phase-plan approval decision to its respective draft node; retain the existing combined-package feedback arrow.
4. Keep the phase-output-to-next-phase-planning loop, but route it through the fresh-instruction node rather than directly treating phase-plan drafting as automatic.
5. Rewrite the adjacent explanation to say that the diagram's handoff nodes cover the required fresh instruction or authorization; it must not say implementation proceeds automatically after a freeze.

Exit criteria: the README graph has no direct freeze-to-work transition and all three approval decisions visibly handle feedback.

### `TASK-002` Replace formal README traceability graph

Dependencies: `TASK-001`.

Interfaces:

1. Consumes: `SPEC-002` and current planning-and-conformance section.
2. Produces: short plain-language planning and verification guidance.

Implementation:

1. Remove the text diagram that presents `SPEC`, `VER`, `DEC`, `TASK`, and `CHECK` as a relationship model.
2. Replace its accompanying explanation with concise prose: plans state the intended outcome and boundaries; tasks perform the agreed work; checks generate evidence for verification; exact IDs and mappings are proportional to the work rather than an operator workflow.
3. Leave the small/medium versus large/phased sizing explanation, architecture-snapshot note, documentation-artifact summary, and package-shape explanation intact except for replacing "plan" with "applicable planning artifact" where needed to cover large anchor specs.

Exit criteria: the README remains understandable to an operator without the removed trace-ID graph and does not overstate a plan-only execution record.

### `TASK-003` Correct compact operator guidance

Dependencies: `TASK-001` and `TASK-002`.

Interfaces:

1. Consumes: `SPEC-003`, the approved execution-selection terminology, and the freeze-gate sequence.
2. Produces: an operator note consistent with the README and canonical sources.

Implementation:

1. State that an approved execution selection is recorded in the applicable planning artifact before its freeze; make clear that a large/phased anchor spec can carry the selection.
2. Replace language that suggests selection metadata appears only after a fresh authorization or only in a plan.
3. Replace "Freeze it once" with wording that freezes each current planning package, and state that large/phased work needs a fresh instruction before phase-plan drafting and a fresh authorization before implementation.
4. Create `deltas/operator-manual.delta.md` with the same bounded operator-facing behavior change.

Exit criteria: the note does not contradict the current freeze gate, phase sequence, or execution-selection record.

### `TASK-004` Validate and commit the documentation update

Dependencies: `TASK-001` through `TASK-003`.

Interfaces:

1. Consumes: changed documents, `VER-001` through `VER-003`, and the planned implementation subject.
2. Produces: validation evidence, an implementation changelog fragment, and one documentation commit.

Implementation:

1. Run the harness validator and inspect the changed Mermaid source in the rendered README view.
2. Search the two user-facing documents for direct freeze-to-work wording, the removed trace-ID graph, `Freeze it once`, and post-authorization metadata claims; inspect each remaining match.
3. Run `git diff --check` and review the complete diff for scope, wording, and accidental changes to canonical policy.
4. Create `changelog/implementation.md` using the synchronized heading `## 2026-07-18_lifecycle-doc-clarity -- clarify lifecycle gates and planning guidance`.
5. Stage only the approved documentation, delta, and implementation changelog files and commit with `docs: lifecycle-doc-clarity -- clarify lifecycle gates and planning guidance` after all checks pass.

Exit criteria: all checks pass, the implementation changelog matches the commit subject, and the commit contains only the approved work.

## Plan checks

### `CHECK-001` Harness policy validation

Covers: `VER-001`, `VER-002`, `VER-003`.

Method: `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Expected result: exit code `0` with all policy checks passing.

### `CHECK-002` User-facing lifecycle inspection

Covers: `VER-001`, `VER-002`, `VER-003`.

Method: inspect the rendered README Mermaid diagram and run `rg -n "Freeze it once|SPEC \(Specification Commitment\)|VER \(Verification Criterion\)|after the harness freeze and fresh instruction authorize execution" README.md .agents/skills/dev-doc-harness/docs/operator-note.md`.

Expected result: the diagram visibly pauses after each freeze, all three approval nodes have feedback paths, and the obsolete formal or temporal wording has no matches.

### `CHECK-003` Diff and changelog hygiene

Covers: `VER-001`, `VER-002`, `VER-003`.

Method: `python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --lint`, `git diff --check`, and complete diff review.

Expected result: fragment lint and whitespace checks exit `0`; the diff is limited to the two user-facing documents and this work item's direct documentation artifacts.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: lifecycle-doc-clarity -- approve user-facing documentation corrections` |
| Implementation | `docs: lifecycle-doc-clarity -- clarify lifecycle gates and planning guidance` |

One cohesive implementation commit is required unless the variance route authorizes a stable, independently reviewable split.

## Validation and variance

Equivalent Mermaid syntax or wording changes may proceed when they preserve the
specified approval boundaries and evidence purpose. Stop for an amendment if
execution would alter canonical lifecycle policy, add new states or workflow
branches, change templates or validators, broaden the README redesign, or
require a different model/effort/orchestration choice.

## Implementation handoff

1. Frozen package: this approved spec and plan, the approved operator-manual delta, and any approved amendment.
2. Next activity: `TASK-001` — repair README lifecycle gates.
3. First task: `TASK-001`.
4. Approved execution selection and fallback: balanced tier at medium reasoning under `economy-default`; stop for an operator decision if unavailable.
5. Artifact rehydration: read the frozen package, current `AGENTS.md`, harness router, current worktree, and validation baseline before editing.
6. Variance stop condition: stop for the material scope changes listed in Validation and variance.
7. Upcoming-stage sub-agent assessment: `Sub-agents: None` because the corrections are tightly coupled and require no independent reviewer.

## Readiness

- [x] Inputs, scope, tasks, checks, documentation, and changelog entry are clear.
- [x] Proposed execution selection and implementation handoff are explicit.
- [x] No required decision or ownerless deferral remains.

## Completion

1. Required work and evidence are complete; any noteworthy variance is recorded.
2. Planned changes are committed, or the blocker is stated.

## Approval

- Status: Approved
- Superseded by: None
