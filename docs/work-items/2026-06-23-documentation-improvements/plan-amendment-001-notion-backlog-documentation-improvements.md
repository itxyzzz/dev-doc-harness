# Plan Amendment 001: Notion Backlog

Work ID: `2026-06-23-documentation-improvements`
Short ID: `documentation-improvements`
Status: Approved
Harness release: `0.3.0`
Schema: `schema:plan.amendment`
Policy references: `module:lifecycle`, `module:freeze-gate`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Original plan reference

- File: `docs/work-items/2026-06-23-documentation-improvements/plan-documentation-improvements.md`
- Section or task: `## Tasks`
- Original instruction: Rewrite `TODO.md` into a normalized backlog format with priority suggestions and current review follow-ups.

## Discovered issue

The operator clarified after implementation that `TODO.md` should not remain the durable backlog surface. Instead, the repository backlog should move to Notion cards, completed items from the current conversation should be removed from the active backlog, and remaining work should be re-reviewed for priority, grouping, dependency, and complexity.

This is broader than the approved implementation. The approved plan preserved an in-repository `TODO.md`; the new direction removes that file and introduces an external Notion backlog as the active tracking surface.

## Proposed change

Replace the repository-local `TODO.md` backlog with Notion cards.

Implementation should:

- Use the Notion MCP server to create a `Dev Doc Harness Backlog` database or equivalent private Notion task collection if no target parent is provided.
- Include properties for status, group, priority, complexity, source, and dependency notes.
- Remove items completed in the current documentation-improvements work from the active Notion backlog.
- Review the committed `TODO.md` content against what was actually delivered in commit `9379de8` and clarify the remaining work before card creation.
- Keep directly dependent work together in one Notion card when splitting would create artificial ordering overhead.
- Re-rank priorities within groups by marginal value rather than copying the previous group-level priority.
- Add complexity estimates to every card.
- Delete root `TODO.md` from the repository after the Notion cards are created and verified.
- Update `CHANGELOG.md` before the implementation commit.
- Commit the repository deletion and changelog with the planned amended implementation subject.

Proposed card groups and initial priority/complexity guidance:

| Card | Group | Priority | Complexity | Notes |
|---|---|---|---|---|
| Run disposable large-work trial | Validation and adoption evidence | P1 | M | Highest marginal value because it validates the harness end to end before adding more polish. |
| Add CI wiring for harness validation | Validation and adoption evidence | P1 | S | Shared safety net for current validator; pre-commit remains separate and lower priority. |
| Track validation failures and learnings | Validation and adoption evidence | P2 | S | Valuable after the trial or real failures exist; avoid inventing taxonomy too early. |
| Test Superpowers conversion flow | Compatibility and adapters | P1 | M | Directly tests an advertised compatibility path; should include invocation, output location, pointer stubs, and freeze interruption. |
| Document Superpowers copy/convert guidance | Compatibility and adapters | P2 | S | Dependent on the conversion test; keep in the same card as the test if the guidance is small. |
| Verify spec-kit adapter mechanics | Compatibility and adapters | P2 | M | Discovery before adapter work; include preset, override, template, and extension behavior. |
| Build minimal spec-kit adapter if supported | Compatibility and adapters | P3 | L | Dependent on mechanics verification; lower priority until spec-kit demand is proven. |
| Add planning-only PR checklist | PR and review workflow | P2 | S | Clarify this adds PR presentation guidance, not a new freeze behavior; existing harness already supports plan-only PR checkpoints. |
| Define PR artifact and evidence presentation | PR and review workflow | P2 | M | Combine artifact links, validation output, amendments, and source-vs-derived evidence because they shape the same PR contract. |
| Split validator if growth pressure continues | Validator tooling | P2 | M | Conditional refactor only after new checks make the current file hard to review. |
| Create optional portable artifact validator | Validator tooling | P2 | M | Useful only if cross-platform adoption matters; should stay structural and standard-library based. |
| Decide pre-commit wiring after CI | Validator tooling | P3 | S | Dependent on CI experience; opt-in local friction is lower marginal value than CI. |
| Create examples library | Examples and artifact templates | P2 | M | Depends on a disposable trial and real examples; examples must remain illustrative. |
| Define snapshot and living-delta templates | Examples and artifact templates | P2 | M | Group closely related artifact-shape templates; defer detailed schemas until usage proves need. |
| Define evidence-heavy report templates | Examples and artifact templates | P3 | M | Lower priority until evidence-heavy work appears repeatedly. |
| Design in-team distribution and versioning | Governance | P3 | XL | Combine distribution, cross-repo versioning, migration, audit, and rollback because they are one governance problem. |
| Harden testing documentation policy | Governance | P3 | L | High eventual value but broad process impact; needs more work-item evidence. |
| Define amendment approval markers and documentation debt tracking | Governance | P3 | M | Combine lightweight governance markers that need more examples before policy hardening. |
| Define retention, archive, and older-repo migration policy | Governance | P3 | L | Keep together because they all govern historical artifact lifecycle. |
| Add bootstrapping script | Adoption automation | P3 | M | Only after repeated manual setup pain is demonstrated. |
| Review public agentic-instruction repositories | Research parking lot | P3 | M | Timebox and extract only portable patterns. |
| Confirm model classes in operator environment | Research parking lot | P3 | S | Do only when concrete model names become necessary. |

## Reason this change is necessary

The approved plan's `TODO.md` cleanup no longer matches the operator's desired repository shape. Keeping both a repository `TODO.md` and Notion cards would create duplicate backlog sources. Deleting `TODO.md` without creating the Notion cards first would lose useful future-work context.

## Impact assessment

| Area | Impact |
|---|---|
| Scope | Adds external Notion backlog creation and repository `TODO.md` deletion. |
| Acceptance criteria | Adds successful Notion card creation, card review, and verified `TODO.md` removal. |
| API/interface | No code API changes; changes the backlog tracking interface from repository Markdown to Notion. |
| Data model/migration | Migrates backlog items into Notion card properties and page content. |
| Security/privacy/compliance | Uses authenticated Notion MCP; cards should avoid secrets and include only repository backlog content. |
| Tests | Harness validation and git diff checks remain required; Notion creation must be verified by returned Notion URLs or fetched database rows. |
| Documentation | `CHANGELOG.md` records the migration; root `TODO.md` is removed. |
| Rollout/operations | Notion becomes the active backlog surface; repository history preserves prior `TODO.md` content. |

## Approval

- Required: Yes
- Status: Approved
- Superseded by: not applicable

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during amendment approval, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Amendment approval | `documentation-improvements amendment 001: move backlog to Notion` | `2026-06-23-documentation-improvements: move backlog to Notion` | Approval commit for this amendment. |
| Amended implementation | `documentation-improvements docs: migrate backlog to Notion` | `2026-06-23-documentation-improvements: migrate backlog to Notion` | Commit for deleting `TODO.md` and updating `CHANGELOG.md` after Notion cards are created and verified. |

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`. Implementation remains paused until the approved amendment is frozen.
