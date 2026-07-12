# Superpowers Compatibility Guidance Spec

Work ID: `2026-07-07_superpowers-compat-guidance`
Short ID: `superpowers-compat-guidance`
Status: Approved
Harness release: `0.4+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:release`, `module:freeze-gate`, `rule:lifecycle.superpowers-compatibility`, `rule:lifecycle.work-item-architecture-decisions`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`, `rule:release.identity`, `rule:release.release-notes`

Artifact style baseline: this spec is final draft content for operator review. It keeps the compatibility boundary explicit, avoids a second source of truth, and records release-baseline findings discovered during investigation.

## Goal

Clarify how Dev Doc Harness should be used together with Superpowers after recent harness changes, and correct the current release-baseline mismatch that makes the harness validator look for the wrong development release notes.

## Source and Intent

Source input:

1. The operator asked to re-review how the harness plays together with Superpowers and perhaps revise README guidance.
2. The read-only investigation found that canonical harness policy is clearer than operator-facing guidance, while Superpowers defaults still point to full artifacts under `docs/superpowers`.
3. The operator clarified that the latest available release branch is `release/0.5`, so current development branches should remain on `0.5+`; after release `0.x`, `master` and other non-default branches remain on `0.x+` until release `0.x+1` is prepared. Release notes should exist for `0.4` and `0.5`, and no `0.6` notes should be created until that branch is created.

Desired operator/user outcome:

1. Operators and future agents can use Superpowers methodology without accidentally creating duplicate durable specs or plans outside the harness work-item package.
2. The repository validator checks the correct current development release baseline and no longer reports a missing `0.4+.md` release-note file.

Success summary:

1. The harness documents a concrete adapter flow: Superpowers may drive brainstorming, planning, TDD, execution, review, and finishing, while the harness remains canonical for artifact location, freeze gates, variance, changelog, and model/sub-agent notation.
2. Release identity and validation surfaces align with `release/0.5` having already been cut: current development branches remain on `0.5+` until `0.6` release preparation, `0.4.0.md` and `0.5.0.md` release notes are expected, and `0.6` notes are out of scope.

## Scope Boundary

### In scope

1. Audit and update the Superpowers compatibility guidance in current harness surfaces where needed:
   - `README.md`
   - `AGENTS.md`
   - `.agents/skills/dev-doc-harness/SKILL.md`
   - `.agents/skills/dev-doc-harness/references/artifact-contract.md`
   - `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
   - `.agents/skills/dev-doc-harness/docs/operator-note.md`
   - `docs/release-branch-process.md`
   - current templates or template source blocks only if a prompt gap would keep producing bad compatibility artifacts
2. Add or tighten validator coverage for the concrete Superpowers adapter flow when practical.
3. Correct current release-baseline surfaces so the marker, release policy, release branch process, release notes, and validator match the operator-confirmed `0.5+` development state.
4. Preserve existing harness workflow behavior: approval-first freeze gates, immutable planning snapshots, planned commit subjects, changelog-before-commit, and variance handling.

### Non-scope

1. Do not redesign Superpowers itself or edit installed Superpowers plugin files.
2. Do not introduce a separate adapter framework, new artifact hierarchy, or full rule-versioning system.
3. Do not create full durable specs or plans under `docs/superpowers`.
4. Do not create `0.6` release notes or advance the repository to a `0.6+` development marker.
5. Do not rewrite frozen historical work-item artifacts only to update release stamps, naming style, or compatibility language.

### Assumptions

1. `compatibility-improv` is the active working branch for this work item.
2. `release/0.5` exists remotely, so current development branches should remain on `0.5+` until `0.6` release preparation begins.
3. The release branch process in `docs/release-branch-process.md` is the current repository-local release process.
4. Current Superpowers skills are external workflow inputs; repository policy can adapt their output locations, but should not fork or duplicate their full text.

### Open questions

