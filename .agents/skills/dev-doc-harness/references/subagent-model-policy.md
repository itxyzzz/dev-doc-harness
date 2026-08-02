# Task Orchestration and Model Policy

This document is the canonical source for upcoming-stage orchestration, model selection, sub-agent strategy, review, reporting, and final integration policy in this repository.

Module: `module:models`

Owned rule IDs:

| Rule ID | Local owner |
|---|---|
| `rule:models.strategy-required` | `### Upcoming-stage sub-agent assessment` |
| `rule:models.selection-dimensions` | `## Upcoming-stage selection` and `### Model facets` |
| `rule:models.orchestration-mode` | `### Orchestration selection` |
| `rule:models.next-stage-continuity` | ``#### `Run in` (next-stage continuity)`` |
| `rule:models.context-strategy` | `### Sub-agent context` |
| `rule:models.approved-strategy-authorized` | `### Sub-agent authorization` |
| `rule:models.fresh-confirmation` | `### Sub-agent authorization` |
| `rule:models.concurrent-cap` | `### Sub-agent allocation` |
| `rule:models.enterprise-default` | `#### Policy: enterprise-default` |
| `rule:models.economy-default` | `#### Policy: economy-default` |
| `rule:models.execution-review-contract` | `## Execution method and reviewer contract` |
| `rule:models.final-review` | `#### Final review` |
| `rule:models.final-integration-ownership` | `#### Final integration ownership` |

## Task and session terminology

Use these compact labels whenever `task` could mean more than one thing:

- **Orchestration session:** the top-level operator-facing conversation or controller context that owns scope, integration, validation, and the user-facing result. An adapted distribution may use its platform's native product label while preserving this distinction.
- **Current orchestration session** drafts, reviews, or freezes the current package. The **next-stage orchestration session** performs its documented next lifecycle stage; they may be the same or different sessions.
- **Plan Task:** a numbered task in an approved implementation plan.
- **Agent run** or **sub-agent run:** a bounded delegated assignment; it is not a Plan Task or an orchestration session.
- **External method session:** an external workflow controller, such as a Superpowers execution session.

## Upcoming-stage selection

`rule:lifecycle.stage-boundaries` is the sole owner of the documented next lifecycle stage. This module consumes that stage and owns how it runs; it does not repeat the lifecycle transition mapping.

Upcoming-stage orchestration and model selection for substantial work is actionable and must not use `not exposed` for Method, Orchestration mode, `Run in`, Review, Generation, Capability tier, or Reasoning effort. A draft says **Next-stage recommendation**, while a frozen package says **Approved next stage**.

The next-stage summary is ordered as:

1. **Next lifecycle stage** records the next documented stage determined by `rule:lifecycle.stage-boundaries`.
2. **Orchestration** records Method, Orchestration mode, `Run in` (next-stage continuity: same or new orchestration session), and the stage-appropriate Review arrangement.
3. **Model** records the independent Generation, Capability tier, and Reasoning effort for the next orchestration session.
4. **Fallbacks and limits** record only an applicable availability fallback, required artifact loading, authorization state, or material-variance stop.

When the combined Orchestration and Model choices are non-obvious from the documented stage, selected Method, active model policy, or repository and runtime constraints, record a concise rationale in the surrounding strategy prose. This conditional rationale covers the selection as a whole; it is not another field in the Orchestration or Model groups or in required notation.

### Orchestration selection

The Orchestration group defines four fields at first use:

- **Method:** the named workflow used for the documented next lifecycle stage.
- **Orchestration mode:** the agent/controller topology used to perform that stage.
- **Run in:** next-stage continuity, recorded as `same orchestration session` or `new orchestration session`.
- **Review:** the stage-appropriate planning-review or execution Plan Task/final-review arrangement.

#### Method and orchestration mode

Method always names the workflow for the documented next lifecycle stage. Planning stages (`plan drafting` and `phase-plan drafting`) record a planning method and planning-review arrangement; they do not invoke the execution-method cascade or Plan Task reviewer contract. Execution stages (`plan execution` and `phase execution`) record an execution method and the execution-stage Plan Task and final review arrangement.

Available orchestration modes are:

