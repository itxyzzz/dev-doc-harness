## Spec readiness checklist

- [ ] Source input and desired outcome are captured.
- [ ] Scope, non-scope, assumptions, open questions, and known unknowns are explicit.
- [ ] Specification Commitments are atomic, bounded, and contain every implementation obligation in their Statements.
- [ ] Verification Criteria have valid Covers sets, expected evidence, deterministic local/cross-cutting placement, and explicit cross-phase ownership.
- [ ] Repository evidence and compatibility constraints are recorded.
- [ ] Interfaces, data, control flow, operations, and safety/privacy/migration impacts are checked.
- [ ] Risks and rejected alternatives are listed or explicitly absent after review.
- [ ] Phase decomposition explains why each phase belongs and what future phase-plan output will hold it.
- [ ] Each phase is expected to fit one orchestration session with bounded delegation, or the spec explains the escalation boundary.
- [ ] Optional current-session diagnostics contain only Resolved model profile and Context visibility and are omitted unless exposed and material; the Next-stage recommendation includes Method, Orchestration mode, `Run in`, Review, Generation, Capability tier, and Reasoning; each upcoming stage records `Sub-agents: None` with a fit reason or an authorized bounded strategy.
- [ ] Documentation artifact matrix decisions have paths or reasons.
- [ ] Planned implementation commit subjects are clear and any batch phase-planning exception is stable and independently plannable; planning approval has no changelog entry.
- [ ] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain before approval or handoff.

## Approval

- Status: Draft
- Superseded by: None
