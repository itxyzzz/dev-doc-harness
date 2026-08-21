# Route Name Simplification Spec

Work ID: `2026-08-21_route-name-simplification`
Short ID: `route-name-simplification`
Status: Approved
Harness release: `0.9+`
Schema: `schema:spec.small-medium`
Companion plan: `plan_route-name-simplification.md`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `rule:lifecycle.documentation-assessment`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

## Goal

Make the active Dev Doc Harness route names concise and unambiguous: the former `lean/small` route becomes `small`, the former `small/medium` route becomes `medium`, and `large/phased` remains unchanged.

## Source and Intent

Source input:

1. The operator requested that the distracting `small/lean` (`small-lean`) and `small/medium` (`small-medium`) names be renamed throughout the harness, including operator-facing language and schemas/template names. Repository inspection confirmed that the implemented first route is currently rendered as `lean/small` (`lean-small`).
2. The operator approved a clean active-surface cutover without legacy aliases and added a mandatory sequence: rename `small/medium` to `medium` before renaming `lean/small` to `small`.

Desired operator outcome:

1. An operator can select and understand three distinct active routes named `small`, `medium`, and `large/phased` without encountering stale route-owned filenames, schemas, template blocks, or validation assertions.

Success summary:

1. The canonical active harness uses `small` only for the former lean route and `medium` only for the former small/medium route.
2. Generated templates and the policy validator agree with that namespace, while frozen historical records retain the terminology that was true when they were created.

## Scope Boundary

### In scope

1. Active router and operator guidance: `README.md`, `AGENTS.md`, `.agents/skills/dev-doc-harness/SKILL.md`, and `.agents/skills/dev-doc-harness/docs/operator-note.md`.
2. Active reference guidance: `references/artifact-contract.md`, `references/artifact-style.md`, `references/context-and-quality-gates.md`, `references/maintenance-architecture.md`, `references/planning-freeze-gates.md`, and `references/subagent-model-policy.md`.
3. Route-owned template filenames, assembly-manifest filenames and outputs, schemas, source-block filenames, generated templates, assembler assembly list, and policy-validator assertions.
4. The deterministic rename order, generated-output refresh, and validation evidence needed to establish the new canonical namespace.

### Non-scope

1. Changes to the behavior, eligibility, approval mechanics, lifecycle transitions, required policy inputs, or large/phased route.
2. Compatibility aliases, filename shims, schema normalization, or dual acceptance of old and new route namespaces.
3. Rewriting frozen `docs/work-items/**`, historical root `CHANGELOG.md` entries, or versioned release notes. A new implementation record may describe this migration, but existing historical text remains immutable.

## Repository Context

### Current state

1. The active harness has three implemented routes: `lean/small` with `lean-small` assets and schemas, `small/medium` with `small-medium` assets and schemas, and `large/phased` with `large-phased` assets.
2. The former medium route currently owns several `.small.` source blocks. Renaming the lean route first would collide with those block names and leave `small` ambiguous.
3. `assemble_templates.py` has an explicit six-item assembly registry, and `test_harness_policy.py` contains explicit route maps, schema assertions, permitted block scopes, active-template paths, and lean-flow fixture/scenario references.

### Evidence read

1. `README.md`, `AGENTS.md`, `.agents/skills/dev-doc-harness/SKILL.md`, `.agents/skills/dev-doc-harness/docs/operator-note.md`, and the six in-scope active reference files named in Scope Boundary.
2. `.agents/skills/dev-doc-harness/assets/templates/`, its `assemblies/` manifests and route-specific `blocks/`, plus `.agents/skills/dev-doc-harness/scripts/assemble_templates.py` and `scripts/test_harness_policy.py`.
3. Two authorized read-only audits of operator/template surfaces and schema/validation surfaces; both found the same namespace collision and advised preserving frozen history.

### Constraints and compatibility

1. Active route-owned terms must follow the ordered cutover: `small/medium` and `small-medium` to `medium` first; only then may `lean/small` and `lean-small` become `small`.
2. `large/phased` and `large-phased` remain exactly as they are.
3. The repository's immutable-snapshot rules prohibit editing frozen work items and historical release/changelog entries merely to remove old terminology.
4. Template outputs must be regenerated only through `assemble_templates.py`, and active harness changes must pass `test_harness_policy.py` before an implementation commit.

## Assumptions and Open Questions

### Assumptions

1. A clean cutover is appropriate because the operator explicitly approved no aliases and the harness is internally maintained in this repository.
2. Existing users of route-owned file paths and schema keys will migrate with the released harness; no external compatibility contract was identified in the repository audit.

### Open questions

1. None identified after repository-context review.

## Commitments and verification

### `SPEC-001` Establish the canonical route vocabulary

Statement:

1. The active harness must call the former `small/medium` route `medium` and the former `lean/small` route `small`; it must preserve `large/phased` unchanged.
2. Implementation must complete the medium rename before beginning the small rename.

#### `VER-001` Active route vocabulary is unambiguous

Covers: `SPEC-001`.

Criterion: Active canonical guidance and templates use `small`, `medium`, and `large/phased` as the only route labels, with no stale route-label or route-identifier occurrence outside preserved history.

Expected evidence: Focused active-surface searches and review of the generated templates.

### `SPEC-002` Rename route-owned template and schema namespaces

Statement:

