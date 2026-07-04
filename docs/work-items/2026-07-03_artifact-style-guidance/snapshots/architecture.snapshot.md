# Artifact Style Guidance Architecture Snapshot

Work ID: `2026-07-03_artifact-style-guidance`
Source spec: `../spec_artifact-style-guidance.md`
Status: Approved
Harness release: `0.4+`
Schema: `schema:snapshot.architecture`
Policy references: `module:lifecycle`, `module:quality`, `module:architecture`, `module:evidence`, `rule:lifecycle.work-item-architecture-decisions`, `rule:lifecycle.immutable-snapshots`, `rule:lifecycle.variance-policy`, `rule:quality.spec-handoff`, `rule:evidence.preservation`

## Purpose

Preserve the work-item architecture decision for adding artifact-style guidance without overloading routine harness routes or duplicating existing lifecycle, quality, model, and evidence policy.

## Decision Ledger

### `DEC-001` Add `module:artifact-style`

Selected approach:

1. Add a lightweight canonical reference at `.agents/skills/dev-doc-harness/references/artifact-style.md`.
2. Give it ownership of artifact readability, structure choice, placeholder and example grammar, template prompt boundaries, traceability density, and final cleanup style.

Affected boundaries:

1. Canonical module catalog.
2. Operation router.
3. Template policy references and local guidance cues.
4. Validator graph and structural checks.

Source spec sections:

1. `REQ-001`
2. `REQ-002`
3. `REQ-004`

Validation cues:

1. `AC-001`
2. `AC-002`
3. `AC-011`

Rejected alternatives:

1. Template-only cleanup, because it leaves no stable policy owner.
2. Broad repository documentation style guide, because it exceeds harness artifact needs.

### `DEC-002` Keep style routing conditional, with mandatory large-document cases

Selected approach:

1. Keep routine small/medium planning routes within the existing route-budget intent.
2. Make `module:artifact-style` mandatory for large anchor specs.
3. Require `module:artifact-style` when any spec, plan, snapshot, amendment, report, handoff, or operator-facing document becomes large enough that readability risk is material.
4. Keep a very short baseline readability block outside the style module so minimal direction remains visible without loading it.

Affected boundaries:

1. `SKILL.md` operation router.
2. `policy-architecture.md` router inputs and route-budget guidance.
3. `durable-planning-quality.md` baseline readability guidance.
4. Primary planning templates.

Source spec sections:

1. `REQ-002`
2. `REQ-003`
3. `REQ-004`

Validation cues:

1. `AC-003`
2. `AC-004`
3. `AC-012`

Rejected alternatives:

1. Always-required style module for every routine planning route, because that strains route-budget design.
2. Optional style guidance with no baseline cues, because that leaves routine artifacts under-guided.

### `DEC-003` Route evidence durability through `module:evidence`

Selected approach:

1. Keep mutable external evidence preservation under existing `module:evidence`.
2. Let the new style module cross-reference evidence preservation only where artifact readability depends on stable cited inputs.

Affected boundaries:

1. `artifact-style.md`
2. `durable-planning-quality.md`
3. Template evidence prompts where present.
4. Router guidance for evidence-heavy review or reports.

Source spec sections:

1. `REQ-008`

Validation cues:

1. `AC-009`

Rejected alternatives:

1. Duplicate evidence preservation rules in the style module, because it would create competing policy ownership.

### `DEC-004` Preserve frozen implemented artifacts

Selected approach:

1. Apply polish to current harness policy, templates, validation, and operator-facing docs.
2. Do not modify already implemented July 2 and July 3 specs, plans, or snapshots.

Affected boundaries:

1. Implementation diff scope.
2. Validation or manual review for historical artifact exclusion.

Source spec sections:

1. `REQ-011`

Validation cues:

1. `AC-013`

Rejected alternatives:

1. Rewrite frozen artifacts to remove template residue, because that would undermine immutable snapshot semantics.

## Decision Drivers

1. Durable artifacts must be easy for humans and agents to consume without hidden chat history.
2. Large anchor specs have high handoff value and high readability risk.
3. Routine routes should remain compact and practical.
4. Templates are the surfaces agents most often copy while drafting.
5. Existing module boundaries already separate lifecycle, quality, model strategy, evidence, and policy architecture.
6. Frozen historical artifacts should preserve what was approved.

## Constraints

1. `module:quality` owns what durable artifacts must preserve.
2. `module:lifecycle` owns artifact lifecycle, immutability, variance, documentation matrix, and changelog discipline.
3. `module:models` owns model and sub-agent policy.
4. `module:evidence` owns evidence preservation.
5. `module:architecture` already means policy architecture, not work-item architecture.
6. Generated templates must be changed through source blocks and assemblies.
7. Validator changes must remain structural and high-signal.

## Future Durable-Doc Boundary

This work item does not create a repository-level documentation style guide, ADR process, `ARCHITECTURE.md` workflow, or handoff snapshot schema. Those are separate future work items if needed.

## Approval

- Status: Approved
- Superseded by: None
