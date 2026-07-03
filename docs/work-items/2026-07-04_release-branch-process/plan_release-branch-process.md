# Release Branch Process Plan

Work ID: `2026-07-04_release-branch-process`
Short ID: `release-branch-process`
Status: Approved
Harness release: `0.4+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `module:release`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`, `rule:release.release-notes`, `rule:release.changelog-source`, `rule:release.package-boundary`

Artifact style baseline: write final artifact content, resolve required decisions, remove authoring scaffolds, and use scannable sections, lists, and tables.

## Input Artifacts

Read these before implementation:

1. Approved spec: `spec_release-branch-process.md`.
2. Architecture input: None; the spec marks architecture snapshot as not applicable because this is an agent-executable documentation/process change.
3. Required snapshots or deltas: None.
4. Relevant repository files:
   - `AGENTS.md`
   - `CHANGELOG.md`
   - `.agents/skills/dev-doc-harness/VERSION`
   - `.agents/skills/dev-doc-harness/references/release-policy.md`
   - `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md`
   - `.agents/skills/dev-doc-harness/docs/releases/0.4.0.md`
   - `docs/work-items/2026-07-04_release-branch-process/spec_release-branch-process.md`
5. Unresolved implementation context to confirm before editing: None identified.

If architecture changes before freeze, update the draft spec before finalizing this plan. If implementation adds a release automation script, stop and request an amendment because automation is out of scope.

## Spec Traceability

Requirement coverage:

1. `REQ-001`: implemented by `T-001` and `T-002`; verified by `V-001`.
2. `REQ-002`: implemented by `T-003`; verified by `V-002`.
3. `REQ-003`: implemented by `T-002`; verified by `V-003`, `V-004`, `V-005`, and `V-006`.
4. `REQ-004`: implemented by `T-002`; verified by `V-004` and `V-005`.
5. `REQ-005`: implemented by `T-002`; verified by `V-006`.
6. `REQ-006`: implemented by `T-005`; verified by `V-007`.
7. `REQ-007`: already completed before planning; verified by `V-008`.

Acceptance coverage:

1. `AC-001`: `T-001`, `T-002`; `V-001`.
2. `AC-002`: `T-003`; `V-002`.
3. `AC-003`: `T-002`; `V-003`.
4. `AC-004`: `T-002`; `V-004`.
5. `AC-005`: `T-002`; `V-005`.
6. `AC-006`: `T-002`; `V-006`.
7. `AC-007`: `T-005`; `V-007`.
8. `AC-008`: pre-planning cleanup; `V-008`.

Risk and boundary coverage:

1. `RISK-001`: `T-002`, `T-003`; package path and AGENTS pointer keep root docs distinct from package release notes.
2. `RISK-002`: `T-002`; concrete `0.4` to `0.5.0` example defines version notation.
3. `RISK-003`: `T-002`; first runbook step exits when not on `master`.
4. `RISK-004`: `T-002`; release notes source section is required.
5. `RISK-005`: `T-005`; diff review checks no script is added.

Architecture coverage:

1. Architecture input: None; no architecture snapshot is required.
2. Plan usage: Keep implementation to root docs and AGENTS pointer; do not introduce automation or package-boundary changes.
3. Drift path: edit this draft before approval; after freeze, use variance or amendment for automation, package-boundary, or release-policy changes.
4. Reinterpretation guard: implementation must not move release notes out of `.agents/skills/dev-doc-harness/docs/releases/`.

## Implementation Approach

Implement this as a small documentation/process change. First add the root-level runbook so the full agent-executable process exists in one place. Then add a compact pointer from `AGENTS.md` that directs release-branch chat requests to the runbook while leaving the harness entrypoint and model-policy sections intact.

The runbook should be direct and command-oriented. It should tell the agent what to do after the operator asks to create a release branch, include the operator's step order, define `LRV` and `CV`, show the package-local release-note filename, describe the two commits, and state which branch is pushed. It should not create or imply a root-level release-notes folder.

## Change Surfaces

Expected edits:

