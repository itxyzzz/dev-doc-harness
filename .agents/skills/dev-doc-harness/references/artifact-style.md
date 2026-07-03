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

## Final artifact content

Write durable artifacts as final repository documents, not as chat transcripts
or drafting instructions.

Use precise, descriptive language:

- State decisions, constraints, scope, and acceptance criteria directly.
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
- Use numbered lists for ordered decisions, requirements, tasks, and checks.
- Use tables when readers must compare the same fields across rows.
- Break wide or dense tables into smaller sections when the row content becomes
  harder to read than a list.
- Keep trace IDs stable and searchable when later work depends on them.

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

- Use IDs for requirements, acceptance criteria, risks, decisions, amendments,
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
