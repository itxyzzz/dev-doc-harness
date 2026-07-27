## Model and Sub-agent Strategy

Use `module:models`, including `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, and `rule:models.fresh-confirmation`. Record only the compact strategy needed for this work item or phase.

### Current planning Codex task

1. Model generation: `<generation or not exposed>`.
2. Resolved profile: `<concrete runtime profile or not exposed>`.
3. Reasoning effort: `<runtime value or not exposed>`.
4. Context visibility: `<exposed signal or not exposed>`.

### Next-stage recommendation

#### Activity

Next activity: `<named activity>`; First Plan Task: `<TASK-NNN or not applicable>`.

#### Orchestration

Method: `<method>`; Run in: `<same Codex task / new Codex task>`; Plan Task reviewers: `<per-Plan-Task reviewers and final reviewer, or route-specific disclosure>`.

#### Model

Model: `<actionable model or policy-relative selection instruction>`; Reasoning: `<runtime value>`.

#### Fallbacks and limits

`<availability fallback, required artifact loading, authorization state, and material-variance stop only when applicable>`.

At freeze, relabel this block **Approved next stage** without changing its values. Do not add routine model-policy source, override scope, expiry, or open-ended rehydration fields.

Upcoming-stage sub-agent assessment:

1. Sub-agents: None, or `<bounded strategy below>`.
2. Fit reason: `<stage-specific reason delegation would not help, or why it is useful>`.
3. Authorization state: `<Not needed / Pending operator approval / Approved>`.
4. When useful and unapproved, ask the operator to approve the recorded roles,
   context, outputs, model/effort envelope, write authority, concurrency, and
   fallback before dispatch.

Use sub-agents only when they improve isolation, review quality, parallel
exploration, specialized execution, or risk reduction enough to justify the
coordination cost. For each proposed sub-agent, record purpose, context
strategy, input context, output artifact, model policy and allocation, write
authority, concurrency, and blast radius. An approved in-envelope strategy does
not need another generic confirmation; route an out-of-envelope dispatch through
the existing operator-approval path.

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
