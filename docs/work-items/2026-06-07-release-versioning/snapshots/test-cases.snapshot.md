# Release Versioning Test Cases Snapshot

Work ID: `2026-06-07-release-versioning`
Status: Final
Harness release: `0.3.0`

## Purpose

Capture the release validation scenarios that must exist before Phase 03 implementation begins. These cases focus on `0.3.0` package identity, changelog-derived release notes, current-release changelog metadata, package boundary, template release context, and team adoption or rollback discoverability.

## Source references

- Approved spec: `../spec-release-versioning.md`
- Architecture snapshot: `architecture.snapshot.md`
- Draft Phase 03 plan: `../plan-phase-03-release-hardening-release-versioning.md`
- Package release policy: `../../../../.agents/skills/dev-doc-harness/references/release-policy.md`
- Package release notes: `../../../../.agents/skills/dev-doc-harness/docs/releases/0.3.0.md`

## Release scenarios

| Scenario ID | Entrypoint | Required files or modules | Expected behavior | Script evidence checked |
|---|---|---|---|---|
| `scenario:release.package-identity` | `.agents/skills/dev-doc-harness/VERSION` | `module:release`, `rule:release.identity`, `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md` | A team or agent can identify the installed harness as `0.3.0`, and release notes for that version are present inside the package. | `release.identity` checks the exact version marker and matching release-note file. |
| `scenario:release.release-notes-source` | `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md` then `CHANGELOG.md` | `rule:release.changelog-source`, `rule:release.release-notes` | Release notes contain the required release-facing sections and trace listed source entries back to actual changelog headings. | `release.notes` checks required headings and source heading traceability. |
| `scenario:release.changelog-schema` | `CHANGELOG.md` | `rule:release.changelog-source`, current `2026-06-07-release-versioning` entries | Current release-versioning changelog entries carry low-friction release metadata without forcing historical changelog rewrites. | `release.changelog-schema` checks `Release target`, `Package impact`, and `Release-note` fields for current release entries only. |
| `scenario:release.package-boundary` | `.agents/skills/dev-doc-harness/references/release-policy.md`, release notes, and README | `rule:release.package-boundary`, `rule:release.team-adoption` | The distributable package is discoverable as root `AGENTS.md` plus `.agents/`, and this repository's `docs/work-items/` is excluded from downstream copies. | `release.package-boundary` checks package-boundary and exclusion wording in package-local policy plus repository guidance. |
| `scenario:release.template-context` | Work-item templates under `.agents/skills/dev-doc-harness/assets/templates/` | `rule:release.artifact-context`, current template schema anchors | New work-item artifacts have exactly one harness release context field and avoid extra versioning fields. | `release.template-context` checks one literal `Harness release: <version or unknown>` line per current template. |
| `scenario:release.team-adoption-rollback` | Release policy, release notes, and README | `rule:release.team-adoption` | Team repositories can adopt via a dedicated harness update commit or PR and roll back by reverting that update. | `release.package-boundary` checks rollback and revert guidance in package-local and README surfaces. |

## Validation command

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1
```

Expected result: the command exits `0` and prints one `PASS <check-id>` line for every existing harness check plus the Phase 03 `release.*` checks.

## Negative-check safety

Negative checks must not leave temporary mutations in the worktree. If an implementation agent tests failure behavior by temporarily changing `VERSION`, release notes, changelog metadata, package-boundary text, or template release fields, restore the original content before staging or committing.
