## Architecture Decisions

Use this section for work-item architecture, not general repository architecture policy. Capture constraints that come from the problem statement and deliberate tradeoffs selected during planning.

Architecture snapshot status:

1. `Required`: use `snapshots/architecture.snapshot.md` when meaningful architecture decisions are made or depended on.
2. `Not applicable`: record the reason when the work has no architectural decision beyond local implementation mechanics.
3. `Deferred`: record the owner or event that must resolve the snapshot before implementation, phase planning, or approval.

Decision summary:

1. Drivers: `<user, operator, product, technical, compliance, operational, migration, or review forces>`.
2. Constraints: `<repository, interface, data, config, infra, agentic, security, privacy, rollout, or phase constraints>`.
3. Selected approach: `<architecture direction chosen before planning execution>`.
4. Affected boundaries: `<repositories, components, interfaces, schemas, config, infra, docs, agents, or phases>`.
5. Rejected alternatives: `<alternatives and why they were rejected>`.
6. Validation cues: `<commands, review checks, acceptance criteria, or later phase signals that prove the decision held>`.

Repository-level durable architecture documents such as `ARCHITECTURE.md` are future work for a separate harness extension.
