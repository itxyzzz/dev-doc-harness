# Architecture Snapshot

Work ID: `<work-id>`
Short ID: `<short-id>`
Status: Draft
Harness release: `<version or unknown>`
Schema: `schema:snapshot.architecture`
Policy references: `module:lifecycle`, `module:quality`, `rule:lifecycle.work-item-architecture-decisions`, `rule:lifecycle.immutable-snapshots`, `rule:lifecycle.variance-policy`, `rule:quality.spec-handoff`

## Purpose

Capture work-item architecture decisions that future implementation, review, or phase planning must preserve. This is a frozen work-item snapshot after approval or handoff, not a repository-level architecture manual.

## Decision Drivers

1. `<driver from the operator request, problem statement, product outcome, technical constraint, review risk, migration, rollout, compliance, or operational need>`.

## Constraints

1. `<repository, component, interface, data model, config, infrastructure, agentic/process, security, privacy, compliance, migration, rollback, or phase constraint>`.

## Selected Approach

1. `<chosen architecture direction>`.
2. `<why this approach fits the drivers and constraints>`.

## Affected Boundaries

1. Repositories: `<paths, services, packages, or None>`.
2. Components or modules: `<names, paths, or None>`.
3. Interfaces, schemas, config, or infra: `<names, paths, contracts, or None>`.
4. Agentic, process, documentation, or phase boundaries: `<workflows, artifacts, phases, or None>`.

## Rejected Alternatives

### `<alternative name>`

Decision:

1. `<why this alternative was rejected, deferred, or left for a later work item>`.

## Validation Cues

1. `<acceptance criterion, command, review check, phase handoff, rollout signal, or manual observation that verifies the architecture held>`.

## Future Durable-Doc Boundary

Repository-level durable architecture documents such as `ARCHITECTURE.md` are future work for a separate harness extension. Use `deltas/architecture-summary.delta.md` only when this work item needs an optional later project-documentation update.

## Approval

- Status: Draft
- Superseded by: record only when this artifact is superseded
