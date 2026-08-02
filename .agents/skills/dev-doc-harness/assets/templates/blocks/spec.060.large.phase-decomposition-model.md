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

1. Each phase should be safely executable by one orchestration session with bounded delegation.
2. Shared setup, discovery, migrations, hardening, and review phases are acceptable when vertical slicing would make task execution less safe.
3. If phase objectives are independently plannable, later phase-plan drafting may use curated-artifact sub-agents under `module:models`.

## Model and Sub-agent Strategy

Use `module:models`, including `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, and `rule:models.fresh-confirmation`. Record only the compact strategy needed for this large/phased work item.

### Current orchestration session diagnostics

Omit unless exposed and material.

1. Resolved model profile: `<concrete runtime profile>`.
2. Context visibility: `<exposed material signal>`.

### Next-stage recommendation

Rename it `### Approved next stage` at freeze without changing its values.
Do not render both headings together.

#### Next lifecycle stage

Stage: `phase-plan drafting`.

#### Orchestration

Method: `<planning method for phase-plan drafting>`; Orchestration mode: `<single-agent / bounded delegated sub-agents / platform multi-agent / hybrid>`; Run in: `<same orchestration session / new orchestration session>`; Review: `<planning-review arrangement>`.
Orchestration mode fit: `<why this topology fits phase-plan drafting>`.

#### Model

Generation: `<latest available or concrete generation>`; Capability tier: `<flagship / balanced / fast/economy>`; Reasoning: `<recommended effort>`.

#### Fallbacks and limits

`<availability fallback, required artifact loading, authorization state, and material-variance stop only when applicable>`.

Fit assessment:

1. Complexity: `<low/medium/high plus reason>`.
2. Risk and blast radius: `<low/medium/high plus consequence>`.
3. Ambiguity: `<low/medium/high plus reason>`.
4. Budget and latency fit: `<acceptable constraints or tradeoff>`.

The anchor records a recommendation/default envelope only. Each later phase plan records its concrete approved next lifecycle stage from that envelope or an approved amendment.

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
5. Active model policy: `<active repository policy, enterprise-default, economy-default, or operator override with source>`.
6. Recommended sub-agent model: Generation `<generation>`; Capability tier `<flagship / balanced / fast/economy>`; Reasoning effort `<low/medium/high/max when supported plus reason>`.
7. Resolved target profile: `<concrete runtime mapping, only when exposed and useful; otherwise omit>`.
8. Availability/fallback: `<availability result and approved fallback>`.
9. Selection reason: `<why this delegation is useful>`.
10. Parallel execution: `<Yes/No and dependency>`.
11. Blast radius if wrong: `<Low/Medium/High plus consequence>`.
12. Write authority: `<read-only / bounded paths / other approved scope>`.
13. Concurrency: `<single run / approved concurrent count and coordination boundary>`.
