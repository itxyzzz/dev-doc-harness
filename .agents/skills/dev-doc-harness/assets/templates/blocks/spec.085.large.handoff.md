## Next-task handoff

Use `rule:lifecycle.large-phase-orchestration`, `rule:models.execution-continuity`, `rule:freeze.approval-freeze`, and `rule:execution-quality.execution-thread-start`.

1. Planning shape: `large/phased anchor` unless an approved combined-planning exception says otherwise.
2. Frozen package: `<approved anchor spec plus required snapshots, amendments, evidence, and other anchor-named inputs>`.
3. Next activity: `phase-plan drafting` for `<named phase or first phase-planning activity>`.
4. Execution continuity: `<same task / new task with curated-artifact handoff / justified alternative>`.
5. Context visibility: `<exposed signal or not exposed>`.
6. Artifact rehydration required: `<Yes/No plus reason>`.
7. Exact authoritative artifacts: `<approved spec, plan or phase plan, architecture snapshot, amendments, and required evidence paths>`.
8. Approved strategy and fallback: `<section or artifact reference>`.
9. First activity: `<named phase-planning task or review action>`.
10. Variance stop condition: `<approval-required variance or other explicit stop>`.

After the anchor actually freezes, a new-task route displays a conditional copy-ready prompt for the documented phase-plan drafting activity. It names the exact artifacts above, applicable `AGENTS.md` and harness rules, `rule:execution-quality.execution-thread-start`, the approved strategy and fallback, and the variance stop condition without duplicating frozen requirements. Follow `rule:freeze.approval-freeze` for any configured task-creation offer or manual fallback.
