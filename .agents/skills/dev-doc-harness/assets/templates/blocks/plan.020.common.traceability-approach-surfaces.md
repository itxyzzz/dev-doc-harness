## Spec Traceability

Map the approved spec to execution without restating the spec. Use one compact review matrix for requirement and acceptance coverage. Keep cells short by citing IDs plus a short title only when useful.

| Requirement or acceptance criterion | Primary tasks | Validation |
|---|---|---|
| `REQ-001` `<short title>` | `T-001`, `T-002` | `V-001`, `V-002` |
| `AC-001` `<short title>` | `T-002`, `T-003` | `V-003` |

Include one row for each `REQ` and `AC` that must be implemented, validated, or marked not applicable with a reason. Do not include risk rows in the default matrix; cover risks through task `Notes`, implementation boundaries, validation entries, or a separate plan-specific risk section only when needed.

Architecture coverage:

1. Architecture input: `<spec section, snapshots/architecture.snapshot.md, amendment, or None with reason>`.
2. Plan usage: `<how tasks consume architecture decisions for sequencing, boundaries, validation, rollout, or review>`.
3. Drift path: `<draft spec/snapshot update before freeze, or variance/amendment after freeze>`.
4. Reinterpretation guard: plans reference approved architecture decisions and do not reinterpret missing or frozen architecture silently.

## Implementation Approach

State the implementation approach in a few concise paragraphs. Focus on sequencing, dependencies, technical shape, integration points, and review strategy. Do not repeat the spec except to record implementation tradeoffs.

## Change Surfaces

Expected edits:

1. `<file or directory>`: `<kind of change and boundary>`.

Stable interfaces:

1. `<API, schema, config, template, workflow, or None>`: `<what must remain compatible>`.

Changed interfaces:

1. `<API, schema, config, template, workflow, or None>`: `<what changes and who consumes it>`.

Implementation boundaries:

1. `<nearby file, behavior, cleanup, later phase, or follow-up>` stays out of scope because `<reason>`.
