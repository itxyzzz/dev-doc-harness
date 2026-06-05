# Sub-Agent Model Policy

This document is the canonical source for sub-agent model-selection policy in this repository.

## Common rules

Sub-agent model and reasoning-effort selection must be deliberate for substantial work. Do not treat lack of operator mention as a prohibition on sub-agent use. For substantial work, assess whether sub-agents are justified by isolation, review quality, parallel throughput, or risk reduction. Record either a bounded sub-agent strategy or `Sub-agents: None` with a brief fit reason.

Plans that propose sub-agents must specify:

- Purpose.
- Context strategy.
- Input context.
- Output artifact.
- Model policy.
- Model class or profile.
- Reasoning effort.
- Reason for selection.
- Whether the task can run in parallel.
- Blast radius if the task is wrong.

Context strategy describes how the sub-agent receives context, not just which files or artifacts it should inspect. Use deliberate, compact labels:

- `curated prompt`: a narrow task prompt with selected file paths, facts, or constraints. Prefer this for bounded explorers, reviewers, and workers when the orchestration thread can summarize the relevant context.
- `curated artifacts`: specific specs, plans, snapshots, reports, diffs, or other durable files. Prefer this when work should be grounded in approved artifacts rather than chat history.
- `full-history fork`: the conversation history is forked because prior discussion nuance is essential and hard to reconstruct. Use deliberately because it can carry stale context, increase token load, and, depending on platform behavior, force inheritance of model, reasoning, or agent type.
- `no repo context`: the sub-agent only needs supplied text or a narrow external artifact and should not inspect repository context.

Prefer curated context for bounded sub-agent work. Do not use full-history forks as a convenience default. If a task appears to need both full conversational context and a different model or reasoning profile, choose the trade-off explicitly in the plan and record why.

When known, account for the current orchestration model and reasoning effort. Judge fit against complexity, risk, ambiguity, blast radius, budget, and latency. Recommend changing the orchestration model/profile or reasoning effort when the current setup is clearly mismatched to the work.

Prefer stronger reasoning for planning, architecture, integration design, unclear debugging, security, privacy, compliance, migrations, irreversible changes, high-blast-radius changes, and final review.

Prefer lower or medium reasoning for bounded exploration, mechanical edits, local refactors, test enumeration from clear requirements, documentation cleanup, and summarization.

If an approved frozen spec, plan, phase plan, or amendment includes a sub-agent strategy, that strategy is authorized after the normal post-freeze operator authorization to begin implementation. Do not ask for another sub-agent-specific confirmation solely because the start instruction does not repeat the word `sub-agent`.

Fresh confirmation is required before applying choices not covered by the approved strategy, including unplanned sub-agents, more concurrent sub-agents than approved, a stronger model class or reasoning effort that was not recorded, write-capable work where only read-only work was approved, or more than 3 concurrent sub-agents.

If platform or runtime policy restricts sub-agent spawning or model/reasoning overrides, still document the intended strategy and ask for explicit operator confirmation before applying any restricted action.

Use sub-agents for isolation, review quality, or parallelism: independent investigation, read-heavy exploration, test-risk review, spec review, code-quality review, or bounded implementation with disjoint file ownership. Avoid sub-agents for small tasks, tightly coupled work, same-file edits by multiple agents, immediate main-thread blockers, or cases where coordination overhead exceeds the value.

Sub-agents are not a default cost-saving mechanism. Prefer read-only explorer or reviewer agents before write-capable workers.

Default concurrent fan-out:

- Small task: 0 sub-agents.
- Moderate uncertainty: 1 read-only explorer or reviewer.
- Clearly independent substantial work: 2-3 concurrent sub-agents.
- More than 3 concurrent sub-agents: requires explicit extraordinary justification and operator approval.

The normal cap is 3 concurrent sub-agents. This is a concurrency guardrail, not a total-lifetime cap. Long-running orchestrations may use more than 3 total sub-agents in separate waves when the approved plan supports those waves and no more than 3 sub-agents are active at once.

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

Large or phased work item specs or phase plans using sub-agents must include a compact Model and Sub-agent Strategy:

```md
## Model and Sub-agent Strategy

Current orchestration: `<model/profile if known>`, `<reasoning effort if known>`
Fit assessment: `<complexity/risk/ambiguity/blast-radius/budget/latency judgment>`
Recommended change: `<none or concrete model/reasoning change with reason>`

| Phase | Purpose | Context strategy | Input context | Output artifact | Model policy | Model class/profile | Reasoning effort | Reason | Parallel? | Blast radius if wrong |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | Repository or API discovery | curated prompt | Relevant files, docs, specs, and decisions | Discovery notes | economy-default | smaller/faster | medium | Bounded exploration | Yes | Low plus consequence |
| 02 | Data model design review | curated artifacts | Spec decisions, schemas, migrations, and API contracts | Review memo | economy-default | latest strongest | high | High blast radius | Yes/No | High plus consequence |
| 03 | Test plan generation | curated artifacts | Requirements, acceptance criteria, and known risks | Test cases | economy-default | standard | medium | Clear inputs | Yes | Medium plus consequence |
| 04 | Final implementation review | curated prompt | Completed changes, validation evidence, and variance log | Review findings | economy-default | latest strongest | high | Subtle integration risk | No | High plus consequence |
```

The rows above are examples, not required phase names or required sub-agent choices. Replace them with the actual sub-agent tasks for the work item. Omit the table when no sub-agents are proposed.

Prefer policy-relative model classes over hardcoded model names unless the environment requires concrete names.

## Sub-agent report requirements

Every sub-agent report must include:

- Assigned scope.
- Files inspected or changed.
- Commands and tests run.
- Assumptions.
- Uncertainty or residual risk.
- Recommended next step.

The orchestration thread's implementation completion report must also include de-facto sub-agent use when sub-agents were authorized or used:

- Total sub-agents used.
- Roles or scopes handled.
- Whether they ran concurrently or in waves.
- Context strategy actually used for each sub-agent, including whether full-history fork was used.
- The de-facto model, model class, or profile used for each sub-agent when the platform exposes it.
- Observed context/model inheritance behavior when known, such as full-history fork forcing inherited model, reasoning, or agent type.
- An explicit note when exact model details are unavailable, with the planned policy-relative class or observed profile information instead.

## Escalation rules

Escalate model strength or reasoning effort when:

- A cheaper attempt fails or produces uncertain output.
- Requirements remain ambiguous after exploration.
- The task affects public APIs, data models, migrations, security, privacy, compliance, or irreversible operations.
- The output will become the basis for implementation by other agents.
- The work is a final high-risk review.

Record escalation rationale in the spec, phase plan, or review notes.

Using the latest strongest model class for a sub-agent, upgrading model strength, or increasing reasoning effort requires a written reason. Escalate after failure or uncertainty with that reason recorded.

## Final review

Final review of high-blast-radius work must be done by the orchestration thread or a latest strongest model class with high reasoning. Bounded low-risk work may use the orchestration thread without sub-agents.

## Final integration ownership

The orchestration thread owns final decomposition, file or module ownership boundaries, final integration, conflict resolution, final validation, and the user-facing summary. Sub-agents may advise or implement bounded scopes, but they do not own final integration judgment.
