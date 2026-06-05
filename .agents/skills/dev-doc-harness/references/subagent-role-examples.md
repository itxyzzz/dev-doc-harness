# Sub-Agent Role Examples

These examples are optional patterns for specs and plans. Keep roles bounded,
policy-relative, and easy for a fresh agent to execute.

## Common roles

| Role | Use when | Model class | Effort | Output |
|---|---|---|---|---|
| Explorer | Inputs are scattered and read-heavy. | smaller/faster | low or medium | Discovery notes with file references. |
| Research verifier | Plans depend on cited claims. | standard or latest strongest | medium or high | Verified claims, discrepancies, and reliability assessment. |
| Test-risk reviewer | Behavior is clear but coverage risk is uncertain. | standard | medium | Test gaps and recommended cases. |
| Bounded implementer | Files are disjoint and the plan is concrete. | coding-specialized or standard | medium | Patch plus commands run. |
| Security reviewer | Changes touch auth, secrets, inputs, data, or dependencies. | latest strongest | high | Findings with severity, impact, and remediation. |
| Final reviewer | Integration risk or blast radius is high. | latest strongest | high | Blocking findings, residual risk, and release recommendation. |

## Portable role shape

Use policy names in portable artifacts. Put concrete model names only in
environment-specific adapters or run metadata.

```yaml
id: test-risk-reviewer
role: review
model_policy: standard-review
reasoning_effort: medium
context_strategy: curated artifacts
inputs:
  - docs/work-items/<work-id>/spec-<short-id>.md
  - docs/work-items/<work-id>/plan-<short-id>.md
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
