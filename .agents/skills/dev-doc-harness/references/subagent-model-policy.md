# Sub-Agent Model Policy

This document is the canonical source for sub-agent model-selection policy in this repository.

Module: `module:models`

Owned rule IDs:

| Rule ID | Local owner |
|---|---|
| `rule:models.strategy-required` | `## Common rules` and `## Required notation` |
| `rule:models.selection-dimensions` | `## Selection dimensions` |
| `rule:models.orchestration-mode` | `## Orchestration mode` |
| `rule:models.execution-continuity` | `## Execution continuity` |
| `rule:models.context-strategy` | `## Common rules` |
| `rule:models.approved-strategy-authorized` | `## Common rules` |
| `rule:models.fresh-confirmation` | `## Common rules` |
| `rule:models.concurrent-cap` | `## Common rules` |
| `rule:models.enterprise-default` | `## Policy: enterprise-default` |
| `rule:models.economy-default` | `## Policy: economy-default` |
| `rule:models.final-review` | `## Final review` |
| `rule:models.final-integration-ownership` | `## Final integration ownership` |

## Selection dimensions

Model selection for substantial work records independent dimensions rather than collapsing them into one model-class/profile label:

- Model generation: the provider generation or `not exposed`.
- Capability tier: the durable policy-relative tier.
- Reasoning effort: the independently selected effort or `not exposed`.
- Orchestration mode: the execution shape defined by `rule:models.orchestration-mode`.
- Resolved profile: the concrete runtime model/profile when exposed; otherwise `not exposed`.
- Availability/fallback: runtime availability plus the approved fallback if the preferred combination is unavailable or prohibited.

Permanent capability tiers are vendor-neutral:

- `flagship`: strongest available tier for architecture, subtle integration, high-blast-radius work, and final review.
- `balanced`: capable general-purpose tier for bounded implementation and review where cost and latency matter.
- `fast/economy`: fastest or lowest-cost suitable tier for mechanical and low-risk bounded work.

Concrete names are current mappings, not permanent policy vocabulary. The current GPT-5.6 mapping is Sol to `flagship`, Terra to `balanced`, and Luna to `fast/economy`. Later generations or providers may map differently without changing the tier definitions.

Reasoning effort stays independent of capability tier. Use the effort values exposed by the runtime, commonly low, medium, high, and `max` where supported. `Ultra` is not a reasoning-effort value or capability tier.

## Orchestration mode

Record one orchestration mode and a fit reason:

- `single-agent`: one orchestration thread performs implementation and integration.
- `bounded delegated sub-agents`: the harness strategy names controlled roles, context, outputs, and review boundaries.
- `platform multi-agent`: platform-managed multi-agent coordination; current GPT-5.6 `ultra` maps here.
- `hybrid`: platform multi-agent plus separately controlled harness roles, only when the runtime supports both and the plan justifies the boundary.

Platform multi-agent mode does not automatically provide harness-managed task partitioning, context strategies, per-agent model selection, file ownership, independent reports, or reviewer gates. The orchestration thread still owns validation, integration judgment, variance, and the user-facing result.

## Execution continuity

Every substantial strategy records:

- Execution continuity: `same task`, `new task with curated-artifact handoff`, or another explicit justified choice.
- Context visibility: `exposed` with the available signal, or `not exposed`.
- Artifact rehydration required: `Yes` or `No` with a reason.

Prefer `new task with curated-artifact handoff` when the main model generation, capability tier, resolved profile, or platform multi-agent profile changes. Preserve same-task continuation when the current model/profile remains suitable or when an explicit continuity reason outweighs the transition benefit.

A same-task model switch must re-read the frozen package and reconcile scope before edits, regardless of operator-requested or runtime-managed compaction. When exact remaining context is not exposed, do not claim a precise remaining context value or prescribe compaction from an inferred threshold; runtime-managed compaction remains a platform responsibility.

Emit a transition handoff only at an actual frozen package boundary. Keep it minimal: name the authoritative frozen artifacts, approved strategy and fallback, startup rule, the package's documented next activity, and variance stop condition without restating the full requirements. Lifecycle classifies the boundary and freeze-gate policy owns its operator-facing result; continuity selection must not infer a planning stage from a generic handoff heading.

