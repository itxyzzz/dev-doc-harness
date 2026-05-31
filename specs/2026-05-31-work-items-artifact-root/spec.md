# Work Items Artifact Root Spec

Work ID: `2026-05-31-work-items-artifact-root`
Status: Draft

## Goal

Move the harness durable planning artifact contract from the ambiguous root-level
`specs/<work-id>/` layout to `docs/work-items/<work-id>/`, with filenames that
remain easy for operators to reference in chat. The new layout should reduce
confusion when Superpowers is active by making the harness package canonical
while allowing only minimal Superpowers pointer stubs.

## Scope

- Change the canonical work item folder from `specs/<work-id>/` to
  `docs/work-items/<work-id>/`.
- Change durable planning artifact filenames so top-level specs, plans, phase
  plans, and amendments start with their artifact kind and end with the short
  work ID suffix.
- Flatten per-work-item supplemental documentation by moving `docs/snapshots/`
  to `snapshots/` and `docs/living/` to `deltas/`.
- Preserve existing snapshot and delta filenames.
- Keep `handoff/` and `implementation-notes/variance-log.md` as direct children
  of the work item folder.
- Update the harness skill, artifact contract, planning freeze references,
  durable planning quality reference, templates, README, TODO notes, and
  existing local planning package to match the new contract.
- Add explicit Superpowers compatibility rules so the full durable package lives
  under `docs/work-items/<work-id>/`, while optional `docs/superpowers/...`
  artifacts are minimal pointer stubs only.

## Non-scope

- No runtime source code, API, schema, CLI, persistence, or product behavior
  changes.
- No change to work sizing rules, freeze-gate approval semantics, variance
  classes, changelog requirements, or model/sub-agent policy.
- No migration automation or validation script in this work item.
- No long-term retention or archive policy for old work item packages.

## Current state

The harness currently treats `specs/<work-id>/` as the canonical package root.
Within a package, top-level durable artifacts are named generically, such as
`spec.md`, `plan.md`, `plan-phase-01-discovery.md`, and
`plan-amendment-001-short-title.md`.

Supplemental documentation is nested under a second `docs/` folder inside the
work item package:

```text
specs/<work-id>/
  docs/
    snapshots/
    living/
```

This layout creates three operator and agent usability problems:

- `specs/` implies everything in the package is a spec, even though plans,
  amendments, handoffs, variance logs, snapshots, and deltas also live there.
- Generic filenames such as `spec.md` and `plan.md` are hard to reference with
  chat `@` mentions when a repository contains multiple work item packages.
- Superpowers defaults can point agents toward `docs/superpowers/...`, creating
  competing locations unless the harness gives explicit compatibility rules.

## Proposed behavior

Every substantial work item uses this canonical package root:

```text
docs/work-items/<work-id>/
```

The folder keeps the full dated work ID for ordering and uniqueness. Durable
planning filenames append a shorter suffix derived from the work ID by removing
only the leading `YYYY-MM-DD-`. If an issue key is present after the date, it is
preserved in the suffix.

Examples:

```text
docs/work-items/2026-05-31-artifact-root/spec-artifact-root.md
docs/work-items/2026-05-31-artifact-root/plan-artifact-root.md
docs/work-items/2026-05-31-PROJ-123-import/spec-PROJ-123-import.md
docs/work-items/2026-05-31-PROJ-123-import/plan-PROJ-123-import.md
```

Small or medium work item layout:

```text
docs/work-items/<work-id>/
  spec-<short-id>.md
  plan-<short-id>.md

  snapshots/
    test-cases.snapshot.md
    architecture.snapshot.md
    api-contract.snapshot.md

  deltas/
    testing-guide.delta.md
    operator-manual.delta.md
    api-reference.delta.md
    architecture-summary.delta.md

  implementation-notes/
    variance-log.md
```

Large or phased work item layout:

