## Spec readiness checklist

- [ ] Goal, source and intent, scope, constraints, architecture decisions, commitment statements, and verifications are mutually consistent.
- [ ] All relevant operator input is preserved in this specification or through `module:evidence` and `rule:evidence.preservation`.
- [ ] Commitment statements are atomic, bounded, and form a complete set that covers the full scope and achieves the goal; no obligation exists only in rationale or examples.
- [ ] Verification Criteria cover all applicable Commitments, have no hidden procedure or scope, and identify cross-phase ownership where applicable.
- [ ] This specification file with `snapshots/architecture.snapshot.md` is self-contained enough that a fresh session can draft each actionable phase plan without reconstructing original session context.
- [ ] Phase decomposition explains why each phase belongs, identifies its future phase-plan output, and keeps each phase within one orchestration session or records the escalation boundary.
- [ ] The Next-stage recommendation records the required lifecycle, orchestration, model, fallback, and stage-specific sub-agent decisions; optional current-session diagnostics are omitted unless material, and the recommendation is relabeled `Approved next stage` at freeze.
- [ ] Impact Surfaces, triage/debugging/operations, risks, documentation obligations, planned commits, and any batch-planning exception have been assessed.
- [ ] No unresolved placeholders, plan-affecting decisions, missing sections, or ownerless deferrals remain.

## Approval

- Status: Draft
- Superseded by: None
