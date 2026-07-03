## Requirements

A requirement defines scope: what the work must provide, change, or preserve. Keep each requirement specific, achievable, relevant to the desired outcome, bounded by lifecycle timing, and testable through acceptance criteria.

Use one block per requirement:

### `REQ-001` `<specific requirement>`

Rationale:

1. State why this requirement belongs in scope and what value or risk it addresses.

Acceptance links:

1. Link to acceptance criterion IDs, or write a short placeholder such as `Covered by AC-001`.

Notes:

1. Add constraints, dependencies, deferrals, phase expectations, or implementation-neutral details when helpful.

Requirement quality prompts:

1. Specific: names the concrete behavior, documentation surface, interface, or decision.
2. Achievable: fits the approved work size or phase structure.
3. Relevant: traces back to the stated operator/user outcome.
4. Bounded: has clear lifecycle timing such as before freeze, during validation, or before commit.
5. Testable: connects to at least one acceptance criterion.

## Acceptance Criteria

An acceptance criterion defines observable verification: how a reviewer, command, manual check, test, or operator acceptance can tell that a requirement has been satisfied.

Use one block per criterion:

### `AC-001` `<observable outcome or scenario>`

Verifies:

1. Link to requirement IDs or a named scope item.

Method:

1. Name the command, manual check, review finding, phase completion signal, or operator acceptance path.

Optional example shape:

1. Given `<initial context>`, when `<event or action>`, then `<observable outcome>`.
2. Use this only when it makes the outcome clearer than prose.

Acceptance quality prompts:

1. Measurable: the outcome can be observed or reviewed.
2. Specific: it names the expected result, not only the implementation activity.
3. Time-bounded: it says when verification happens, such as before implementation, across phases, during validation, or before commit.
4. Independent enough: each criterion can be checked without relying on unrelated criteria where practical.
