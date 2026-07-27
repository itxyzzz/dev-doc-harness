## Implementation handoff

Render this section at the plan's real frozen boundary. The combined
small/medium plan owns this handoff.

## Current planning Codex task

Keep observed model/profile, reasoning, and context facts separate from the frozen result.

## Next-stage recommendation

Before freeze, use the four groups: **Activity** (next activity and First Plan Task), **Orchestration** (Method, Run in: `<same Codex task / new Codex task>`, and Plan Task reviewers), **Model** (Model and Reasoning), and **Fallbacks and limits** (only applicable limits).

## Approved next stage

At the real frozen boundary, repeat the selected values in those same groups and mirror them in chat.

1. Frozen package: `<approved spec, plan, snapshots, amendments, and required evidence>`.
2. Next activity: `<named implementation activity>`.
3. First Plan Task: `<TASK-NNN>`.
4. Method, Run in, Plan Task reviewers, Model, Reasoning, and applicable fallback: `<selected grouped values>`.
5. Artifact rehydration: `<required artifacts and startup rule>`.
6. Variance stop condition: `<approval-required variance or other explicit stop>`.
7. Upcoming-stage sub-agent assessment: `Sub-agents: None` with a fit reason, or an approved bounded strategy.

Use `rule:execution-quality.execution-thread-start`; do not duplicate a
spec-owned handoff or infer a different transition.
