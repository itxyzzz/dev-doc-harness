# Plain-language Artifact Policy Architecture Snapshot

Work ID: `2026-07-14_plain-language-artifacts`
Status: Approved
Source spec: `spec_plain-language-artifacts.md`

## Decision record

### `DEC-001` Architecture Decision — Anchor modal language in the authoring path

Status: Approved

Source spec sections:

1. `SPEC-001`.
2. `SPEC-002`.
3. `SPEC-003`.

Context:

1. The current commitment model makes authoring statements prominent, but the prior modal-language preference exists only in immutable historical material.
2. A policy rule without required routing or template visibility is easy for future planning agents to miss.

Decision:

1. `module:artifact-style` owns the modal-language rule.
2. `SKILL.md` requires that module for small/medium drafting.
3. The shared commitment source block repeats one concise cue; generated templates are assembler outputs.
4. The existing policy validator checks the complete authoring path and a narrow active-path scan.

Consequences:

1. Small/medium planners load one additional required reference.
2. The style rule has one canonical owner and one controlled wording exception.
3. Validator maintenance remains bounded because it validates declared active paths rather than repository-wide prose.

Rejected alternatives:

1. Keeping the instruction only in a template.
2. Adding the rule only to a general policy paragraph with no routing change.
3. Scanning every repository file, including frozen work items and legal text.
4. Rewriting historical artifacts.

Validation:

1. `VER-001` through `VER-003` and `CHECK-001` through `CHECK-004` in the combined package.

## Boundary map

| Boundary | Owner or producer | Consumer | Constraint |
|---|---|---|---|
| Canonical modal rule | `artifact-style.md` | planners and templates | One semantic owner. |
| Required discovery | `SKILL.md` | small/medium drafting agents | Style module loads before authoring. |
| Moment-of-writing cue | shared specification source block | generated specification templates | Prompt stays concise. |
| Regression protection | policy validator | maintainers and CI-like local checks | Active paths only; controlled exceptions only. |
| Historical and legal material | frozen work items and `LICENSE` | readers | No rewrite and no scan target. |

## Approval

- Status: Approved
- Superseded by: None
