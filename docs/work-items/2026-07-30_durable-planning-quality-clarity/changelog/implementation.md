## 2026-07-30 docs: durable-planning-quality-clarity -- clarify plans and conformance

Release target: `unreleased`
Package impact: `distributable`
Release-note: `source-only`

#### Changed

- Applied one quality bar to all durable specs and plans, with a separate execution-size requirement only for phase plans.
- Clarified the plain-language and material-open-question rules, preserved material operator-provided source context in durable handoffs, and removed duplicate rejected-alternatives wording.
- Defined a lightweight evidence model: `SPEC` commitments are established by `VER` criteria, while `CHECK` records the method, result, and evidence without mandatory mapping tables.
- Regenerated affected plan templates and replaced the unreachable mandatory-matrix validator fixture with active local-link coverage.
