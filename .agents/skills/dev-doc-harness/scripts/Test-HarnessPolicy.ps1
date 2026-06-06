Set-StrictMode -Version 2.0

$Script:RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..")
$Script:Failures = @()

$Script:KnownPassMarkers = @(
  "PASS paths.required-files",
  "PASS ids.module-owners",
  "PASS ids.safety-rules",
  "PASS templates.schema-anchors",
  "PASS router.required-routes",
  "PASS discoverability.safety",
  "PASS phrases.duplicated-policy",
  "PASS placeholders.current-surfaces",
  "PASS scenarios.golden-traversal"
)

function Join-RepoPath {
  param([Parameter(Mandatory = $true)][string]$Path)
  return Join-Path $Script:RepoRoot $Path
}

function Read-RepoText {
  param([Parameter(Mandatory = $true)][string]$Path)
  $fullPath = Join-RepoPath $Path
  if (-not (Test-Path -LiteralPath $fullPath)) {
    Add-Failure "paths.required-files" "Missing file before read: $Path"
    return ""
  }
  return [System.IO.File]::ReadAllText($fullPath)
}

function Add-Failure {
  param(
    [Parameter(Mandatory = $true)][string]$CheckId,
    [Parameter(Mandatory = $true)][string]$Detail
  )
  $Script:Failures += [PSCustomObject]@{
    CheckId = $CheckId
    Detail = $Detail
  }
}

function Assert-PathExists {
  param(
    [Parameter(Mandatory = $true)][string]$CheckId,
    [Parameter(Mandatory = $true)][string]$Path
  )
  if (-not (Test-Path -LiteralPath (Join-RepoPath $Path))) {
    Add-Failure $CheckId "Missing path: $Path"
  }
}

function Assert-TextContains {
  param(
    [Parameter(Mandatory = $true)][string]$CheckId,
    [Parameter(Mandatory = $true)][string]$Path,
    [Parameter(Mandatory = $true)][string]$Pattern,
    [string]$Label = $Pattern
  )
  $text = Read-RepoText $Path
  if ($text -notmatch $Pattern) {
    Add-Failure $CheckId "Missing $Label in $Path"
  }
}

function Assert-TextNotContains {
  param(
    [Parameter(Mandatory = $true)][string]$CheckId,
    [Parameter(Mandatory = $true)][string]$Path,
    [Parameter(Mandatory = $true)][string]$Pattern,
    [string]$Label = $Pattern
  )
  $text = Read-RepoText $Path
  if ($text -cmatch $Pattern) {
    Add-Failure $CheckId "Unexpected $Label in $Path"
  }
}

function Assert-RouteContains {
  param(
    [Parameter(Mandatory = $true)][string]$Operation,
    [Parameter(Mandatory = $true)][string[]]$RequiredPatterns
  )
  $checkId = "router.required-routes"
  $path = ".agents/skills/dev-doc-harness/SKILL.md"
  $text = Read-RepoText $path
  $routeLine = ($text -split "`r?`n" | Where-Object { $_ -match [regex]::Escape($Operation) } | Select-Object -First 1)
  if (-not $routeLine) {
    Add-Failure $checkId "Missing operation route: $Operation"
    return
  }
  foreach ($pattern in $RequiredPatterns) {
    if ($routeLine -notmatch $pattern) {
      Add-Failure $checkId "Route '$Operation' is missing target pattern: $pattern"
    }
  }
}

function Assert-ScenarioEvidence {
  param(
    [Parameter(Mandatory = $true)][string]$ScenarioId,
    [Parameter(Mandatory = $true)][object[]]$Evidence
  )
  $checkId = "scenarios.golden-traversal"
  foreach ($item in $Evidence) {
    Assert-TextContains $checkId $item.Path $item.Pattern "$ScenarioId evidence '$($item.Label)'"
  }
}

function Write-CheckResult {
  param([Parameter(Mandatory = $true)][string]$CheckId)
  $failed = @($Script:Failures | Where-Object { $_.CheckId -eq $CheckId })
  if ($failed.Count -eq 0) {
    Write-Output "PASS $CheckId"
    return
  }
  foreach ($failure in $failed) {
    Write-Output "FAIL $CheckId`: $($failure.Detail)"
  }
}

