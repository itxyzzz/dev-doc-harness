# Architecture Summary Delta: Graph Validation And Lifecycle Decomposition

Work ID: `2026-06-07-followup-hardening`
Status: Final

## Structural graph model

The harness now treats current textual policy as a graph of owned IDs and references. Current owners come from canonical module declarations, canonical rule owner tables, template schema anchors, and current scenario or metric anchors. Current references come from router entries, template policy-reference lines, README and operator guidance, validation documentation, and the validation script.

Validation fails when a current reference has no owner, when a current rule or schema has multiple owners, when a declared owner-table heading is missing, or when a template omits modules required by its router operation family.

## Retrieval and traversal budget

Routine operation routes should stay within three required canonical modules before optional context. The validation script enforces this budget for the current router table so future changes cannot silently expand the amount of policy an agent must retrieve for common work.

## Duplicate policy boundary

Duplicate-block validation applies to current reusable-policy surfaces and templates. It intentionally excludes frozen historical work-item artifacts, because those artifacts are review history rather than current policy owners.

## Lifecycle decomposition

`references/artifact-contract.md` remains the lifecycle owner for this phase. The next architectural move, if edit pressure continues, should be section-level lifecycle ownership first. A later file split should be justified by concrete churn, with changelog and documentation-matrix policy as the likely first extraction candidate.