```text
docs/work-items/<work-id>/
  spec-<short-id>.md
  plan-phase-01-discovery-<short-id>.md
  plan-phase-02-core-implementation-<short-id>.md
  plan-phase-03-hardening-<short-id>.md
  plan-amendment-001-short-title-<short-id>.md

  snapshots/
    test-cases.snapshot.md
    architecture.snapshot.md
    api-contract.snapshot.md

  deltas/
    testing-guide.delta.md
    operator-manual.delta.md
    api-reference.delta.md
    architecture-summary.delta.md

  handoff/
    implementation-handoff.md
    review-handoff.md

  implementation-notes/
    variance-log.md
```

Superpowers remains responsible for its methodology: brainstorming, design
discussion, planning workflow, TDD, review, and finishing. The harness remains
responsible for durable repository artifact location, freeze gates, variance
handling, changelog requirements, and handoff quality.

If Superpowers creates or expects files under `docs/superpowers`, those files
may exist only as minimal pointer stubs. A valid stub contains a title, status,
and link to the canonical package or canonical artifact under
`docs/work-items/<work-id>/`. Stubs must not duplicate full specs or plans and
must not become a second source of truth.

The existing local package under
`specs/2026-05-31-planning-approval-freeze-flow/` should be migrated to:

```text
docs/work-items/2026-05-31-planning-approval-freeze-flow/
  spec-planning-approval-freeze-flow.md
  plan-planning-approval-freeze-flow.md
```

The migration should preserve the approved status and substantive content of
that package, changing only path and filename references needed to keep the
repository contract coherent.

## Interfaces and data

Affected repository-facing documentation and template interfaces:

- `.agents/skills/dev-doc-harness/SKILL.md`
- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
- `.agents/skills/dev-doc-harness/assets/templates/*.md`
- `README.md`
- `TODO.md`
- `CHANGELOG.md`
- Existing local planning package under `specs/`

No public API, runtime config, generated data format, database schema, CLI
surface, or persistence interface is affected.

## Risks

- Stale references to `specs/<work-id>/`, `spec.md`, or `plan.md` could keep
  agents using the old layout.
- Overly permissive Superpowers language could reintroduce duplicate specs or
  plans under `docs/superpowers`.
- Moving approved artifacts could look like rewriting frozen planning history
  unless the change is framed as a repository layout migration with substantive
  content preserved.
- Filename examples could become too long if the full dated work ID is used in
  every artifact filename; the short suffix rule avoids this.

## Acceptance criteria

- The harness canonical root is `docs/work-items/<work-id>/` in the skill,
  artifact contract, templates, README, TODO notes, and related references.
- Durable planning artifact filenames use the `spec-<short-id>.md`,
  `plan-<short-id>.md`, `plan-phase-NN-title-<short-id>.md`, and
  `plan-amendment-NNN-title-<short-id>.md` patterns.
- The short ID is defined as the work ID with only the leading `YYYY-MM-DD-`
  removed, preserving issue keys.
- Supplemental package folders are flattened to `snapshots/` and `deltas/`.
- Existing snapshot and delta filenames remain unchanged.
- Superpowers compatibility language explicitly allows only minimal pointer
  stubs under `docs/superpowers/...` and requires the full durable package under
  `docs/work-items/<work-id>/`.
- The existing local planning package is migrated to the new root and filename
  convention without changing its approved planning substance.
- `CHANGELOG.md` receives a newest-first entry before the implementation commit.
- Validation confirms no stale canonical `specs/<work-id>/`, `docs/snapshots/`,
  or `docs/living/` instructions remain except where describing legacy
  migration.

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Required for planning approval and implementation commits |
| Test cases | Snapshot | No | Not applicable | snapshots/test-cases.snapshot.md | Documentation/process layout change only |
| Testing guide delta | Living delta | No | Not applicable | deltas/testing-guide.delta.md | No test workflow change |
| Operator manual delta | Living delta | No | Not applicable | deltas/operator-manual.delta.md | README and harness references are updated directly |
| API reference delta | Living delta | No | Not applicable | deltas/api-reference.delta.md | No API change |
| Architecture snapshot | Snapshot | No | Not applicable | snapshots/architecture.snapshot.md | No architecture change |
| Architecture summary delta | Living delta | No | Not applicable | deltas/architecture-summary.delta.md | No long-lived architecture summary change |

## Approval

- Status: Draft
- Superseded by: None