1. None identified after repository-context review. If implementation discovers that `0.5.0.md` cannot be curated from the changelog or existing release branch state, the implementation must stop and report the ambiguity instead of inventing release content.

## Repository Context

### Current state

1. `AGENTS.md` says Superpowers should provide normal software-development methodology while the harness supplies the artifact-location and lifecycle contract.
2. `.agents/skills/dev-doc-harness/references/artifact-contract.md` says full durable packages must live under `<work-item-path>`, and any `docs/superpowers` files may only be minimal pointer stubs with title, status, and a link to the canonical work-item package or artifact.
3. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md` says the harness freeze gate layers on top of Superpowers and pauses if another workflow would normally implement immediately after planning.
4. README introduces the relationship at a high level but does not show the concrete adapter flow or pointer-stub behavior.
5. `.agents/skills/dev-doc-harness/docs/operator-note.md` summarizes the harness for adopters but does not mention Superpowers explicitly.
6. Superpowers `brainstorming` and `writing-plans` default to `docs/superpowers/specs/` and `docs/superpowers/plans/`, and their flows normally commit or transition to execution choices.
7. The current validator passes its golden Superpowers traversal scenario but fails because `CURRENT_RELEASE` and the package `VERSION` still point at `0.4+` and the validator expects `.agents/skills/dev-doc-harness/docs/releases/0.4+.md`.
8. The repository has package release notes for `0.3.0` and `0.4.0`, but not `0.5.0`.

### Evidence read

1. `README.md`
2. `AGENTS.md`
3. `.agents/skills/dev-doc-harness/SKILL.md`
4. `.agents/skills/dev-doc-harness/VERSION`
5. `.agents/skills/dev-doc-harness/references/artifact-contract.md`
6. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
7. `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`
8. `.agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md`
9. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
10. `.agents/skills/dev-doc-harness/references/release-policy.md`
11. `.agents/skills/dev-doc-harness/docs/operator-note.md`
12. `.agents/skills/dev-doc-harness/docs/releases/0.4.0.md`
13. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`
14. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
15. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
16. `.agents/skills/dev-doc-harness/assets/templates/architecture-snapshot.md`
17. `docs/release-branch-process.md`
18. `CHANGELOG.md`
19. `docs/work-items/2026-05-31-work-items-artifact-root/spec-work-items-artifact-root.md`
20. `docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md`
21. `docs/work-items/2026-06-23-documentation-improvements/plan-amendment-001-notion-backlog-documentation-improvements.md`
22. Installed Superpowers skills: `using-superpowers`, `brainstorming`, `writing-plans`, `executing-plans`, `subagent-driven-development`, `test-driven-development`, `requesting-code-review`, `verification-before-completion`, `using-git-worktrees`, and `finishing-a-development-branch`.
23. Commands run during investigation: `git status -sb`, `git branch -a`, `rg` searches for Superpowers and release wording, and `python .agents\skills\dev-doc-harness\scripts\test_harness_policy.py`.

### Constraints and compatibility

1. The selected repository policy remains `economy-default`; this work must not switch it.
2. Superpowers instructions say user instructions have priority, so repository harness rules may adapt Superpowers default paths and transition points.
3. The harness freeze gate must interrupt any Superpowers flow that would otherwise immediately commit full planning docs or proceed to implementation.
4. The full durable artifact source of truth remains `docs/work-items/2026-07-07_superpowers-compat-guidance/`.
5. `docs/superpowers` artifacts, if created, must be pointer stubs only and must not duplicate full specs or plans.
6. The validator baseline must become compatible with the current release process: `0.5+` development marker for current development branches, `0.4.0.md` and `0.5.0.md` release notes, no `0.6` release notes.

## Requirements

### `REQ-001` Document the Superpowers adapter flow

Rationale:

1. Operators need to know how Superpowers and the harness compose in practice, not only that they are compatible.

Acceptance links:

1. Covered by `AC-001`, `AC-002`, and `AC-003`.

Notes:

