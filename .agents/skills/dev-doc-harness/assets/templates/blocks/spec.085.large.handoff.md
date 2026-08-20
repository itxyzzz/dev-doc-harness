## Anchor-to-phase transition

Use `rule:lifecycle.large-phase-orchestration`, `rule:models.next-stage-continuity`, and `rule:freeze.approval-freeze`.

1. Planning shape: `large/phased anchor` unless an approved combined-planning exception says otherwise.
2. Next lifecycle stage: `phase-plan drafting`.
3. The default is rolling: draft and freeze one phase plan, implement it, record actual outputs, then plan the next phase.
4. Batch planning is an explicit exception only for stable, independently plannable phases.
5. This anchor’s approved next-stage selection governs `phase-plan drafting`. Each phase plan records its own phase-execution handoff, required artifacts, and variance stop condition at its freeze boundary.
