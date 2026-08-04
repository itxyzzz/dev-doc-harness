# Documentation Assessment Simplification Test Cases

Status: Approved planning evidence

## `CASE-001` Canonical assessment policy is compact

Given the current lifecycle reference is updated, when the static policy validator reads the documentation-assessment section, then it finds exactly these ordered IDs: `DOC-TEST-CASE`, `DOC-TEST-GUIDE`, `DOC-OPS-GUIDE`, `DOC-API-GUIDE`, and `DOC-ARCH-SUMMARY`; it finds no assessment row for changelog records or architecture snapshots.

## `CASE-002` Generated specs require readable decisions

Given either generated specification template, when a planning agent reaches `## Documentation assessment`, then it sees the same five status bullets; `Required` asks for a path and Plan Task, and `Deferred` asks for an owner and resolution point.

## `CASE-003` Enforcement layers stay separate

Given the policy, template body, and readiness blocks, when static assertions inspect them, then policy owns IDs and statuses, template body owns the five bullets, and readiness uses generic completeness/task/deferral wording without a second ID list or catalog-trigger prose.

## `CASE-004` Planning templates do not carry changelog procedure

Given current specification, plan, and phase-plan source blocks, when searches inspect documentation-assessment and phase documentation-task prompts, then no changelog path, timing, fragment, or root-consolidation row is present; small and phase plan prompts retain only the concise before-implementation reminder to follow `module:implementation-changelog`.

## `CASE-005` Phase plans consume rather than duplicate assessment

Given a phase plan is drafted from an approved anchor, when its documentation-task section is completed, then it identifies only phase-owned required or deferred documentation outputs and their task/owner details; it does not restate the complete catalog or architecture-snapshot status.

## `CASE-006` Current changelog rules have one operational owner

Given the current lifecycle, naming, implementation-changelog, planning, and release references, when static policy checks inspect changelog guidance, then generic commit-subject grammar stays in naming; current fragment path/name, entry-heading/synchronization, metadata, lint, consolidation, compatibility, and cleanup instructions appear in `implementation-changelog.md`; and planning freeze has no changelog action.

## `CASE-007` Every audience receives only relevant changelog detail

Given active templates and user-facing guidance, when static checks inspect current surfaces, then specs and amendment templates contain no changelog procedure; plans and phase plans contain only the concise before-implementation handoff; README/operator note contain only an implementation-only summary or link; and release policy/runbook retain only release-stage consolidation context.