- `single-agent`: one orchestration session performs the stage and owns its integrated result.
- `bounded delegated sub-agents`: the harness strategy names controlled roles, context, outputs, and review boundaries.
- `platform multi-agent`: platform-managed multi-agent coordination; current GPT-5.6 `ultra` maps here.
- `hybrid`: platform multi-agent plus separately controlled harness roles, only when the runtime supports both and the plan justifies the boundary.

Platform multi-agent mode does not automatically provide harness-managed task partitioning, context strategies, per-agent model selection, file ownership, independent reports, or reviewer gates. The orchestration session still owns validation, integration judgment, variance, and the user-facing result.

#### `Run in` (next-stage continuity)

Method does not determine next-stage continuity. `Run in` accepts only `same orchestration session` or `new orchestration session`. Prefer `new orchestration session` when the current profile or context suitability is `not exposed`, the approved profile cannot be reconciled with the current profile, or multiple Plan Tasks, validation cycles, reviewer/fix loops, or integration work make a clean context safer. Choose `same orchestration session` only when the current profile is known suitable, context risk is known suitable or immaterial, and the artifact records a concrete continuity benefit.

A new orchestration session loads the applicable instructions, harness, exact frozen package, amendments and variance, approval/baseline, documented next lifecycle stage, and variance stop before edits. A same-session route rereads the frozen package after a model switch or recorded continuity risk. Do not use numeric context thresholds, invent remaining-context estimates, or predict compaction when the runtime does not expose those signals.

Emit a transition handoff only at an actual frozen package boundary. Keep it minimal: name the authoritative frozen artifacts, approved strategy and fallback, startup rule, the package's documented next lifecycle stage, and variance stop condition without restating the full requirements. Lifecycle classifies the boundary and freeze-gate policy owns its operator-facing result; continuity selection must not infer a planning stage from a generic handoff heading.

### Review arrangement

#### Independent review

Use an independent sub-agent reviewer by default with curated artifacts: the approved spec and plan, relevant snapshot or amendment, changed diff, validation evidence, and a short role prompt. Give the reviewer one named lens, such as requirements traceability, regression risk, security or migration, test adequacy, or adversarial counterexamples. Apply the route-specific mandatory obligations in `rule:models.execution-review-contract`; a separate task or thread is an operator-managed fallback, not the default, until inter-task reporting in the required modality is proven.

Findings must be evidence-backed and include severity plus a reproduction or validation path. A reviewer may use more effort or a stronger allocation than a clear-plan executor when missed defects justify it. Isolated read-only review remains valuable even when concurrent writing would be too tightly coupled.

#### Final review

Final review of high-blast-radius work must use the independent reviewer contract in `rule:models.execution-review-contract`, subject only to that rule's documented unavailable-review or operator-declined-review disclosure and authorization exception. Bounded low-risk work may use orchestration-session self-review when the applicable route allows it.

#### Final integration ownership

The execution orchestration session owns final decomposition, file or module ownership boundaries, final integration, conflict resolution, final validation, and the user-facing summary. It consumes independent reviewer findings but is not itself independent review. Sub-agents may advise or implement bounded scopes, but they do not own final integration judgment.

## Model selection

### Model facets

The Model group selects three independent facets:

- **Generation:** the model provider's model family or version cohort, such as `latest available` or a concrete compatibility-constrained generation.
- **Capability tier:** the durable vendor-neutral class used to express task fit independently from a provider's concrete model name.
- **Reasoning effort:** the independently selected runtime effort, commonly low, medium, high, and `max` where supported.

Permanent capability tiers are:

- `flagship`: strongest available tier for architecture, subtle integration, high-blast-radius work, and final review.
- `balanced`: capable general-purpose tier for bounded implementation and review where cost and latency matter.
- `fast/economy`: fastest or lowest-cost suitable tier for mechanical and low-risk bounded work.

Concrete names are current mappings, not permanent policy vocabulary. The current GPT-5.6 mapping is Sol to `flagship`, Terra to `balanced`, and Luna to `fast/economy`. Later generations, model providers, or host runtimes may map differently without changing the tier definitions.

Reasoning effort stays independent of capability tier. Use the effort values exposed by the runtime, commonly low, medium, high, and `max` where supported. `Ultra` is not a reasoning-effort value or capability tier.

**Resolved profile** is the concrete runtime mapping of those three choices when exposed. It is not a fourth durable selection facet. Host runtimes and model providers may expose different concrete names, availability signals, and mappings without changing the three durable facets.

