# Sub-Agent Context Strategy Spec

Work ID: `2026-06-05-subagent-context-strategy`
Short ID: `subagent-context-strategy`
Status: Approved

## Goal

Make sub-agent context shaping a deliberate part of the harness model and sub-agent strategy, rather than an incidental tool parameter.

The operator-visible outcome is that future specs and plans should say how each sub-agent receives context, including whether it uses a curated prompt, selected artifacts, a full-history fork, or another explicit context shape. Implementation completion reports should also say which context strategy was actually used.

## Scope

- Add a `Context strategy` column to the `## Model and Sub-agent Strategy` tables in the canonical policy and reusable templates.
- Define expected context strategy values and guidance, including curated prompt, curated artifacts, full-history fork, and no repo context.
- Clarify that full-history forks are powerful and should be deliberate because they may include stale or broad chat context, increase token load, and inherit or constrain model/reasoning choices on some platforms.
- Require plans to explain why the chosen context strategy fits the sub-agent role, risk, input needs, and model/reasoning constraints.
- Extend sub-agent and orchestration completion reporting so agents report the de-facto context strategy used, including whether full-history fork was used and whether it affected model/reasoning inheritance.
- Align the small/medium plan template, large/phased spec template, large/phased phase-plan template, optional role examples if applicable, README, and changelog.

## Non-scope

- No change to the existing approved-plan authorization rule for sub-agent use.
- No change to the 3-concurrent-sub-agent guardrail or wave-based long-running allowance.
- No change to the active repository model policy of `economy-default`.
- No platform-specific enforcement of `fork_context` or other sub-agent tool parameters.
- No runtime code, API, schema, persistence, CLI, or automation changes.

## Current state

The current policy requires Model and Sub-agent Strategy tables to record purpose, input context, output artifact, model policy, model class/profile, reasoning effort, reason, parallelism, and blast radius. It does not require plans to record how the sub-agent's context is shaped.

The recent implementation added proactive sub-agent assessment, approved-plan authorization, a 3-concurrent-sub-agent cap, wave allowance, and de-facto sub-agent/model reporting. During that implementation, an attempted full-history fork exposed an important platform behavior: when full-history fork is used, the sub-agent tool may force inherited agent type, model, and reasoning settings. That context decision can therefore affect both quality and model/reasoning control.

## Proposed behavior

Every Model and Sub-agent Strategy table that proposes sub-agents should include a `Context strategy` column. Plans should use the column to specify how the sub-agent receives context, not just what files it should inspect.

Recommended context strategy vocabulary:

- `curated prompt`: use a narrow task prompt plus selected file paths or facts. Prefer this for bounded reviewers, explorers, and simple workers where the orchestration thread can summarize the relevant context.
- `curated artifacts`: pass or point to specific specs, plans, snapshots, reports, diffs, or other durable files. Prefer this when the work should be grounded in approved artifacts rather than chat history.
- `full-history fork`: fork the conversation history when prior discussion nuance is essential and hard to reconstruct. Use deliberately because it can carry stale context, increase token load, and, depending on platform behavior, force inheritance of model, reasoning, or agent type.
- `no repo context`: use when the sub-agent only needs supplied text or a narrow external artifact and should not inspect the repository.

The policy should prefer curated context for bounded sub-agent work. Full-history forks should not be the convenience default. If a task appears to need both full conversational context and a different model/reasoning profile, the plan should explicitly choose the trade-off and record why.

At implementation completion, de-facto reporting should include the context strategy actually used for each sub-agent. If the platform exposed inheritance behavior, such as full-history fork forcing inherited model/reasoning settings, the agent should report that. If exact details are unavailable, the agent should say so.

## Interfaces and data

Affected repository interfaces are documentation-facing:

- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
- `.agents/skills/dev-doc-harness/references/subagent-role-examples.md`
- `README.md`
- `CHANGELOG.md`

No public API, runtime config, schemas, persistence, CLI flags, or generated data formats are affected.

## Risks

- If the column is too vague, agents may fill it mechanically without making a real context decision.
- If full-history fork language is too permissive, agents may overuse it and import stale context or unnecessary token load.
- If full-history fork language is too restrictive, agents may lose nuanced operator intent that matters for high-context work.
- If templates are not aligned, future plans may keep omitting context strategy even after the canonical policy is updated.
- Platform behavior around context fork, model inheritance, or exact model visibility may vary.

## Acceptance criteria

- `subagent-model-policy.md` adds `Context strategy` to the required sub-agent strategy fields and table example.
- `subagent-model-policy.md` defines context strategies and guidance for curated prompt, curated artifacts, full-history fork, and no repo context.
- `subagent-model-policy.md` states that full-history fork should be deliberate and may force inherited model/reasoning/agent-type behavior depending on platform.
- The small/medium plan template, large/phased spec template, and large/phased phase-plan template include `Context strategy` in their Model and Sub-agent Strategy tables.
- Sub-agent role examples are updated when their portable role shape would otherwise omit context strategy.
- Completion reporting expectations include de-facto context strategy used and any observed context/model inheritance behavior.
- README operator-facing text explains that context strategy is part of sub-agent planning.
- `CHANGELOG.md` receives a newest-first entry before the implementation commit.

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Required for the approval planning commit and final implementation commit |
| Test cases | Snapshot | No | Not applicable | snapshots/test-cases.snapshot.md | Documentation/process wording change only |
| Testing guide delta | Living delta | No | Not applicable | deltas/testing-guide.delta.md | No test workflow change |
| Operator manual delta | Living delta | No | Not applicable | deltas/operator-manual.delta.md | README and harness references are the operator-facing docs for this repo |
| API reference delta | Living delta | No | Not applicable | deltas/api-reference.delta.md | No API change |
| Architecture snapshot | Snapshot | No | Not applicable | snapshots/architecture.snapshot.md | No architecture change |
| Architecture summary delta | Living delta | No | Not applicable | deltas/architecture-summary.delta.md | No long-lived architecture summary change |

## Approval

- Status: Approved
- Superseded by: None
