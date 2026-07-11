## Model and Sub-agent Strategy

Use `module:models`, including `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, and `rule:models.fresh-confirmation`. Record only the compact strategy needed for this work item or phase.

Selection dimensions:

1. Model generation: `<generation or not exposed>`.
2. Capability tier: `<flagship / balanced / fast/economy>`.
3. Reasoning effort: `<runtime value or not exposed>`.
4. Orchestration mode: `<single-agent / bounded delegated sub-agents / platform multi-agent / justified hybrid>`.
5. Resolved profile: `<concrete runtime profile or not exposed>`.
6. Availability/fallback: `<availability result and approved fallback>`.
7. Execution continuity: `<same task / new task with curated-artifact handoff / justified alternative>`.
8. Context visibility: `<exposed signal or not exposed>`.
9. Artifact rehydration required: `<Yes/No plus reason>`.
10. Model-policy source: `<AGENTS.md active repository policy, operator override with date, approved plan, or not exposed>`.
11. Override scope and expiry: `<work item, phase, final review, or None>`.

Fit assessment:

1. Complexity: `<low/medium/high plus reason>`.
2. Risk and blast radius: `<low/medium/high plus consequence>`.
3. Ambiguity: `<low/medium/high plus reason>`.
4. Budget and latency fit: `<acceptable constraints or tradeoff>`.

Recommended selection change:

1. `<None, or concrete generation/tier/effort/orchestration/continuity change with reason>`.

Sub-agents:

1. `<None with rationale, or bounded strategy below>`.

Use sub-agents only when they improve isolation, review quality, parallel exploration, specialized execution, or risk reduction enough to justify the coordination cost. If the work needs many sub-agents, multiple waves, or additional planning hierarchy to stay understandable, split, re-scope, or escalate before freeze.

For each proposed sub-agent, record a short block:

Sub-agent `<role or task id>`:

1. Purpose: `<bounded task-specific purpose>`.
2. Context strategy: `<curated prompt / curated artifacts / full-history fork / no repo context>`.
3. Input context: `<files, specs, docs, diffs, decisions, or supplied text>`.
4. Output artifact: `<notes, review findings, patch scope, test list, or other deliverable>`.
5. Model policy: `<active repository policy, enterprise-default, economy-default, or operator override with source>`.
6. Model generation: `<generation or not exposed>`.
7. Capability tier: `<flagship / balanced / fast/economy>`.
8. Resolved profile: `<concrete runtime profile or not exposed>`.
9. Availability/fallback: `<availability result and approved fallback>`.
10. Reasoning effort: `<low/medium/high/max when supported plus reason>`.
11. Selection reason: `<why this delegation is useful>`.
12. Parallel execution: `<Yes/No and dependency>`.
13. Blast radius if wrong: `<Low/Medium/High plus consequence>`.
