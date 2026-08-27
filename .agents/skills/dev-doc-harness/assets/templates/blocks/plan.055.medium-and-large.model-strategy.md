## Model and Sub-agent Strategy

Use `module:models`, including `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, and `rule:models.fresh-confirmation`. Record only the compact strategy needed for this work item or phase.

Upcoming-stage sub-agent assessment:

1. Sub-agents: None, or `<bounded strategy below>`.
2. Fit reason: `<stage-specific reason delegation would not help, or why it is useful>`.
3. Authorization state: `<Not needed / Pending operator approval / Approved>`.
4. A no-proactive-spawn environment rule blocks unapproved dispatch and never substitutes for this assessment or an operator-approval request.
5. When useful and unapproved, ask the operator to approve the recorded roles, context, outputs, model/effort envelope, write authority, concurrency, and fallback before dispatch.

Use sub-agents only when they improve isolation, review quality, parallel exploration, specialized execution, or risk reduction enough to justify the coordination cost. For each proposed sub-agent, record purpose, context strategy, input context, output artifact, model policy and allocation, write authority, concurrency, and blast radius. An approved in-envelope strategy does not need another generic confirmation; route an out-of-envelope dispatch through the existing operator-approval path.

For each proposed sub-agent, record a short block:

Sub-agent `<role or task id>`:

1. Purpose: `<bounded task-specific purpose>`.
2. Context strategy: `<curated prompt / curated artifacts / full-history fork / no repo context>`.
3. Input context: `<files, specs, docs, diffs, decisions, or supplied text>`.
4. Output artifact: `<notes, review findings, patch scope, test list, or other deliverable>`.
5. Active model policy: `<active repository policy, quality-first, efficiency-first, or operator override with source>`.
6. Recommended sub-agent model: Generation `<generation>`; Capability tier `<flagship / balanced / fast/economy>`; Reasoning effort `<low/medium/high/max when supported plus reason>`.
7. Resolved target profile: `<concrete runtime mapping, only when exposed and useful; otherwise omit>`.
8. Availability/fallback: `<availability result and approved fallback>`.
9. Selection reason: `<why this delegation is useful>`.
10. Parallel execution: `<Yes/No and dependency>`.
11. Blast radius if wrong: `<Low/Medium/High plus consequence>`.
12. Write authority: `<read-only / bounded paths / other approved scope>`.
13. Concurrency: `<single run / approved concurrent count and coordination boundary>`.
