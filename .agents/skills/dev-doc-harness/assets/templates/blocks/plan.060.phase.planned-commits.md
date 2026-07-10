## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during phase-plan approval, and their title snippets must stay synchronized with the matching `docs/work-items/<work-id>/changelog/*.md` fragment headings or bullet-level snippets. Update this section before committing if implementation changes the subject wording. Root `CHANGELOG.md` is updated later by consolidation at an operator-owned checkpoint.

Phase plan approval:

1. Planned subject: `<planning-commit-subject>`.
2. Changelog title or snippet: `<changelog-heading>`.
3. Notes: `Approval commit for this phase plan.`

Phase implementation:

1. Planned subject: `<commit-subject>`.
2. Changelog title or snippet: `<changelog-heading>`.
3. Notes: `<add one block per expected phase implementation, validation, release, or maintenance commit>`.
