---
name: dev-doc-harness
description: Use for repository development work except very small mechanical edits.
---

# Dev Doc Harness

This skill defines the repository-local documentation and artifact contract for development work. It is deliberately small: it does not replace Codex plan mode, Superpowers, spec-kit, testing discipline, or project architecture decisions.

## When to invoke

Use this skill for all repository development work except very small mechanical edits. The detailed sizing rules live in `references/artifact-contract.md`.

Very small mechanical edits may skip this harness when the operator has not requested durable planning.

## Core references

Before creating or reviewing artifacts, read:

- `references/artifact-contract.md` for work item folders, required files, immutable snapshots, living deltas, documentation matrices, and variance handling.
- `references/durable-planning-quality.md` for spec and phase-plan quality bars, handoff preservation, and fresh-thread executability.
- `references/planning-freeze-gates.md` for approval-first planning gates before implementation or later planning continues.
- `references/subagent-model-policy.md` for the active model policy, sub-agent notation, escalation rules, and final-review rules.

Use these supplemental references when relevant:

- `references/context-and-quality-gates.md` for context load order, environment compensation, and increment quality gates.
- `references/subagent-role-examples.md` for compact policy-relative sub-agent role patterns.
- `references/evidence-and-report-artifacts.md` for spikes, investigations, agent reports, or review evidence; skip for routine changes covered by normal validation and changelog notes.

## Workflow

1. Classify the work as small/mechanical, small/medium work item, or large/phased work item. Features, bug fixes, prior issue investigations, refactors, migrations, and documentation/process changes all use this sizing model when substantial.
2. Choose a work ID using `YYYY-MM-DD-short-kebab-title`, or `YYYY-MM-DD-ISSUE-short-kebab-title` when a JIRA key or other issue-tracker ID is available.
3. Create or update the work item folder under `specs/<work-id>/`.
4. Draft the required spec, plan, phase plans, documentation matrix, and variance log using the templates in `assets/templates/`.
5. For large or phased work items, make `spec.md` the central planning anchor and handoff from the initial planning session to later phase-planning sessions. Preserve all decisions, constraints, risks, assumptions, acceptance criteria, and important rejected alternatives there before writing phase plans.
6. Treat drafts as editable until explicit operator approval and the approval commit, or until explicit handoff.
7. Before approval, stage draft planning artifacts without committing and ask the operator for approval or feedback.
8. If the operator gives feedback before approval, edit the drafts directly, refresh staging, and ask for approval again.
9. After explicit approval or explicit handoff, run the Planning Artifact Freeze Gate before implementation or later planning continues.
10. After the approval commit or explicit handoff snapshot, treat approved specs, plans, phase plans, snapshots, and amendments as immutable snapshots.
11. During implementation, record justified plan variance in `implementation-notes/variance-log.md`.
12. Update `CHANGELOG.md` before each commit with concise entries tied to the current work ID, phase, task, or spec/plan decision.
13. For post-freeze high-impact variance, create a plan amendment and get operator approval before proceeding.

## Planning Artifact Freeze Gate

When durable planning artifacts are ready for operator review, approval, handoff, or freeze, follow `references/planning-freeze-gates.md`. Treat that reference as the only source for review, freeze-gate procedure, and continuation rules.

## Superpowers compatibility

When Superpowers is installed and active, use Superpowers for brainstorming, planning, TDD, execution, review, and finishing workflows. This harness only controls where approved artifacts live and what documentation lifecycle decisions must be recorded.

If Superpowers produces specs or plans outside `specs/<work-id>/`, copy or convert the approved content into the harness work item folder before implementation begins. Do not duplicate Superpowers methodology in this harness.

## spec-kit compatibility

If spec-kit is installed and active, prefer a project-local adapter that points back to this skill and the artifact contract. Do not make spec-kit templates the canonical source of the harness rules.

## Completion checklist

- The work item folder follows `specs/<work-id>/`.
- Required small/medium or large/phased work item artifacts exist.
- Large or phased work item `spec.md` is detailed enough to hand off all important planning decisions to later phase-plan authors.
- Each approved or handed-off spec, plan, phase plan, or amendment has passed the Planning Artifact Freeze Gate.
- The documentation artifact matrix marks each artifact as required, not applicable, or deferred with a reason.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- Frozen snapshots are not silently rewritten.
- Nontrivial variance is recorded.
- High-impact variance has an amendment and operator approval.
- Plans include validation commands and expected outputs.
- Sub-agent use, if any, follows the active model policy notation.
