## Phase decomposition

Use actual phases for this work item. The output filenames below are future phase-plan outputs, not files to create during the anchor-spec planning package unless combined planning was explicitly requested.

Phase `01`: `<phase name>`

1. Objective: `<mid-level objective that advances the full-work-item goal>`.
2. Scope: `<covered areas or decisions>`.
3. Depends on: `<None, prior phase, external event, or approved amendment>`.
4. Future phase-plan output: `<phase-plan-filename>`.
5. Conformance focus: `<VER ids, owning phase, or phase-specific evidence signal>`.

Phase `02`: `<phase name>`

1. Objective: `<mid-level objective that advances the full-work-item goal>`.
2. Scope: `<covered areas or decisions>`.
3. Depends on: `<phase ids, artifacts, or external events>`.
4. Future phase-plan output: `<phase-plan-filename>`.
5. Conformance focus: `<VER ids, owning phase, or phase-specific evidence signal>`.

Phase decomposition prompts:

1. Each phase should be safely executable by one orchestration thread with bounded delegation.
2. Shared setup, discovery, migrations, hardening, and review phases are acceptable when vertical slicing would make task execution less safe.
3. If phase objectives are independently plannable, later phase-plan drafting may use curated-artifact sub-agents under `module:models`.

## Model and Sub-agent Strategy

Use `module:models`, including `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, and `rule:models.fresh-confirmation`. Record only the compact strategy needed for this large/phased work item.

### Current planning Codex task

1. Model generation: `<generation or not exposed>`.
2. Resolved profile: `<concrete runtime profile or not exposed>`.
3. Reasoning effort: `<runtime value or not exposed>`.
4. Context visibility: `<exposed signal or not exposed>`.

### Next-stage recommendation

#### Activity

Next activity: `<phase-plan drafting>`; First Plan Task: `<not applicable until a phase plan>`.

#### Orchestration

Method: `<recommended method>`; Run in: `<same Codex task / new Codex task>`; Plan Task reviewers: `<recommended route-specific arrangement and final reviewer>`.

#### Model

Model: `<policy-relative recommendation>`; Reasoning: `<recommended effort>`.

#### Fallbacks and limits

`<availability fallback, required artifact loading, authorization state, and material-variance stop only when applicable>`.

Fit assessment:

1. Complexity: `<low/medium/high plus reason>`.
2. Risk and blast radius: `<low/medium/high plus consequence>`.
3. Ambiguity: `<low/medium/high plus reason>`.
4. Budget and latency fit: `<acceptable constraints or tradeoff>`.

The anchor records a recommendation/default envelope only. Each later phase plan records its concrete approved next stage from that envelope or an approved amendment.

Upcoming-stage sub-agent assessment:

1. Sub-agents: None, or `<bounded strategy below>`.
2. Fit reason: `<stage-specific reason delegation would not help, or why it is useful>`.
3. Authorization state: `<Not needed / Pending operator approval / Approved>`.
4. If useful and unapproved, ask the operator to approve the recorded role, context, output, model/effort envelope, write authority, concurrency, and fallback before dispatch.

Prefer curated-artifact sub-agent phase-plan drafting after anchor-spec freeze when phases are independently plannable and platform support is available. For each proposed role, record a short block:

Sub-agent `<role or phase id>`:

1. Purpose: `<bounded explorer, reviewer, phase-plan drafter, or worker task>`.
2. Context strategy: `<curated prompt / curated artifacts / full-history fork / no repo context>`.
3. Input context: `<approved spec, amendments, prior phase outputs, files, docs, or decisions>`.
4. Output artifact: `<phase plan, notes, review findings, patch scope, test list, or other deliverable>`.
5. Model policy: `<active repository policy, enterprise-default, economy-default, or operator override with source>`.
6. Model generation: `<generation or not exposed>`.
7. Capability tier: `<flagship / balanced / fast/economy>`.
8. Resolved profile: `<concrete runtime profile or not exposed>`.
9. Availability/fallback: `<availability result and approved fallback>`.
10. Reasoning effort: `<low/medium/high/max when supported plus reason>`.
11. Selection reason: `<why this delegation is useful>`.
12. Parallel execution: `<Yes/No and dependency>`.
13. Blast radius if wrong: `<Low/Medium/High plus consequence>`.
