# Plan Amendment NNN: <Short Title>

Work ID: `<work-id>`
Short ID: `<short-id>`
Status: Proposed
Harness release: `<version or unknown>`
Schema: `schema:plan.amendment`
Policy references: `module:lifecycle`, `module:naming`, `module:freeze-gate`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Original plan reference

- File:
- Section or task:
- Original instruction:

## Discovered issue

Describe the issue that makes the approved plan insufficient or unsafe to follow as written.

## Proposed change

Describe the replacement instruction or scope adjustment.

## Reason this change is necessary

Explain why the implementation cannot proceed under the approved plan.

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
- Status: Proposed / Approved / Rejected / Superseded
- Superseded by: record only when this artifact is superseded

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during amendment approval, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Amendment approval | `<planning-commit-subject>` | `<changelog-heading>` | Approval commit for this amendment. |
| Amended implementation | `<commit-subject>` | `<changelog-heading>` | Add or update rows for implementation commits affected by this amendment. |

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`. Implementation remains paused until the approved amendment is frozen.
