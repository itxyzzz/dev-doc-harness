## Spec Traceability

Map the approved spec to execution without restating the spec. Use compact numbered lists or short blocks; avoid wide tables when cells need more than a few words.

Requirement coverage:

1. `REQ-001`: implemented by `<task ids>`; verified by `<validation ids or acceptance criteria>`.

Acceptance coverage:

1. `AC-001`: implemented by `<task ids>`; verified by `<validation ids, manual check, review finding, or operator acceptance path>`.

Risk and boundary coverage:

1. `RISK-001` or scope boundary: handled by `<task ids, validation ids, later phase ids, or explicit no-op rationale>`.

## Implementation Approach

Describe the implementation approach in a few paragraphs. Focus on sequencing, dependencies, technical shape, integration points, and review strategy. Do not repeat the spec except to explain implementation tradeoffs.

## Change Surfaces

Expected edits:

1. `<file or directory>`: `<kind of change and boundary>`.

Stable interfaces:

1. `<API, schema, config, template, workflow, or None>`: `<what must remain compatible>`.

Changed interfaces:

1. `<API, schema, config, template, workflow, or None>`: `<what changes and who consumes it>`.

Implementation boundaries:

1. `<nearby file, behavior, cleanup, later phase, or follow-up>` stays out of scope because `<reason>`.
