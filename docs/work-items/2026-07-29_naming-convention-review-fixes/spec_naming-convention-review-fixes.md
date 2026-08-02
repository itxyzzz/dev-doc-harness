# Naming Convention Review Fixes Spec

Work ID: `2026-07-29_naming-convention-review-fixes`
Short ID: `naming-convention-review-fixes`
Status: Approved
Harness release: `0.8+`
Schema: `schema:spec.small-medium`
Companion plan: `plan_naming-convention-review-fixes.md`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

## Goal

Make the canonical naming reference internally consistent and remove the review-identified duplication without rewriting historical frozen work-item artifacts.

## Source and Intent

Source input:

1. Seven inline review comments on `.agents/skills/dev-doc-harness/references/naming-conventions.md` dated 2026-07-29.

Desired operator outcome:

1. Current reusable harness policy uses two-digit amendment identifiers, kebab-case planning artifact types, a consistent optional issue-key expression, and the canonical `<date> <commit-subject>` changelog-heading grammar.

Success summary:

1. The naming reference states each current grammar once at its owning location, dependent current policy and validator checks agree, and the harness validator passes.

## Scope Boundary

### In scope

1. Review-driven corrections to current reusable naming policy, its direct lifecycle consumer, and focused validator assertions.
2. Replace `NNN` amendment placeholders with `NN`, including the canonical example using `01`.
3. Use kebab-case `phase-NN-plan` and `amendment-NN` artifact types.
4. Canonicalize the work-ID optional issue-key expression as `<date>_[<issue-key>_]<short-title>`.
5. Remove local restatements that duplicate Fields or Derived patterns, and retain one date-and-subject changelog heading grammar.

### Non-scope

1. Rewriting historical changelog entries, frozen specs, plans, snapshots, or prior examples under `docs/work-items/`.
2. Changing the separator convention between semantic fields or title normalization rules.
3. Renaming existing work-item directories or previously created amendment files.

### Assumptions

1. The review clarification establishes `## <date> <commit-subject>` as the sole changelog-heading grammar. The harness specifies a commit subject, not a full commit message.
2. Historical files are retained as immutable evidence of their original conventions.

### Open questions

1. None identified after repository-context review.

## Repository Context

### Current state

1. `naming-conventions.md` currently uses prose artifact types with spaces, `NNN` amendment identifiers, and duplicated local restatements of canonical grammar.
2. The current validator asserts the `plan_amendment-NNN` text. `artifact-contract.md` still permits a full commit message as a changelog heading instead of referring to the commit-subject grammar.
3. The worktree already contains an unrelated-to-this-package uncommitted one-line edit to the naming reference's `<changelog-heading>` table row; implementation must reconcile that row with the approved heading grammar rather than discard it.

### Evidence read

1. `.agents/skills/dev-doc-harness/references/naming-conventions.md`.
2. `.agents/skills/dev-doc-harness/references/artifact-contract.md`.
3. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
4. `.agents/skills/dev-doc-harness/SKILL.md`, its planning templates, and applicable `AGENTS.md` instructions.

### Constraints and compatibility

1. The repository-local Dev Doc Harness requires a combined small/medium package, an approval freeze, a planning-only commit, and fresh authorization before implementation.
2. Current reusable policy and validation must change together; frozen historical work-item artifacts must not be silently rewritten.

## Commitments and verification

### `SPEC-001` Canonical naming grammar

Statement:

1. Current reusable naming policy must use `phase-NN-plan`, `amendment-NN`, `<date>_[<issue-key>_]<short-title>`, and `<date> <commit-subject>` as the one changelog-heading grammar; examples must demonstrate the same grammar.

#### `VER-001` Canonical grammar evidence

Covers: `SPEC-001`.

Criterion: The canonical reference and direct lifecycle consumer express the approved grammar without conflicting duplicate forms.

Expected evidence: Focused inspection and targeted searches of current reusable policy surfaces.

### `SPEC-002` Current-policy validation and historical preservation

Statement:

1. The validator must assert the updated current naming policy, and implementation must not alter historical work-item artifacts solely to normalize old examples.

#### `VER-002` Validator and scope evidence

Covers: `SPEC-002`.

Criterion: The full harness-policy validator passes and the implementation diff is limited to approved current-policy, validator, changelog, and work-item-package paths.

Expected evidence: Harness validator output and `git diff --check` plus a scoped diff inspection.

## Architecture Decisions

Architecture snapshot status: Not applicable; this is a localized documentation-policy correction with no architectural boundary change.

Decision summary:

1. Drivers: reviewer-requested consistency and reduced duplication.
2. Constraints: preserve immutable historical artifacts and one source of truth per grammar.
3. Selected approach: update only active reusable surfaces and their direct validator assertions.
4. Affected boundaries: naming policy, lifecycle wording, and harness-policy validation.
5. Rejected alternatives: bulk-renaming historical artifacts and retaining an alternate work-ID or full-commit-message changelog heading.
6. Validation cues: `VER-001`, `VER-002`, and the plan checks.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. Harness artifact and changelog naming grammar in documentation and validator expectations.

### Data, config, and persistence

1. None.

### State and control flow

1. None.

### Safety, security, privacy, migration, and rollback

1. None identified after repository-context review. The change is documentation and validation policy only; existing historical names remain valid records.

## Risks and Rejected Alternatives

### `RISK-001` Incomplete grammar alignment

Decision or mitigation:

1. Search current reusable harness surfaces and update the focused validator before running the full policy test.

Notes:

1. Historical occurrences are intentionally excluded from normalization unless a separate approved migration is requested.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: naming-convention-review-fixes -- approve naming cleanup` |
| Implementation | `docs: naming-convention-review-fixes -- reconcile review feedback` |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Root changelog | Living | Yes | Planning freeze | `CHANGELOG.md` | Required by the repository freeze gate. |
| Changelog source | Living | Yes | Before planning-freeze commit | `changelog/planning-approval.md` | Required by the harness approval-freeze gate; its entry title matches the planning-approval subject. |
| Test cases | Snapshot | No | N/A | N/A | Focused validator checks are documented in the plan. |
| Testing guide delta | Living delta | No | N/A | N/A | No user-facing test workflow changes. |
| Operator manual delta | Living delta | No | N/A | N/A | No operator workflow changes beyond the policy text itself. |
| API reference delta | Living delta | No | N/A | N/A | No API changes. |
| Architecture snapshot | Snapshot | No | N/A | N/A | No work-item architecture decision. |
| Architecture summary delta | Living delta | No | N/A | N/A | No durable architecture change. |

## Planning shape and transition ownership

1. Planning shape: `combined small/medium`.
2. Companion plan: `plan_naming-convention-review-fixes.md` is drafted with this spec.
3. Transition owner: the companion plan owns the implementation handoff after an approved freeze.
4. Next activity: implement the approved naming-policy corrections and validator alignment.

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Commitments and verification criteria are bounded and testable.
- [x] Repository evidence, constraints, and historical-artifact boundary are recorded.
- [x] Architecture, interface, data, and safety impacts are explicitly assessed.
- [x] Documentation artifact decisions and planned commits are explicit.
- [x] The companion plan is present and owns the implementation handoff.
- [x] Sub-agents: None; the scoped sequential documentation and validator changes do not justify delegation.
- [x] No unresolved placeholders, required decisions, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