### Model selection policies

#### Policy: enterprise-default

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

#### Policy: economy-default

Cost and usage limits are active optimization factors.

Under `economy-default`, `balanced/medium` (Terra medium or equivalent) is the suggested baseline for substantial bounded work with explicit outputs and validation. The parenthetical profile is a current mapping, not permanent policy vocabulary or a mandate; the operator retains override authority.

Use `balanced/high` (Terra high or equivalent) as an effort escalation when the task model remains suitable but needs fuller dependency or edge-case traversal. Use `flagship/medium` (Sol medium or equivalent) as a tier escalation when ambiguity handling, competing interpretations, an unclear causal chain, or difficult judgment remains limiting. Reserve `flagship/high` (Sol high or equivalent) for an exceptional escalation with a written reason after `flagship/medium` leaves a high-impact unresolved conflict or evidence gap.

For later-stage escalation, name the residual uncertainty or new variance that remains after the frozen artifacts or prior work. De-escalate when frozen artifacts, deterministic checks, or a fixed review lens make the remaining work bounded. Missing product input, an undecided requirement, or a plan contradiction is a variance or approval problem, not a spending trigger.

Use fast/economy allocations for initial repository exploration, summarization, mechanical edits, simple test scaffolding, documentation formatting, and low-risk refactors with strong tests.

A cheaper sub-agent must not be the final authority for high-blast-radius decisions.

## Current-session diagnostics

Optional current-session diagnostics may inform the continuity choice but do not repeat the actionable next-stage selection. Omit unless exposed and material. When retained, record only:

- **Resolved model profile:** the concrete profile exposed for the current orchestration session.
- **Context visibility:** the exposed runtime context signal relevant to continuity.

Do not infer either value or use the diagnostic block as a substitute for the required upcoming-stage Orchestration and Model groups.

## Execution method and reviewer contract

Choose the execution method independently from next-stage continuity. The ordered method cascade is owned by `rule:lifecycle.superpowers-compatibility`: prefer `superpowers:subagent-driven-development`, then `superpowers:executing-plans` while Superpowers is available, then host-native execution only when Superpowers is unavailable. Apply the route-specific review contract before host-native execution proceeds. A fresh explicit operator execution-start instruction may select another available method, model/profile, reasoning effort, or continuity; record the actual selection without a plan amendment solely for that runtime choice.

Route-specific review obligations are mandatory:

- `superpowers:subagent-driven-development`: use an Independent reviewer after each Plan Task and an Independent final whole-branch reviewer. These reviews satisfy the harness review default without a duplicate workflow.
- `superpowers:executing-plans`: Preserve executing-plans checkpoints. Provide Reviewer capability disclosure: name the independent reviewer when reviewer tooling is available; otherwise state the execution controller's self-review limitation and the fallback reason.
- Host-native execution: an independent reviewer sub-agent with curated artifacts, a named lens, and evidence-backed findings is the default. The execution orchestration session owns final integration. When independent review is unavailable or the operator explicitly declines it, disclose and record the missing review, its reason, the assurance gap, and the focused self-review and validation. If the operator has not already decided, ask once whether to proceed without independent review and pause when there is no response. An explicit instruction to proceed is recorded authorization; do not request it again. For host-native execution, `Sub-agents: None` is valid only with recorded operator authorization and the disclosure record. The completion report must state whether independent review ran; if it did not, include the operator decision, limitation, and compensating self-review and validation evidence.

For Superpowers, the external method session is the execution controller's session, not necessarily the planning orchestration session. A new orchestration session may load the frozen package, invoke the selected method, and remain the controller for Plan Task and reviewer sub-agent runs.

## Using sub-agents

### Upcoming-stage sub-agent assessment

Sub-agent model and reasoning-effort selection must be deliberate for substantial work. Before each upcoming-stage spec drafting, plan or phase-plan drafting, amendment or replanning, implementation, or consequential review stage, assess whether sub-agents are justified by isolation, review quality, parallel throughput, specialized execution, or risk reduction. Record either a bounded strategy or `Sub-agents: None` with a stage-specific fit reason.

This preserves the pre-spec assessment boundary without adding a pre-spec artifact, lifecycle stage, gate, or mandatory reviewer. A durable pre-spec selection mechanism is future work.

### Sub-agent authorization