1. The guidance must state that Superpowers owns methodology and the harness owns durable artifact location and lifecycle.
2. The guidance must describe how to handle Superpowers default `docs/superpowers` outputs without creating duplicate durable artifacts.

### `REQ-002` Preserve harness freeze-gate authority over planning-to-execution transitions

Rationale:

1. Superpowers skills often transition from design to plan, then from plan to execution. The harness must preserve operator review and approval before implementation.

Acceptance links:

1. Covered by `AC-002` and `AC-004`.

Notes:

1. The implementation should clarify that approved Superpowers-derived content is copied or converted into the harness work-item folder before the harness freeze gate.
2. A Superpowers execution choice must happen after the harness freeze gate and fresh operator authorization, not before.

### `REQ-003` Align operator-facing and package-local compatibility surfaces

Rationale:

1. README, `AGENTS.md`, router guidance, lifecycle rules, freeze rules, and the operator note should not teach different mental models.

Acceptance links:

1. Covered by `AC-003` and `AC-005`.

Notes:

1. Implementation should prefer compact clarifications over duplicating canonical policy.
2. Canonical policy remains in `module:lifecycle` and `module:freeze-gate`; README and operator-note text should point to those owners.

### `REQ-004` Correct current release-baseline expectations

Rationale:

1. The validator currently fails because it expects development notes for `0.4+`, but the latest available release branch is `release/0.5` and current development branches should remain on `0.5+` until `0.6` release preparation.

Acceptance links:

1. Covered by `AC-006`, `AC-007`, and `AC-008`.

Notes:

1. Implementation should update the package marker, release policy examples, validator constants or logic, and package-local release notes as needed.
2. Implementation should update `docs/release-branch-process.md` so future release preparation keeps release marker, release notes, release policy, and validator expectations consistent.
3. `0.6` release notes are explicitly out of scope.

### `REQ-005` Keep validator coverage high-signal

Rationale:

1. The validator should prevent recurrence of the adapter-flow and release-baseline confusion without becoming a semantic parser.

Acceptance links:

1. Covered by `AC-004`, `AC-006`, and `AC-009`.

Notes:

1. Superpowers checks should verify discoverability plus the concrete pointer-stub/canonical-package rule when practical.
2. Release checks should align with the release process and operator-confirmed branch state.

## Acceptance Criteria

### `AC-001` Compatibility guidance names the split of responsibility

Verifies:

1. `REQ-001`

Method:

1. Manual review of changed compatibility surfaces confirms the same split appears consistently: Superpowers methodology; harness artifact location, freeze gates, variance, changelog, and model/sub-agent notation.

### `AC-002` Adapter flow preserves canonical work-item artifacts

Verifies:

1. `REQ-001`
2. `REQ-002`

Method:

1. Manual review confirms guidance tells agents to copy or convert approved Superpowers specs/plans into `docs/work-items/<work-id>/` before implementation and to keep `docs/superpowers` files as pointer stubs only when needed.

### `AC-003` Operator-facing docs are coherent

Verifies:

1. `REQ-001`
2. `REQ-003`

Method:

1. `rg -n "Superpowers|docs/superpowers|pointer stub|freeze gate|0.5\\+|0\\.x\\+" README.md AGENTS.md .agents/skills/dev-doc-harness docs/release-branch-process.md` shows the expected compatibility and release-baseline language in canonical and operator-facing surfaces without contradictory current-development guidance.

### `AC-004` Planning-to-execution transition remains gated

Verifies:

1. `REQ-002`
2. `REQ-005`

Method:

1. Manual review and validator output confirm that a Superpowers planning workflow must still pause for the harness draft review and approval freeze before implementation.

### `AC-005` Package-local operator note helps downstream adopters

Verifies:

1. `REQ-003`

Method:

1. Manual review of `.agents/skills/dev-doc-harness/docs/operator-note.md` confirms downstream adopters can understand how Superpowers should be used with copied harness packages.

