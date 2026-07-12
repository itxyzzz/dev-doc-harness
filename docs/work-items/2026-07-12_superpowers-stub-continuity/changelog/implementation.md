# Changelog Source

## 2026-07-12_superpowers-stub-continuity -- prohibit bootstrapping compatibility pointers

Release target: `unreleased`
Package impact: `distributable`
Release-note: `include`

### Changed

- Required `docs/superpowers` to predate the current work and contain previous documentation packages before new compatibility documents may be added.
- Prohibited creating or seeding the directory to satisfy the continuity exception.
- Preserved the minimal title, status, and canonical work-item link schema for permitted pointer stubs.
- Strengthened the golden Superpowers traversal validation across canonical and operator-facing live surfaces.

### Removed

- Removed the repository's six current Superpowers pointer stubs so an absent `docs/superpowers` remains the intentional default state here.
