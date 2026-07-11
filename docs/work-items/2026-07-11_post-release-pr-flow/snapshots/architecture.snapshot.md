# Protected Post-Release Synchronization Architecture Snapshot

Work ID: `2026-07-11_post-release-pr-flow`
Status: Approved
Harness release: `0.5+`

## Decision

The release branch is the source of the immutable released state. A dedicated post-release topic branch, created from that release branch, is the only vehicle for introducing the subsequent `Unreleased` state and development marker to protected `master`. The topic branch reaches `master` solely through a pull request.

## Drivers

1. Direct pushes to `master` are disabled for security.
2. New work branches must inherit the released changelog state.
3. The process must retain GitHub review and audit controls.

## Boundaries

1. `release/<major>.<minor>`: released baseline and source branch.
2. `post-release/<major>.<minor>-start-development`: temporary PR source branch.
3. `master`: protected shared development baseline after PR merge.
4. `CHANGELOG.md`: proof-bearing release history that must preserve the released segment.

## Verification boundary

After the PR merge and a remote fetch, `origin/release/<major>.<minor>` must be an ancestor of `origin/master`, and the substring beginning at `## Release <major>.<minor>` must match between the two remote changelogs. New development branches are blocked until both checks pass.

## Rejected alternative

A direct-push bypass is rejected because GitHub bypass permissions are ongoing actor permissions rather than a narrow, one-time release-reset exception.

## Rollback

Before merge, close or supersede the PR. After merge, correct any error with a follow-up PR; do not force-push protected `master`.
