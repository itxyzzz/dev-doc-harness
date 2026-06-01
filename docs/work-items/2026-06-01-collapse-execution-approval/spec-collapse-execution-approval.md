# Collapse Execution Approval Spec

Work ID: `2026-06-01-collapse-execution-approval`
Short ID: `collapse-execution-approval`
Status: Approved

## Goal

Reduce the post-freeze operator approval loop from three acknowledgements to two by allowing the model, reasoning-effort, and sub-agent confirmation step to also authorize implementation when the operator's response clearly says to begin.

## Scope

- Update the canonical planning freeze gate so its post-commit prompt asks for execution settings and implementation authorization together.
- Clarify that implementation still cannot begin in the same turn as the freeze commit unless the operator gives a fresh explicit post-gate instruction.
- Clarify that a post-gate response such as `Confirm, proceed` can satisfy both execution-setting confirmation and implementation authorization.
- Update any templates or operator-facing docs that would otherwise keep implying a separate third approval is always required.

## Non-scope

- No change to the draft planning review approval before the freeze commit.
- No change to the requirement that finalized planning artifacts are committed before implementation begins.
- No change to work item sizing, artifact layout, variance handling, or amendment approval rules.
- No runtime code, API, schema, persistence, CLI, or automation enforcement changes.

## Current state

The freeze gate currently asks the operator to confirm model, reasoning-effort, and sub-agent policy choices after the approved planning package is committed. It also says implementation must not begin unless the operator gives a fresh explicit instruction after the gate.

In practice, agents can treat a bare `Confirm` response as settings-only and then ask for another implementation approval. The resulting conversation has three approvals:

1. Approve the draft planning package.
2. Confirm execution settings.
3. Say `proceed` to begin implementation.

The third approval adds friction without adding meaningful safety when the second prompt could ask for both settings confirmation and start authorization.

## Proposed behavior

After the freeze commit, the agent should report the commit hash and approved artifact paths, remind the operator about the draft plan-only PR option, and ask one combined question:

> Confirm the model, reasoning-effort, and sub-agent policy choices, and say whether to begin implementation now.

If the operator responds with clear start authorization in that post-gate turn, such as `Confirmed, proceed`, `Confirm and start`, or another equivalent phrase, the agent may begin implementation in the next agent turn. If the operator only confirms settings and does not authorize implementation, the agent must continue waiting for an explicit implementation instruction.

A response of only `Confirm` may authorize implementation only when the agent's combined prompt explicitly made clear that confirmation also means beginning implementation now. Otherwise, `Confirm` remains settings-only and the agent should ask whether to start.

## Interfaces and data

Affected repository interfaces are documentation-facing:

- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
- `README.md`
- `CHANGELOG.md`

No public API, runtime config, schemas, persistence, CLI flags, or generated data formats are affected.

## Risks

- If the wording is too loose, agents may start implementation after an ambiguous settings-only confirmation.
- If the wording is too strict, agents may keep requiring the redundant third approval.
- If only the canonical freeze gate is updated, stale template or README language may still encourage the old interaction pattern.

The implementation should keep the safety invariant: implementation starts only after a post-freeze operator response that explicitly authorizes starting, or after a combined prompt where the operator confirms that starting is included.

## Acceptance criteria

- `planning-freeze-gates.md` tells agents to combine execution-setting confirmation with the question of whether to begin implementation now.
- `planning-freeze-gates.md` states that a clear post-gate start response can satisfy both requirements.
- `planning-freeze-gates.md` preserves the rule that implementation cannot begin in the same turn as the freeze commit.
- Ambiguous settings-only confirmation remains insufficient unless the combined prompt made start semantics explicit.
- Relevant templates and README wording no longer imply a separate third approval is always required after execution settings are confirmed.
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
