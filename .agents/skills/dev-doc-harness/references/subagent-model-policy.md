# Sub-Agent Model Policy

This document is the canonical source for sub-agent model-selection policy in this repository.

## Common rules

Sub-agent model and reasoning-effort selection must be deliberate for substantial work. Plans that propose sub-agents must specify:

- Purpose.
- Input context.
- Output artifact.
- Model policy.
- Model class or profile.
- Reasoning effort.
- Reason for selection.
- Whether the task can run in parallel.
- Blast radius if the task is wrong.

Prefer stronger reasoning for planning, architecture, integration design, unclear debugging, security, privacy, compliance, migrations, irreversible changes, high-blast-radius changes, and final review.

Prefer lower or medium reasoning for bounded exploration, mechanical edits, local refactors, test enumeration from clear requirements, documentation cleanup, and summarization.

## Policy: enterprise-default

Cost minimization is not the primary optimization factor.

Optimize for:

1. Correctness.
2. Risk reduction.
3. Context isolation.
4. Parallel throughput.
5. Review quality.
6. Efficient main-thread use.

Use the latest strongest available model class for architecture, security, compliance, schema or persistence changes, complex debugging, high-blast-radius implementation, and final review.

Use a latest smaller or faster model class only for narrow search, summarization, mechanical file inspection, simple documentation extraction, and other bounded low-risk work.

Do not fall back to older or cheaper models solely to save cost.

## Policy: economy-default

Cost and usage limits are active optimization factors.

Default to next-to-latest or smaller faster model classes for bounded tasks when risk is low and the task has clear inputs and outputs.

Escalate to the latest strongest available model class for unclear requirements, architecture decisions, subtle debugging, high-risk reviews, security, privacy, compliance, migrations, public APIs, persistence changes, and failures after one cheaper attempt.

Use cheaper or smaller model classes for initial repository exploration, summarization, mechanical edits, simple test scaffolding, documentation formatting, and low-risk refactors with strong tests.

A cheaper sub-agent must not be the final authority for high-blast-radius decisions.

## Required notation

Large-feature specs or phase plans using sub-agents must include:

```md
## Sub-agent orchestration

| Phase | Sub-agent task | Model policy | Model class | Effort | Reason | Output |
|---|---|---|---|---|---|---|
| 01 | Repository or API discovery | economy-default | smaller/faster | medium | Bounded exploration | Discovery notes |
| 02 | Data model design review | economy-default | latest strongest | high | High blast radius | Review memo |
| 03 | Test plan generation | economy-default | standard | medium | Clear inputs | Test cases |
| 04 | Final implementation review | economy-default | latest strongest | high | Subtle integration risk | Review findings |
```

The rows above are examples, not required phase names or required sub-agent choices. Replace them with the actual sub-agent tasks for the feature. Omit the table when no sub-agents are proposed.

Prefer policy-relative model classes over hardcoded model names unless the environment requires concrete names.

## Escalation rules

Escalate model strength or reasoning effort when:

- A cheaper attempt fails or produces uncertain output.
- Requirements remain ambiguous after exploration.
- The task affects public APIs, data models, migrations, security, privacy, compliance, or irreversible operations.
- The output will become the basis for implementation by other agents.
- The work is a final high-risk review.

Record escalation rationale in the spec, phase plan, or review notes.

## Final review

Final review of high-blast-radius work must be done by the orchestration thread or a latest strongest model class with high reasoning. Bounded low-risk work may use the orchestration thread without sub-agents.
