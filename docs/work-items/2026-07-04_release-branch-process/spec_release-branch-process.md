# Release Branch Process Spec

Work ID: `2026-07-04_release-branch-process`
Short ID: `release-branch-process`
Status: Approved
Harness release: `0.4+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:release`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`, `rule:release.release-notes`, `rule:release.changelog-source`, `rule:release.package-boundary`

Artifact style baseline: write final artifact content, resolve required decisions, remove authoring scaffolds, and use scannable sections, lists, and tables.

## Goal

Document a repeatable agent-executable process for cutting a new harness release branch from `master`, curating package-local release notes, pushing the release branch, and resetting `master` for the next development cycle after an operator asks for the release in chat.

## Source and Intent

Source input:

1. Operator request on 2026-07-04 to make creating a new release branch repeatable and painless.
2. Operator-provided release flow covering branch preflight, latest remote release detection, version increment, `VERSION` and changelog updates, package-local release notes, release branch creation/push, and post-release `master` reset.
3. Operator clarification that the desired workflow is chat-driven: the operator tells the agent to create the new release branch, and the agent follows the documented steps and performs the work.
4. Operator instruction to delete the now-redundant empty root-level `docs/releases` folder before planning.

Desired operator/user outcome:

1. Operators can tell the agent in chat to create the next release branch, and the agent can follow one root-level repository document to do the work end to end.
2. Agents can find that release-branch process from `AGENTS.md` before editing release files or creating branches.
3. Release notes remain part of the distributable harness package under `.agents/skills/dev-doc-harness/docs/releases/` as Markdown files.

Success summary:

1. A root-level, non-distributable release-branch runbook describes the exact agent-executable release branch workflow.
2. `AGENTS.md` points agents to the runbook while preserving the package boundary.
3. The runbook aligns with the existing release policy and current `0.4+` development-version notation.

## Scope Boundary

### In scope

1. Create a root-level process document under `docs/` for agents to execute when an operator asks them to cut a release branch.
2. Reference the process document from root `AGENTS.md` so release-branch requests route to it.
3. Specify that release notes live at `.agents/skills/dev-doc-harness/docs/releases/<CV>.md`.
4. Specify how to derive the latest release version from remote `release/*` branches and increment the minor version.
5. Specify the release branch name as `release/<major>.<minor>` without trailing `.0`.
6. Specify that the agent performs the release-prep edits, release-prep commit, release branch checkout/create, release branch push, `master` checkout, post-release reset edits, and post-release reset commit.
7. Specify the two-commit shape: one release-prep commit before creating the release branch and one post-branch `master` reset commit.
8. Specify that `release/0.4`-style branch pushes happen during the release process, while the post-reset `master` commit is local until the operator pushes it or separately asks the agent to push it.
9. Preserve the explicit `master` preflight: exit before changes when the current branch is not `master`.
10. Preserve the already-completed deletion of empty root-level `docs/releases` as pre-planning cleanup.

### Non-scope

1. Do not create a separate automation script in this work item; the agent-executable chat workflow is the deliverable.
2. Do not perform an actual release branch cut.
3. Do not change release policy semantics inside the distributable package unless implementation finds a direct contradiction with the runbook.
4. Do not change historical release notes except as required by this work item planning or later implementation.
5. Do not push `master` as part of the documented default flow.
6. Do not add changelog or release-note generation machinery beyond documented agent-executed steps.

### Assumptions

1. Remote release branches use the current naming convention `release/<major>.<minor>`, such as `release/0.4`.
2. The latest release branch determines the latest release version by treating `release/X.Y` as `X.Y.0`.
3. The next current version `CV` increments only the minor version and resets patch to zero; other release types require explicit operator instructions outside this default flow.
4. The post-release development marker should follow the existing repository notation `<major>.<minor>+`, such as `0.5+` after cutting `0.5.0`.
5. Release notes are curated from changelog entries and source-only changelog entries may appear in the release notes source list for traceability.
6. The current branch for this planning work is `templates-improvements`; the future release process itself requires starting on `master`.

### Open questions

1. None identified after repository-context review.

## Repository Context

### Current state

1. Root `AGENTS.md` points agents to the harness entrypoint, active model policy, and compatibility rules, but does not reference a release-branch workflow.
2. Root `docs/` currently contains tracked work-item history and no `docs/releases` folder after the requested cleanup.
3. Package-local release policy says distributable release notes live under `.agents/skills/dev-doc-harness/docs/releases/`.
4. The current package-local marker is `.agents/skills/dev-doc-harness/VERSION` with value `0.4+`.
5. The current changelog is grouped by release and has a top `## Unreleased` section.
6. Existing release branches use names such as `release/0.4`, while release notes use Markdown files such as `0.4.0.md`.

### Evidence read

1. `AGENTS.md`
2. `CHANGELOG.md`
3. `.agents/skills/dev-doc-harness/SKILL.md`
4. `.agents/skills/dev-doc-harness/VERSION`
5. `.agents/skills/dev-doc-harness/references/artifact-contract.md`
6. `.agents/skills/dev-doc-harness/references/release-policy.md`
7. `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`
8. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
9. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
10. `.agents/skills/dev-doc-harness/references/naming-conventions.md`
11. `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md`
12. `.agents/skills/dev-doc-harness/docs/releases/0.4.0.md`
13. `docs/work-items/2026-07-03_artifact-style-guidance/spec_artifact-style-guidance.md`
14. `docs/work-items/2026-07-03_artifact-style-guidance/plan_artifact-style-guidance.md`
15. `git status --short --branch`
16. `Test-Path docs/releases`

### Constraints and compatibility

1. The work is a small/medium documentation/process change and uses the harness planning lifecycle.
2. Implementation must not begin until the draft planning artifacts are approved and frozen, then followed by a fresh operator instruction.
3. Root `docs/` is outside the distributable package; `.agents/skills/dev-doc-harness/docs/releases/` is inside it.
4. The runbook must not suggest root-level release notes.
5. The runbook must be safe for agents to execute by exiting early if not on `master`.
6. The runbook should use exact commands, checkable steps, and expected outcomes where practical.

## Requirements

### `REQ-001` Root agent-executable release-branch runbook exists

Rationale:

1. Agents need one durable, non-distributable repository document to execute the release branch sequence after an operator asks for it in chat.

Acceptance links:

1. Covered by `AC-001`.

### `REQ-002` AGENTS.md references the runbook

Rationale:

1. Agents should discover the release process without searching root `docs/` ad hoc.

Acceptance links:

1. Covered by `AC-002`.

### `REQ-003` Runbook preserves the operator's release sequence

Rationale:

1. The operator supplied the process order and safety boundaries that should become the canonical agent-executed flow.

Acceptance links:

1. Covered by `AC-003`, `AC-004`, `AC-005`, and `AC-006`.

### `REQ-004` Version and branch naming rules are explicit

Rationale:

1. The workflow depends on consistent translation between remote branch names, exact release versions, package `VERSION`, changelog headings, release-note filenames, and development markers.

Acceptance links:

1. Covered by `AC-004` and `AC-005`.

### `REQ-005` Release notes stay package-local Markdown files

Rationale:

1. Release notes are part of the distributable harness package and must live under `.agents/skills/dev-doc-harness/docs/releases/`.

Acceptance links:

1. Covered by `AC-006`.

### `REQ-006` Implementation avoids automation scope creep

Rationale:

1. The requested deliverable is a documented process. Adding a script would broaden validation and maintenance responsibilities.

Acceptance links:

1. Covered by `AC-007`.

### `REQ-007` Cleanup of root docs/releases remains complete

Rationale:

1. A root-level release notes folder would reinforce the mistaken package boundary.

Acceptance links:

1. Covered by `AC-008`.

## Acceptance Criteria

### `AC-001` Runbook is present under root docs

Verifies:

1. `REQ-001`.

Method:

1. Review `docs/release-branch-process.md` and confirm it describes the release-branch workflow as agent-executable instructions triggered by an operator chat request.

### `AC-002` AGENTS.md references the runbook

Verifies:

1. `REQ-002`.

Method:

1. Review `AGENTS.md` and confirm it points release-branch work to `docs/release-branch-process.md`.

### `AC-003` Master preflight exits before changes

Verifies:

1. `REQ-003`.

Method:

1. Review `docs/release-branch-process.md` and confirm the first release step checks the current branch and exits before edits when it is not `master`.

### `AC-004` Latest remote release branch and CV derivation are explicit

Verifies:

1. `REQ-003` and `REQ-004`.

Method:

1. Review `docs/release-branch-process.md` and confirm it defines `LRV` from remote `release/*` branches, derives `CV` by a minor version increment, and treats non-minor releases as requiring explicit operator instructions outside the default flow.

### `AC-005` VERSION and changelog transitions are explicit

Verifies:

1. `REQ-003` and `REQ-004`.

Method:

1. Review `docs/release-branch-process.md` and confirm it describes setting `VERSION` to `CV`, converting the top `Unreleased` changelog group into the release group, returning to `master`, adding a new empty `Unreleased` section, and setting `VERSION` to the `<major>.<minor>+` development marker.

### `AC-006` Release notes path and source contract are explicit

Verifies:

1. `REQ-003` and `REQ-005`.

Method:

1. Review `docs/release-branch-process.md` and confirm it creates release notes at `.agents/skills/dev-doc-harness/docs/releases/<CV>.md`, describes curating them from the changelog entries for `CV`, and includes source changelog traceability.

### `AC-007` No release automation is added

Verifies:

1. `REQ-006`.

Method:

1. Review `git diff --name-status` before the implementation commit and confirm it does not add release automation scripts.

### `AC-008` Root docs/releases folder is absent

Verifies:

1. `REQ-007`.

Method:

1. Run `Test-Path -LiteralPath docs/releases` and confirm it returns `False`.

## Architecture Decisions

Architecture snapshot status:

1. `Not applicable`: the work documents an agent-executable release process and adds an agent pointer. It does not introduce a new code boundary, package boundary, public API, schema, or automation interface.

Decision summary:

1. Drivers: Release branch creation should be repeatable, package boundaries should stay clear, and agents should have a precise chat-triggered flow before any standalone automation exists.
2. Constraints: Release notes belong in `.agents/skills/dev-doc-harness/docs/releases/`, root `docs/` stays non-distributable, and implementation must not begin before the planning freeze gate.
3. Selected approach: Add a root-level agent-executable runbook plus an `AGENTS.md` pointer; do not add a script.
4. Affected boundaries: Root `docs/`, root `AGENTS.md`, `CHANGELOG.md`, and future package-local release notes.
5. Rejected alternatives: Add a release automation script now; place release notes under root `docs/releases`; push `master` automatically after the post-release reset.
6. Validation cues: Runbook review, `AGENTS.md` review, root folder absence check, and diff review for script additions.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. Root `AGENTS.md` gains a release-branch process pointer.
2. Root `docs/release-branch-process.md` becomes the repository-local agent workflow for release branch creation.

### Data, config, and persistence

1. No runtime data, config, persistence, schema, or migration changes.
2. The documented future process changes `.agents/skills/dev-doc-harness/VERSION`, `CHANGELOG.md`, package-local release notes, and Git branches when followed.

### State and control flow

1. The documented process tells the agent to start from `master`, exit if not on `master`, derive `CV`, commit release-prep changes, create and push `release/<major>.<minor>`, return to `master`, commit the next-development reset, and stop without pushing `master` unless separately instructed.

### Safety, security, privacy, migration, and rollback

1. No security, privacy, compliance, or data migration impact.
2. The runbook should warn that branch creation and push are durable Git operations.
3. Rollback for implementation is a normal revert of the docs commit.
4. Rollback for a future release run is outside this work item and should require explicit operator instruction if a release branch is pushed in error.

## Risks and Rejected Alternatives

### `RISK-001` Runbook could conflict with package release policy

Decision or mitigation:

1. Cite the package-local release-note path and keep root docs outside the distributable package.

### `RISK-002` CV and development marker notation could be ambiguous

Decision or mitigation:

1. Define examples in the runbook: latest remote branch `release/0.4` gives `LRV = 0.4.0`, `CV = 0.5.0`, release branch `release/0.5`, release note `0.5.0.md`, and post-reset marker `0.5+`.

### `RISK-003` Process could accidentally run from a feature branch

Decision or mitigation:

1. Make the first step a hard preflight that exits before edits when current branch is not `master`.

### `RISK-004` Manual release notes could drift from changelog

Decision or mitigation:

1. Document that release notes are curated from changelog entries for `CV` and include a source changelog entries section.

### `RISK-005` Automation could expand scope

Decision or mitigation:

1. Keep scripts out of scope and record automation as a future enhancement after the agent-executed process is stable.

## Planned commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `spec: release-branch-process -- approve release process plan` | `2026-07-04_release-branch-process -- approve release process plan` | Approval commit for this spec, plan, and `CHANGELOG.md`. |
| Implementation | `docs: release-branch-process -- document release branch workflow` | `2026-07-04_release-branch-process -- document release branch workflow` | Implementation commit for `docs/release-branch-process.md`, `AGENTS.md`, and `CHANGELOG.md`. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Required for planning approval and implementation commits |
| Test cases | Snapshot | No | Before implementation | Not applicable | Manual docs checks and static commands cover this documentation/process change |
| Testing guide delta | Living delta | No | During or after implementation | Not applicable | No test workflow changes |
| Operator manual delta | Living delta | No | After implementation | Not applicable | The root runbook is the agent-facing process documentation target |
| API reference delta | Living delta | No | During or after API work | Not applicable | No public API surface |
| Architecture snapshot | Snapshot | No | Before implementation | Not applicable | No new architecture boundary or automation interface |
| Architecture summary delta | Living delta | No | After review | Not applicable | No repository architecture document update |

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Requirements are specific, relevant, bounded, and linked to acceptance criteria.
- [x] Acceptance criteria are observable, testable, and tied to requirements or scope items.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Interfaces, data, control flow, and safety/privacy/migration impacts are checked.
- [x] Risks and rejected alternatives are listed or explicitly absent after review.
- [x] Documentation artifact matrix decisions have paths or reasons.
- [x] Planned commit subjects and changelog title snippets are synchronized.
- [x] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain before approval or handoff.

## Approval

- Status: Approved
- Superseded by: None
