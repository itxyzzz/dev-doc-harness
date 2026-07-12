# Variance Log

Work ID: `2026-07-12_new-task-handoff-visibility`
Harness release: `0.5+`
Schema: `schema:variance-log`
Policy references: `module:lifecycle`, `module:naming`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`

## Entries

### `VAR-001` 2026-07-12 - align-handoff-block-names

- Variance class: `Local technical`
- Original plan reference: `plan_new-task-handoff-visibility.md`, `TASK-003` and Change Surfaces items 5-6
- What changed: Renamed the three context-specific handoff source blocks to `spec.085.small.handoff.md`, `spec.085.large.handoff.md`, and `plan.085.common.handoff.md`; updated all four manifests and matching validator assumptions.
- Why it changed: The implemented `handoff.085.common.*` compatibility grammar incorrectly labeled spec-specific blocks as common and diverged from the repository's established `<artifact>.<order>.<scope>.<name>` block grammar.
- Impact on scope: `None`; the frozen planning-shape, continuity, approval, fallback, and handoff behavior is unchanged.
- Impact on tests: Updated template-assembly path assertions, filename grammar, and shared-block lookup; full harness validation remains the required evidence.
- Impact on documentation: Source block paths and assembly manifests changed; generated template content is unchanged.
- Risk: `Low`; an incorrect manifest or validator path would make template assembly fail deterministically.
- Approval required: `No`
- Approval status: `Not required`
- Approval evidence: Operator follow-up instruction on 2026-07-12 to proceed with the agreed naming correction.
- Superseded by: None
