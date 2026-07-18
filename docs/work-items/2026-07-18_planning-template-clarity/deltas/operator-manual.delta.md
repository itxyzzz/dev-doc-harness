# Operator Manual Delta: Planning Template Clarity

Work ID: `2026-07-18_planning-template-clarity`
Short ID: `planning-template-clarity`
Status: Approved
Harness release: `0.7+`

## Proposed Update

Planning artifacts distinguish what is known about the current planning task
from what should be selected for execution. Current model, profile, reasoning,
or context observations may be `not exposed`. The approved execution selection
must still name an actionable model or policy-relative target, tier, reasoning
effort, orchestration mode, fallback, continuity, and rehydration requirement.
When substantial work cannot verify that the current allocation and context are
suitable, prefer a fresh task with the intentionally selected configuration and
a curated-artifact handoff.

A combined small/medium package freezes its spec and plan together, and the plan
owns the implementation handoff. A staged spec-only package is an explicit
exception that hands off only to plan drafting. Large/phased work normally uses
a rolling sequence: freeze the anchor, plan and freeze one phase, implement it,
then use its actual outputs to plan the next phase. Operators still approve each
freeze and start boundary, but the harness presents the exact next activity.

Superpowers may guide work inside these boundaries. The harness remains
authoritative for durable artifact location, numbered plan tasks, approved
commit boundaries, freeze and variance handling, model-policy bounds, review,
and final integration.

Before each upcoming spec, plan or phase-plan, amendment or replanning,
implementation, or consequential review stage, the agent assesses whether bounded sub-agents would materially
help. If they would and are not already authorized, the agent presents the
roles, context, outputs, model/effort envelope, write scope, concurrency, and
fallback and explicitly asks the operator to approve that use. If they would
not help, the transition records `Sub-agents: None` with a stage-specific
reason. Approval authorizes the recorded in-envelope dispatch without another
generic confirmation; higher-priority platform limits and out-of-envelope
changes still require their normal handling.
