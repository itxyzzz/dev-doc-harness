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
- Section or task: `<heading, TASK ID, SPEC ID, VER ID, CHECK ID, or DEC ID>`
- Original instruction: `<approved text or concise summary>`

## Discovered issue

State the material change: outcome, architecture, API, data, security, privacy,
compliance, scope, or invalidated evidence.

## Proposed change

State the replacement instruction or scope adjustment.

## Impact assessment

State the affected outcome, proof, interfaces, data, risk, and documentation.

## Approval

- Required: Yes
- Status: Proposed
- Approval evidence: `<operator approval message, approval commit, or None while proposed>`
- Superseded by: None

## Planned commits

Use `rule:lifecycle.commit-message-format`; keep the matching changelog fragment
in sync.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Amendment approval | `<planning-commit-subject>` | `<changelog-heading>` | Approval commit for this amendment. |
| Amended implementation | `<commit-subject>` | `<changelog-heading>` | Add or update rows for implementation commits affected by this amendment. |

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`. Implementation remains paused until the approved amendment is frozen.
