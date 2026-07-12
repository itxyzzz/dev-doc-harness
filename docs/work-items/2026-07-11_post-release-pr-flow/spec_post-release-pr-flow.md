# Protected Post-Release Synchronization Spec

Work ID: `2026-07-11_post-release-pr-flow`
Short ID: `post-release-pr-flow`
Status: Approved
Harness release: `0.5+`
Schema: `schema:spec.small-medium`

## Source and intent

The `0.5.0` release-preparation commit exists on `origin/release/0.5` but not on `origin/master`; a later development branch therefore inherited a changelog that still marked the released entries as unreleased. Direct pushes to `master` are prohibited by the repository's GitHub protection policy. The release runbook must make a pull request, rather than a direct push, the mandatory promotion path for the post-release development state.

## Scope

In scope:

1. Update `docs/release-branch-process.md` so the post-release development reset occurs on a topic branch created from the pushed release branch.
2. Require a pull request from that topic branch to protected `master`.
3. Require a post-merge remote verification that the release branch is an ancestor of `origin/master` and that the released changelog segment is unchanged.
4. State the blocking rule: do not create new development branches from `master` until the post-release PR is merged and the verification passes.

Out of scope:

1. Changing GitHub branch-protection, ruleset, bypass, or merge-queue configuration.
2. Creating or merging a pull request for the already released `0.5.0` state.
3. Updating package contents, release notes, or the current release version.
4. Adding new automation to GitHub Actions or the harness validator.

## Requirements

### `REQ-001` Use a protected post-release PR

The runbook must replace its direct `master` post-release-reset path with a `post-release/<major>.<minor>-start-development` topic branch created from `release/<major>.<minor>`. It must direct the operator to push that topic branch and open a pull request targeting `master` under normal GitHub protections.

### `REQ-002` Preserve the released changelog state

The topic branch must start from the release branch, retain the concrete `## Release <major>.<minor>` section and its exact metadata, add one empty `## Unreleased` group above it, and set only the listed post-release development surfaces to `<major>.<minor>+`.

### `REQ-003` Gate future development branches

Before any new development branch is created from `master`, the runbook must require fetching `origin`, checking that `origin/release/<major>.<minor>` is an ancestor of `origin/master`, and checking that the `## Release <major>.<minor>`-and-earlier changelog portion on both remotes is identical.

### `REQ-004` Specify failure handling

If the PR is unmerged, the ancestry check fails, or the released changelog segment differs, the runbook must stop and direct the operator to repair the post-release PR or resolve the divergence before branching new work.

## Acceptance criteria

### `AC-001` Protected promotion is executable

Before a release runbook implementation commit, a reviewer can follow the documented commands to create a topic branch from `release/<major>.<minor>`, push it, and open a PR to `master` without any direct push to `master`.

### `AC-002` Release metadata is preserved

The documented topic-branch reset instructions explicitly retain the release heading and exact release-target metadata while adding only the empty `Unreleased` heading and development-marker changes.

### `AC-003` Shared-base verification is observable

After the PR merges, the documented `git merge-base --is-ancestor origin/release/<major>.<minor> origin/master` command exits `0`, and the documented PowerShell comparison exits `0` only when the released changelog portions match.

### `AC-004` Divergence blocks new work

The failure-handling section explicitly says not to create a new development branch when either verification fails.

## Architecture decisions

Architecture snapshot status: Required. The protected PR is a process-control boundary between immutable release state and subsequent development state. See `snapshots/architecture.snapshot.md`.

## Interfaces, data, and control flow

Interfaces affected: The chat-triggered release-runbook procedure in `docs/release-branch-process.md`.

Data, configuration, and persistence: The documented state transition for `CHANGELOG.md`, `.agents/skills/dev-doc-harness/VERSION`, release policy, and validator expectations. No runtime data or application configuration changes.

State and control flow: `release/<version>` becomes the source of a post-release topic branch; the protected PR merges that branch into `master`; only the verified remote `master` may seed later development branches.

Safety, security, privacy, migration, and rollback: The design preserves branch protection and PR auditability. If the post-release PR is incorrect, close or supersede it before merge; after merge, use a follow-up corrective PR rather than force-pushing `master`.

## Risks and rejected alternatives

### `RISK-001` A direct-push bypass weakens the intended security boundary

Decision: Reject standing bypass access. GitHub bypass permissions are actor-scoped rather than one-time, release-scoped exceptions; the protected PR uses the existing review and audit controls.

### `RISK-002` A new branch is created before remote synchronization

Decision: Require remote ancestry and changelog-segment checks after the PR merge and before any new development branch is created.

### `RISK-003` The release group is accidentally changed during the reset

Decision: Require an exact released-portion comparison between `origin/release/<major>.<minor>` and `origin/master`.

## Planned commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `post-release-pr-flow plan: approve protected post-release synchronization` | `post-release-pr-flow plan: approve protected post-release synchronization` | Freezes this spec, plan, snapshots, and approval fragment. |
| Implementation | `post-release-pr-flow docs: require protected post-release synchronization` | `post-release-pr-flow docs: require protected post-release synchronization` | Updates the release runbook and its implementation changelog fragment. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source | Living | Yes | Before each commit | `docs/work-items/2026-07-11_post-release-pr-flow/changelog/*.md` | Planning and implementation entries use the planned title snippets. |
| Root changelog consolidation | Living | No | Not applicable | `CHANGELOG.md` | This work does not run a consolidation checkpoint. |
| Test cases | Snapshot | Yes | Before implementation | `snapshots/test-cases.snapshot.md` | Covers the documented release-flow checks. |
| Testing guide delta | Living delta | No | Not applicable | None | No automated test procedure changes are introduced. |
| Operator manual delta | Living delta | No | Not applicable | None | The runbook itself is the directly updated operator documentation. |
| API reference delta | Living delta | No | Not applicable | None | No API change. |
| Architecture snapshot | Snapshot | Yes | Before implementation | `snapshots/architecture.snapshot.md` | Records the protected-PR process boundary. |
| Architecture summary delta | Living delta | No | Not applicable | None | No repository architecture summary change. |

## Approval

- Status: Approved
- Superseded by: None
