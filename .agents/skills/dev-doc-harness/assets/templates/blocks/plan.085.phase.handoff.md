## Phase transitions

Render these transitions at the phase plan's real frozen boundary.
The normal route is rolling: implement this phase, record actual outputs, then
plan the next phase. Batch planning is an explicit exception only for stable,
independently plannable phases.

### Current-phase implementation handoff

1. Frozen package: `<approved anchor, phase plan, amendments, prior outputs, and required evidence>`.
2. Next activity: `<named current-phase implementation>`.
3. First task: `<TASK-NNN>`.
4. Approved execution selection and fallback: `<selection section or concise values>`.
5. Variance stop condition: `<approval-required variance or other explicit stop>`.

### Post-phase transition

1. Expected next activity: `<next-phase planning or work-item completion>`.
2. Required actual outputs: `<outputs, validation, variance, commit state, and inputs for the next activity>`.
3. The completion report supplies the actual values; it does not begin the next activity automatically.
4. Upcoming-stage sub-agent assessment: `Sub-agents: None` with a fit reason, or an approved bounded strategy.
