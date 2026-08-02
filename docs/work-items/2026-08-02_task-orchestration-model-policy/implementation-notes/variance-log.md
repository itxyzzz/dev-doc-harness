# Variance Log

Work ID: `2026-08-02_task-orchestration-model-policy`
Harness release: `0.8+`
Schema: `schema:variance-log`
Policy references: `module:lifecycle`, `module:naming`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`

## Entries

### `VAR-002` 2026-08-02 - Complete reviewer-identified selection template safeguards

- Variance class: `Routine equivalent adjustment`
- Original plan reference: `AMD-001-TASK-002`, `AMD-001-CHECK-003`, `AMD-001-CHECK-005`, and `AMD-001-CHECK-008` in `plan_amendment-01_selection-policy-consistency_task-orchestration-model-policy.md`
- What changed: Added a follow-up implementation commit that constrains fixed-stage Method and Review prompts, requires an Orchestration mode fit rationale, gives the large anchor the standard draft-to-frozen heading transition, replaces three position-dependent canonical references with stable rule IDs, and extends semantic validator mutations for those contracts. The execution-review contract is unchanged because the operator declined reviewer finding 1 as unnecessary duplication of Superpowers-controlled behavior.
- Why it changed: The approved independent reviewer found template and canonical-clarity gaps after the initial amended implementation and ownership-structure follow-up commits. The operator explicitly selected findings 2, 3, 4, and the three position-dependent references for correction.
- Evidence and scope stay equivalent: `Yes`; the changes complete the approved stage-applicability, orchestration-selection, freeze-label, and validator outcomes without changing lifecycle stages, execution-method ordering, authorization boundaries, or `enterprise-default` semantics.
- Documented implementation subject: `docs: task-orchestration-model-policy -- tighten selection templates`
- Superseded by: None

### `VAR-001` 2026-08-02 - Reparent model policies without changing enterprise-default semantics

- Variance class: `Routine equivalent adjustment`
- Original plan reference: `AMD-001-DEC-003`, `Explicit non-scope: enterprise-default`, and `AMD-001-CHECK-007` in `plan_amendment-01_selection-policy-consistency_task-orchestration-model-policy.md`
- What changed: Reparented the unchanged `enterprise-default` and `economy-default` policy bodies beneath `### Model selection policies`, changing their headings from H2 to H4 so the canonical document follows the operator-approved responsibility structure. Updated the corresponding rule-owner headings; no policy name, allocation rule, or semantics changed.
- Why it changed: Post-implementation review found that the canonical policy structure still separated model-selection policies from the Model selection responsibility they define. The operator authored the reorganization and explicitly authorized recording the `enterprise-default` relocation as variance.
- Evidence and scope stay equivalent: `Yes`; the full policy suite validates the nested rule owners and selection contract, while direct diff inspection confirms that the `enterprise-default` body is unchanged apart from heading level and location.
- Documented implementation subject: `docs: task-orchestration-model-policy -- correct policy ownership structure`
- Superseded by: None