1. `docs/release-branch-process.md`: create the agent-executable release-branch runbook.
2. `AGENTS.md`: add a concise release-branch process pointer.
3. `CHANGELOG.md`: add planning approval and implementation entries at the required commit points.

Stable interfaces:

1. `.agents/skills/dev-doc-harness/references/release-policy.md` remains the package release policy owner.
2. `.agents/skills/dev-doc-harness/docs/releases/` remains the package-local release-note directory.
3. `.agents/skills/dev-doc-harness/VERSION` remains the package-local release marker.

Changed interfaces:

1. Root `AGENTS.md` gains a release-branch process pointer.
2. Root `docs/release-branch-process.md` becomes the repository-local agent-executable process.

Implementation boundaries:

1. No release automation scripts are created.
2. No actual release branch is created during this implementation.
3. No release-policy semantics are changed unless implementation finds text that directly contradicts the runbook.
4. Root `docs/releases` remains absent.

## Model and Sub-agent Strategy

Current orchestration:

1. Model/profile and reasoning effort if known: Codex desktop thread; exact model/profile and reasoning effort are not exposed.
2. Model-policy source: active repository policy from `AGENTS.md`, `economy-default`.
3. Override scope and expiry: None.

Fit assessment:

1. Complexity: Low to medium; the implementation is documentation-only but includes release safety sequencing.
2. Risk and blast radius: Medium; incorrect release steps could cause branch or version mistakes when followed later.
3. Ambiguity: Low; the operator supplied the process and the remaining notation choices are recorded in the spec.
4. Budget and latency fit: Good for one orchestration thread.

Recommended orchestration change:

1. None. Use the current orchestration thread.

Sub-agents:

1. None. The edit is small, tightly scoped, and benefits more from main-thread integration than delegation.

## Task Plan

- [ ] `T-001` Dependencies: Approved planning package; inspect `AGENTS.md`, `CHANGELOG.md`, `.agents/skills/dev-doc-harness/VERSION`, `.agents/skills/dev-doc-harness/references/release-policy.md`, and package release-note examples before editing; Traces: `REQ-001`.
- [ ] `T-002` Dependencies: `T-001`; create `docs/release-branch-process.md` with the agent-executable process: operator chat trigger, master preflight and exit, latest remote release branch detection, `LRV` and `CV` derivation, release-prep edits, release notes under `.agents/skills/dev-doc-harness/docs/releases/<CV>.md`, release-prep commit, branch creation as `release/<major>.<minor>`, release branch push, return to `master`, new empty `Unreleased` changelog section, development marker `<major>.<minor>+`, and post-reset commit; Traces: `REQ-001`, `REQ-003`, `REQ-004`, `REQ-005`, `RISK-001`, `RISK-002`, `RISK-003`, `RISK-004`.
- [ ] `T-003` Dependencies: `T-002`; update `AGENTS.md` with a short section that points release-branch creation and release-note placement work to `docs/release-branch-process.md`; Traces: `REQ-002`, `RISK-001`.
- [ ] `T-004` Dependencies: `T-002`, `T-003`; update `CHANGELOG.md` with `2026-07-04_release-branch-process -- document release branch workflow`; Traces: planned implementation commit.
- [ ] `T-005` Dependencies: `T-004`; run validation commands, confirm no automation script was added, confirm root `docs/releases` is absent, review the diff, and commit with the planned implementation subject; Traces: `REQ-006`, `REQ-007`, all acceptance criteria.

## Planned commits

Planning approval commit:

1. Planned subject: `spec: release-branch-process -- approve release process plan`.
2. Changelog title or snippet: `2026-07-04_release-branch-process -- approve release process plan`.
3. Notes: Approval commit for `spec_release-branch-process.md`, `plan_release-branch-process.md`, and `CHANGELOG.md`.

Implementation commit:

1. Planned subject: `docs: release-branch-process -- document release branch workflow`.
2. Changelog title or snippet: `2026-07-04_release-branch-process -- document release branch workflow`.
3. Notes: Implementation commit for `docs/release-branch-process.md`, `AGENTS.md`, and `CHANGELOG.md`.

