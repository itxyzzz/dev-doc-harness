# Architecture Snapshot

Work ID: `2026-07-07_superpowers-compat-guidance`
Short ID: `superpowers-compat-guidance`
Status: Approved
Harness release: `0.4+`
Schema: `schema:snapshot.architecture`
Policy references: `module:lifecycle`, `module:quality`, `module:release`, `rule:lifecycle.work-item-architecture-decisions`, `rule:lifecycle.immutable-snapshots`, `rule:lifecycle.variance-policy`, `rule:lifecycle.superpowers-compatibility`, `rule:quality.spec-handoff`, `rule:release.identity`, `rule:release.release-notes`

## Purpose

Capture the work-item architecture decisions that future implementation and review must preserve while improving Superpowers compatibility guidance and correcting the release-validation baseline.

## Decision Ledger

### `DEC-001` Keep harness work-item artifacts canonical when Superpowers is active

Selected approach:

1. Superpowers remains the methodology layer for brainstorming, design, planning technique, TDD, execution, review, and finishing.
2. The harness remains the canonical artifact and lifecycle layer for durable specs, plans, snapshots, freeze gates, variance, changelog, and model/sub-agent notation.
3. If a Superpowers skill creates or expects `docs/superpowers` files during harness-managed work, those files may only be pointer stubs with a title, status, and link to the canonical harness package or artifact under `docs/work-items/<work-id>/`.

Affected boundaries:

1. Repositories: `D:\Code\dev-doc-harness`.
2. Components or modules: `README.md`, `AGENTS.md`, `.agents/skills/dev-doc-harness/SKILL.md`, lifecycle and freeze references, operator note, validator, and optionally template source blocks.
3. Interfaces, schemas, config, or infra: harness artifact layout, Superpowers compatibility guidance, validator structural scenarios.
4. Agentic, process, documentation, or phase boundaries: Superpowers planning-to-execution transitions must pause for the harness freeze gate before implementation.

Source spec sections:

1. `REQ-001`
2. `REQ-002`
3. `REQ-003`
4. `RISK-001`
5. `RISK-002`

Validation cues:

1. `AC-001`
2. `AC-002`
3. `AC-003`
4. `AC-004`
5. `AC-005`
6. `AC-009`

Rejected alternatives:

1. Duplicating full durable specs and plans under `docs/superpowers` is rejected because it creates two sources of truth.
2. Replacing Superpowers with harness-native methodology is rejected because the harness explicitly does not own TDD, code-review methodology, or execution technique.
3. Leaving guidance at a high-level compatibility sentence is rejected because the current practical conflict is about paths, commits, and execution timing.

### `DEC-002` Treat `0.x+` as the post-release development baseline

Selected approach:

1. Align `.agents/skills/dev-doc-harness/VERSION`, release policy examples, release branch process guidance, and validator release checks with the already available `release/0.5` branch.
2. Expect package-local release notes for released minors `0.4.0` and `0.5.0`.
3. Do not create `0.6` release notes until the future release branch process creates that branch.
4. Preserve the generic release-marker rule: after release `0.x`, `master` and other non-default development branches stay on `0.x+` until release `0.x+1` preparation.

Affected boundaries:

1. Repositories: `D:\Code\dev-doc-harness`.
2. Components or modules: `.agents/skills/dev-doc-harness/VERSION`, `.agents/skills/dev-doc-harness/references/release-policy.md`, `.agents/skills/dev-doc-harness/docs/releases/`, `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, `docs/release-branch-process.md`, and `CHANGELOG.md`.
3. Interfaces, schemas, config, or infra: package-local release marker and validator release-note expectations.
4. Agentic, process, documentation, or phase boundaries: release branch process remains the owner for creating future `0.6` release notes.

Source spec sections:

1. `REQ-004`
2. `REQ-005`
3. `RISK-003`
4. `RISK-005`

Validation cues:

1. `AC-006`
2. `AC-007`
3. `AC-008`

Rejected alternatives:

1. Creating `.agents/skills/dev-doc-harness/docs/releases/0.4+.md` is rejected because development markers are not release versions.
2. Advancing to `0.6+` is rejected because the operator stated that `0.6` notes should be created only when that branch is created.
3. Ignoring the validator failure is rejected because it would hide real release-baseline drift in later implementation work.

## Decision Drivers

1. Operators need a practical, low-friction way to use Superpowers without violating harness artifact lifecycle rules.
2. Future agents need a single durable artifact source of truth for substantial work.
3. Freeze gates must preserve explicit approval before implementation even when another workflow would normally continue.
4. Validator output should distinguish real policy drift from expected release state.
5. Release notes must remain curated release artifacts, not development-marker placeholders.

## Constraints

1. Repository-local `AGENTS.md` and operator instructions override Superpowers default artifact paths.
2. Canonical harness rules live in routed references; README and operator-note prose should not become competing policy.
3. Full durable specs and plans under `docs/superpowers` are not allowed for harness-managed work.
4. Current branch for this work is `compatibility-improv`.
5. Remote `release/0.5` exists.
6. Current implementation must not create `0.6` release artifacts.

## Future Durable-Doc Boundary

Repository-level durable architecture documents such as `ARCHITECTURE.md` are future work for a separate harness extension. This work does not create `deltas/architecture-summary.delta.md` because the decisions are specific to the compatibility guidance and release-baseline package.

## Approval

- Status: Approved
- Superseded by: None
