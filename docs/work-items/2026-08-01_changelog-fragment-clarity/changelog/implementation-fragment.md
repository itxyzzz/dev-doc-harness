### 2026-08-01 refactor: changelog-fragment-clarity -- clarify current fragment lifecycle

Meta -- `unreleased` : `distributable`

#### Changed

- Renamed current implementation and phase changelog examples to explicit `-fragment` filenames while preserving generic discovery for frozen historical paths.
- Moved frozen legacy-format and root-migration guidance into a final compatibility section, leaving routine authoring and consolidation guidance first.
- Normalized root changelog entry separators deterministically and added regression coverage for spacing, release-heading preservation, and idempotent reruns.
