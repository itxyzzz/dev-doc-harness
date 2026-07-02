## Plan readiness checklist

- [ ] Input artifacts and relevant repository context have been read and listed.
- [ ] Every spec requirement and acceptance criterion has at least one task and one validation path.
- [ ] Risks, scope boundaries, interfaces, and documentation decisions are either covered by tasks or explicitly marked as no-op with a reason.
- [ ] Task detail is sufficient for a fresh implementation agent or delegated sub-agent to execute its assigned part without inventing task order, file scope, validation, or documentation steps.
- [ ] Validation entries have exact commands, manual checks, review findings, or operator acceptance paths with expected signals.
- [ ] Planned commits and changelog title snippets are synchronized.
- [ ] Variance handling is clear for likely implementation drift.
- [ ] The work still fits one orchestration thread with a bounded sub-agent strategy. If it does not, split, re-scope, or escalate to large/phased handling before freeze.
- [ ] Sub-agent strategy follows `module:models`, or `Sub-agents: None` has a brief fit rationale.
- [ ] No unresolved placeholders remain before approval or handoff.

## Completion criteria

- Acceptance criteria in `<spec-filename>` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- The frozen plan had enough detail for each assigned execution part or delegated sub-agent to proceed safely.
- Execution remained within one orchestration thread with a bounded sub-agent strategy; otherwise the work was split, re-scoped, or escalated before implementation.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- Commit subjects match the approved planned subjects or recorded variance, and changelog title snippets are synchronized.
- Planned implementation changes are committed, or the completion report names the exact blocker or explicit no-commit instruction plus current worktree status.
- Variance log is present and current.
- De-facto sub-agent use is reported when applicable, including count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.

## Approval

- Status: Draft / Approved / Superseded
- Superseded by: record only when this artifact is superseded
