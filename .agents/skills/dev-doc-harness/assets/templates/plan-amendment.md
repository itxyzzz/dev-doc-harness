# Plan Amendment NNN: <Short Title>

Work ID: `<YYYY-MM-DD-short-kebab-title>` or `<YYYY-MM-DD-ISSUE-short-kebab-title>`
Short ID: `<short-kebab-title>` or `<ISSUE-short-kebab-title>`
Status: Proposed
Harness release: `<version or unknown>`
Schema: `schema:plan.amendment`
Policy references: `module:lifecycle`, `module:freeze-gate`, `rule:lifecycle.variance-policy`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

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

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`. Implementation remains paused until the approved amendment is frozen.
