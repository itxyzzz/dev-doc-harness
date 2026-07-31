## 2026-07-31 docs: lifecycle-stage-boundaries -- clarify freeze lifecycle stages

Release target: `unreleased`
Package impact: `distributable`
Release-note: `source-only`

#### Changed

- Defined canonical lifecycle-stage boundaries, made the approval commit the only formal planning-freeze route, and preserved fresh authorization and variance boundaries.
- Updated template source blocks and regenerated templates to render `Next lifecycle stage` instead of task-level transition fields; the policy validator now enforces that contract and rejects retired handoff-snapshot wording.
- Confirmed that the intentionally simplified README remains semantically compatible and left it unchanged.
- Used the assembler's required `--write` mode before its freshness check; this is equivalent to the planned regeneration step.
- Included the operator-authorized formatting-only line-wrap change in `references/evidence-and-report-artifacts.md` without changing its semantics.
