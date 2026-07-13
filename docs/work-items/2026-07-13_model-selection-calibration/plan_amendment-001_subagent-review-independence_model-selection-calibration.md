# Plan Amendment 001: Sub-agent Review Independence

Work ID: `2026-07-13_model-selection-calibration`
Short ID: `model-selection-calibration`
Status: Approved
Harness release: `0.6+`
Schema: `schema:plan.amendment`
Policy references: `module:lifecycle`, `module:models`, `rule:lifecycle.variance-policy`, `rule:lifecycle.commit-message-format`

## Original plan reference

- Amendment ID: `AMD-001`
- File: `plan_model-selection-calibration.md`
- Section or task: `SPEC-003`, `VER-003`, `TASK-002`, `TASK-004`, and `CHECK-003`.
- Original instruction: Define independent review as a separate task or thread with curated artifacts and evidence-backed findings.

## Discovered issue

The separate-task/thread review shape assumes reliable Codex inter-task reporting in the required modality. That capability is not yet proven, so making it the default would make the approved orchestration policy depend on an unverified platform behavior.

## Approved change

Use an independent sub-agent reviewer as the default review shape. Retain curated artifacts, one named lens, evidence-backed findings with severity and a reproduction or validation path, and orchestration-owned final integration. A separate task or thread becomes an operator-managed fallback pending research and proof of the required inter-task reporting capability.

## Reason this change is necessary

Sub-agent independence provides the required review separation now. Higher task/thread isolation remains a desirable future option but cannot be the default until the required reporting behavior is demonstrated.

## Impact assessment

| Area | Impact |
|---|---|
| Scope | Amends review orchestration only; no new product surface. |
| Verification Criteria and Plan Checks | `VER-003` and `CHECK-003` use the amended default and fallback boundary. |
| API/interface | None. |
| Data model/migration | None. |
| Security/privacy/compliance | None. |
| Tests | Focused policy assertions cover the sub-agent default and operator-managed fallback. |
| Documentation | Canonical policy, advisory example, operator-manual delta, review evidence, and changelog are updated. |
| Rollout/operations | Higher-isolation task/thread review remains deferred pending platform research. |

## Approval

- Required: Yes
- Status: Approved
- Approval evidence: Operator instruction on 2026-07-14: “Independence of sub-agents is sufficient for now.”
- Superseded by: None

## Planned commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Amended implementation | `docs: model-selection-calibration -- retain subagent review default` | `2026-07-13_model-selection-calibration -- retain subagent review default` | Records the approved review-orchestration correction. |
