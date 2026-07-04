## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Newest-first entries grouped by change type; title snippets synchronized with planned commit subjects |
| Test cases | Snapshot | Yes/No | Before implementation | `snapshots/test-cases.snapshot.md` | Capture expected behavior before code changes |
| Testing guide delta | Living delta | Yes/No | During or after implementation | `deltas/testing-guide.delta.md` | Update if operator or test flow changes |
| Operator manual delta | Living delta | Yes/No | After implementation | `deltas/operator-manual.delta.md` | Update if runtime or operator behavior changes |
| API reference delta | Living delta | Yes/No | During or after API work | `deltas/api-reference.delta.md` | Required for public API changes |
| Architecture snapshot | Snapshot | Yes/No/Deferred | Before implementation or phase-plan drafting | `snapshots/architecture.snapshot.md` | Work-item-bound frozen decision snapshot when meaningful architecture decisions are made or depended on |
| Architecture summary delta | Living delta | Yes/No/Deferred | After review | `deltas/architecture-summary.delta.md` | Optional future input if long-lived architecture docs change outside this work-item snapshot flow |
