## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during phase-plan approval, and their title snippets must stay synchronized with the matching `docs/work-items/<work-id>/changelog/*.md` fragment headings or bullet-level snippets. Update this section before committing if implementation changes the subject wording. Root `CHANGELOG.md` is updated later by consolidation at an operator-owned checkpoint.

| Stage | Planned subject |
|---|---|
| Phase-plan approval | `<planning-commit-subject>` |
| Phase implementation | `<commit-subject>` |

One cohesive phase implementation commit is the default. Record an essential
exception or independently reviewable split as concise prose below.