## Validation Plan

| ID | Command or check | Expected result |
|---|---|---|
| `V-001` | `Select-String -Path docs/release-branch-process.md -Pattern "operator asks|agent|chat"` | Finds the chat-triggered agent workflow wording; covers `AC-001`. |
| `V-002` | `Select-String -Path AGENTS.md -Pattern "docs/release-branch-process.md"` | Finds the release-process pointer; covers `AC-002`. |
| `V-003` | `Select-String -Path docs/release-branch-process.md -Pattern "master|exit"` | Finds the branch preflight and exit instruction; covers `AC-003`. |
| `V-004` | `Select-String -Path docs/release-branch-process.md -Pattern "LRV|CV|minor|release/"` | Finds version derivation and branch naming rules; covers `AC-004`. |
| `V-005` | `Select-String -Path docs/release-branch-process.md -Pattern "VERSION|Unreleased|\\+"` | Finds release and post-release version/changelog transitions; covers `AC-005`. |
| `V-006` | `Select-String -Path docs/release-branch-process.md -Pattern "\\.agents/skills/dev-doc-harness/docs/releases/.+\\.md|Source Changelog Entries"` | Finds package-local release-note path and traceability section guidance; covers `AC-006`. |
| `V-007` | `git diff --name-status` | Shows only `AGENTS.md`, `CHANGELOG.md`, `docs/release-branch-process.md`, and expected planning artifacts when run before implementation commit; no script files are added; covers `AC-007`. |
| `V-008` | `Test-Path -LiteralPath docs/releases` | Prints `False`; covers `AC-008`. |
| `V-009` | `git diff --check` | Exits 0 with no whitespace errors. |

Every validation entry states the expected signal before implementation starts.

## Plan variance handling

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

Local variance that may proceed with a note in the completion report:

1. The runbook filename changes to another root `docs/*.md` path if the operator requests a naming tweak before implementation.
2. The `AGENTS.md` pointer lands in a differently named section while still referencing the runbook.
3. The runbook uses `## Release <major>.<minor>` as the changelog group heading to match current changelog style, while explicitly naming `CV` in the release target metadata and release notes.

Variance requiring operator approval before continuing:

1. Adding an automation script.
2. Moving release notes outside `.agents/skills/dev-doc-harness/docs/releases/`.
3. Changing release-policy package boundary semantics.
4. Pushing `master` as part of the documented default flow.
5. Performing an actual release branch cut during implementation.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

Draft review status: Operator approved the staged planning package on 2026-07-04.
Approval commit status: Approved for the planning freeze commit.
Post-freeze implementation authorization status: Not authorized; implementation requires a fresh operator instruction after the planning approval commit.

## Plan readiness checklist

- [x] Input artifacts and relevant repository context have been read and listed.
- [x] Every spec requirement and acceptance criterion has at least one task and one validation path.
- [x] Risks, scope boundaries, interfaces, and documentation decisions are either covered by tasks or explicitly marked as no-op with a reason.
- [x] Task detail is sufficient for a fresh implementation agent to execute without inventing task order, file scope, validation, or documentation steps.
- [x] Validation entries have exact commands or manual checks with expected signals.
- [x] Planned commits and changelog title snippets are synchronized.
- [x] Variance handling is clear for likely implementation drift.
- [x] The work still fits one orchestration thread with no sub-agents.
- [x] Sub-agent strategy follows `module:models`, or `Sub-agents: None` has a brief fit rationale.
- [x] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain before approval or handoff.

## Completion criteria

- Acceptance criteria in `spec_release-branch-process.md` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- Execution remains within one orchestration thread with no sub-agents.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- Commit subjects match the approved planned subjects or recorded variance, and changelog title snippets are synchronized.
- Planned implementation changes are committed, or the completion report names the exact blocker or explicit no-commit instruction plus current worktree status.
- Root `docs/releases` remains absent.

## Approval

- Status: Approved
- Superseded by: None
