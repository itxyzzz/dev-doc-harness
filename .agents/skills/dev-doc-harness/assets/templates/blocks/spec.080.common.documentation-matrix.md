## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Newest-first entries grouped by change type; title snippets synchronized with planned commit subjects |
| Test cases | Snapshot | Yes/No | Before implementation | `snapshots/test-cases.snapshot.md` | Capture expected behavior before code changes |
| Testing guide delta | Living delta | Yes/No | During or after implementation | `deltas/testing-guide.delta.md` | Update if operator or test flow changes |
| Operator manual delta | Living delta | Yes/No | After implementation | `deltas/operator-manual.delta.md` | Update if runtime or operator behavior changes |
| API reference delta | Living delta | Yes/No | During or after API work | `deltas/api-reference.delta.md` | Required for public API changes |
| Architecture snapshot | Snapshot | Yes/No | Before or after design stabilization | `snapshots/architecture.snapshot.md` | Work-item-bound decision snapshot |
| Architecture summary delta | Living delta | Yes/No | After review | `deltas/architecture-summary.delta.md` | Update if long-lived architecture docs change |