When useful delegation is not already authorized, record the roles, context, outputs, model and effort envelope, write authority, concurrency, and fallback, then explicitly ask the operator to approve that bounded strategy before dispatch. An approved in-envelope strategy does not need a repeated confirmation; approval does not override unavailable tooling, higher-priority platform limits, or an out-of-envelope role, model/effort, write scope, concurrency, or boundary.

When `module:lifecycle` uses one orchestration session with bounded delegation as a work-sizing boundary, this module owns the related context strategy, concurrency, model-selection, authorization, and final integration mechanics.

### Sub-agent context

Plans that propose sub-agents must specify:

- Purpose.
- Context strategy.
- Input context.
- Output artifact.
- Active model policy.
- Recommended sub-agent model: Generation, Capability tier, and Reasoning effort.
- Resolved target profile when a concrete runtime mapping is exposed and useful.
- Availability/fallback.
- Reason for selection.
- Write authority.
- Whether the task can run in parallel.
- Blast radius if the task is wrong.
- Concurrency.

Context strategy describes how the sub-agent receives context, not just which files or artifacts it should inspect. Use deliberate, compact labels:

- `curated prompt`: a narrow task prompt with selected file paths, facts, or constraints. Prefer this for bounded explorers, reviewers, and workers when the orchestration session can summarize the relevant context.
- `curated artifacts`: specific specs, plans, snapshots, reports, diffs, or other durable files. Prefer this when work should be grounded in approved artifacts rather than chat history.
- `full-history fork`: the conversation history is forked because prior discussion nuance is essential and hard to reconstruct. Use deliberately because it can carry stale context, increase token load, and, depending on platform behavior, force inheritance of model, reasoning, or agent type.
- `no repo context`: the sub-agent only needs supplied text or a narrow external artifact and should not inspect repository context.

Prefer curated context for bounded sub-agent work. Do not use full-history forks as a convenience default. If a task appears to need both full conversational context and a different model or reasoning profile, choose the trade-off explicitly in the plan and record why.

For large or phased work, post-anchor phase-plan drafting should prefer curated-artifact sub-agent orchestration when phases are independently plannable, the approved anchor spec and amendments provide enough context, and the platform supports sub-agents. Use `rule:lifecycle.large-phase-orchestration` for phase order. Use the approved spec, approved amendments, and relevant prior phase outputs as curated artifacts. When a curated-artifact sub-agent is not used for phase-plan drafting, record the fallback reason, such as unavailable tooling, tightly coupled phases, coordination overhead, or a need for main-thread synthesis.

### Sub-agent allocation

When exposed and material, account for the current session's Resolved model profile and Context visibility when judging continuity. For allocation, judge the recommended next-stage model against complexity, risk, ambiguity, blast radius, budget, and latency, and change its capability tier or reasoning effort when the proposed selection is clearly mismatched to the work.

Prefer stronger reasoning for planning, architecture, integration design, unclear debugging, security, privacy, compliance, migrations, irreversible changes, high-blast-radius changes, and final review.

Prefer lower or medium reasoning for bounded exploration, mechanical edits, local refactors, test enumeration from clear requirements, documentation cleanup, and summarization.

An approved sub-agent strategy starts with the plan's normal post-freeze instruction. Do not ask again merely because that instruction does not repeat `sub-agent`.

Use the approved strategy or its recorded fallback when runtime permission and availability allow it. Ask only before a choice outside that strategy: an unplanned sub-agent, stronger tier or effort, broader write authority, or more concurrency. Platform rules may still require their own confirmation.

Use sub-agents for isolation, review quality, or parallelism: independent investigation, read-heavy exploration, test-risk review, spec review, code-quality review, or bounded implementation with disjoint file ownership. Avoid concurrent write-capable workers for small tasks, tightly coupled work, same-file edits, immediate main-thread blockers, or cases where coordination overhead exceeds the value. Tightly coupled or same-file work primarily constrains concurrent write-capable workers; those conditions do not make an isolated read-only reviewer unsuitable.

When Superpowers dispatches a task-specific executor or reviewer under an approved strategy, explicitly record its recommended sub-agent model as Generation, Capability tier, and Reasoning effort together. Add a Resolved target profile only when the platform or operator exposes a useful concrete mapping; do not silently inherit an unknown session allocation. Keep this recommendation separate from the active model policy. A dispatch outside the approved policy envelope, availability fallback, concurrency guardrail, write authority, or review boundary requires the existing approval path before it starts.