$requiredFiles = @(
  "AGENTS.md",
  "README.md",
  "CHANGELOG.md",
  ".agents/skills/dev-doc-harness/SKILL.md",
  ".agents/skills/dev-doc-harness/references/policy-architecture.md",
  ".agents/skills/dev-doc-harness/references/artifact-contract.md",
  ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md",
  ".agents/skills/dev-doc-harness/references/subagent-model-policy.md",
  ".agents/skills/dev-doc-harness/references/durable-planning-quality.md",
  ".agents/skills/dev-doc-harness/references/context-and-quality-gates.md",
  ".agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md",
  ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
  ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
  ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
  ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
  ".agents/skills/dev-doc-harness/assets/templates/plan-amendment.md",
  ".agents/skills/dev-doc-harness/assets/templates/variance-log.md",
  "docs/work-items/2026-06-05-refactor-as-code/snapshots/test-cases.snapshot.md",
  "docs/work-items/2026-06-05-refactor-as-code/deltas/testing-guide.delta.md",
  "docs/work-items/2026-06-05-refactor-as-code/deltas/operator-manual.delta.md",
  "docs/work-items/2026-06-05-refactor-as-code/deltas/architecture-summary.delta.md"
)

foreach ($path in $requiredFiles) {
  Assert-PathExists "paths.required-files" $path
}
Write-CheckResult "paths.required-files"

