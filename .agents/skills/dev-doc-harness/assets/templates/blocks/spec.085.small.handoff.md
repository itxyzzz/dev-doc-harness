## Planning shape and transition ownership

Use `rule:lifecycle.planning-shape`, `rule:models.next-stage-continuity`, `rule:freeze.approval-freeze`, and `rule:execution-quality.execution-thread-start`.

Default combined package:

1. Planning shape: `combined small/medium`.
2. Companion plan: `<plan-filename>` is drafted and presented with this spec in the same planning turn.
3. Transition owner: `<plan-filename>` owns the `plan execution` transition after the combined package freezes.
4. Next lifecycle stage: `plan execution`.

For an explicit staged spec-only exception, record the operator-requested or
operator-approved staging reason, the spec-only frozen package, and `plan drafting`
as the next lifecycle stage. Do not duplicate the later plan's implementation handoff here. Include the conditional selection below only for this explicit exception; omit it from the default combined package.

### Next-stage recommendation

Rename it `### Approved next stage` at freeze without changing its values. Do not render both headings together.

#### Next lifecycle stage

Stage: `plan drafting`.

#### Orchestration

Method: `<planning method for plan drafting>`; Orchestration mode: `<single-agent / bounded delegated sub-agents / platform multi-agent / hybrid>`; Run in: `<same orchestration session / new orchestration session>`; Review: `<planning-review arrangement>`.
Orchestration mode fit: `<why this topology fits plan drafting>`.

#### Model

Generation: `<latest available or concrete generation>`; Capability tier: `<flagship / balanced / fast/economy>`; Reasoning: `<runtime value>`.

#### Fallbacks and limits

`<availability fallback, required artifact loading, authorization state, and material-variance stop only when applicable>`.

Upcoming-stage sub-agent assessment: `Sub-agents: None` with a plan-drafting fit reason, or `<authorized bounded strategy>`.
