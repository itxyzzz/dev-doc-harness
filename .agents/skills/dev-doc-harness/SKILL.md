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

- `references/artifact-contract.md` for feature folders, required files, immutable snapshots, living deltas, documentation matrices, and variance handling.
- `references/subagent-model-policy.md` for the active model policy, sub-agent notation, escalation rules, and final-review rules.

## Workflow

1. Classify the work as small/mechanical, small/medium feature, or large feature.
2. Choose a feature ID using `YYYY-MM-DD-short-kebab-title`, or `YYYY-MM-DD-ISSUE-short-kebab-title` when a JIRA key or other issue-tracker ID is available.
3. Create or update the feature folder under `specs/<feature-id>/`.
4. Draft the required spec, plan, phase plans, documentation matrix, and variance log using the templates in `assets/templates/`.
5. For large features, make `spec.md` the central planning anchor and handoff from the initial planning session to later phase-planning sessions. Preserve all decisions, constraints, risks, assumptions, acceptance criteria, and important rejected alternatives there before writing phase plans.
6. Treat drafts as editable until operator approval or explicit handoff.
7. When a durable spec, plan, phase plan, or plan amendment is finalized, run the Planning Artifact Freeze Gate before implementation or later planning continues.
8. After approval, treat approved specs, plans, phase plans, snapshots, and amendments as immutable snapshots.
9. During implementation, record justified plan variance in `implementation-notes/variance-log.md`.
10. Update `CHANGELOG.md` before each commit with concise entries tied to the current feature ID, phase, task, or spec/plan decision.
11. For high-impact variance, create a plan amendment and get operator approval before proceeding.

## Planning Artifact Freeze Gate

The freeze gate is mandatory when durable planning artifacts are finalized. It applies to `spec.md`, `plan.md`, `plan-phase-*.md`, and `plan-amendment-*.md`.

At each gate:

1. Update `CHANGELOG.md`.
2. Verify the finalized planning artifacts and changelog.
3. Commit the finalized planning artifacts and changelog together.
4. Stop before implementation.
5. Report the commit hash and artifact paths.
6. Remind the operator that this is the right point to push and create a draft plan-only PR when desired.
7. Ask the operator to confirm any model, reasoning-effort, or sub-agent policy changes before implementation or the next planning stage.

Proceed to implementation only after a fresh explicit operator instruction after the freeze gate. For very large features, run multiple freeze gates: after the anchor spec, after each finalized phase-plan batch, and after each approved high-impact amendment.

## Superpowers compatibility

When Superpowers is installed and active, use Superpowers for brainstorming, planning, TDD, execution, review, and finishing workflows. This harness only controls where approved artifacts live and what documentation lifecycle decisions must be recorded.

If Superpowers produces specs or plans outside `specs/<feature-id>/`, copy or convert the approved content into the harness feature folder before implementation begins. Do not duplicate Superpowers methodology in this harness.

## spec-kit compatibility

If spec-kit is installed and active, prefer a project-local adapter that points back to this skill and the artifact contract. Do not make spec-kit templates the canonical source of the harness rules.

## Completion checklist

- The feature folder follows `specs/<feature-id>/`.
- Required small/medium or large-feature artifacts exist.
- Large-feature `spec.md` is detailed enough to hand off all important planning decisions to later phase-plan authors.
- Each finalized spec, plan, phase plan, or amendment has passed the Planning Artifact Freeze Gate.
- The documentation artifact matrix marks each artifact as required, not applicable, or deferred with a reason.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- Approved snapshots are not silently rewritten.
- Nontrivial variance is recorded.
- High-impact variance has an amendment and operator approval.
- Plans include validation commands and expected outputs.
- Sub-agent use, if any, follows the active model policy notation.
