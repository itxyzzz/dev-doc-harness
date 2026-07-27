# Artifact Style

This document is the canonical style owner for durable harness artifacts. It
defines how specs, plans, snapshots, amendments, reports, and handoffs stay easy
to read after the chat context is gone.

Module: `module:artifact-style`

Owned rule IDs:

| Rule ID | Local owner |
|---|---|
| `rule:style.final-artifact-content` | `## Final artifact content` |
| `rule:style.scannable-structure` | `## Scannable structure` |
| `rule:style.placeholder-control` | `## Placeholder control` |
| `rule:style.trace-density` | `## Traceability density` |
| `rule:style.template-prompts` | `## Template prompts` |
| `rule:style.plain-language` | `## Plain language` |
| `rule:style.entity-presentation` | `## Entity presentation` |
| `rule:style.verification-criterion-placement` | `## Verification Criterion placement` |
| `rule:style.proportional-traceability` | `## Proportional traceability` |

## When it applies

Load this module when artifact readability is part of the work, when a document
is large enough that readers may miss decisions, or when a future agent must
consume the artifact without chat history.

This module is required for large anchor specs. It is also required for any
spec, plan, phase plan, snapshot, amendment, report, handoff, or operator-facing
document that becomes large or hard to scan. Routine small/medium planning can
use the short baseline guidance in `module:quality` and the templates unless
readability risk is material.

This module owns artifact style. It does not own work sizing, artifact
lifecycle, immutable snapshots, variance, naming, model strategy, evidence
preservation, release policy, or durable completeness.

## Plain language

Use `must` for binding obligations and `should` for guidance.

Use short, everyday words. Say what to do and why only when the reason helps
the reader act. Avoid legalistic authority language, inflated status labels,
and process narration that does not change a decision.

Do not use `shall` in author-facing current guidance or newly created durable artifacts.
The sentence naming it is a definition-only exception; validator fixtures may
identify it to test enforcement.

## Final artifact content

For a next-stage summary, presentation owns grouping and plain-label readability only: render **Activity**, **Orchestration**, **Model**, and **Fallbacks and limits** in that order. Do not define method, model, reviewer, continuity, or lifecycle semantics here.

Write durable artifacts as final repository documents, not as chat transcripts
or drafting instructions.

Use precise, descriptive language:

- State Architecture Decisions, constraints, Specification Commitments, and Verification Criteria directly.
- Prefer concrete paths, owners, events, IDs, commit subjects, and validation
  signals over vague future intent.
- Use `None`, `Not applicable`, or a reasoned deferral when a field has no
  value.
- Keep conversational setup, apologies, speculation, and process narration out
  of approved or handed-off artifacts.

## Scannable structure

Choose Markdown structure that helps a human or agent find the next decision
quickly.

- Use short sections with one purpose each.
- Use numbered lists for ordered decisions, commitments, tasks, and checks.
- Use tables when readers must compare the same fields across rows.
- Break wide or dense tables into smaller sections when the row content becomes
  harder to read than a list.
- Keep trace IDs stable and searchable when later work depends on them.

## Entity presentation

Use stable IDs with short titles wherever an entity list appears. Define an
entity family once when a reader needs the name; after that, compact forms such
as ``### `SPEC-001` Preserve logins`` are preferred. Use full names where they
improve first-read clarity, not as a repeated heading requirement.

## Verification Criterion placement

Keep the ordinary review path local: place a single-commitment Verification Criterion immediately below its Specification Commitment. Put a genuinely cross-cutting criterion exactly once in `## Cross-cutting Verification Criteria`. Explicit `Covers` metadata preserves navigation and stable IDs preserve references if Draft refinement moves a criterion.

## Proportional traceability

Use local links by default. Add a mapping only when it helps a reader or tool
check coverage, continue a handoff, or validate deterministically. Keep tasks
and checks in distinct sections; do not create a large table merely because IDs
exist.

Extra blank lines are useful around major sections, tables, and dense lists.
Avoid spacing that makes one related unit look like several unrelated blocks.

## Placeholder control

Placeholders are authoring aids. They must not survive approval, handoff, or
implementation completion unless they are structural grammar examples.

Allowed structural examples include names such as `<work-id>`,
`<spec-filename>`, `<phase-plan-filename>`, and `<commit-subject>` when the
document is teaching grammar or template shape.

Do not leave free-form fill text such as `<describe the thing>` in a concrete
work-item artifact. Replace it with a final value, `None`, `Not applicable`, or
a deferred item with an owner and resolving event.

## Traceability density

Traceability should reduce rereading, not bury the reader.

- Use IDs for Specification Commitments, Verification Criteria, risks, Architecture Decisions, amendments,
  variance entries, and validation checks when later artifacts cite them.
- Keep each ID attached to a short, concrete title.
- Cross-reference only the relationships a future reader needs to execute,
  validate, review, or assess variance.
- Avoid repeating full requirement text in every downstream table when an ID and
  concise note is enough.

## Template prompts

Templates are guidance surfaces. They should make the desired final artifact
shape visible without copying long reusable policy.

Template prompts should:

- Name the final value expected in each field.
- Prefer controlled states and concrete examples over broad conversational
  verbs.
- Remind agents to resolve required decisions, ownerless deferrals, and
  authoring scaffolds before freeze.
- Route mutable external evidence to `module:evidence` and
  `rule:evidence.preservation` instead of defining evidence policy locally.

Templates may use short cues such as "Final artifact content" or "Scannable
structure" when those cues prevent common mistakes. Long writing guidance
belongs in this module.
