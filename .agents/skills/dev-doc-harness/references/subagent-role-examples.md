# Sub-Agent Role Examples

These examples are optional patterns for specs and plans. Keep roles bounded,
policy-relative, and easy for a fresh agent to execute.

Module: `module:role-examples`

This is advisory example content. It offers optional role patterns and report
shape examples, but it does not make any sub-agent role mandatory policy.

## Common roles

Keep the active model policy separate from each recommended sub-agent model. Present that recommendation as Generation, Capability tier, and Reasoning effort together; add a Resolved target profile only when a concrete runtime mapping is exposed and useful. A bounded role below uses `bounded delegated sub-agents`; platform multi-agent/`ultra` is a different orchestration choice and does not imply these role boundaries or report gates.

| Role | Use when | Recommended sub-agent model (Generation; tier; reasoning) | Orchestration mode | Output |
|---|---|---|---|---|
| Explorer | Inputs are scattered and read-heavy. | latest available; fast/economy or balanced; low or medium | bounded delegated sub-agents | Discovery notes with file references. |
| Research verifier | Plans depend on cited claims. | latest available; balanced or flagship; medium or high | bounded delegated sub-agents | Verified claims, discrepancies, and reliability assessment. |
| Test-risk reviewer | Behavior is clear but coverage risk is uncertain. | latest available; balanced; medium | bounded delegated sub-agents | Test gaps and recommended cases. |
| Bounded implementer | Files are disjoint and the plan is concrete. | latest available; balanced; medium | bounded delegated sub-agents | Patch plus commands run. |
| Security reviewer | Changes touch auth, secrets, inputs, data, or dependencies. | latest available; flagship; high | bounded delegated sub-agents | Findings with severity, impact, and remediation. |
| Final reviewer | Integration risk or blast radius is high. | latest available; flagship; high | bounded delegated sub-agents | Blocking findings, residual risk, and release recommendation. |

## Portable role shape

Use policy names in portable artifacts. Put concrete model names only in
environment-specific adapters or run metadata.

```yaml
id: test-risk-reviewer
role: review
active_model_policy: active repository policy
model_policy_source: AGENTS.md
model_policy_scope: this work item
model_policy_expires: when the work item completes unless the operator changes it
recommended_sub_agent_model:
  generation: latest available
  capability_tier: balanced
  reasoning_effort: medium
orchestration_mode: bounded delegated sub-agents
availability_fallback: orchestration session review
context_strategy: curated artifacts
inputs:
  - <work-item-path><spec-filename>
  - <work-item-path><plan-filename>
outputs:
  - review/test-risk-notes.md
allowed_actions:
  - read
  - write-artifact
```

## Report requirements

Each sub-agent report must include:

- Assigned scope.
- Files inspected or changed.
- Commands or tests run.
- Assumptions.
- Uncertainty or residual risk.
- Recommended next step.
- Context strategy actually used and observed context/model inheritance behavior, if any.

The orchestration session owns decomposition, integration, conflict resolution,
final validation, and the user-facing summary.

## Independent reviewer pattern

Use an independent sub-agent reviewer by default with curated artifacts, the changed diff, validation evidence, and a short role prompt. Give it one named lens, such as requirements traceability, regression risk, test adequacy, or adversarial counterexamples. A separate task or thread is an operator-managed fallback, not the default, until inter-task reporting in the required modality is proven. Each finding is evidence-backed and records severity plus a reproduction or validation path. The reviewer advises; the orchestration session retains final integration ownership.

For a fresh-orchestration-session reviewer or model transition, use curated artifacts and `rule:execution-quality.execution-thread-start`; name the first activity and stop for approval-required variance.