### `AC-006` Current release marker and release policy are aligned

Verifies:

1. `REQ-004`
2. `REQ-005`

Method:

1. Manual review confirms `.agents/skills/dev-doc-harness/VERSION`, `.agents/skills/dev-doc-harness/references/release-policy.md`, `docs/release-branch-process.md`, and `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` all treat current development as `0.5+` and preserve the generic rule that development branches remain on `0.x+` until `0.x+1` release preparation.

### `AC-007` Package release notes match expected released minors

Verifies:

1. `REQ-004`

Method:

1. Manual review confirms `.agents/skills/dev-doc-harness/docs/releases/0.4.0.md` and `.agents/skills/dev-doc-harness/docs/releases/0.5.0.md` exist, and no `.agents/skills/dev-doc-harness/docs/releases/0.6.0.md` or `.agents/skills/dev-doc-harness/docs/releases/0.6+.md` is created.

### `AC-008` Harness validator passes after implementation

Verifies:

1. `REQ-004`
2. `REQ-005`

Method:

1. Run `python .agents\skills\dev-doc-harness\scripts\test_harness_policy.py`; expected result is all checks pass with exit code `0`.

### `AC-009` Validator catches the compatibility scenario at the right level

Verifies:

1. `REQ-005`

Method:

1. Manual review of `test_harness_policy.py` confirms the golden Superpowers scenario or an adjacent structural check covers the canonical package plus pointer-stub rule without parsing full natural-language policy.

## Architecture Decisions

Architecture snapshot status:

1. `Required`: this work changes agentic workflow boundaries and release-validation behavior, so `snapshots/architecture.snapshot.md` records the adapter decision.

Decision summary:

1. Drivers: prevent duplicate durable artifacts, preserve Superpowers methodology, preserve harness approval gates, and remove release-baseline validator noise.
2. Constraints: repository-local AGENTS instructions have priority over Superpowers defaults; release process must preserve that after release `0.x`, development branches remain on `0.x+` until `0.x+1` release preparation; package-local release notes live under `.agents/skills/dev-doc-harness/docs/releases/`.
3. Selected approach: document an adapter flow instead of redesigning either workflow. Superpowers content is converted into harness artifacts; `docs/superpowers` remains pointer-only when present.
4. Affected boundaries: README, root instructions, harness router, lifecycle and freeze policy references, operator note, validator, release policy, version marker, and package-local release notes.
5. Rejected alternatives: duplicating full artifacts under `docs/superpowers`; replacing Superpowers methodology; creating `0.6` release notes early; leaving the validator red as accepted baseline noise.
6. Validation cues: acceptance criteria `AC-001` through `AC-009` and the harness validator.

Repository-level durable architecture documents such as `ARCHITECTURE.md` are future work for a separate harness extension.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. Operator-facing README guidance may change.
2. Root `AGENTS.md` compatibility guidance may change if needed for bootstrap clarity.
3. `.agents/skills/dev-doc-harness/SKILL.md` router guidance may change if needed to route Superpowers compatibility work more concretely.
4. Canonical references may change in `artifact-contract.md`, `planning-freeze-gates.md`, and `release-policy.md`.
5. Validator expectations in `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` may change.
6. `docs/release-branch-process.md` should change so future release branch preparation keeps the marker, release policy, release notes, and validator expectations synchronized.
7. Template source blocks may change only if implementation finds that current prompts would keep generating bad Superpowers compatibility artifacts.

### Data, config, and persistence

1. `.agents/skills/dev-doc-harness/VERSION` should change from `0.4+` to `0.5+`.
2. `.agents/skills/dev-doc-harness/docs/releases/0.5.0.md` should be added or restored as package-local release notes for the already-cut release.
3. No application data, persistence layer, schema, or runtime configuration changes are expected.

### State and control flow

