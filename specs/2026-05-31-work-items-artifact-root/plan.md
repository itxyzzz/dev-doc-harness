# Work Items Artifact Root Plan

Work ID: `2026-05-31-work-items-artifact-root`
Status: Draft

## Implementation summary

Update the harness documentation contract so agents consistently place durable
planning packages under `docs/work-items/<work-id>/`, use short-ID-bearing
artifact filenames, and flatten supplemental package documentation into
`snapshots/` and `deltas/`.

This is a documentation and template migration. The implementation should first
update the canonical artifact contract, then align the skill entry point,
freeze-gate and quality references, templates, README, TODO notes, and the
existing local planning package. The implementation must avoid changing the
substantive meaning of the already-approved planning approval freeze flow
package beyond path and filename references required by the new layout.

## Files and interfaces

Expected files or directories to change:

- `.agents/skills/dev-doc-harness/SKILL.md`
- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
- `.agents/skills/dev-doc-harness/assets/templates/*.md`
- `README.md`
- `TODO.md`
- `CHANGELOG.md`
- `specs/2026-05-31-planning-approval-freeze-flow/`
- `docs/work-items/2026-05-31-planning-approval-freeze-flow/`

Interfaces expected to remain stable:

- Work ID format: `YYYY-MM-DD-short-kebab-title` or
  `YYYY-MM-DD-ISSUE-short-kebab-title`.
- Approval-first freeze gate lifecycle.
- Immutable snapshot, variance log, and plan amendment semantics.
- Active `economy-default` model and sub-agent policy.

## Model and Sub-agent Strategy

Current orchestration: GPT-5 Codex, reasoning effort not explicitly provided.
Fit assessment: moderate documentation/process risk because this change touches
the canonical artifact contract and many examples. Implementation is cohesive
and mostly text-based, so a single orchestration thread is preferable for
consistent wording.
Recommended change: None.

Sub-agents: None. The task is cross-document consistency work with a small
repository surface; sub-agent parallelism would increase the risk of mismatched
terms.

## Tasks

- [ ] Update `artifact-contract.md` first so it defines
  `docs/work-items/<work-id>/`, short-ID filename suffixes, flattened
  `snapshots/` and `deltas/`, and Superpowers pointer-stub rules.
- [ ] Update `SKILL.md` so workflow, compatibility, and completion checklist
  language point to the new canonical package root and filenames.
- [ ] Update `planning-freeze-gates.md` and `durable-planning-quality.md` so
  durable artifact references use the new filename patterns without changing
  freeze or variance semantics.
- [ ] Update all templates so generated specs, plans, phase plans, amendments,
  documentation matrices, variance reminders, and completion criteria use the
  new root, short-ID filenames, `snapshots/`, and `deltas/`.
- [ ] Update `README.md` operator guidance to describe the new
  `docs/work-items/<work-id>/` package root and the chat-friendly artifact
  filenames.
- [ ] Update `TODO.md` follow-ups so validation and Superpowers compatibility
  tasks refer to the new layout.
- [ ] Migrate the existing approved local planning package from
  `specs/2026-05-31-planning-approval-freeze-flow/` to
  `docs/work-items/2026-05-31-planning-approval-freeze-flow/`, renaming
  `spec.md` to `spec-planning-approval-freeze-flow.md` and `plan.md` to
  `plan-planning-approval-freeze-flow.md`.
- [ ] Update moved package content only where needed to keep path, filename, and
  documentation-matrix references consistent with the new contract.
- [ ] Add a newest-first `CHANGELOG.md` entry for the implementation commit.
- [ ] Review changed files for consistent terminology: work item package,
  canonical package root, short ID, snapshot, delta, pointer stub, freeze gate,
  variance, and amendment.

## Validation commands

| Command | Expected result |
|---|---|
| `rg -n "specs/<work-id>|specs/|docs/snapshots|docs/living|docs/superpowers|spec\\.md|plan\\.md|plan-phase-|plan-amendment-" .agents README.md TODO.md CHANGELOG.md docs specs` | Matches are either updated examples, migrated historical references, filename patterns with short IDs, or explicit legacy-migration notes |
| `rg -n "docs/work-items/<work-id>|spec-<short-id>\\.md|plan-<short-id>\\.md|snapshots/|deltas/" .agents README.md TODO.md specs` | Confirms the new layout and naming patterns are represented in canonical docs and templates |
| `git diff --check` | No whitespace errors |
| `git status --short` | Only intended harness documentation, template, changelog, and planning package migration files are modified, added, deleted, or staged |

## Plan variance handling

Before approval, operator feedback edits this draft directly and does not
require an amendment. After the approval commit or explicit handoff snapshot,
approved plans are immutable snapshots. Record nontrivial implementation
variance in `implementation-notes/variance-log.md`. Create a plan amendment and
request operator approval before proceeding when post-freeze variance affects
architecture, APIs, data, security, privacy, compliance, scope, acceptance
criteria, or plan feasibility.

## Planning artifact freeze gate

When this plan is ready for operator review, follow the repository-root
reference `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`:
stage the draft without committing, request approval or feedback, revise
directly on feedback, and commit only after explicit approval.

## Completion criteria

- Acceptance criteria in `spec.md` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- Variance log is present and current.

## Approval

- Status: Draft
- Superseded by: None
