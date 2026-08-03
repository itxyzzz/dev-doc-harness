## Phase implementation handoff

Finalize this handoff at the phase plan's real frozen boundary. It owns only the current phase's `phase execution` stage. The normal route is rolling: implement this phase, record actual outputs, then plan the next phase. Batch planning is an explicit exception only for stable, independently plannable phases. Batched or parallel execution follows each approved phase plan's recorded coordination boundary and does not create an automatic later transition.

### Next-stage recommendation

Rename it `### Approved next stage` at freeze without changing its values. Do not render both headings together. Mirror the phase's frozen selection in chat.

#### Next lifecycle stage

Stage: `phase execution`.

#### Orchestration

Method: `<execution method for phase execution>`; Orchestration mode: `<single-agent / bounded delegated sub-agents / platform multi-agent / hybrid>`; Run in: `<same orchestration session / new orchestration session>`; Review: `<execution Plan Task/final-review arrangement>`.

#### Model

Generation: `<latest available or concrete generation>`; Capability tier: `<flagship / balanced / fast/economy>`; Reasoning: `<runtime value>`.

#### Fallbacks and limits

`<availability fallback, required artifact loading, authorization state, and material-variance stop only when applicable>`.

### Phase-execution startup

1. Frozen package: `<approved anchor, phase plan, amendments, prior outputs, and required evidence>`.
2. Artifact rehydration: `<required artifacts and startup rule>`.
3. Variance stop condition: `<approval-required variance or other explicit stop>`.

Use `rule:execution-quality.execution-thread-start`; do not infer a later lifecycle transition from this handoff.
