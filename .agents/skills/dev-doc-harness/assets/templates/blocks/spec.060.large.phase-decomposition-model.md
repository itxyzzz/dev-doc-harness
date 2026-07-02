## Phase decomposition

Use actual phases for this work item. The output filenames below are future phase-plan outputs, not files to create during the anchor-spec planning package unless combined planning was explicitly requested.

Phase `01`: `<phase name>`

1. Objective: `<mid-level objective that advances the full-work-item goal>`.
2. Scope: `<covered areas or decisions>`.
3. Depends on: `<None, prior phase, external event, or approved amendment>`.
4. Future phase-plan output: `<phase-plan-filename>`.
5. Acceptance focus: `<AC ids or phase-specific review signal>`.

Phase `02`: `<phase name>`

1. Objective: `<mid-level objective that advances the full-work-item goal>`.
2. Scope: `<covered areas or decisions>`.
3. Depends on: `<phase ids, artifacts, or external events>`.
4. Future phase-plan output: `<phase-plan-filename>`.
5. Acceptance focus: `<AC ids or phase-specific review signal>`.

Phase decomposition prompts:

1. Each phase should be safely executable by one orchestration thread with bounded delegation.
2. Shared setup, discovery, migrations, hardening, and review phases are acceptable when vertical slicing would make task execution less safe.
3. If phase objectives are independently plannable, later phase-plan drafting may use curated-artifact sub-agents under `module:models`.

## Model and Sub-agent Strategy

Use `module:models`, including `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, and `rule:models.fresh-confirmation`. Record only the compact strategy needed for this large/phased work item.

Current orchestration:

1. Model/profile and reasoning effort if known: `<value or not exposed>`.

Fit assessment:

1. Complexity: `<low/medium/high plus reason>`.
2. Risk and blast radius: `<low/medium/high plus consequence>`.
3. Ambiguity: `<low/medium/high plus reason>`.
4. Budget and latency fit: `<acceptable constraints or tradeoff>`.

Recommended orchestration change:

1. `<None, or concrete model/profile/reasoning change with reason>`.

Sub-agents:

1. `<None with rationale, or bounded strategy below>`.

Prefer curated-artifact sub-agent phase-plan drafting after anchor-spec freeze when phases are independently plannable and platform support is available. For each proposed role, record a short block:

Sub-agent `<role or phase id>`:

1. Purpose: `<bounded explorer, reviewer, phase-plan drafter, or worker task>`.
2. Context strategy: `<curated prompt / curated artifacts / full-history fork / no repo context>`.
3. Input context: `<approved spec, amendments, prior phase outputs, files, docs, or decisions>`.
4. Output artifact: `<phase plan, notes, review findings, patch scope, test list, or other deliverable>`.
5. Model policy: `<active repository policy unless changed by operator>`.
6. Model class/profile: `<policy-relative class or concrete profile if required>`.
7. Reasoning effort: `<low/medium/high plus reason>`.
8. Selection reason: `<why this delegation is useful>`.
9. Parallel execution: `<Yes/No and dependency>`.
10. Blast radius if wrong: `<Low/Medium/High plus consequence>`.
