# Variance Log

Work ID: `2026-07-14_plain-language-artifacts`
Harness release: `0.6+`
Schema: `schema:variance-log`
Policy references: `module:lifecycle`, `rule:lifecycle.variance-policy`

## Entries

### `VAR-001` 2026-07-14 — Expand current authoring-surface coverage

- Variance class: `Scope change`
- Original plan reference: `plan_plain-language-artifacts.md`, `TASK-001`, `TASK-003`, and `TASK-004`
- What changed: The post-diff review found that the approved two-template consumer set does not cover the remaining current plan, snapshot, amendment, and variance templates, and the active-path scan excludes those templates.
- Why it changed: Leaving the existing optional style-loading cues and unscanned current templates in place would weaken the intended current authoring policy.
- Impact on scope: Requires an approved amendment before expanding template consumers and the active-path validation boundary.
- Impact on tests: Requires focused validator assertions for the complete current template set and exact canonical-exception presence.
- Impact on documentation: Requires the amended template source and generated-output record.
- Risk: `Medium`; incomplete policy coverage can mislead future artifact authors.
- Approval required: `Yes`
- Approval status: `Approved amendment`
- Approval evidence: `plan_amendment-001_template-scope_plain-language-artifacts.md`, approved in commit `f7840cc5e69c7b195a2dc95b62cf2fbbc410b9dd`
- Superseded by: None
