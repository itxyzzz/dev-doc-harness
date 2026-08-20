## 2026-07-29 docs: worktree-continuity-rules -- clarify new-task worktree baselines

Release target: `unreleased`
Package impact: `distributable`
Release-note: `include`

#### Changed

- Reworked the freeze-gate continuity guidance into separate new-task and
  same-task rules while preserving the existing authorization and fallback
  safeguards.
- Required each new task to select and report its Git starting state, disclose
  copied uncommitted paths, and avoid the implicit default-branch fallback.
- Added policy-test coverage for the readable continuity section and the
  starting-state safeguards.
