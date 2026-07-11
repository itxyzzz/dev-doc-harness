## Next-task handoff

Use `rule:models.execution-continuity` and `rule:execution-quality.execution-thread-start`. Keep the handoff minimal and refer to authoritative artifacts instead of summarizing their requirements.

1. Execution continuity: `<same task / new task with curated-artifact handoff / justified alternative>`.
2. Context visibility: `<exposed signal or not exposed>`.
3. Artifact rehydration required: `<Yes/No plus reason>`.
4. Exact authoritative artifacts: `<approved spec, plan or phase plan, architecture snapshot, amendments, and required evidence paths>`.
5. Approved strategy and fallback: `<section or artifact reference>`.
6. First activity: `<named task, phase-planning step, or review action>`.
7. Variance stop condition: `<approval-required variance or other explicit stop>`.

When execution continuity selects a new task or a different model/profile, include a copy-ready prompt that names the exact artifacts above, requires applicable `AGENTS.md` and harness rules, cites `rule:execution-quality.execution-thread-start`, refers to the approved strategy and fallback, starts at the first activity, and stops for approval-required variance. Do not duplicate the frozen requirements in the prompt.
