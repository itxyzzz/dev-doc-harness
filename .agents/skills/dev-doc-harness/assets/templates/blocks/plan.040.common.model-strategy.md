## Model and Sub-agent Strategy

Use `module:models`, including `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, and `rule:models.fresh-confirmation`. Record only the compact strategy needed for this work item or phase.

Current orchestration:

1. Model/profile and reasoning effort if known: `<value or not exposed>`.
2. Model-policy source: `<AGENTS.md active repository policy, operator override with date, approved plan, or not exposed>`.
3. Override scope and expiry: `<work item, phase, final review, or None>`.

Fit assessment:

1. Complexity: `<low/medium/high plus reason>`.
2. Risk and blast radius: `<low/medium/high plus consequence>`.
3. Ambiguity: `<low/medium/high plus reason>`.
4. Budget and latency fit: `<acceptable constraints or tradeoff>`.

Recommended orchestration change:

1. `<None, or concrete model/profile/reasoning change with reason>`.

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
6. Model class/profile: `<policy-relative class or concrete profile if required>`.
7. Reasoning effort: `<low/medium/high plus reason>`.
8. Selection reason: `<why this delegation is useful>`.
9. Parallel execution: `<Yes/No and dependency>`.
10. Blast radius if wrong: `<Low/Medium/High plus consequence>`.
