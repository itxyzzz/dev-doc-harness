## Anchor-to-phase transition

Use `rule:lifecycle.large-phase-orchestration`, `rule:models.next-stage-continuity`, `rule:freeze.approval-freeze`, and `rule:execution-quality.execution-thread-start`.

1. Planning shape: `large/phased anchor` unless an approved combined-planning exception says otherwise.
2. Next lifecycle stage: `phase-plan drafting`.
3. The default is rolling: draft and freeze one phase plan, implement it, record actual outputs, then plan the next phase.
4. Batch planning is an explicit exception only for stable, independently plannable phases.
5. The approved next-stage selection, artifacts, and variance stop condition are rendered at the actual phase-plan boundary under `rule:freeze.approval-freeze`.
