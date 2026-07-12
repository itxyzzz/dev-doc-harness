## Next-task handoff

Use `rule:lifecycle.planning-shape`, `rule:models.execution-continuity`, `rule:freeze.approval-freeze`, and `rule:execution-quality.execution-thread-start`. Render this section only for the actual frozen plan, phase-plan, or amendment boundary.

1. Planning shape: `<combined small/medium plan / phase plan / amendment>`.
2. Frozen package: `<approved spec, applicable plan or phase plan, required snapshots, applicable amendments, required evidence, and other plan-named inputs>`.
3. Next activity: `<documented implementation, review, resumed-execution, or replanning activity>`.
4. Execution continuity: `<same task / new task with curated-artifact handoff / justified alternative>`.
5. Context visibility: `<exposed signal or not exposed>`.
6. Artifact rehydration required: `<Yes/No plus reason>`.
7. Exact authoritative artifacts: `<approved spec, plan or phase plan, architecture snapshot, amendments, and required evidence paths>`.
8. Approved strategy and fallback: `<section or artifact reference>`.
9. First activity: `<named task or review action>`.
10. Variance stop condition: `<approval-required variance or other explicit stop>`.

For `new task with curated-artifact handoff`, display a copy-ready prompt as a primary conversation result after freeze. The prompt names the exact artifacts above, applicable `AGENTS.md` and harness rules, `rule:execution-quality.execution-thread-start`, the approved strategy and fallback, the First activity, and the variance stop condition without duplicating frozen requirements.

Display the proposed model generation, resolved profile when exposed, capability tier, reasoning effort, orchestration mode, and fallback. When the platform exposes compatible task creation, ask for explicit approval to create the task, then use only the exact supported recorded model and reasoning configuration after approval. When task creation or the recorded configuration is unavailable, state the limitation and provide the same manual copy-ready handoff; do not silently substitute settings. Keep the `same task` and justified-alternative routes separate as defined by `rule:freeze.approval-freeze`.
