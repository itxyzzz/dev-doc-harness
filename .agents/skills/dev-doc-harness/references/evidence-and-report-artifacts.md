# Evidence And Report Artifacts

Use this reference when a work item needs durable evidence, derived review
artifacts, or report templates.

## Evidence policy

- Preserve source evidence once it is used for review, comparison, or handoff.
- Put repaired, normalized, or derived review artifacts in a separate location.
- Link derived artifacts back to their source evidence.
- Do not rewrite original evidence to hide drift, failed checks, or manual repair.

For harness-managed work, source evidence usually belongs under the work item
folder. Derived summaries may live under `handoff/`, `docs/living/`, or another
work-item-local review folder named in the plan.

## Artifact index

For evidence-heavy work, create a short index:

```md
# Artifact Index

- Work ID: `<work-id>`
- Source evidence: `<path>`
- Derived artifacts: `<path>`
- Snapshot policy: source evidence is preserved; derived artifacts are review-owned.

## Files

- `<artifact>`
- `<artifact>`
```

## Report sections

Keep reports sparse and specific.

| Report | Required sections |
|---|---|
| Research verification | Verification summary, verified claims, discrepancies, quality assessment, references. |
| Test report | Tests added or checked, commands run, results, remaining gaps. |
| Security review | Scope, findings by severity, changed files reviewed, unresolved risks, gate status. |
| Command log | Command, working directory, result, notable output, blocker if any. |
| Handoff summary | Scope, files changed, validation, assumptions, residual risk, next step. |

## Stop conditions

Stop and record the blocker when:

- A required input artifact is missing.
- A required report cannot be produced.
- A write would escape the approved workspace or work item scope.
- Verification fails after the planned repair attempts.
- Unresolved high-impact security, data, API, or scope risk appears.

High-impact variance still requires a plan amendment and operator approval before
proceeding.