$moduleOwners = @(
  @{ Path = ".agents/skills/dev-doc-harness/references/policy-architecture.md"; Pattern = "module:architecture" },
  @{ Path = ".agents/skills/dev-doc-harness/references/artifact-contract.md"; Pattern = "module:lifecycle" },
  @{ Path = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"; Pattern = "module:freeze-gate" },
  @{ Path = ".agents/skills/dev-doc-harness/references/subagent-model-policy.md"; Pattern = "module:models" },
  @{ Path = ".agents/skills/dev-doc-harness/references/durable-planning-quality.md"; Pattern = "module:quality" },
  @{ Path = ".agents/skills/dev-doc-harness/references/context-and-quality-gates.md"; Pattern = "module:execution-quality" },
  @{ Path = ".agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md"; Pattern = "module:evidence" }
)

foreach ($owner in $moduleOwners) {
  Assert-TextContains "ids.module-owners" $owner.Path ([regex]::Escape($owner.Pattern)) $owner.Pattern
}
Write-CheckResult "ids.module-owners"

$safetyRules = @(
  @{ Path = ".agents/skills/dev-doc-harness/references/artifact-contract.md"; Pattern = "rule:lifecycle.work-sizing" },
  @{ Path = ".agents/skills/dev-doc-harness/references/artifact-contract.md"; Pattern = "rule:lifecycle.immutable-snapshots" },
  @{ Path = ".agents/skills/dev-doc-harness/references/artifact-contract.md"; Pattern = "rule:lifecycle.variance-policy" },
  @{ Path = ".agents/skills/dev-doc-harness/references/artifact-contract.md"; Pattern = "rule:lifecycle.changelog-before-commit" },
  @{ Path = ".agents/skills/dev-doc-harness/references/artifact-contract.md"; Pattern = "rule:lifecycle.documentation-matrix" },
  @{ Path = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"; Pattern = "rule:freeze.draft-review" },
  @{ Path = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"; Pattern = "rule:freeze.approval-freeze" },
  @{ Path = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"; Pattern = "rule:freeze.stop-before-implementation" },
  @{ Path = ".agents/skills/dev-doc-harness/references/subagent-model-policy.md"; Pattern = "rule:models.strategy-required" },
  @{ Path = ".agents/skills/dev-doc-harness/references/subagent-model-policy.md"; Pattern = "rule:models.approved-strategy-authorized" },
  @{ Path = ".agents/skills/dev-doc-harness/references/subagent-model-policy.md"; Pattern = "rule:models.fresh-confirmation" },
  @{ Path = ".agents/skills/dev-doc-harness/references/durable-planning-quality.md"; Pattern = "rule:quality.phase-plan-fresh-thread" }
)

foreach ($rule in $safetyRules) {
  Assert-TextContains "ids.safety-rules" $rule.Path ([regex]::Escape($rule.Pattern)) $rule.Pattern
}

foreach ($publicRule in @("rule:lifecycle.work-sizing", "rule:lifecycle.variance-policy", "rule:lifecycle.changelog-before-commit", "rule:freeze.draft-review", "rule:freeze.approval-freeze", "rule:freeze.stop-before-implementation", "rule:models.strategy-required", "rule:quality.phase-plan-fresh-thread")) {
  Assert-TextContains "ids.safety-rules" ".agents/skills/dev-doc-harness/SKILL.md" ([regex]::Escape($publicRule)) "$publicRule public route"
}
Write-CheckResult "ids.safety-rules"

$schemaAnchors = @(
  @{ Path = ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md"; Pattern = "schema:spec.small-medium" },
  @{ Path = ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md"; Pattern = "schema:plan.small-medium" },
  @{ Path = ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md"; Pattern = "schema:spec.large-phased" },
  @{ Path = ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md"; Pattern = "schema:plan.phase" },
  @{ Path = ".agents/skills/dev-doc-harness/assets/templates/plan-amendment.md"; Pattern = "schema:plan.amendment" },
  @{ Path = ".agents/skills/dev-doc-harness/assets/templates/variance-log.md"; Pattern = "schema:variance-log" }
)

foreach ($schema in $schemaAnchors) {
  Assert-TextContains "templates.schema-anchors" $schema.Path ([regex]::Escape($schema.Pattern)) $schema.Pattern
  Assert-TextContains "templates.schema-anchors" $schema.Path "Policy references:" "policy-reference anchor"
}
Write-CheckResult "templates.schema-anchors"

Assert-RouteContains "Classify work size" @("module:lifecycle", "rule:lifecycle.work-sizing")
Assert-RouteContains "Draft or review small/medium specs and plans" @("module:lifecycle", "module:quality")
Assert-RouteContains "Draft or review large anchor specs" @("module:lifecycle", "module:quality", "module:models")
Assert-RouteContains "Draft or review phase plans" @("module:quality", "module:lifecycle", "module:models")
Assert-RouteContains "Freeze planning packages" @("module:freeze-gate", "module:lifecycle")
Assert-RouteContains "Execute approved work and record variance" @("module:lifecycle", "module:execution-quality")
Assert-RouteContains "Use or review sub-agent strategy" @("module:models", "rule:models.strategy-required")
Assert-RouteContains "Evidence-heavy review or reports" @("module:evidence")
Assert-RouteContains "Update templates or router guidance" @("module:architecture")
Assert-RouteContains "Superpowers or spec-kit compatibility" @("module:lifecycle")
Write-CheckResult "router.required-routes"

$discoverability = @(
  @{ Path = ".agents/skills/dev-doc-harness/SKILL.md"; Pattern = "Classify work size"; Label = "work sizing" },
  @{ Path = ".agents/skills/dev-doc-harness/SKILL.md"; Pattern = "Planning Artifact Freeze Gate"; Label = "planning freeze gates" },
  @{ Path = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"; Pattern = "stop before implementation"; Label = "stop before implementation" },
  @{ Path = ".agents/skills/dev-doc-harness/references/artifact-contract.md"; Pattern = "Immutable snapshots"; Label = "immutable snapshots" },
  @{ Path = ".agents/skills/dev-doc-harness/references/artifact-contract.md"; Pattern = "Variance policy"; Label = "variance and amendments" },
  @{ Path = ".agents/skills/dev-doc-harness/references/artifact-contract.md"; Pattern = "CHANGELOG.md.+before commits"; Label = "changelog before commit" },
  @{ Path = ".agents/skills/dev-doc-harness/references/artifact-contract.md"; Pattern = "Documentation artifact matrix"; Label = "documentation matrix" },
  @{ Path = "AGENTS.md"; Pattern = "single repository-local selection point"; Label = "active repository model policy" },
  @{ Path = ".agents/skills/dev-doc-harness/SKILL.md"; Pattern = "Superpowers compatibility"; Label = "Superpowers compatibility" },
  @{ Path = ".agents/skills/dev-doc-harness/references/policy-architecture.md"; Pattern = "Historical artifacts are not updated"; Label = "historical artifact handling" }
)

foreach ($topic in $discoverability) {
  Assert-TextContains "discoverability.safety" $topic.Path $topic.Pattern $topic.Label
}
Write-CheckResult "discoverability.safety"

$duplicatePhraseTargets = @(
  "AGENTS.md",
  "README.md",
  ".agents/skills/dev-doc-harness/SKILL.md",
  ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
  ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
  ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
  ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
  ".agents/skills/dev-doc-harness/assets/templates/plan-amendment.md",
  ".agents/skills/dev-doc-harness/assets/templates/variance-log.md"
)
$disallowedPhrases = @(
  "Fresh confirmation is still required",
  "Long-running .*more than 3 total sub-agents",
  "Context strategy must say how",
  "Before approval, operator feedback edits this draft directly",
  "When this .*ready for operator review, follow",
  "After this .*approved, frozen, and followed"
)
foreach ($target in $duplicatePhraseTargets) {
  foreach ($phrase in $disallowedPhrases) {
    Assert-TextNotContains "phrases.duplicated-policy" $target $phrase $phrase
  }
}
Write-CheckResult "phrases.duplicated-policy"

$placeholderTargets = @(
  "AGENTS.md",
  "README.md",
  ".agents/skills/dev-doc-harness/SKILL.md",
  ".agents/skills/dev-doc-harness/references/policy-architecture.md",
  ".agents/skills/dev-doc-harness/references/artifact-contract.md",
  ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md",
  ".agents/skills/dev-doc-harness/references/subagent-model-policy.md",
  ".agents/skills/dev-doc-harness/references/durable-planning-quality.md",
  ".agents/skills/dev-doc-harness/references/context-and-quality-gates.md",
  ".agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md",
  ".agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1",
  "docs/work-items/2026-06-05-refactor-as-code/snapshots/test-cases.snapshot.md",
  "docs/work-items/2026-06-05-refactor-as-code/deltas/testing-guide.delta.md",
  "docs/work-items/2026-06-05-refactor-as-code/deltas/operator-manual.delta.md",
  "docs/work-items/2026-06-05-refactor-as-code/deltas/architecture-summary.delta.md"
)
$placeholderPatterns = @("Status:[ ]Draft", "T[D]B", "T[O]DO", "R[e]place", "blank u[n]less", "unresolved d[e]cision")
foreach ($target in $placeholderTargets) {
  foreach ($pattern in $placeholderPatterns) {
    Assert-TextNotContains "placeholders.current-surfaces" $target $pattern $pattern
  }
}
Write-CheckResult "placeholders.current-surfaces"

$scenarioSnapshot = "docs/work-items/2026-06-05-refactor-as-code/snapshots/test-cases.snapshot.md"
$scenarioIds = @(
  "scenario:work-size.very-small-skip",
  "scenario:planning.small-medium",
  "scenario:planning.large-anchor-freeze",
  "scenario:planning.phase-plan-freeze",
  "scenario:execution.post-freeze-authorization",
  "scenario:variance.high-impact-amendment",
  "scenario:models.sub-agent-authorization",
  "scenario:compat.superpowers",
  "scenario:history.historical-artifact-handling"
)
foreach ($scenarioId in $scenarioIds) {
  Assert-TextContains "scenarios.golden-traversal" $scenarioSnapshot ([regex]::Escape($scenarioId)) "$scenarioId snapshot row"
}

Assert-ScenarioEvidence "scenario:work-size.very-small-skip" @(
  @{ Path = "AGENTS.md"; Pattern = "Very small mechanical edits"; Label = "root sizing summary" },
  @{ Path = ".agents/skills/dev-doc-harness/SKILL.md"; Pattern = "Classify work size"; Label = "router sizing route" },
  @{ Path = ".agents/skills/dev-doc-harness/references/artifact-contract.md"; Pattern = "Small mechanical work may skip"; Label = "lifecycle sizing rule" }
)
Assert-ScenarioEvidence "scenario:planning.small-medium" @(
  @{ Path = ".agents/skills/dev-doc-harness/SKILL.md"; Pattern = "Draft or review small/medium specs and plans"; Label = "small medium route" },
  @{ Path = ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md"; Pattern = "schema:spec.small-medium"; Label = "small spec schema" },
  @{ Path = ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md"; Pattern = "schema:plan.small-medium"; Label = "small plan schema" }
)
Assert-ScenarioEvidence "scenario:planning.large-anchor-freeze" @(
  @{ Path = ".agents/skills/dev-doc-harness/SKILL.md"; Pattern = "Draft or review large anchor specs"; Label = "large route" },
  @{ Path = ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md"; Pattern = "schema:spec.large-phased"; Label = "large spec schema" },
  @{ Path = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"; Pattern = "Approval freeze checkpoint"; Label = "freeze owner" }
)
Assert-ScenarioEvidence "scenario:planning.phase-plan-freeze" @(
  @{ Path = ".agents/skills/dev-doc-harness/SKILL.md"; Pattern = "Draft or review phase plans"; Label = "phase plan route" },
  @{ Path = ".agents/skills/dev-doc-harness/references/durable-planning-quality.md"; Pattern = "rule:quality.phase-plan-fresh-thread"; Label = "fresh thread rule" },
  @{ Path = ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md"; Pattern = "schema:plan.phase"; Label = "phase schema" },
  @{ Path = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"; Pattern = "rule:freeze.approval-freeze"; Label = "phase freeze owner" }
)
Assert-ScenarioEvidence "scenario:execution.post-freeze-authorization" @(
  @{ Path = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"; Pattern = "fresh operator response"; Label = "fresh authorization" },
  @{ Path = ".agents/skills/dev-doc-harness/references/artifact-contract.md"; Pattern = "rule:lifecycle.variance-policy"; Label = "variance rule" },
  @{ Path = ".agents/skills/dev-doc-harness/references/context-and-quality-gates.md"; Pattern = "Implementation stayed within scope"; Label = "scope quality gate" },
  @{ Path = ".agents/skills/dev-doc-harness/references/artifact-contract.md"; Pattern = "CHANGELOG.md.+before commits"; Label = "changelog expectation" }
)
Assert-ScenarioEvidence "scenario:variance.high-impact-amendment" @(
  @{ Path = ".agents/skills/dev-doc-harness/references/artifact-contract.md"; Pattern = "plan-amendment-NNN-short-title"; Label = "amendment path" },
  @{ Path = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"; Pattern = "Amendment freeze"; Label = "amendment freeze" },
  @{ Path = ".agents/skills/dev-doc-harness/assets/templates/plan-amendment.md"; Pattern = "schema:plan.amendment"; Label = "amendment schema" }
)
Assert-ScenarioEvidence "scenario:models.sub-agent-authorization" @(
  @{ Path = ".agents/skills/dev-doc-harness/references/subagent-model-policy.md"; Pattern = "rule:models.approved-strategy-authorized"; Label = "approved strategy rule" },
  @{ Path = ".agents/skills/dev-doc-harness/references/subagent-model-policy.md"; Pattern = "rule:models.fresh-confirmation"; Label = "fresh confirmation rule" },
  @{ Path = ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md"; Pattern = "Context strategy"; Label = "small plan strategy table" },
  @{ Path = ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md"; Pattern = "Context strategy"; Label = "large spec strategy table" },
  @{ Path = ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md"; Pattern = "Context strategy"; Label = "phase plan strategy table" }
)
Assert-ScenarioEvidence "scenario:compat.superpowers" @(
  @{ Path = "AGENTS.md"; Pattern = "Superpowers"; Label = "root compatibility" },
  @{ Path = ".agents/skills/dev-doc-harness/SKILL.md"; Pattern = "Superpowers compatibility"; Label = "router compatibility" },
  @{ Path = ".agents/skills/dev-doc-harness/references/artifact-contract.md"; Pattern = "rule:lifecycle.superpowers-compatibility"; Label = "lifecycle compatibility" }
)
Assert-ScenarioEvidence "scenario:history.historical-artifact-handling" @(
  @{ Path = ".agents/skills/dev-doc-harness/references/artifact-contract.md"; Pattern = "rule:lifecycle.immutable-snapshots"; Label = "immutable rule" },
  @{ Path = ".agents/skills/dev-doc-harness/references/policy-architecture.md"; Pattern = "Historical artifacts are not updated"; Label = "historical handling" },
  @{ Path = "docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md"; Pattern = "scenario:history.historical-artifact-handling"; Label = "source scenario" }
)
Write-CheckResult "scenarios.golden-traversal"

if ($Script:Failures.Count -gt 0) {
  exit 1
}
exit 0
