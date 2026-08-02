### 2026-07-30 refactor: artifact-style-ownership-cleanup -- consolidate readability policy

Release target: `unreleased`
Package impact: `distributable`
Release-note: `include`

#### Changed

- Moved author-facing plain-language guidance to Quality as `rule:quality.plain-language` and kept Quality as the Verification Criterion semantic owner.
- Focused Artifact Style on conditional presentation, consolidated its traceability guidance under the retained `rule:style.trace-density`, and preserved the scoped one-line reflow while correcting the identified whitespace.
- Regenerated the spec templates from their source block and updated policy validation to enforce the Quality owner without a definition-only modal exception.
