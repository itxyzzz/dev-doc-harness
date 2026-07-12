# Superpowers Compatibility Guidance Plan

Work ID: `2026-07-07_superpowers-compat-guidance`
Short ID: `superpowers-compat-guidance`
Status: Approved
Harness release: `0.4+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:release`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:lifecycle.superpowers-compatibility`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:release.identity`, `rule:release.release-notes`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

Artifact style baseline: this plan is written as executable draft content. It keeps tasks small enough for one orchestration thread and records validation signals before implementation begins.

## Input Artifacts

Read these before finalizing implementation planning:

1. Approved spec: `spec_superpowers-compat-guidance.md`.
2. Architecture input: `snapshots/architecture.snapshot.md`.
3. Required snapshots or deltas: `snapshots/test-cases.snapshot.md`.
4. Relevant repository files, tests, docs, logs, or review comments:
   - `README.md`
   - `AGENTS.md`
   - `.agents/skills/dev-doc-harness/SKILL.md`
   - `.agents/skills/dev-doc-harness/VERSION`
   - `.agents/skills/dev-doc-harness/references/artifact-contract.md`
   - `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
   - `.agents/skills/dev-doc-harness/references/release-policy.md`
   - `.agents/skills/dev-doc-harness/docs/operator-note.md`
   - `.agents/skills/dev-doc-harness/docs/releases/0.4.0.md`
   - `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`
   - `.agents/skills/dev-doc-harness/assets/templates/blocks/`
   - `.agents/skills/dev-doc-harness/assets/templates/assemblies/`
   - `docs/release-branch-process.md`
   - `CHANGELOG.md`
5. Unresolved implementation context to confirm before editing: none identified. If `0.5.0` release-note source entries cannot be curated from the changelog, stop and report the ambiguity.

If architecture is missing, ambiguous, or changed before freeze, update the draft spec or architecture snapshot before finalizing this plan. If architecture changes after freeze, use variance handling and an amendment when `rule:lifecycle.variance-policy` requires approval. Do not reinterpret architecture decisions in the plan.

## Spec Traceability

Requirement coverage:

1. `REQ-001`: implemented by `T-002`, `T-003`, and `T-004`; verified by `V-002`, `V-003`, and `V-006`.
2. `REQ-002`: implemented by `T-002`, `T-003`, and `T-004`; verified by `V-002`, `V-003`, and `V-006`.
3. `REQ-003`: implemented by `T-002`, `T-003`, and `T-004`; verified by `V-003`, `V-004`, and `V-006`.
4. `REQ-004`: implemented by `T-005`, `T-006`, and `T-007`; verified by `V-001`, `V-004`, and `V-005`.
5. `REQ-005`: implemented by `T-007` and `T-008`; verified by `V-001`, `V-005`, and `V-006`.

Acceptance coverage:

1. `AC-001`: implemented by `T-002`, `T-003`, and `T-004`; verified by `V-002` and `V-003`.
2. `AC-002`: implemented by `T-002`, `T-003`, and `T-004`; verified by `V-002` and `V-003`.
3. `AC-003`: implemented by `T-002` through `T-006`; verified by `V-003`.
4. `AC-004`: implemented by `T-003` and `T-008`; verified by `V-001`, `V-002`, and `V-006`.
5. `AC-005`: implemented by `T-004`; verified by `V-002` and `V-003`.
6. `AC-006`: implemented by `T-005` and `T-007`; verified by `V-004` and `V-005`.
7. `AC-007`: implemented by `T-006`; verified by `V-004` and `V-005`.
8. `AC-008`: implemented by `T-007` and `T-008`; verified by `V-001`.
9. `AC-009`: implemented by `T-008`; verified by `V-006`.

Risk and boundary coverage:

1. `RISK-001`: handled by `T-002`, `T-003`, and `T-004`; verified by `V-002`.
2. `RISK-002`: handled by `T-003` and `T-008`; verified by `V-003` and `V-006`.
3. `RISK-003`: handled by `T-006`; verified by `V-004`.
4. `RISK-004`: handled by `T-008`; verified by `V-006`.
5. `RISK-005`: handled by `T-006` and `T-007`; verified by `V-004` and `V-005`.

Architecture coverage:

1. Architecture input: `snapshots/architecture.snapshot.md`.
2. Plan usage: tasks preserve the selected adapter flow, canonical artifact boundary, and release-validation boundary.
3. Drift path: before freeze, edit this draft package directly. After freeze, use the variance log for local technical drift or an amendment for changes to compatibility authority, artifact canonicality, release identity, or validator feasibility.
4. Reinterpretation guard: implementation may clarify existing policy but must not make `docs/superpowers` a second durable source of truth or create early `0.6` release artifacts.

## Implementation Approach

Implementation should first update the smallest set of user-facing and canonical compatibility surfaces needed to teach the adapter flow. README and the package operator note should explain the practical sequence for operators and adopters. Canonical lifecycle and freeze-gate references should own the durable artifact and approval rules, with router text pointing agents to those owners.

Next, implementation should correct release-baseline drift. The release branch process and remote branch list show `release/0.5` exists, so current development branches remain on `0.5+` until `0.6` release preparation begins. The validator should stop looking for a release-note file named after a development marker and should instead expect released-minor notes for `0.4.0` and `0.5.0` while leaving `0.6` uncreated.

Finally, implementation should run the harness validator and review compatibility search output. If template source blocks need a small prompt adjustment, edit the source block or manifest first, regenerate with the assembler, and validate. If templates do not need adjustment, leave them unchanged.

## Change Surfaces

Expected edits:

1. `README.md`: add practical operator guidance for using Superpowers with the harness.
2. `AGENTS.md`: adjust only if the bootstrap compatibility sentence needs a pointer to concrete adapter behavior.
3. `.agents/skills/dev-doc-harness/SKILL.md`: adjust router compatibility text only if needed for discoverability.
4. `.agents/skills/dev-doc-harness/references/artifact-contract.md`: clarify lifecycle-owned adapter rules only if current wording is insufficient.
5. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: clarify the pause-before-execution interaction only if current wording is insufficient.
6. `.agents/skills/dev-doc-harness/docs/operator-note.md`: add compact downstream-adopter Superpowers guidance.
7. `.agents/skills/dev-doc-harness/VERSION`: update to `0.5+`.
8. `.agents/skills/dev-doc-harness/references/release-policy.md`: update release identity and release-note examples for `0.5+` and the expected released notes.
9. `.agents/skills/dev-doc-harness/docs/releases/0.5.0.md`: add package-local release notes for the already-cut `0.5` release if missing.
10. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: update release-baseline and compatibility structural checks.
11. `docs/release-branch-process.md`: update release preparation guidance so each future release keeps `VERSION`, release policy, release notes, and validator expectations synchronized, and so development branches remain on `0.x+` until `0.x+1` preparation.
12. `.agents/skills/dev-doc-harness/assets/templates/blocks/` and generated templates: change only if compatibility prompt gaps are found during implementation.
13. `CHANGELOG.md`: add the required implementation entry before commit.

Stable interfaces:

1. Harness work-item package layout remains `docs/work-items/<work-id>/`.
2. `docs/superpowers` remains non-canonical for harness-managed durable specs and plans.
3. Release notes remain package-local under `.agents/skills/dev-doc-harness/docs/releases/`.
4. The active model policy remains selected in `AGENTS.md` as `economy-default`.

Changed interfaces:

1. Validator release expectations change from `0.4+` development notes to `0.5+` development marker with `0.4.0` and `0.5.0` release notes, and the release process records the repeatable `0.x+` development-marker rule.
2. Operator-facing Superpowers guidance becomes a concrete adapter flow rather than a high-level compatibility statement.

Implementation boundaries:

1. Installed Superpowers plugin files stay out of scope because they are external workflow inputs.
2. `0.6` release artifacts stay out of scope because the future release branch process owns them.
3. Frozen historical artifacts stay out of scope because the harness does not rewrite them for release-stamp or wording drift.
4. Broad template redesign stays out of scope unless a narrow source-block prompt fix is necessary.

## Model and Sub-agent Strategy

Current orchestration:

1. Model/profile and reasoning effort if known: not exposed.
2. Model-policy source: `AGENTS.md` active repository policy, `economy-default`.
3. Override scope and expiry: none.

Fit assessment:

1. Complexity: medium, because the work crosses operator docs, canonical policy, validator behavior, and release identity.
2. Risk and blast radius: medium, because mistakes affect future agent workflow and package validation but not runtime product behavior.
3. Ambiguity: low-to-medium, because the operator clarified the release baseline and the canonical compatibility boundary already exists.
4. Budget and latency fit: acceptable for one orchestration thread with focused validation.

Recommended orchestration change:

1. None. Use the current orchestration thread for implementation and final integration.

Sub-agents:

1. Sub-agents: none planned. The work is documentation and validator maintenance across tightly related files, and one orchestration thread can preserve the compatibility and release-baseline context without coordination overhead.

## Task Plan

- [ ] `T-001` Dependencies: none; re-read the approved spec, architecture snapshot, test-case snapshot, release branch process, release policy, and validator before editing; Traces: `REQ-001`, `REQ-004`, `RISK-003`.
- [ ] `T-002` Dependencies: `T-001`; update README guidance to explain the practical Superpowers plus harness adapter flow, including canonical work-item artifacts, optional pointer stubs, freeze-gate pause, and post-freeze execution; Traces: `REQ-001`, `REQ-002`, `REQ-003`, `AC-001`, `AC-002`, `AC-003`.
- [ ] `T-003` Dependencies: `T-001`; update canonical compatibility surfaces only where needed so lifecycle and freeze-gate ownership remains clear without duplicating README prose; Traces: `REQ-001`, `REQ-002`, `REQ-003`, `AC-001`, `AC-002`, `AC-004`.
- [ ] `T-004` Dependencies: `T-002`, `T-003`; update the package-local operator note and, if needed, root `AGENTS.md` or router text so downstream adopters discover the adapter flow; Traces: `REQ-003`, `AC-003`, `AC-005`.
- [ ] `T-005` Dependencies: `T-001`; update the package release marker, release policy examples, and release branch process from `0.4+` to `0.5+`, preserving release-level compatibility semantics and the generic rule that current development branches remain on `0.x+` until `0.x+1` release preparation; Traces: `REQ-004`, `AC-006`.
- [ ] `T-006` Dependencies: `T-001`; add or restore `.agents/skills/dev-doc-harness/docs/releases/0.5.0.md` by curating from `CHANGELOG.md` and the release process; do not create `0.6` notes; Traces: `REQ-004`, `AC-007`, `RISK-003`, `RISK-005`.
- [ ] `T-007` Dependencies: `T-005`, `T-006`; update validator release checks so current development is `0.5+` and expected release notes are concrete released-version files rather than a development-marker file; Traces: `REQ-004`, `REQ-005`, `AC-006`, `AC-008`.
- [ ] `T-008` Dependencies: `T-002`, `T-003`, `T-007`; add or adjust high-signal validator coverage for the Superpowers adapter scenario and release-baseline expectations; Traces: `REQ-005`, `AC-004`, `AC-009`.
- [ ] `T-009` Dependencies: `T-002` through `T-008`; if template source-block changes were required, run the template assembler with `--write`; otherwise record that templates stayed unchanged after review; Traces: `REQ-003`, `REQ-005`.
- [ ] `T-010` Dependencies: `T-002` through `T-009`; update `CHANGELOG.md` with the implementation entry before staging; Traces: `REQ-003`, `REQ-004`.
- [ ] `T-011` Dependencies: `T-010`; run validation commands, review `git diff`, and commit the implementation changes with the planned subject if validation passes; Traces: `AC-001` through `AC-009`.

## Planned commits

Planning approval commit:

1. Planned subject: `spec: superpowers-compat-guidance -- approve adapter guidance plan`.
2. Changelog title or snippet: `2026-07-07_superpowers-compat-guidance -- approve adapter guidance plan`.
3. Notes: approval commit for `spec_superpowers-compat-guidance.md`, `plan_superpowers-compat-guidance.md`, `snapshots/test-cases.snapshot.md`, and `snapshots/architecture.snapshot.md`.

Implementation commit:

1. Planned subject: `docs: superpowers-compat-guidance -- document adapter flow and fix release baseline`.
2. Changelog title or snippet: `2026-07-07_superpowers-compat-guidance -- document adapter flow and fix release baseline`.
3. Notes: expected implementation commit for compatibility guidance, validator release-baseline correction, `0.5+` marker alignment, `0.5.0` release notes, and required changelog entry.

## Validation Plan

| Command | Expected result |
|---|---|
| `python .agents\skills\dev-doc-harness\scripts\test_harness_policy.py` | Exit code `0`; all harness checks pass, including golden Superpowers traversal and release identity/notes checks. |
| `rg -n "0\.4\+|0\.5\+|0\.5\.0|0\.x\+|0\.6" .agents/skills/dev-doc-harness README.md AGENTS.md docs/release-branch-process.md CHANGELOG.md` | Shows `0.5+` as the current development marker, keeps historical `0.4+` mentions only where they describe prior history, includes `0.5.0` release notes/process references, records the generic `0.x+` development-marker rule in the release process, and does not show newly created `0.6` release notes. |
| `rg -n "Superpowers|docs/superpowers|pointer stub|freeze gate|work-item" README.md AGENTS.md .agents/skills/dev-doc-harness` | Shows the adapter flow is discoverable from operator-facing and canonical surfaces without contradicting the lifecycle owner. |
| `git diff --check` | No whitespace errors. |
| `git diff --name-only` | Contains only approved implementation surfaces plus `CHANGELOG.md`; templates appear only if source-block review justified them. |
| Manual review of `.agents/skills/dev-doc-harness/docs/releases/` | Confirms `0.4.0.md` and `0.5.0.md` exist, and no `0.6.0.md` or `0.6+.md` exists. |

Every validation entry states the expected signal before implementation starts. Failed validation blocks completion unless the operator approves a revised plan or amendment.

## Plan variance handling

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact changes to compatibility authority, canonical artifact location, release identity, release-note scope, validator feasibility, active model policy, scope, acceptance criteria, or plan feasibility.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

Draft review status: approved by operator on 2026-07-07.

Approval commit status: approved for freeze-gate commit.

Post-freeze implementation authorization status: not authorized. Implementation must wait for a fresh operator response after the freeze gate.

## Plan readiness checklist

- [x] Input artifacts and relevant repository context have been read and listed.
- [x] Every spec requirement and acceptance criterion has at least one task and one validation path.
- [x] Risks, scope boundaries, interfaces, and documentation decisions are either covered by tasks or explicitly marked as no-op with a reason.
- [x] Task detail is sufficient for a fresh implementation agent or delegated sub-agent to execute its assigned part without inventing task order, file scope, validation, or documentation steps.
- [x] Validation entries have exact commands, manual checks, review findings, or operator acceptance paths with expected signals.
- [x] Planned commits and changelog title snippets are synchronized.
- [x] Variance handling is clear for likely implementation drift.
- [x] The work still fits one orchestration thread with a bounded sub-agent strategy.
- [x] Sub-agent strategy follows `module:models`, with `Sub-agents: none` and a fit rationale.
- [x] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain before approval or handoff.

## Completion criteria

- Acceptance criteria in `spec_superpowers-compat-guidance.md` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- The frozen plan had enough detail for each assigned execution part to proceed safely.
- Execution remained within one orchestration thread with no sub-agent delegation.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- Commit subjects match the approved planned subjects or recorded variance, and changelog title snippets are synchronized.
- Planned implementation changes are committed, or the completion report names the exact blocker or explicit no-commit instruction plus current worktree status.
- Variance log is present and current if nontrivial variance occurs.
- De-facto sub-agent use is reported as none unless implementation variance changes the strategy with approval.

## Approval

- Status: Approved
- Superseded by: None
