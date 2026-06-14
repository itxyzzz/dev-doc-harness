# Commit Message Format Spec

Work ID: `2026-06-14-commit-message-format`
Short ID: `commit-message-format`
Status: Approved
Harness release: `unknown`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:quality`, `rule:lifecycle.documentation-matrix`, `rule:quality.spec-handoff`

## Goal

Make commit messages a deliberate, reviewable part of the harness planning process so harness-managed history is informative, consistent, and aligned with the planning artifacts and changelog.

## Scope

- Add a canonical lifecycle rule for harness commit message format.
- Apply the format to all commits made under the harness, including planning approval, implementation, phase, amendment, validation, release, and maintenance commits.
- Require commit subjects to start with the work short ID; when an issue tracking ID is present, the short ID already includes that issue key.
- Keep planning approval commit subjects stable and tied to the approved artifact type.
- Require implementation and other non-approval commit subjects to use the work short ID, a compact type, and an informative action snippet.
- Require planned commit subjects to appear in specs and plans so operators can review and request wording changes during normal artifact review.
- Require commit subject wording to stay synchronized with the matching `CHANGELOG.md` entry heading or title snippet.
- Update affected templates and canonical references so future work items expose planned commit subjects before approval.

## Non-scope

- No git hook, CI check, or automated enforcement script is required in this work item.
- No rewrite of historical commit messages or historical changelog headings.
- No adoption of the full Conventional Commits specification beyond the small type-and-scope format approved here.
- No change to package release note curation other than preserving clearer changelog source headings.

## Current state

The harness requires `CHANGELOG.md` to be updated before every commit and requires planning artifacts to pass the approval freeze gate before implementation. It does not currently define commit subject formats or require commit subjects to be planned. Recent history contains readable but inconsistent subjects such as `Approve release versioning phase 03 plan`, `Implement release versioning package identity`, and `Harden release versioning validation`.

Because commit messages are not treated as reviewable planning content, approval commits and implementation commits can drift from the artifact titles and changelog headings. Operators also cannot suggest commit naming changes during spec or plan review because planned subjects are not recorded.

## Proposed behavior

Add `rule:lifecycle.commit-message-format` to `artifact-contract.md` as the canonical policy for harness-managed commits.

All harness commits must use a planned or documented subject. The subject must start with the work short ID. If an issue tracking ID is present in the work ID, the short ID already includes that issue key, so the issue key must not be duplicated as a separate prefix.

Planning approval commits use stable approval formats. The examples below use uppercase syntax variables, not unresolved planning placeholders:

```text
SHORT-ID - Spec: TITLE-SNIPPET
SHORT-ID - Plan: TITLE-SNIPPET
SHORT-ID - Phase N plan: TITLE-SNIPPET
SHORT-ID - Amendment NNN: TITLE-SNIPPET
```

Implementation and other non-approval commits use a small typed format:

```text
SHORT-ID TYPE: EXPANDED-TITLE-SNIPPET
```

For example: `KEY-123 chore: update Spring Boot to 3.4`.

Allowed types are `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `spike`, `release`, and `security`.

The title snippet is the human-readable phrase shared by the durable planning artifact, planned commit row, and `CHANGELOG.md` entry heading. Implementation snippets should be more informative than planning approval snippets and should describe the concrete delivered change or phase output.

Commit subjects and changelog entry titles must stay synchronized:

- The `CHANGELOG.md` entry heading for a commit must contain the same work ID and the same title snippet represented in the planned commit subject.
- When a commit subject changes during review or implementation, the matching planned commit row and changelog heading must be updated before committing.
- When one changelog entry covers multiple commits for the same work item, each commit subject must match a listed planned commit row or a clear bullet-level title snippet under that changelog heading.

Specs and plans gain a `Planned commits` section. For small/medium work, the spec records the expected planning approval subject and the plan records the concrete implementation and validation commit subjects. For large or phased work, the anchor spec records the anchor approval subject and expected phase-plan subject pattern, while each phase plan records concrete approval and implementation commit subjects for that phase.

## Interfaces and data

Affected documentation and template interfaces:

- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md`
- `README.md` if operator-facing flow summaries mention approval commits or changelog discipline.
- `CHANGELOG.md` before implementation commits.

No runtime APIs, data schemas, persistence, or CLI behavior are affected.

## Risks

- A too-strict format could make small commits feel cumbersome. Mitigation: keep the subject patterns compact and allow a small type list.
- Changelog and commit-subject synchronization can be misunderstood when one changelog entry covers multiple implementation commits. Mitigation: explicitly allow matching bullet-level snippets under a shared work-item heading.
- Templates could become noisy if the planned commit section is too large. Mitigation: keep the section compact and require only the likely approval and implementation subjects.
- Historical examples may remain inconsistent. Mitigation: state that historical rewrites are out of scope and update current reusable examples only.

## Acceptance criteria

- `artifact-contract.md` owns `rule:lifecycle.commit-message-format` and defines short-ID prefixing, non-duplicated issue keys, approval commit formats, typed implementation formats, allowed types, planned-subject requirement, and changelog synchronization invariant.
- `planning-freeze-gates.md` requires approval freeze commits to use the planned subject from the approved artifacts.
- Small/medium, large/phased, phase-plan, and amendment templates include a compact `Planned commits` section.
- Template guidance requires operators to review planned commit subjects during normal spec and plan review.
- Changelog guidance says headings or bullet-level title snippets must stay synchronized with commit subject snippets.
- Validation confirms no current canonical template or reference still treats commit messages as an unspecified implementation detail.

## Planned commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `commit-message-format - Spec: commit message format` | `2026-06-14-commit-message-format: commit message format` | Approval commit for this spec and plan after operator approval. |
| Implementation | `commit-message-format docs: define harness commit message format` | `2026-06-14-commit-message-format: define harness commit message format` | Implementation commit for canonical references, templates, README if needed, and changelog. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Heading/title snippet must match the planned commit subject snippet. |
| Test cases | Snapshot | No | Before implementation | `snapshots/test-cases.snapshot.md` | Documentation-only policy change; validation commands cover behavior. |
| Testing guide delta | Living delta | No | During or after implementation | `deltas/testing-guide.delta.md` | No test workflow change beyond validation command expectations. |
| Operator manual delta | Living delta | No | After implementation | `deltas/operator-manual.delta.md` | No separate operator manual exists in scope. |
| API reference delta | Living delta | No | During or after API work | `deltas/api-reference.delta.md` | No public API change. |
| Architecture snapshot | Snapshot | No | Before or after design stabilization | `snapshots/architecture.snapshot.md` | This adds lifecycle policy but does not change harness architecture. |
| Architecture summary delta | Living delta | No | After review | `deltas/architecture-summary.delta.md` | No long-lived architecture summary update required. |

## Approval

- Status: Approved
- Superseded by: not applicable
