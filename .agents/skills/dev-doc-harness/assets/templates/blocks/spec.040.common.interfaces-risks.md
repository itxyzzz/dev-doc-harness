## Interfaces, Data, and Control Flow

### Interfaces affected

1. Record public APIs, internal interfaces, CLI flags, config, schemas, generated artifacts, templates, or docs affected by the change.
2. State `None` when the change does not affect interfaces.

### Data, config, and persistence

1. Record data model, persistence, migration, configuration, release-identity, or rollout effects.
2. State `None` when the change does not affect data, config, or persistence.

### State and control flow

1. Record lifecycle, routing, state-machine, validation, request flow, jobs, concurrency, retries, or process-flow changes.
2. State `None` when the change does not affect state or control flow.

### Safety, security, privacy, migration, and rollback

1. Record safety, auth, data exposure, privacy, compliance, migration, rollout, rollback, destructive-operation, and operator-safety considerations.
2. State `None identified after repository-context review` only after checking the relevant code and docs.

## Risks and Rejected Alternatives

Use one block per risk, mitigation, or rejected option:

### `RISK-001` `<risk, ambiguity, compatibility concern, or rejected alternative>`

Decision or mitigation:

1. Record the mitigation, owner, reason for rejection, phase boundary, or follow-up condition.

Notes:

1. Add severity or likelihood only when it changes implementation, phase order, validation, rollout, or review.

Risk prompts:

1. Behavioral or compatibility regressions.
2. Migration, security, privacy, compliance, rollout, or operational concerns.
3. Over-scoping, under-specifying, or making the work too large for the selected lifecycle path.
4. Alternatives rejected because they duplicate canonical harness policy, import too much external process, or create reviewer burden.
