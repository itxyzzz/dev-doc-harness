# Variance Log

Work ID: `2026-08-02_task-orchestration-model-policy`
Harness release: `0.8+`
Schema: `schema:variance-log`
Policy references: `module:lifecycle`, `module:naming`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`

## Entries

### `VAR-001` 2026-08-02 - Reparent model policies without changing enterprise-default semantics

- Variance class: `Routine equivalent adjustment`
- Original plan reference: `AMD-001-DEC-003`, `Explicit non-scope: enterprise-default`, and `AMD-001-CHECK-007` in `plan_amendment-01_selection-policy-consistency_task-orchestration-model-policy.md`
- What changed: Reparented the unchanged `enterprise-default` and `economy-default` policy bodies beneath `### Model selection policies`, changing their headings from H2 to H4 so the canonical document follows the operator-approved responsibility structure. Updated the corresponding rule-owner headings; no policy name, allocation rule, or semantics changed.
- Why it changed: Post-implementation review found that the canonical policy structure still separated model-selection policies from the Model selection responsibility they define. The operator authored the reorganization and explicitly authorized recording the `enterprise-default` relocation as variance.
- Evidence and scope stay equivalent: `Yes`; the full policy suite validates the nested rule owners and selection contract, while direct diff inspection confirms that the `enterprise-default` body is unchanged apart from heading level and location.
- Documented implementation subject: `docs: task-orchestration-model-policy -- correct policy ownership structure`
- Superseded by: None
