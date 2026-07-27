## Phase transitions

Render these transitions at the phase plan's real frozen boundary.
The normal route is rolling: implement this phase, record actual outputs, then
plan the next phase. Batch planning is an explicit exception only for stable,
independently plannable phases.

## Current planning Codex task

Keep observed model/profile, reasoning, and context facts separate from the frozen result.

At this phase-plan boundary, render one state heading only: use
`## Next-stage recommendation` while the phase plan is draft, then substitute
`## Approved next stage` after freeze. Never emit both. Preserve **Activity**
(next activity and First Plan Task), **Orchestration** (Method, Run in:
`<same Codex task / new Codex task>`, and Plan Task reviewers), **Model**
(Model and Reasoning), and **Fallbacks and limits** (only applicable limits);
mirror the phase's frozen selection in chat.

### Current-phase implementation handoff

1. Frozen package: `<approved anchor, phase plan, amendments, prior outputs, and required evidence>`.
2. Next activity: `<named current-phase implementation>`.
3. First Plan Task: `<TASK-NNN>`.
4. Method, Run in, Plan Task reviewers, Model, Reasoning, and applicable fallback: `<selected grouped values>`.
5. Variance stop condition: `<approval-required variance or other explicit stop>`.

### Post-phase transition

1. Expected next activity: `<next-phase planning or work-item completion>`.
2. Required actual outputs: `<outputs, validation, variance, commit state, and inputs for the next activity>`.
3. The completion report supplies the actual values; it does not begin the next activity automatically.
4. Upcoming-stage sub-agent assessment: `Sub-agents: None` with a fit reason, or an approved bounded strategy.
