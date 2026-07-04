## Task Plan

Write one checkbox per implementation, test, validation, documentation, or handoff step. Tasks should be SMART:

1. Specific enough that a fresh implementation agent or delegated sub-agent knows which files, behavior, tests, docs, or decisions are in scope.
2. Measurable through a linked acceptance criterion, validation command, review finding, or explicit artifact update.
3. Achievable within the approved scope and one orchestration thread with bounded delegation.
4. Relevant to the approved spec, phase objective, acceptance criterion, risk, interface, documentation need, or commit boundary.
5. Time-bounded by lifecycle checkpoint, such as before editing, before validation, before commit, or during final review.

Order tasks by implementation dependency and reviewability. Label dependencies explicitly as `Dependencies: <None, task ids, artifacts, prior phase, or external event>`. Do not force vertical slices when shared setup, tests, refactors, or interface updates need to happen first.

- [ ] `<T-001>` Dependencies: `<None or task/artifact ids>`; `<specific task with files/scope>`; Traces: `<REQ/AC/risk/phase ids>`.
- [ ] `<T-002>` Dependencies: `<T-001 or None>`; `<specific validation, documentation, changelog, or review task>`; Traces: `<AC/risk/phase ids>`.
