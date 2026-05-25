---
name: dev-doc-harness
description: Use for substantial repository development work that needs durable specs, plans, phase plans, variance handling, or documentation artifact tracking.
---

# Dev Doc Harness

This skill defines the repository-local documentation and artifact contract for substantial development work. It is deliberately small: it does not replace Codex plan mode, Superpowers, spec-kit, testing discipline, or project architecture decisions.

## When to invoke

Use this skill for:

- New features.
- Medium or large refactors.
- API, interface, schema, persistence, migration, security, privacy, or compliance-sensitive changes.
- Multi-step implementation.
- Bug fixes that need nontrivial investigation or durable handoff.
- Work that may require tests, operator notes, API docs, architecture notes, or living documentation deltas.

Small mechanical edits may skip this harness when the operator has not requested durable planning.

## Core references

Before creating or reviewing artifacts, read:

- `references/artifact-contract.md` for feature folders, required files, immutable snapshots, living deltas, documentation matrices, and variance handling.
- `references/subagent-model-policy.md` for the active model policy, sub-agent notation, escalation rules, and final-review rules.

## Workflow

1. Classify the work as small/mechanical, small/medium feature, or large feature.
2. Choose a feature ID using `YYYY-MM-DD-short-kebab-title`.
3. Create or update the feature folder under `specs/<feature-id>/`.
4. Draft the required spec, plan, phase plans, documentation matrix, and variance log using the templates in `assets/templates/`.
5. Treat drafts as editable until operator approval or explicit handoff.
6. After approval, treat approved specs, plans, phase plans, snapshots, and amendments as immutable snapshots.
7. During implementation, record justified plan variance in `implementation-notes/variance-log.md`.
8. For high-impact variance, create a plan amendment and get operator approval before proceeding.

## Superpowers compatibility

When Superpowers is installed and active, use Superpowers for brainstorming, planning, TDD, execution, review, and finishing workflows. This harness only controls where approved artifacts live and what documentation lifecycle decisions must be recorded.

If Superpowers produces specs or plans outside `specs/<feature-id>/`, copy or convert the approved content into the harness feature folder before implementation begins. Do not duplicate Superpowers methodology in this harness.

## spec-kit compatibility

If spec-kit is installed and active, prefer a project-local adapter that points back to this skill and the artifact contract. Do not make spec-kit templates the canonical source of the harness rules.

## Completion checklist

- The feature folder follows `specs/<feature-id>/`.
- Required small/medium or large-feature artifacts exist.
- The documentation artifact matrix marks each artifact as required, not applicable, or deferred with a reason.
- Approved snapshots are not silently rewritten.
- Nontrivial variance is recorded.
- High-impact variance has an amendment and operator approval.
- Plans include validation commands and expected outputs.
- Sub-agent use, if any, follows the active model policy notation.