Sub-agents are not a default cost-saving mechanism. Prefer read-only explorer or reviewer agents before write-capable workers.

Default concurrent fan-out:

- Small task: 0 sub-agents.
- Moderate uncertainty: 1 read-only explorer or reviewer.
- Clearly independent substantial work: 2-3 concurrent sub-agents.
- More than 3 concurrent sub-agents: requires explicit extraordinary justification and operator approval.

The normal cap is 3 concurrent sub-agents. This is a concurrency guardrail, not a total-lifetime cap. Long-running orchestrations may use more than 3 total sub-agents in separate waves when the approved plan supports those waves and no more than 3 sub-agents are active at once.

Escalate model strength or reasoning effort when a cheaper attempt fails or remains uncertain; requirements stay ambiguous after exploration; the task affects public APIs, data models, migrations, security, privacy, compliance, or irreversible operations; the output governs later implementation; or the work is a final high-risk review. Record the escalation rationale. Using the latest strongest model class for a sub-agent, upgrading model strength, or increasing reasoning effort requires a written reason.

### Runtime report requirements

Every sub-agent report must include:

- Assigned scope.
- Files inspected or changed.
- Commands and tests run.
- Assumptions.
- Uncertainty or residual risk.
- Recommended next step.

The orchestration session's implementation completion report must also include de-facto sub-agent use when sub-agents were authorized or used:

- Total sub-agents used.
- Roles or scopes handled.
- Whether they ran concurrently or in waves.
- Context strategy actually used for each sub-agent, including whether full-history fork was used.
- The de-facto model, model class, or profile used for each sub-agent when the platform exposes it.
- Observed context/model inheritance behavior when known, such as full-history fork forcing inherited model, reasoning, or agent type.
- An explicit note when exact model details are unavailable, with the planned policy-relative class or observed profile information instead.

When the preferred execution strategy or fallback was exercised, completion also records the de-facto orchestration mode, runtime-permission result, platform-availability result, fallback use, next-stage continuity, context visibility, and artifact rehydration performed.

## Required notation

Substantial small/medium plans and large or phased work item specs or phase plans must include a compact Model and Sub-agent Strategy. Small/medium plans may render required sub-agent fields as bullets or card-style blocks when that is easier to read.

For plans and phase plans, put the optional current orchestration session diagnostics once as header metadata, put the grouped next-stage summary once near the final handoff or transition, and keep the shared strategy section for the upcoming-stage sub-agent assessment and any bounded role records. The large anchor spec retains its single grouped strategy presentation. Omit current-session diagnostics unless they are exposed and material.

The following normative notation block defines the required labels and ordering. Large anchor specs render it as one section; plans and phase plans distribute the same fields between current-session diagnostics, the upcoming-stage sub-agent assessment from `rule:models.strategy-required`, and the final selection from `rule:models.selection-dimensions`.

```md
## Model and Sub-agent Strategy

### Current orchestration session diagnostics (large anchor spec; omit unless exposed and material)

Resolved model profile: `<concrete runtime profile>`
Context visibility: `<exposed material signal>`

### Next-stage recommendation (draft only, large anchor spec)

#### Next lifecycle stage

Stage: `<plan drafting / phase-plan drafting / plan execution / phase execution / documented resumed stage>`

#### Orchestration

Method: `<planning or execution method for Stage>`
Orchestration mode: `<single-agent / bounded delegated sub-agents / platform multi-agent / hybrid>`
Run in: `<same orchestration session / new orchestration session>`
Review: `<planning-review arrangement or execution Plan Task/final-review arrangement>`

#### Model

Generation: `<generation>`
Capability tier: `<flagship / balanced / fast/economy>`
Reasoning: `<runtime value>`

#### Fallbacks and limits

`<availability fallback, required artifact loading, authorization state, and material-variance stop only when applicable>`

At freeze, relabel this same block **Approved next stage**. Routine notation omits the model-policy source, override scope, expiry, and open-ended rehydration explanations.

```

Use `rule:models.selection-dimensions`, `rule:models.orchestration-mode`, `rule:models.next-stage-continuity`, and `rule:models.strategy-required` for normative meanings, and use `module:role-examples` for optional role examples.
