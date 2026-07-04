# Plan Amendment NNN: <Short Title>

Work ID: `<work-id>`
Short ID: `<short-id>`
Status: Proposed
Harness release: `<version or unknown>`
Schema: `schema:plan.amendment`
Policy references: `module:lifecycle`, `module:naming`, `module:freeze-gate`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Original plan reference

- Amendment ID: `AMD-001`
- File: `<plan, phase plan, spec, or snapshot path>`
- Section or task: `<heading, task ID, requirement ID, or decision ID>`
- Original instruction: `<approved text or concise summary>`

## Discovered issue

State the issue that makes the approved plan insufficient or unsafe to follow as written.

## Proposed change

State the replacement instruction or scope adjustment.

## Reason this change is necessary

State why the implementation cannot proceed under the approved plan.

## Impact assessment

| Area | Impact |
|---|---|
| Scope | |
| Acceptance criteria | |
| API/interface | |
| Data model/migration | |
| Security/privacy/compliance | |
| Tests | |
| Documentation | |
| Rollout/operations | |

## Approval

- Required: Yes
- Status: Proposed
- Approval evidence: `<operator approval message, approval commit, or None while proposed>`
- Superseded by: None

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during amendment approval, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Amendment approval | `<planning-commit-subject>` | `<changelog-heading>` | Approval commit for this amendment. |
| Amended implementation | `<commit-subject>` | `<changelog-heading>` | Add or update rows for implementation commits affected by this amendment. |

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`. Implementation remains paused until the approved amendment is frozen.
