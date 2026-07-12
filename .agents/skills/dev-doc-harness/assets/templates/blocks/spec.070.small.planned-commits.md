## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during spec and plan review, and their title snippets must stay synchronized with the matching `docs/work-items/<work-id>/changelog/*.md` fragment headings or bullet-level snippets. Root `CHANGELOG.md` is updated later by consolidation at an operator-owned checkpoint.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `<planning-commit-subject>` | `<changelog-heading>` | Approval commit for this spec and related planning artifacts. |
| Implementation | `<commit-subject>` | `<changelog-heading>` | Replace with the expected implementation commit subject, or defer to the plan with a reason. |
