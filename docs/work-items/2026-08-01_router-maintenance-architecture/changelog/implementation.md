## 2026-08-01 refactor: router-maintenance-architecture -- isolate maintenance and freeze context

Release target: `unreleased`
Package impact: `distributable`
Release-note: `include`

#### Changed

- Made `SKILL.md` the sole operational router and moved maintenance-only module ownership to `references/maintenance-architecture.md`.
- Removed duplicate routing and unused maintenance taxonomy content while preserving module ownership, dependency, validation, and lifecycle-maintenance guidance.
- Made naming an explicit planning input, deferred freeze-gate references from draft plan templates, regenerated the templates, and strengthened structural validation for those boundaries.
