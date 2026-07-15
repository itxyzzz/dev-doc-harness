# Model-Selection Calibration Variance Log

Work ID: `2026-07-13_model-selection-calibration`
Harness release: `0.6+`
Schema: `schema:variance-log`
Policy references: `module:lifecycle`, `module:models`, `rule:lifecycle.variance-policy`

## Entries

### 2026-07-14 — retain sub-agent review as the default

- Variance class: Scope change affecting `SPEC-003`, `VER-003`, and `CHECK-003` review orchestration.
- Original plan reference: `plan_model-selection-calibration.md`, `TASK-002`, `TASK-004`, and `CHECK-003`.
- What changed: Independent sub-agents are the default review mechanism. Separate tasks or threads are operator-managed fallbacks until Codex inter-task reporting in the required modality is researched and proven.
- Why it changed: The approved implementation assumed a separate task or thread could reliably return review findings. That capability is not yet demonstrated, while independent sub-agent review is available now.
- Impact on scope: No new product surface; the review-orchestration commitment is amended.
- Impact on verification: Focused policy assertions now protect the independent sub-agent default and the manual fallback boundary.
- Impact on documentation: Canonical policy, advisory examples, operator-manual delta, amendment, review evidence, and changelog are updated.
- Risk: Low to medium. Higher isolation remains desirable but is deferred until the platform capability is proven.
- Approval required: Yes.
- Approval status: Approved by the operator on 2026-07-14: “Independence of sub-agents is sufficient for now.”
