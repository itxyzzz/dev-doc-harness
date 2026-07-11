# Protected Post-Release Synchronization Test Cases

Work ID: `2026-07-11_post-release-pr-flow`
Status: Approved
Harness release: `0.5+`

## `TC-001` Post-release branch uses the release baseline

Given a pushed `release/<major>.<minor>` branch, when the runbook creates the post-release topic branch, then the documented branch command uses that release branch as its start point and never uses stale `origin/master` as the baseline.

## `TC-002` Protected PR is required

Given the post-release topic branch contains the empty `Unreleased` heading and `<major>.<minor>+` marker, when the runbook promotes it, then it instructs a PR to `master` and contains no direct push to `master`.

## `TC-003` Release segment check detects divergence

Given `origin/master` does not contain the release branch state, when the documented ancestry or normalized changelog comparison runs, then it exits nonzero and the runbook directs the operator to stop before creating a new development branch.

## `TC-004` Release segment check accepts the merged state

Given the post-release PR has merged without modifying the released section, when the documented remote checks run after `git fetch --prune origin`, then the ancestry check and normalized segment comparison both exit `0`.
