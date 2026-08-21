# Route Name Simplification Test Cases

Work ID: `2026-08-21_route-name-simplification`
Status: Approved

| Scenario | Given | When | Then |
|---|---|---|---|
| `scenario:medium-first-cutover` | The former `small/medium` route owns `.small.` blocks and `small-medium-*` assets | `TASK-001` completes before `TASK-002` starts | The former medium route owns only `medium` names, freeing `small` without a collision. |
| `scenario:small-second-cutover` | `TASK-001` has passed its targeted checks | `TASK-002` renames the former lean route | The former lean route owns only `small` names, and no obsolete lean route identifier remains active. |
| `scenario:schemas-and-generated-templates` | Manifests, blocks, assembler registry, and validator use the canonical names | The assembler and policy validator run | Generated outputs are current and all route schemas, paths, and assertions agree. |
| `scenario:large-route-preservation` | The active harness contains large/phased policy and template paths | The migration completes | `large/phased` and `large-phased` remain unchanged. |
| `scenario:historical-boundary` | Frozen work items, existing changelog entries, and release notes contain prior terminology | The scoped diff is reviewed | Historical files remain unchanged; only this work item's new evidence may appear under `docs/work-items/`. |