## Common rules

Sub-agent model and reasoning-effort selection must be deliberate for substantial work. Do not treat lack of operator mention as a prohibition on sub-agent use. For substantial work, assess whether sub-agents are justified by isolation, review quality, parallel throughput, or risk reduction. Record either a bounded sub-agent strategy or `Sub-agents: None` with a brief fit reason.

When `module:lifecycle` uses one orchestration thread with bounded delegation as a work-sizing boundary, this module owns the related context strategy, concurrency, model-selection, authorization, and final integration mechanics.

Plans that propose sub-agents must specify:

- Purpose.
- Context strategy.
- Input context.
- Output artifact.
- Model policy.
- Model generation.
- Capability tier.
- Resolved profile when exposed.
- Availability/fallback.
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

For large or phased work, post-anchor phase-plan drafting should prefer curated-artifact sub-agent orchestration when phases are independently plannable, the approved anchor spec and amendments provide enough context, and the platform supports sub-agents. Use `rule:lifecycle.large-phase-orchestration` for phase order. Use the approved spec, approved amendments, and relevant prior phase outputs as curated artifacts. When a curated-artifact sub-agent is not used for phase-plan drafting, record the fallback reason, such as unavailable tooling, tightly coupled phases, coordination overhead, or a need for main-thread synthesis.

When known, account for the current orchestration model and reasoning effort. Judge fit against complexity, risk, ambiguity, blast radius, budget, and latency. Recommend changing the orchestration model/profile or reasoning effort when the current setup is clearly mismatched to the work.

Prefer stronger reasoning for planning, architecture, integration design, unclear debugging, security, privacy, compliance, migrations, irreversible changes, high-blast-radius changes, and final review.

Prefer lower or medium reasoning for bounded exploration, mechanical edits, local refactors, test enumeration from clear requirements, documentation cleanup, and summarization.

An approved sub-agent strategy starts with the plan's normal post-freeze
instruction. Do not ask again merely because that instruction does not repeat
`sub-agent`.

Use the approved strategy or its recorded fallback when runtime permission and
availability allow it. Ask only before a choice outside that strategy: an
unplanned sub-agent, stronger tier or effort, broader write authority, or more
concurrency. Platform rules may still require their own confirmation.

Use sub-agents for isolation, review quality, or parallelism: independent investigation, read-heavy exploration, test-risk review, spec review, code-quality review, or bounded implementation with disjoint file ownership. Avoid sub-agents for small tasks, tightly coupled work, same-file edits by multiple agents, immediate main-thread blockers, or cases where coordination overhead exceeds the value.

When Superpowers dispatches a task-specific executor or reviewer under an approved strategy, explicitly choose and record its capability tier and reasoning effort. Record model generation and resolved profile as `not exposed` unless the platform or operator exposes them; do not silently inherit an unknown session allocation. A dispatch outside the approved policy envelope, availability fallback, concurrency guardrail, write authority, or review boundary requires the existing approval path before it starts.

Sub-agents are not a default cost-saving mechanism. Prefer read-only explorer or reviewer agents before write-capable workers.

Default concurrent fan-out:

- Small task: 0 sub-agents.
- Moderate uncertainty: 1 read-only explorer or reviewer.
- Clearly independent substantial work: 2-3 concurrent sub-agents.
- More than 3 concurrent sub-agents: requires explicit extraordinary justification and operator approval.

The normal cap is 3 concurrent sub-agents. This is a concurrency guardrail, not a total-lifetime cap. Long-running orchestrations may use more than 3 total sub-agents in separate waves when the approved plan supports those waves and no more than 3 sub-agents are active at once.

## Policy: enterprise-default

Cost minimization is not the primary optimization factor.

Under `enterprise-default`, proactively assess platform multi-agent/`ultra` when complex decomposable work may benefit from parallelism, coverage, or throughput, and record why it is or is not selected.

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

Under `economy-default`, Terra medium is the suggested baseline for substantial bounded work with explicit outputs and validation. This is a current mapping to the `balanced` tier, not a permanent tier definition or a mandate; the operator retains override authority.

