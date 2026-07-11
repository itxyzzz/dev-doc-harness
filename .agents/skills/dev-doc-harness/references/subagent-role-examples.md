# Sub-Agent Role Examples

These examples are optional patterns for specs and plans. Keep roles bounded,
policy-relative, and easy for a fresh agent to execute.

Module: `module:role-examples`

This is advisory example content. It offers optional role patterns and report
shape examples, but it does not make any sub-agent role mandatory policy.

## Common roles

Keep Model generation, Capability tier, Reasoning effort, and Orchestration mode separate. A bounded role below uses `bounded delegated sub-agents`; platform multi-agent/`ultra` is a different orchestration choice and does not imply these role boundaries or report gates.

| Role | Use when | Capability tier | Reasoning effort | Orchestration mode | Output |
|---|---|---|---|---|---|
| Explorer | Inputs are scattered and read-heavy. | fast/economy or balanced | low or medium | bounded delegated sub-agents | Discovery notes with file references. |
| Research verifier | Plans depend on cited claims. | balanced or flagship | medium or high | bounded delegated sub-agents | Verified claims, discrepancies, and reliability assessment. |
| Test-risk reviewer | Behavior is clear but coverage risk is uncertain. | balanced | medium | bounded delegated sub-agents | Test gaps and recommended cases. |
| Bounded implementer | Files are disjoint and the plan is concrete. | balanced | medium | bounded delegated sub-agents | Patch plus commands run. |
| Security reviewer | Changes touch auth, secrets, inputs, data, or dependencies. | flagship | high | bounded delegated sub-agents | Findings with severity, impact, and remediation. |
| Final reviewer | Integration risk or blast radius is high. | flagship | high | bounded delegated sub-agents | Blocking findings, residual risk, and release recommendation. |

## Portable role shape

Use policy names in portable artifacts. Put concrete model names only in
environment-specific adapters or run metadata.

```yaml
id: test-risk-reviewer
role: review
model_policy: active repository policy
model_policy_source: AGENTS.md
model_policy_scope: this work item
model_policy_expires: when the work item completes unless the operator changes it
model_generation: not exposed
capability_tier: balanced
reasoning_effort: medium
orchestration_mode: bounded delegated sub-agents
resolved_profile: not exposed
availability_fallback: orchestration thread review
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

The orchestration thread owns decomposition, integration, conflict resolution,
final validation, and the user-facing summary.

For a fresh-task reviewer or model transition, use curated artifacts and `rule:execution-quality.execution-thread-start`; name the first activity and stop for approval-required variance.
