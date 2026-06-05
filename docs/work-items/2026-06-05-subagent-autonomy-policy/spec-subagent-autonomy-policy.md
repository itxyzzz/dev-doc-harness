# Sub-Agent Autonomy Policy Spec

Work ID: `2026-06-05-subagent-autonomy-policy`
Short ID: `subagent-autonomy-policy`
Status: Approved

## Goal

Make the harness encourage justified sub-agent use without requiring the operator to explicitly mention sub-agents on every work request or reconfirm approved sub-agent choices repeatedly.

The operator-visible outcome is that agents should proactively decide whether sub-agents are justified, record the strategy in the spec or plan, and then use the approved strategy during implementation after the normal post-freeze start authorization.

## Scope

- Update the canonical sub-agent model policy so lack of operator mention is not interpreted as a prohibition on sub-agent use.
- Clarify that the agent must assess whether sub-agents are justified for substantial work and record either a bounded strategy or a reason for using none.
- Define that an approved and frozen spec or plan authorizes the listed sub-agent strategy for implementation once the operator gives the normal post-freeze authorization to begin.
- Add a normal cap of no more than 3 concurrent sub-agents unless the plan gives explicit extraordinary justification and receives explicit operator approval.
- Require implementation completion reports to include de-facto sub-agent use and the de-facto model or model class used for each sub-agent when known.
- Preserve escalation and safety rules for high-risk, restricted, or unplanned delegation choices.
- Align reusable templates and operator-facing README wording with the new approval behavior.

## Non-scope

- No change to work item sizing, artifact layout, changelog rules, variance logs, amendment flow, or immutable snapshot rules.
- No change to the active repository model policy of `economy-default`.
- No requirement to spawn sub-agents for small or tightly coupled work.
- No attempt to override platform permissions, runtime limitations, tool availability, or connector/plugin policies that govern actual sub-agent spawning.
- No runtime code, API, schema, persistence, CLI, or automation changes.

## Current state

The current sub-agent policy requires explicit operator confirmation before applying sub-agent choices:

- `references/subagent-model-policy.md` says plans proposing sub-agents or nondefault model/reasoning settings must ask for explicit operator confirmation before applying those choices.
- The small/medium plan template, large/phased spec template, and large/phased phase-plan template repeat that confirmation requirement.
- The freeze gate already asks the operator to confirm model, reasoning-effort, and sub-agent policy choices and say whether implementation should begin.

Together, these rules can be interpreted too restrictively. Agents may treat missing operator mention as a reason to record `Sub-agents: None`, even when exploration, review, or disjoint implementation work would benefit from sub-agents. After approval, agents may also ask for additional confirmations before using the sub-agent strategy that was already reviewed in the approved plan.

## Proposed behavior

The harness should teach agents that sub-agent use is a planning judgment, not a keyword the operator must provide. For substantial work, the agent should consider whether sub-agents would materially improve isolation, review quality, parallel throughput, or risk reduction. If so, the agent should propose a bounded strategy in the spec or plan using the policy notation. If not, the agent should record `Sub-agents: None` with a brief reason.

Once a spec or plan containing a sub-agent strategy is explicitly approved, frozen, and followed by the normal post-freeze operator authorization to begin implementation, the listed sub-agent strategy is authorized. The agent should use the listed sub-agents when their trigger conditions still apply and should not ask for another confirmation solely because the word `sub-agent` was not repeated in the start instruction.

The normal cap is 3 concurrent sub-agents. This cap is intended to avoid fighting platform or system-prompt limits and to provide a reasonable coordination guardrail. It is not a total-lifetime cap for long-running orchestrations. A long-running implementation may use more than 3 sub-agents in total across separate waves when the approved plan supports those waves and no more than 3 are active at once.

More than 3 concurrent sub-agents requires explicit extraordinary justification in the plan and explicit operator approval for that larger concurrent fan-out. Under normal circumstances, agents should prefer 1 read-only explorer or reviewer for moderate uncertainty, 2-3 concurrent sub-agents for clearly independent substantial work, and 0 sub-agents for small or tightly coupled work.

Fresh confirmation remains required when the agent wants to do something not covered by the approved strategy, such as spawning additional concurrent sub-agents beyond the approved concurrent count, exceeding the normal concurrent cap, using a stronger model or reasoning effort not recorded in the plan, assigning write-capable work where only read-only review was approved, or acting under a platform/runtime permission policy that requires confirmation.

At implementation completion, the agent should report de-facto sub-agent use. The report should include how many sub-agents were used, which roles or scopes they handled, whether they ran concurrently or in waves, and the de-facto model, model class, or profile used for each sub-agent when the platform exposes it. If the platform does not expose exact model details, the agent should say so and report the planned policy-relative class or observed profile information instead.

If the approved strategy becomes inappropriate during implementation, the agent should record local variance when the behavioral scope is unchanged, or create an amendment and stop for approval when the variance affects architecture, APIs, data, security, privacy, compliance, scope, acceptance criteria, or plan feasibility.

## Interfaces and data

Affected repository interfaces are documentation-facing:

- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
- `README.md`
- `CHANGELOG.md`

No public API, runtime config, schemas, persistence, CLI flags, or generated data formats are affected.

## Risks

- If the wording is too permissive, agents may spawn sub-agents for low-value or tightly coupled work and increase cost or coordination overhead.
- If the wording remains too confirmation-heavy, agents may continue defaulting silently to no sub-agents or asking for repeated permission.
- If approval semantics are unclear, agents may confuse approval of a strategy with authorization to start implementation in the same turn as the freeze gate.
- If template wording is not aligned with the canonical reference, future plans may keep reintroducing the old confirmation pattern.
- Platform limitations may still prevent actual sub-agent spawning even when the plan authorizes it.

## Acceptance criteria

- `subagent-model-policy.md` says agents should proactively assess sub-agent use for substantial work rather than requiring operator mention.
- `subagent-model-policy.md` says `Sub-agents: None` needs a brief fit reason for substantial work.
- `subagent-model-policy.md` says an approved frozen plan authorizes its listed sub-agent strategy after the normal post-freeze start authorization, without another sub-agent-specific confirmation.
- `subagent-model-policy.md` preserves explicit confirmation requirements for unplanned delegation, more than 3 concurrent sub-agents, non-recorded model/reasoning escalation, write-scope escalation, and platform-restricted actions.
- The normal cap of no more than 3 concurrent sub-agents is documented, while long-running orchestrations may use more than 3 total sub-agents in separate waves when the approved plan supports it.
- `subagent-model-policy.md` requires implementation completion reports to include de-facto sub-agent use and de-facto model/model-class details when known, with an explicit note when exact model details are unavailable.
- Plan/spec templates stop saying every proposed sub-agent strategy needs separate confirmation before applying after approval.
- README operator flow explains that approved plans can authorize justified sub-agent use, so the operator does not need to repeat sub-agent instructions every time.
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
