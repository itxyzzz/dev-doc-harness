## Specification Commitments and Local Verification Criteria

A Specification Commitment defines normative delivery scope. Keep every implementation obligation in its `Statement`; Architecture Decisions may realize or constrain mapped scope but cannot create an independent obligation.

Choose one `Kind`: `Outcome`, `Behavior`, `Quality`, `Constraint`, or `Deliverable`. Precedence is named output, measurable degree, conditional response, restriction/prohibition, otherwise implementation-controlled end state.

Choose one `Intent`: `Establish`, `Change`, `Preserve`, `Maintain`, or `Prevent`. Precedence is prohibition, named regression baseline, ongoing invariant, alteration, otherwise creation. `Concerns` are optional non-normative tags.

### `SPEC-001` Specification Commitment — `<short descriptive title>`

Kind: `<Outcome | Behavior | Quality | Constraint | Deliverable>`

Intent: `<Establish | Change | Preserve | Maintain | Prevent>`

Concerns: `<optional concise tags or None>`

Statement:

1. `<implementation-neutral normative obligation>`.

Rationale:

1. `<non-normative reason; do not add scope here>`.

#### `VER-001` Verification Criterion — `<short descriptive title>`

Covers:

1. `SPEC-001`.

Criterion:

1. `<pass/fail conformance proposition>`.

Expected evidence:

1. `<evidence needed to judge the proposition>`.

Applicability:

1. `<non-default timing, environment, phase, or condition; otherwise omit>`.

Applicable criteria and numbered evidence items are conjunctive by default. Equivalent alternatives use an explicit `Any one of` group with an equivalence basis. Concrete procedures belong in Plan Checks.

### `SPEC-002` Specification Commitment — `<second short title when needed>`

Kind: `<Outcome | Behavior | Quality | Constraint | Deliverable>`

Intent: `<Establish | Change | Preserve | Maintain | Prevent>`

Statement:

1. `<second normative obligation, or remove this example block when unused>`.

## Cross-cutting Verification Criteria

Define a criterion covering two or more commitments exactly once here. Cross-phase criteria name one owning phase in Applicability.

### `VER-002` Verification Criterion — `<short cross-cutting title>`

Covers:

1. `SPEC-001`.
2. `SPEC-002`.

Criterion:

1. `<shared pass/fail conformance proposition without new delivery scope>`.

Expected evidence:

1. `<evidence needed across the covered commitments>`.

Applicability:

1. `<owning phase or other non-default condition>`.
