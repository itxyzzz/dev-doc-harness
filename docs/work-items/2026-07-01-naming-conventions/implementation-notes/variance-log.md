# Naming Conventions Variance Log

Work ID: `2026-07-01-naming-conventions`
Harness release: `0.3.0`
Schema: `schema:variance-log`
Policy references: `module:lifecycle`, `module:naming`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`

## Entries

### 2026-07-01 - deduplicate naming pattern references

- Variance class: Local technical documentation variance.
- Original plan reference: `plan-naming-conventions.md`, `## Planned commits`.
- What changed: Added a second implementation commit after operator review to reduce remaining naming-pattern duplication across current reusable harness surfaces.
- Why it changed: The first implementation centralized the canonical naming rules, but current references and templates still repeated higher-level filename and subject patterns that should be represented as derived naming variables.
- Impact on scope: No scope expansion; this tightens the planned centralization behavior.
- Impact on tests: Existing harness validator remains the primary check; the known unrelated untracked work-item folder still blocks the `tracking.work-items` check.
- Impact on documentation: Adds derived naming variables and replaces duplicated grammar in current references, templates, README/operator guidance, and validation fixtures.
- Risk: Low. The change affects documentation policy surfaces only and preserves historical work-item artifacts.
- Approval required: No.
- Approval status: Operator authorized with "Good, proceed as described".
