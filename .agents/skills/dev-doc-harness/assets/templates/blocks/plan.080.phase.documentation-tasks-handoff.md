## Documentation Tasks

List snapshot or delta artifacts this phase must create, update, or mark not applicable.

1. Changelog source: `docs/work-items/<work-id>/changelog/*.md` before each commit.
2. Root changelog consolidation: `CHANGELOG.md` at the operator-owned checkpoint when root changelog completeness is needed.
3. Test cases: `<snapshot path or not applicable with reason>`.
4. Testing guide delta: `<delta path or not applicable with reason>`.
5. Operator manual delta: `<delta path or not applicable with reason>`.
6. API reference delta: `<delta path or not applicable with reason>`.
7. Architecture snapshot or summary delta: `<path or not applicable with reason>`.

## Handoff output

Record what the implementing agent must report at phase completion:

1. Assigned scope.
2. Files inspected or changed.
3. Commands and tests run.
4. Assumptions, uncertainty, or residual risk.
5. Recommended next step.
6. De-facto sub-agent count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.
7. Exact blocker or explicit no-commit instruction plus current worktree status if planned implementation changes remain uncommitted.
8. Actual outputs, validation evidence, variance, commit state, and the inputs required for the documented next phase or completion activity.
