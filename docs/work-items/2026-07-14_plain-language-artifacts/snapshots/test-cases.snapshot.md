# Plain-language Artifact Policy Test Cases Snapshot

Work ID: `2026-07-14_plain-language-artifacts`
Status: Approved
Source spec: `spec_plain-language-artifacts.md`

## Test cases

### `TC-001` Canonical rule and required route

Given the current reusable harness package,

When the policy validator runs after the implementation,

Then it finds `rule:style.plain-language` in the artifact-style owner and confirms the small/medium drafting route requires `module:artifact-style`.

Covers:

1. `VER-001`.

### `TC-002` Shared prompt and generated outputs

Given the shared commitment-and-verification source block,

When templates are assembled and checked,

Then the source block, the small/medium specification template, and the large/phased specification template contain the same compact `must`/`should` cue and the assembler reports current output.

Covers:

1. `VER-002`.

### `TC-003` Active-surface regression fails

Given a synthetic active authoring Markdown path containing the prohibited legalistic modal outside the canonical definition,

When the focused validator assertion runs,

Then it reports a failure that identifies the path and policy-boundary violation.

Covers:

1. `VER-003`.

### `TC-004` Controlled exclusions remain intact

Given the canonical definition, an intentional validator fixture, a frozen work item, and `LICENSE`,

When the focused validator assertion runs,

Then those inputs are outside the disallowed active-authoring set and no repository file is rewritten.

Covers:

1. `VER-003`.

### `TC-005` Full regression and diff scope pass

Given all planned policy, route, source, and generated-output edits,

When the full policy validator, assembler check, modal scan, whitespace check, and reviewed diff run,

Then every command succeeds and the diff excludes `LICENSE` plus all pre-existing work items.

Covers:

1. `VER-001`.
2. `VER-002`.
3. `VER-003`.

## Approval

- Status: Approved
- Superseded by: None