Use Terra high as an effort escalation when the task model remains suitable but needs fuller dependency or edge-case traversal. Use Sol medium as a tier escalation when ambiguity handling, competing interpretations, an unclear causal chain, or difficult judgment remains limiting. Reserve Sol high for an exceptional escalation with a written reason after Sol medium leaves a high-impact unresolved conflict or evidence gap.

For later-stage escalation, name the residual uncertainty or new variance that remains after the frozen artifacts or prior work. De-escalate when frozen artifacts, deterministic checks, or a fixed review lens make the remaining work bounded. Missing product input, an undecided requirement, or a plan contradiction is a variance or approval problem, not a spending trigger.

Use fast/economy allocations for initial repository exploration, summarization, mechanical edits, simple test scaffolding, documentation formatting, and low-risk refactors with strong tests.

A cheaper sub-agent must not be the final authority for high-blast-radius decisions.

## Independent review

Use an independent sub-agent reviewer by default with curated artifacts: the approved spec and plan, relevant snapshot or amendment, changed diff, validation evidence, and a short role prompt. Give the reviewer one named lens, such as requirements traceability, regression risk, security or migration, test adequacy, or adversarial counterexamples. A separate task or thread is an operator-managed fallback, not the default, until inter-task reporting in the required modality is proven.

Findings must be evidence-backed and include severity plus a reproduction or validation path. A reviewer may use more effort or a stronger allocation than a clear-plan executor when missed defects justify it; this is a suggested quality-control allocation, not a mandatory gate. The orchestration thread retains final integration ownership.

## Required notation

Substantial small/medium plans and large or phased work item specs or phase plans must include a compact Model and Sub-agent Strategy. Small/medium plans may render required sub-agent fields as bullets or card-style blocks when that is easier to read; the table below is an example shape, not a required presentation.

```md
## Model and Sub-agent Strategy

Model generation: `<generation or not exposed>`
Capability tier: `<flagship / balanced / fast/economy>`
Reasoning effort: `<runtime value or not exposed>`
Orchestration mode: `<single-agent / bounded delegated sub-agents / platform multi-agent / justified hybrid>`
Resolved profile: `<concrete runtime profile or not exposed>`
Availability/fallback: `<availability result and approved fallback>`
Execution continuity: `<same task / new task with curated-artifact handoff / justified alternative>`
Context visibility: `<exposed signal or not exposed>`
Artifact rehydration required: `<Yes/No plus reason>`
Fit assessment: `<complexity/risk/ambiguity/blast-radius/budget/latency judgment>`
Recommended change: `<none or concrete model/reasoning change with reason>`

| Phase | Purpose | Context strategy | Input context | Output artifact | Model policy | Model generation | Capability tier | Resolved profile | Reasoning effort | Reason | Parallel? | Blast radius if wrong |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 | Repository or API discovery | curated prompt | Relevant files, docs, specs, and decisions | Discovery notes | active repository policy | not exposed | fast/economy | not exposed | medium | Bounded exploration | Yes | Low plus consequence |
| 02 | Data model design review | curated artifacts | Spec decisions, schemas, migrations, and API contracts | Review memo | active repository policy | latest available | flagship | not exposed | high | High blast radius | Yes/No | High plus consequence |
| 03 | Test plan generation | curated artifacts | Specification Commitments, Verification Criteria, and known risks | Test cases | active repository policy | not exposed | balanced | not exposed | medium | Clear inputs | Yes | Medium plus consequence |
| 04 | Final implementation review | curated prompt | Completed changes, validation evidence, and variance log | Review findings | active repository policy | latest available | flagship | not exposed | high | Subtle integration risk | No | High plus consequence |
```

The rows above are examples, not required phase names or required sub-agent choices. Use actual sub-agent tasks for the work item. Omit the table when no sub-agents are proposed.

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

When the preferred execution strategy or fallback was exercised, completion also records the de-facto orchestration mode, runtime-permission result, platform-availability result, fallback use, execution continuity, context visibility, and artifact rehydration performed.

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
