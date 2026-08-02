# Implementation Changelog

## 2026-07-29 fix: harness-execution-flow-clarity -- deduplicate plan state and restore conditional style routing

Release target: `unreleased`
Package impact: `distributable`
Release-note: `source-only`

- Placed plan-state fields at their single lifecycle boundaries, restored conditional artifact-style loading for routine small/medium artifacts, regenerated active templates, and added focused structural regression coverage.
- **Consolidate reviewed changelog fragments:** Refreshed root `CHANGELOG.md` at the operator-owned post-integration checkpoint.

## 2026-07-28 fix: harness-execution-flow-clarity -- consolidate post-freeze transition guidance

Release target: `unreleased`
Package impact: `distributable`
Release-note: `source-only`

- Folded freeze mechanics into the approval checklist, moved continuation rules into structured post-freeze routing, and made execution handoffs apply explicit operator overrides to the frozen approved selection without rewriting the frozen artifact.

## 2026-07-28 fix: harness-execution-flow-clarity -- clarify freeze transition routing

Release target: `unreleased`
Package impact: `distributable`
Release-note: `source-only`

- Moved the four-group next-stage explanation to draft review, clarified runtime-override recording, made approved agent task creation the default new-task continuation with manual creation as fallback, and stated the normal multi-gate large/phased flow.

## 2026-07-28 refactor: harness-execution-flow-clarity -- separate transition flow from context loading

Release target: `unreleased`
Package impact: `distributable`
Release-note: `source-only`

- Consolidated planning transitions and chat projection in the freeze-gate owner, narrowed execution-quality to context loading and startup consumption, and aligned architecture and validator ownership checks without changing operator-visible behavior.

## 2026-07-28 docs: harness-execution-flow-clarity -- clarify operator guidance and Superpowers workspace

Release target: `unreleased`
Package impact: `distributable`
Release-note: `source-only`

- Reworked the package-local operator note as a human-facing harness explanation, clarified the harness and Superpowers responsibilities, ignored the plan-specific Superpowers workspace, and corrected a README typo.

## 2026-07-28 feat: harness-execution-flow-clarity -- compact bootstrap and add skill metadata

Release target: `unreleased`
Package impact: `distributable`
Release-note: `source-only`

- Compacted the repository bootstrap while preserving its semantic guards, added minimal generated skill UI metadata with focused validation, retained installation-neutral skill routing, and included the operator's README improvements.

## 2026-07-28 fix: harness-execution-flow-clarity -- replace no-review blocker with operator decision

Release target: `unreleased`
Package impact: `distributable`
Release-note: `source-only`

- Replaced the hard no-review execution blocker with disclosure, one-time operator decision, recorded authorization, focused validation, and completion-report evidence while retaining independent review as the default.

## 2026-07-27 docs: harness-execution-flow-clarity -- clarify drift and changelog guidance

Release target: `unreleased`
Package impact: `distributable`
Release-note: `source-only`

- Reworked README as a user-facing harness overview and aligned its focused model-selection checks with the simpler prose and Markdown line wrapping.

## 2026-07-27 fix: harness-execution-flow-clarity -- clarify frozen handoff heading

Release target: `unreleased`
Package impact: `distributable`
Release-note: `source-only`

- Made plan-handoff source blocks select one draft or frozen next-stage heading and extended focused validation to reject simultaneous headings in source and generated plans.

## 2026-07-27 feat: harness-execution-flow-clarity -- enforce combined planning

Release target: `unreleased`
Package impact: `distributable`
Release-note: `source-only`

- Enforced complete combined small/medium packages at review and freeze, retained authorized staged and large-anchor exceptions, and added focused package-shape validation.

## 2026-07-27 fix: harness-execution-flow-clarity -- harden next-stage validation

Release target: `unreleased`
Package impact: `distributable`
Release-note: `source-only`

- Require known-suitable profile, suitable or immaterial context risk, and a concrete continuity benefit for same-Codex-task fixtures; reject mixed draft/frozen state labels.

## 2026-07-27 feat: harness-execution-flow-clarity -- simplify next-stage presentation

Release target: `unreleased`
Package impact: `distributable`
Release-note: `source-only`

- Simplified the next-stage interface into four plain-language groups, added execution terminology and chat projection, refreshed generated templates, and added focused validation.

## 2026-07-27 feat: harness-execution-flow-clarity -- restore execution and review defaults

Release target: `unreleased`
Package impact: `distributable`
Release-note: `source-only`

- Restored the canonical execution-method cascade, route-specific reviewer contract, and start-override validation, including a model-only override fixture that records the selection without requiring an amendment solely for that runtime choice.
