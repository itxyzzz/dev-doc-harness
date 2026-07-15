# Active Authoring Baseline

Work ID: `2026-07-14_harness-simplification`
Status: Approved

This fixed manifest measures the author-facing Markdown surfaces that this work
item changes. It includes reusable sources and generated templates because both
are read by future agents. It excludes Python validation code, work-item
evidence, changelog fragments, frozen history, and `LICENSE`.

## Manifest

1. `.agents/skills/dev-doc-harness/SKILL.md`
2. `.agents/skills/dev-doc-harness/docs/operator-note.md`
3. `.agents/skills/dev-doc-harness/references/artifact-contract.md`
4. `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`
5. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
6. `.agents/skills/dev-doc-harness/references/artifact-style.md`
7. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
8. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.030.common.commitments-verification.md`
9. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.020.common.traceability-approach-surfaces.md`
10. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.050.common.task-plan.md`
11. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.070.common.validation-variance-freeze.md`
12. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.common.handoff.md`
13. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.090.small.readiness-completion-approval.md`
14. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.090.phase.readiness-completion-approval.md`
15. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
16. `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
17. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
18. `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
19. `.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md`
20. `.agents/skills/dev-doc-harness/assets/templates/variance-log.md`
21. `README.md`

## Counting command

Run this command from `D:\Code\dev-doc-harness` before editing and again after
validation. Do not change its path list or token rule during this work item.

```powershell
$paths = @(
  '.agents/skills/dev-doc-harness/SKILL.md',
  '.agents/skills/dev-doc-harness/docs/operator-note.md',
  '.agents/skills/dev-doc-harness/references/artifact-contract.md',
  '.agents/skills/dev-doc-harness/references/context-and-quality-gates.md',
  '.agents/skills/dev-doc-harness/references/durable-planning-quality.md',
  '.agents/skills/dev-doc-harness/references/artifact-style.md',
  '.agents/skills/dev-doc-harness/references/subagent-model-policy.md',
  '.agents/skills/dev-doc-harness/assets/templates/blocks/spec.030.common.commitments-verification.md',
  '.agents/skills/dev-doc-harness/assets/templates/blocks/plan.020.common.traceability-approach-surfaces.md',
  '.agents/skills/dev-doc-harness/assets/templates/blocks/plan.050.common.task-plan.md',
  '.agents/skills/dev-doc-harness/assets/templates/blocks/plan.070.common.validation-variance-freeze.md',
  '.agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.common.handoff.md',
  '.agents/skills/dev-doc-harness/assets/templates/blocks/plan.090.small.readiness-completion-approval.md',
  '.agents/skills/dev-doc-harness/assets/templates/blocks/plan.090.phase.readiness-completion-approval.md',
  '.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md',
  '.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md',
  '.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md',
  '.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md',
  '.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md',
  '.agents/skills/dev-doc-harness/assets/templates/variance-log.md',
  'README.md'
)
$rows = foreach ($path in $paths) {
  $text = Get-Content -Raw $path
  [pscustomobject]@{
    Path = $path
    NonblankLines = @($text -split "`r?`n" | Where-Object { $_.Trim().Length -gt 0 }).Count
    Words = [regex]::Matches($text, '\S+').Count
  }
}
$rows | Format-Table -AutoSize
$rows | Measure-Object -Property NonblankLines -Sum
$rows | Measure-Object -Property Words -Sum
```

Record the full per-file rows and both aggregate sums in the implementation
evidence. The same command defines both the baseline and final measurement.

## Approval

- Status: Approved
- Superseded by: None
