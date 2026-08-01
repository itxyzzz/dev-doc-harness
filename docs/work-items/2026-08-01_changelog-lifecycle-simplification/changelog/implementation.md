### 2026-08-01 refactor: changelog-lifecycle-simplification -- retain only implementation delivery records

Meta -- `unreleased` : `distributable`

#### Changed

- Moved current changelog authoring and consolidation policy into an implementation-only module and removed planning-approval changelog requirements from routing, freeze gates, templates, and validation.
- Replaced root entry metadata with a compact tagged line, removed every root planning-only entry, and retained frozen legacy-fragment parsing for compatibility.
- Added deterministic root migration and idempotency coverage, while keeping release-note curation manual and removing the obsolete root `TODO.md` package-boundary reference.
