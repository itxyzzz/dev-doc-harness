# Protected Post-Release Synchronization Plan

Work ID: `2026-07-11_post-release-pr-flow`
Short ID: `post-release-pr-flow`
Status: Approved
Harness release: `0.5+`
Schema: `schema:plan.small-medium`

## Input artifacts

1. Spec: `spec_post-release-pr-flow.md`.
2. Architecture snapshot: `snapshots/architecture.snapshot.md`.
3. Test cases: `snapshots/test-cases.snapshot.md`.
4. Target documentation: `docs/release-branch-process.md`.
5. Evidence: the `0.5.0` release-prep commit is not an ancestor of `origin/master` or `origin/compatibility-improv`.

## Spec traceability

| Requirement or acceptance criterion | Primary task | Validation |
|---|---|---|
| `REQ-001`, `AC-001` protected post-release PR | `T-001` | `V-001`, `V-004` |
| `REQ-002`, `AC-002` preserve release state | `T-001` | `V-002` |
| `REQ-003`, `AC-003` remote verification | `T-001` | `V-003`, `V-004` |
| `REQ-004`, `AC-004` stop on divergence | `T-001` | `V-004` |

Architecture coverage: `T-001` implements the approved protected-PR boundary. Any change that reintroduces a direct `master` push or omits the post-merge remote gate is a high-impact scope variance and requires an amendment after freeze.

## Implementation approach

Update only the post-release portion of the runbook. The release branch remains the immutable source of the released state. A new topic branch starts from that source, carries the minimal development-marker reset, and is merged to `master` through GitHub's existing protections. The runbook then verifies remote ancestry and extracts the same released changelog segment from both branches before permitting future development branches.

## Change surfaces

1. `docs/release-branch-process.md`: replace the direct post-release `master` reset with the protected PR flow, exact verification commands, and blocking failure handling.
2. `docs/work-items/2026-07-11_post-release-pr-flow/changelog/implementation.md`: record the implementation commit before it is created.

Stable interfaces: release-branch naming, concrete release-note filenames, the `0.5+`-style development marker, and existing validator command remain unchanged.

Changed interface: the runbook's post-release sequence now uses a PR rather than a direct `master` commit.

Implementation boundary: GitHub protection settings, automation, and the current release state remain unchanged.

## Model and sub-agent strategy

Current orchestration: model/profile and reasoning effort are not exposed; model-policy source is `AGENTS.md` active `economy-default`; no override.

Fit assessment: low implementation complexity, medium process/security blast radius, and low ambiguity after the operator selected the PR approach. One orchestration thread can safely perform the focused documentation update and validation.

Sub-agents: None. A separate review agent would duplicate the small, single-document change without improving isolation enough to justify coordination.

## Task plan

### `T-001` Replace the direct reset with a protected PR sequence

Dependencies: Approved `spec_post-release-pr-flow.md` and `snapshots/architecture.snapshot.md`.

Implementation:

1. In `docs/release-branch-process.md`, replace `## Reset Master For The Next Development Cycle` with a post-release development PR section.
2. Document `git checkout -b post-release/<major>.<minor>-start-development release/<major>.<minor>` and retain the empty `Unreleased` heading plus `<major>.<minor>+` development-marker updates on that topic branch.
3. Document pushing the topic branch, opening a PR to `master`, and merging it through GitHub protections; remove any instruction to commit or push directly to `master`.
4. Add a post-merge `git fetch --prune origin` step, an ancestry check, and a normalized PowerShell comparison that starts at `## Release <major>.<minor>` in both remote changelogs.
5. Add failure handling that blocks new development branches until both checks succeed.
6. Before the implementation commit, create `changelog/implementation.md` with the planned implementation subject and matching title snippet.

Exit criteria:

1. `docs/release-branch-process.md` contains no direct-push-to-`master` path for the post-release reset.
2. The documented commands are internally consistent with protected `master` and the existing release-branch naming scheme.
3. The implementation fragment exists and matches the planned implementation subject.

## Planned commits

Planning approval:

1. Subject: `post-release-pr-flow plan: approve protected post-release synchronization`.
2. Changelog title: `post-release-pr-flow plan: approve protected post-release synchronization`.

Implementation:

1. Subject: `post-release-pr-flow docs: require protected post-release synchronization`.
2. Changelog title: `post-release-pr-flow docs: require protected post-release synchronization`.

## Validation plan

| ID | Command or review | Expected result |
|---|---|---|
| `V-001` | `git diff --check -- docs/release-branch-process.md` | Exit `0`; no whitespace errors in the runbook update. |
| `V-002` | Review the documented topic-branch instructions | They start from `release/<major>.<minor>`, retain the release group, add only empty `Unreleased`, and move development-marker surfaces to `<major>.<minor>+`. |
| `V-003` | Review the documented PowerShell comparison and `git merge-base --is-ancestor` command | Both commands compare `origin/release/<major>.<minor>` to `origin/master` after fetch; a mismatch exits nonzero. |
| `V-004` | `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | Exit `0`; current harness policy validation remains green. |

## Variance handling

Before freeze, revise this draft for feedback. After freeze, record local technical variance in `implementation-notes/variance-log.md`; amend the plan for a direct-push exception, changed protection model, automation addition, or altered acceptance criterion.

## Approval

- Status: Approved
- Superseded by: None
