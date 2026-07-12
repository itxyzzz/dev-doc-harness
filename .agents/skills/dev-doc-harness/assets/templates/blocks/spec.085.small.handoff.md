## Next-task handoff

Use `rule:lifecycle.planning-shape`, `rule:models.execution-continuity`, `rule:freeze.approval-freeze`, and `rule:execution-quality.execution-thread-start`.

Default combined package:

1. Planning shape: `combined small/medium`.
2. Frozen package: `<approved spec and plan plus required snapshots, amendments, evidence, and other plan-named inputs>`.
3. Next activity: `<implementation activity named by the approved plan>`.
4. Execution continuity: `<same task / new task with curated-artifact handoff / justified alternative>`.
5. Context visibility: `<exposed signal or not exposed>`.
6. Artifact rehydration required: `<Yes/No plus reason>`.
7. Exact authoritative artifacts: `<approved spec, plan or phase plan, architecture snapshot, amendments, and required evidence paths>`.
8. Approved strategy and fallback: `<section or artifact reference>`.
9. First activity: `<named task or review action from the plan>`.
10. Variance stop condition: `<approval-required variance or other explicit stop>`.

The combined small/medium spec does not emit an independent plan-drafting handoff or task-creation offer. Its plan owns the transition after the combined package freezes.

If the operator explicitly approves a staged small/medium spec-only exception before freeze, replace the default values with the recorded reason, identify the spec-only frozen package, and set plan drafting as the Next activity. Only that actual frozen boundary may emit the conditional copy-ready prompt described by `rule:freeze.approval-freeze`.
