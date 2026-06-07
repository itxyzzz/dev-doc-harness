# Architecture Summary Delta: Validation Hardening

Work ID: `2026-06-05-refactor-as-code`
Status: Proposed delta

## Summary

Phase 05 adds `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` as a lightweight validation script for current harness surfaces.

The script covers:

- Required harness files and Phase 05 validation artifacts.
- Canonical `module:*` owners.
- Safety-critical `rule:*` IDs.
- Template `schema:*` anchors and policy-reference anchors.
- Operation-router routes in `.agents/skills/dev-doc-harness/SKILL.md`.
- Discoverability for work sizing, freeze gates, stop-before-implementation, immutable snapshots, variance and amendments, changelog-before-commit, documentation matrices, active repository model policy, Superpowers compatibility, and historical artifact handling.
- Previously removed long reusable policy phrases.
- Unexpected placeholders in current non-template surfaces.
- Golden traversal scenarios from the Phase 01 architecture snapshot.

## Architecture link

This validation work implements the feasible subset of the Phase 01 metrics and scenario direction, especially:

- `metric:references.broken-tolerance`
- `metric:safety.discoverability`
- `metric:template.duplicated-policy-prose`
- `metric:historical.no-rewrite`
- The nine `scenario:*` golden traversal cases recorded in `snapshots/test-cases.snapshot.md`

Full rule versioning remains deferred. The script validates stable retrieval and ownership anchors; it does not introduce a rule manifest, generated documentation pipeline, or semantic versioning system.
