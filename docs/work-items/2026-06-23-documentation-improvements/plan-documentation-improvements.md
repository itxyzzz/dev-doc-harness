# Documentation Improvements Plan

Work ID: `2026-06-23-documentation-improvements`
Short ID: `documentation-improvements`
Status: Approved
Harness release: `0.3.0`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Implementation summary

Implement the documentation improvements as a focused documentation pass. Keep canonical policy in the existing routed references and use README, TODO, and the new package-local operator note as summary and adoption surfaces.

The package-local operator note should be compact enough to travel with the distributable package without becoming a second manual. It should tell adopters what to copy, how agents should use the harness, where the pause points are, and which files own the canonical contract.

The README change should serve non-operator readers quickly, then flow into the existing operator explanation. The validator-boundary change should make future validation direction clearer without blocking useful structural checks. The TODO revision should normalize item shape and suggest priority so the backlog is actionable.

## Files and interfaces

Expected implementation edits:

- `README.md`: add concise portfolio-oriented project summary and keep existing operator guidance accurate.
- `TODO.md`: reorganize into common item format with priority suggestions and current review follow-ups.
- `.agents/skills/dev-doc-harness/docs/operator-note.md`: add compact package-local operator note.
- `.agents/skills/dev-doc-harness/references/policy-architecture.md`: clarify validator evolution boundary near the validation model or route/duplication guidance.
- `.agents/skills/dev-doc-harness/SKILL.md`: optional short pointer to the package-local operator note if needed for discoverability.
- `CHANGELOG.md`: add newest-first entries before approval and implementation commits.

Interfaces expected to remain stable:

- Harness release remains `0.3.0`.
- Distributable package boundary remains root `AGENTS.md` plus `.agents/`.
- Existing validation command remains `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`.
- No schema, API, CLI, runtime, or release-note interface changes are expected.

## Model and Sub-agent Strategy

Current orchestration: GPT-5 Codex in this thread; reasoning effort not explicitly exposed.
Fit assessment: Low-to-medium complexity, low runtime risk, moderate documentation consistency risk, small blast radius, and no need for parallel throughput.
Recommended change: None.

Sub-agents: None. The work touches tightly related documentation surfaces where consistency is best maintained by the orchestration thread.

## Tasks

- [ ] Add a concise portfolio-oriented summary near the top of `README.md`.
- [ ] Add `.agents/skills/dev-doc-harness/docs/operator-note.md` as a package-local operator note with summary-level adoption guidance and canonical-reference pointers.
- [ ] Decide whether `SKILL.md` needs a brief discoverability pointer to the package-local operator note; add one only if it improves package-local usability without bloating the router.
- [ ] Clarify validator evolution boundary in `.agents/skills/dev-doc-harness/references/policy-architecture.md`.
- [ ] Rewrite `TODO.md` into a normalized backlog format with priority suggestions and consistent item structure.
- [ ] Ensure `TODO.md` includes the current review follow-ups: package-local operator note, portfolio README summary, validator-boundary clarification, CI/pre-commit wiring, disposable large-work trial, examples library, validation-failure tracking, validator split, and portable validator.
- [ ] Preserve explicit out-of-scope status for license changes in this work item.
- [ ] Update `CHANGELOG.md` before the implementation commit with the approved implementation title snippet.
- [ ] Run validation commands and inspect the diff for accidental policy duplication or package-boundary drift.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during plan approval, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets. Update this table before committing if implementation changes the subject wording.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `documentation-improvements spec: document planned documentation updates` | `2026-06-23-documentation-improvements: document planned documentation updates` | Approval commit for this spec and plan. |
| Implementation | `documentation-improvements docs: improve harness documentation surfaces` | `2026-06-23-documentation-improvements: improve harness documentation surfaces` | Expected implementation commit for documentation edits and validation evidence. |

## Validation commands

| Command | Expected result |
|---|---|
| `powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` | Existing harness validation passes with all `PASS` lines and exit code 0. |
| `git diff -- README.md TODO.md .agents/skills/dev-doc-harness/docs/operator-note.md .agents/skills/dev-doc-harness/references/policy-architecture.md .agents/skills/dev-doc-harness/SKILL.md CHANGELOG.md` | Diff shows only the intended documentation changes and no license changes. |
| `rg -n "second source of truth|canonical|semantic parser|heavy parser|portfolio|Priority" README.md TODO.md .agents/skills/dev-doc-harness` | Confirms key documentation concepts are discoverable in the intended surfaces. |

## Plan variance handling

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

Expected low-impact variance that may be recorded in the implementation summary instead of an amendment:

- Choosing a different package-local note filename under `.agents/skills/dev-doc-harness/docs/`.
- Omitting the optional `SKILL.md` pointer if the package-local note is discoverable enough without it.
- Adjusting TODO priority labels during editing while preserving the approved scope.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

Draft review status: Draft package approved by operator on 2026-06-23.
Approval commit status: Approved; approval commit pending.
Post-freeze implementation authorization status: Not authorized yet.

## Completion criteria

- Acceptance criteria in `spec-documentation-improvements.md` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- Commit subjects match the approved planned subjects or recorded variance, and changelog title snippets are synchronized.
- Variance log is present and current if nontrivial variance occurs.
- De-facto sub-agent use is reported when applicable, including count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.

## Approval

- Status: Approved
- Superseded by: not applicable
