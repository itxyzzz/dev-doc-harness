# Test Cases Snapshot

Work ID: `2026-07-07_superpowers-compat-guidance`
Short ID: `superpowers-compat-guidance`
Status: Approved
Harness release: `0.4+`
Schema: `schema:snapshot.test-cases`
Policy references: `module:lifecycle`, `module:quality`, `module:release`, `module:freeze-gate`, `rule:lifecycle.superpowers-compatibility`, `rule:lifecycle.documentation-matrix`, `rule:freeze.stop-before-implementation`, `rule:release.identity`, `rule:release.release-notes`

## Purpose

Preserve the expected review and validation cases for the Superpowers compatibility adapter and release-baseline correction before implementation begins.

## Test Cases

### `TC-001` Superpowers guidance keeps one durable source of truth

Requirement coverage:

1. `REQ-001`
2. `REQ-003`

Setup:

1. Review changed README, `AGENTS.md`, router, lifecycle, freeze-gate, and operator-note text.

Expected result:

1. Guidance says Superpowers may drive methodology while the harness owns canonical durable artifacts under `docs/work-items/<work-id>/`.
2. Guidance does not allow full duplicate specs or plans under `docs/superpowers`.
3. If `docs/superpowers` files are mentioned, they are pointer stubs only.

### `TC-002` Superpowers planning-to-execution transition pauses at the harness freeze gate

Requirement coverage:

1. `REQ-002`

Setup:

1. Review changed compatibility guidance and validator scenario anchors.

Expected result:

1. A Superpowers plan or design created during harness-managed work is copied or converted into the harness work-item folder before implementation.
2. The harness draft review and approval freeze gate happens before any Superpowers execution choice or implementation task begins.
3. Fresh post-freeze operator authorization is still required before implementation.

### `TC-003` Release baseline uses `0.5+` development marker and preserves the `0.x+` rule

Requirement coverage:

1. `REQ-004`

Setup:

1. Inspect `.agents/skills/dev-doc-harness/VERSION`, `.agents/skills/dev-doc-harness/references/release-policy.md`, `docs/release-branch-process.md`, and `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Expected result:

1. Current development marker is `0.5+`.
2. Release-policy examples no longer identify `0.4+` as the current release.
3. Release branch process guidance says that after release `0.x`, `master` and other non-default development branches remain on `0.x+` until release `0.x+1` preparation.
4. Validator release checks no longer expect `.agents/skills/dev-doc-harness/docs/releases/0.4+.md`.

### `TC-004` Released-minor notes exist for `0.4.0` and `0.5.0` only

Requirement coverage:

1. `REQ-004`
2. `REQ-005`

Setup:

1. Inspect `.agents/skills/dev-doc-harness/docs/releases/`.

Expected result:

1. `0.4.0.md` exists.
2. `0.5.0.md` exists.
3. No `0.6.0.md` or `0.6+.md` is created by this work.

### `TC-005` Harness validator passes

Requirement coverage:

1. `REQ-004`
2. `REQ-005`

Setup:

1. Run `python .agents\skills\dev-doc-harness\scripts\test_harness_policy.py`.

Expected result:

1. Command exits with status `0`.
2. Output reports all checks passing.
3. Superpowers compatibility and release identity/notes checks both pass.

### `TC-006` Search output has no contradictory current-release guidance

Requirement coverage:

1. `REQ-003`
2. `REQ-004`

Setup:

1. Run `rg -n "0\.4\+|0\.5\+|0\.x\+|0\.6|docs/superpowers|pointer stub|Superpowers" README.md AGENTS.md .agents/skills/dev-doc-harness docs/release-branch-process.md CHANGELOG.md`.

Expected result:

1. `0.5+` appears as the current development marker in current policy surfaces.
2. The generic `0.x+` rule appears in release-process guidance.
3. `0.4+` appears only in historical changelog or historical context if it appears at all.
4. No newly created `0.6` release-note path appears.
5. Superpowers guidance is consistent with canonical harness artifact ownership.

## Approval

- Status: Approved
- Superseded by: None