1. The harness must rename former medium template and manifest filenames from `small-medium-*` to `medium-*`, schemas from `schema:*\.small-medium` to `schema:*.medium`, and former-medium `.small.` blocks to `.medium.`.
2. After the medium namespace is free, the harness must rename former small template and manifest filenames from `lean-small-*` to `small-*`, schemas from `schema:*\.lean-small` to `schema:*.small`, and former-small `.lean.` blocks to `.small.`.

#### `VER-002` Generated namespace is internally consistent

Covers: `SPEC-002`.

Criterion: Every manifest output, assembler registry entry, generated template header, source-block reference, and validator assertion resolves to the corresponding `medium` or `small` canonical path and schema.

Expected evidence: `assemble_templates.py --check` reports all generated templates current, and the policy validator passes.

### `SPEC-003` Keep validation authoritative through the migration

Statement:

1. The policy validator must encode the new route names, schemas, block scopes, active-template paths, and lean-route scenario identity without accepting obsolete canonical names.
2. The implementation must retain all existing behavioral contracts, changing only the terminology and route-owned identity under this specification.

#### `VER-003` Validation rejects stale canonical surfaces

Covers: `SPEC-003`.

Criterion: The complete harness policy validator passes after the cutover, and focused searches find no old route-owned name in active non-historical surfaces.

Expected evidence: Successful validator output and recorded zero-match search results.

### `SPEC-004` Preserve historical records

Statement:

1. The implementation must not modify frozen work-item artifacts, existing root changelog history, or versioned release notes to retroactively rename prior route terminology.

#### `VER-004` Historical boundaries remain intact

Covers: `SPEC-004`.

Criterion: The implementation diff contains no edits to `docs/work-items/**` other than this work item's new implementation evidence, no edits to existing root changelog entries, and no edits to versioned release notes.

Expected evidence: `git diff --check`, scoped diff review, and `git diff --name-only` evidence before the implementation commit.

## Architecture Decisions

Architecture snapshot status:

1. Not applicable: this is a coordinated naming migration within existing harness files; it makes no new architecture, interface, data, configuration, infrastructure, or phase-ownership decision.

Decision summary:

1. Drivers: eliminate confusing compound route labels while retaining the three-route lifecycle model.
2. Constraints: the old medium route occupies the `small` source-block namespace, so the requested order is required to avoid collisions.
3. Selected approach: hard cutover in two ordered namespace passes, updating generated sources and validator contracts in each pass.
4. Affected boundaries: active operator docs, route policy, templates, schemas, generated outputs, assembler, and validator.
5. Rejected alternatives: aliases and dual schemas would preserve the ambiguity; historical rewrites would violate immutable-record rules; renaming the lean route first risks collisions.
6. Validation cues: `VER-001` through `VER-004`, assembler freshness, policy-validator success, and scoped diff review.

## Impact Surfaces

### Interfaces

- Internal template filenames, assembly manifests, schema literals, source-block names, generated template headers, and validator search contracts change to the new names.

### Data, config, and persistence

- No runtime data, persistence, configuration, or deployment behavior changes.

### State and control flow

- The route-selection and lifecycle behavior stays unchanged. The implementation's rename order is a temporary control-flow constraint for avoiding namespace conflicts.

### Safety, security, privacy, migration, and rollback

- The cutover is a repository-internal naming migration. Rollback is a normal source-control revert of the cohesive implementation commit; no data migration is involved.

## Risks and Rejected Alternatives

### `RISK-001` Namespace collision during rename

Decision or mitigation:

1. Complete and validate the former medium rename before any former-small file, block, schema, or prose receives the `small` name.

Notes:

1. High likelihood if the order is reversed; a partial or reversed rename can make route ownership ambiguous.

### `RISK-002` Stale machine-facing references

Decision or mitigation:

1. Update the assembler and validator in the same task as each route namespace, regenerate outputs, and run the policy validator before finalizing.

### `RISK-003` Loss of historical accuracy

Decision or mitigation:

1. Restrict terminology changes to active canonical surfaces and preserve frozen work items, existing changelog entries, and release notes.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `docs: route-name-simplification -- approve canonical small and medium naming` |
| Implementation | `refactor: route-name-simplification -- simplify active harness route names` |

## Documentation assessment

- `DOC-TEST-CASE`: Required — `snapshots/test-cases.snapshot.md`; Plan Task: `TASK-003`.
- `DOC-TEST-GUIDE`: Not required — existing deterministic assembler and policy-validator commands remain the verification interface.
- `DOC-OPS-GUIDE`: Required — `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md`; Plan Tasks: `TASK-001`, `TASK-002`.
- `DOC-API-GUIDE`: Not required — the harness exposes no external runtime API.
- `DOC-ARCH-SUMMARY`: Not required — no work-item architecture decision exists beyond local rename mechanics.

## Planning shape and transition ownership

1. Planning shape: `combined small/medium`.
2. Companion plan: `plan_route-name-simplification.md` is drafted and reviewed with this specification.
3. Transition owner: `plan_route-name-simplification.md` owns the `plan execution` transition after the combined package freezes.
4. Next lifecycle stage: `plan execution`.

## Spec readiness checklist

- [x] Goal, source and intent, scope, constraints, architecture decisions, commitment statements, and verifications are mutually consistent.
- [x] All relevant operator input and authorized audit evidence is preserved in this specification.
- [x] Commitment statements are atomic, bounded, and cover the full approved scope.
- [x] Verification criteria cover all commitments without adding hidden scope.
- [x] This specification is self-contained for a fresh planning or execution session.
- [x] Documentation assessment covers every required decision.
- [x] No unresolved placeholders, plan-affecting decisions, missing sections, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
