# Work-Item Architecture Decisions Snapshot

Work ID: `2026-07-03_work-item-architecture-decisions`
Source spec: `../spec_work-item-architecture-decisions.md`
Status: Approved
Harness release: `0.4+`
Policy references: `module:lifecycle`, `module:quality`, `module:architecture`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.variance-policy`, `rule:quality.spec-handoff`

## Purpose

This snapshot records the work-item-bounded architecture decision model being introduced by this planning package. It is not a durable repository-level architecture document and does not create an `ARCHITECTURE.md` workflow.

## Decision Summary

The harness should treat architectural decisions as first-class work-item planning content. Architectural decisions may come from the problem statement itself, from compatibility or safety constraints, or from deliberate tradeoffs chosen during planning. Those decisions belong in the spec and, when meaningful enough to preserve separately, in `snapshots/architecture.snapshot.md`.

Implementation plans and phase plans are downstream of those decisions. They may reference architecture, sequence architecture-sensitive implementation work, and validate architectural constraints, but they should not silently invent or reinterpret architecture after the spec and snapshot are frozen.

## Artifact Responsibilities

Spec responsibilities:

1. Capture problem framing, goals, scope, non-scope, assumptions, constraints, requirements, acceptance criteria, and a compact architectural decision summary.
2. Decide whether `snapshots/architecture.snapshot.md` is required, not applicable, or deferred with owner and reason.
3. Record architecture-affecting rejected alternatives when they matter for implementation or future planning.

Architecture snapshot responsibilities:

1. Preserve work-item-specific architectural decisions when the work makes or depends on meaningful choices.
2. Record drivers, constraints, selected approach, affected boundaries, rejected alternatives, validation cues, and future-doc boundaries.
3. Freeze with the planning package as an immutable snapshot under `rule:lifecycle.immutable-snapshots`.

Plan and phase-plan responsibilities:

1. Treat the approved spec and architecture snapshot as input artifacts.
2. Sequence implementation, validation, documentation, and review tasks around those inputs.
3. Route missing architecture back to draft specs and snapshots before freeze.
4. Use variance and amendment handling for high-impact architecture changes after freeze.

## Architecture Snapshot Triggers

Create or require `snapshots/architecture.snapshot.md` when the work makes, changes, or depends on meaningful decisions about one or more of these boundaries:

1. Multiple repositories, services, packages, or components.
2. Public APIs, internal interfaces, schemas, contracts, generated artifacts, or compatibility behavior.
3. Data models, persistence, migrations, retention, or rollback.
4. Configuration, infrastructure, deployment, runtime topology, or operational control flow.
5. Agentic layers, planning orchestration, sub-agent coordination, or human/operator workflow contracts.
6. Security, privacy, compliance, safety, destructive operations, or permission boundaries.
7. Phase ownership, cross-phase sequencing, or future-thread handoff decisions.
8. Deliberate rejection of a plausible architecture alternative that future agents are likely to revisit.

Mark the architecture snapshot not applicable only when repository-context review finds no meaningful architectural decision or dependency to preserve. Defer it only when a named later event or owner must supply missing architecture input before implementation.

## Current Flow

Before approval freeze:

1. Draft the spec.
2. Identify architectural decisions and decide whether an architecture snapshot is required.
3. Draft the snapshot when required.
4. Draft the plan using the spec and snapshot as inputs.
5. Stage the planning package for review.

After approval freeze:

1. Treat the approved spec, plan, and architecture snapshot as immutable planning inputs.
2. Record nontrivial local implementation drift in the variance log.
3. Stop for an amendment when drift affects architecture, APIs, data, security, privacy, compliance, scope, acceptance criteria, or plan feasibility.

## Rejected Alternatives

Always require architecture snapshots:

1. Rejected because many substantial work items are documentation, validation, or narrow implementation changes without meaningful architecture decisions. Mandatory snapshots would create low-signal artifacts and reviewer fatigue.

Spec-only architecture:

1. Rejected because long specs can bury architectural decisions and make future planning threads miss the architecture contract.

Plan-owned architecture:

1. Rejected because plans are sequencing artifacts. Letting plans own architecture would preserve the current ambiguity and make post-freeze drift harder to detect.

Repository-level `ARCHITECTURE.md` now:

1. Rejected for this work item because the harness does not yet have durable-document lifecycle rules for repository-level architecture updates. This remains a separate future extension.

ADR directory now:

1. Rejected because the current need is a work-item-bounded planning artifact, not a permanent cross-work decision registry.

## Future Durable-Document Boundary

This work intentionally leaves these durable-document questions for a future work item:

1. Whether and when a repository should have an `ARCHITECTURE.md`.
2. How work-item architecture snapshots graduate into long-lived architecture summaries.
3. Whether `deltas/architecture-summary.delta.md` becomes a real merge workflow.
4. How durable documents are reviewed, updated, versioned, and rolled back across repositories.

## Validation Cues

Implementation should be considered aligned with this architecture snapshot when:

1. Lifecycle guidance owns the trigger rule for work-item architecture snapshots.
2. Spec templates prompt architecture decisions before plans are drafted.
3. Plan templates list architecture artifacts as inputs and do not prompt plans to make new architectural decisions.
4. The architecture snapshot template is work-item-bounded and does not require `ARCHITECTURE.md`.
5. README and operator note describe the future durable-document boundary.
6. Validator checks remain structural rather than semantic.

## Approval

- Status: Approved
- Superseded by: record only when this artifact is superseded
