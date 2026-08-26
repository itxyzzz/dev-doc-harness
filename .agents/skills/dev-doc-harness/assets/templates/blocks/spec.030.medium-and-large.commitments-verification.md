## Commitments and verification

Keep stable IDs and short titles. Put delivery scope in each Statement;
rationale and examples do not add scope. Every additional `SPEC-*` uses the
complete `SPEC-001` structure: Statement plus a local Verification Criterion,
unless a genuinely cross-cutting criterion explicitly supplies the evidence.

Use `must` for binding Statements and `should` for advisory prose; see `rule:quality.plain-language`.

### `SPEC-001` `<short title>`

Statement:

1. `<approved outcome, behavior, quality bar, constraint, or deliverable>`.

#### `VER-001` `<short title>`

Covers: `SPEC-001`.

Criterion: `<what proves the commitment>`.

Expected evidence: `<test, inspection, review, or other proof>`.

Applicability / owning phase (optional): `<where this applies or which phase owns the evidence, when useful>`.

### `SPEC-002` `<second title when needed>`

Statement:

1. `<second obligation, or remove this example>`.

#### `VER-002` `<second title when needed>`

Covers: `SPEC-002`.

Criterion: `<what proves this commitment>`.

Expected evidence: `<test, inspection, review, or other proof>`.

## Cross-cutting verification

Use this section only when one criterion genuinely covers multiple commitments.

### `VER-002` `<short title>`

Covers: `SPEC-001`, `SPEC-002`.

Criterion: `<shared proof without new delivery scope>`.

Expected evidence: `<shared evidence>`.

Applicability / owning phase (optional): `<where this applies or which phase owns the evidence, when useful>`.
