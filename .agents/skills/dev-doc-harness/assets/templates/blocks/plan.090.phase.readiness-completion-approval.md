## Plan readiness checklist

- [ ] Input artifacts and relevant repository context have been read and listed.
- [ ] The phase preserves the approved anchor spec, amendments, and prior phase outputs without silent reinterpretation.
- [ ] Every in-phase Specification Commitment has an authorized disposition and every applicable Verification Criterion has Plan Check coverage and one owning stage.
- [ ] Frozen later-phase commitments, risks, boundaries, interfaces, and documentation decisions retain exact authorized references or explicit no-op rationale.
- [ ] Task detail is sufficient for a fresh implementation agent or delegated sub-agent to execute its assigned part without inventing task order, file scope, validation, or documentation steps.
- [ ] Plan Checks have complete procedure, result, evidence-record, and stage/environment fields.
- [ ] Planned commits and changelog title snippets are synchronized.
- [ ] Variance handling is clear for likely implementation drift.
- [ ] This phase fits one orchestration thread with bounded delegation. If it does not, split the phase, re-scope it, or amend the anchor before freeze.
- [ ] Sub-agent strategy follows `module:models`, or `Sub-agents: None` has a brief fit rationale.
- [ ] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain before approval or handoff.

## Completion criteria

- Phase objective is met.
- Verification Criteria owned by this phase have evidence-backed status; partial evidence for later-owned criteria remains explicitly partial.
- Validation commands have been run and recorded.
- Documentation tasks are complete or explicitly deferred with reason.
- The frozen phase plan had enough detail for each assigned execution part or delegated sub-agent to proceed safely.
- Execution remained within one orchestration thread with a bounded sub-agent strategy; otherwise the phase was split, re-scoped, or amended before implementation.
- The matching `docs/work-items/<work-id>/changelog/*.md` fragment has a newest-first entry for the phase before each commit.
- Commit subjects match the approved planned subjects or recorded variance, and changelog title snippets are synchronized.
- Planned implementation changes are committed, or the completion report names the exact blocker or explicit no-commit instruction plus current worktree status.
- Variance log is present and current.
- De-facto sub-agent use is reported when applicable, including count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.

## Approval

- Status: Draft
- Superseded by: None
