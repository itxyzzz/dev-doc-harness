### `2026-08-25 refactor: route-name-simplification -- simplify active harness route names`

Meta -- `unreleased` : `distributable`

#### Changed

- Renamed the active planning routes and their template, schema, assembly, and validator namespaces to `small` and `medium`, while preserving `large/phased` and immutable historical records.
- Removed the retired medium spec-only planning exception, regenerated templates, and aligned the policy validator with the combined small and medium package contract.

#### Fixed

- Removed trailing whitespace from active harness guidance.