1. The documented workflow state changes from vague coexistence to an explicit adapter sequence:
   1. Use Superpowers methodology when active.
   2. Convert approved Superpowers content into harness work-item artifacts.
   3. Keep `docs/superpowers` as pointer stubs only when required.
   4. Run the harness draft review and approval freeze gate.
   5. Start Superpowers execution only after fresh post-freeze operator authorization.
2. Release-validation flow should check the current development marker and expected released-minor notes rather than expecting a notes file named after a development marker.

### Safety, security, privacy, migration, and rollback

1. No security, privacy, or migration impact is expected.
2. Rollback is a normal revert of the implementation commit because changes are documentation, validator, release marker, and package-local release notes.
3. The work must not remove historical release notes or rewrite frozen work-item artifacts.

## Risks and Rejected Alternatives

### `RISK-001` Duplicating Superpowers and harness policy

Decision or mitigation:

1. Keep canonical rules in lifecycle, freeze-gate, and release references; use README and operator note for compact operator guidance.

Notes:

1. Excess duplication would increase drift risk the next time Superpowers or the harness changes.

### `RISK-002` Weak adapter guidance still lets agents create full `docs/superpowers` artifacts

Decision or mitigation:

1. Include the pointer-stub rule in the operator-facing flow and add high-signal validation coverage when practical.

Notes:

1. The prior work item `2026-05-31-work-items-artifact-root` already recorded this as a real compatibility risk.

### `RISK-003` Release notes for `0.5.0` may need changelog curation

Decision or mitigation:

1. Implementation must curate from root `CHANGELOG.md` and the release process. If the source entries are ambiguous, stop and report instead of inventing content.

Notes:

1. This avoids treating release notes as an independent feature history.

### `RISK-004` Overcorrecting the validator into a semantic policy checker

Decision or mitigation:

1. Prefer structural checks for expected files, route discoverability, and key compatibility anchors.

Notes:

1. This preserves the existing validator design direction.

### `RISK-005` Creating `0.6` release artifacts too early

Decision or mitigation:

1. Explicitly limit this work to `0.5+` development and `0.5.0` release notes. `0.6` notes wait for the future release branch process.

Notes:

1. This follows the operator's clarification.

## Planned commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `spec: superpowers-compat-guidance -- approve adapter guidance plan` | `2026-07-07_superpowers-compat-guidance -- approve adapter guidance plan` | Approval commit for this spec, plan, and snapshots. |
| Implementation | `docs: superpowers-compat-guidance -- document adapter flow and fix release baseline` | `2026-07-07_superpowers-compat-guidance -- document adapter flow and fix release baseline` | Expected implementation commit for guidance, validator, version marker, release policy, and `0.5.0` notes. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Newest-first entries synchronized with the planned approval and implementation subjects. |
| Test cases | Snapshot | Yes | Before implementation | `snapshots/test-cases.snapshot.md` | Captures adapter-flow and release-baseline validation expectations. |
| Testing guide delta | Living delta | No | Not applicable | None | The validator command is already documented; implementation may update existing guidance directly if needed. |
| Operator manual delta | Living delta | No | Not applicable | None | README and package operator note are expected to receive direct updates. |
| API reference delta | Living delta | No | Not applicable | None | No public API changes. |
| Architecture snapshot | Snapshot | Yes | Before implementation | `snapshots/architecture.snapshot.md` | Records the compatibility adapter and release-validation boundary. |
| Architecture summary delta | Living delta | No | Not applicable | None | Repository-level architecture docs remain out of scope. |

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Requirements are specific, relevant, bounded, and linked to acceptance criteria.
- [x] Acceptance criteria are observable, testable, and tied to requirements or scope items.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Interfaces, data, control flow, and safety/privacy/migration impacts are checked.
- [x] Risks and rejected alternatives are listed or explicitly absent after review.
- [x] Documentation artifact matrix decisions have paths or reasons.
- [x] Planned commit subjects and changelog title snippets are synchronized.
- [x] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain before approval or handoff.

## Approval

- Status: Approved
- Superseded by: None
