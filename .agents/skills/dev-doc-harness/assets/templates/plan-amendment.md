# Plan Amendment NNN: <Short Title>

Work ID: `<work-id>`
Short ID: `<short-id>`
Status: Proposed
Harness release: `<version or unknown>`
Schema: `schema:plan.amendment`
Policy references: `module:lifecycle`, `module:naming`, `module:freeze-gate`, `module:models`, `rule:lifecycle.stage-boundaries`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:models.selection-dimensions`, `rule:models.orchestration-mode`, `rule:models.next-stage-continuity`, `rule:models.strategy-required`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Original plan reference

- Amendment ID: `AMD-001`
- File: `<plan, phase plan, spec, or snapshot path>`
- Section or task: `<heading, TASK ID, SPEC ID, VER ID, CHECK ID, or DEC ID>`
- Original instruction: `<approved text or concise summary>`

## Discovered issue

State the material change: outcome, architecture, API, data, security, privacy,
compliance, scope, or invalidated evidence.

## Proposed change

State the replacement instruction or scope adjustment.

## Impact assessment

State the affected outcome, proof, interfaces, data, risk, and documentation.

## Model and Sub-agent Strategy

Upcoming-stage sub-agent assessment:

1. Sub-agents: None, or `<bounded strategy>`.
2. Fit reason: `<stage-specific reason delegation would not help, or why it is useful>`.
3. Authorization state: `<Not needed / Pending operator approval / Approved>`.
4. When useful and unapproved, ask the operator to approve the recorded roles, context, outputs, recommended sub-agent model, write authority, concurrency, and fallback before dispatch.

Use `module:models` for any bounded role records; keep the active model policy separate from the recommended sub-agent model and include a Resolved target profile only when exposed and useful.

## Next-stage recommendation

Rename it `## Approved next stage` at freeze without changing its values. Do not render both headings together. The amendment resumes the stage documented by the frozen package it changes.

### Next lifecycle stage

Stage: `<documented resumed stage>`.

### Orchestration

Method: `<planning or execution method for Stage>`; Orchestration mode: `<single-agent / bounded delegated sub-agents / platform multi-agent / hybrid>`; Run in: `<same orchestration session / new orchestration session>`; Review: `<planning-review arrangement or execution Plan Task/final-review arrangement>`.

### Model

Generation: `<latest available or concrete generation>`; Capability tier: `<flagship / balanced / fast/economy>`; Reasoning: `<runtime value>`.

### Execution requirements and contingencies

`<required artifact rehydration, outstanding authorization, availability fallback, or material-variance stop; omit any item that does not apply>`.

## Approval

- Required: Yes
- Status: Proposed
- Approval evidence: `<operator approval message, approval commit, or None while proposed>`
- Superseded by: None

## Planned commits

Use `rule:lifecycle.commit-message-format`.

| Stage | Planned subject |
|---|---|
| Amendment approval | `<planning-commit-subject>` |
| Amended implementation | `<commit-subject>` |

Record an essential exception or independently reviewable split as concise prose below.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`. Implementation remains paused until the approved amendment is frozen.
