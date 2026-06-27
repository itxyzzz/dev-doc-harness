Set-StrictMode -Version 2.0

$Script:RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..")
$Script:Failures = @()

$Script:KnownPassMarkers = @(
  "PASS paths.required-files",
  "PASS graph.references",
  "PASS graph.owner-headings",
  "PASS graph.template-routes",
  "PASS router.required-routes",
  "PASS router.route-budget",
  "PASS discoverability.safety",
  "PASS phrases.duplicated-policy",
  "PASS phrases.duplicate-blocks",
  "PASS placeholders.current-surfaces",
  "PASS tracking.work-items",
  "PASS scenarios.golden-traversal",
  "PASS release.identity",
  "PASS release.notes",
  "PASS release.changelog-schema",
  "PASS release.package-boundary",
  "PASS release.template-context",
  "PASS release.route"
)

$Script:CanonicalReferences = @(
  ".agents/skills/dev-doc-harness/references/policy-architecture.md",
  ".agents/skills/dev-doc-harness/references/artifact-contract.md",
  ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md",
  ".agents/skills/dev-doc-harness/references/subagent-model-policy.md",
  ".agents/skills/dev-doc-harness/references/durable-planning-quality.md",
  ".agents/skills/dev-doc-harness/references/release-policy.md",
  ".agents/skills/dev-doc-harness/references/context-and-quality-gates.md",
  ".agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md",
  ".agents/skills/dev-doc-harness/references/subagent-role-examples.md"
)

$Script:TemplateFiles = @(
  ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
  ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
  ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
  ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
  ".agents/skills/dev-doc-harness/assets/templates/plan-amendment.md",
  ".agents/skills/dev-doc-harness/assets/templates/variance-log.md"
)

$Script:CurrentSurfaceFiles = @(
  "AGENTS.md",
  "README.md",
  ".agents/skills/dev-doc-harness/SKILL.md",
  ".agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1",
  "docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md",
  "docs/work-items/2026-06-05-refactor-as-code/snapshots/test-cases.snapshot.md",
  "docs/work-items/2026-06-05-refactor-as-code/deltas/testing-guide.delta.md",
  "docs/work-items/2026-06-05-refactor-as-code/deltas/operator-manual.delta.md",
  "docs/work-items/2026-06-05-refactor-as-code/deltas/architecture-summary.delta.md",
  "docs/work-items/2026-06-07-followup-hardening/snapshots/architecture.snapshot.md",
  "docs/work-items/2026-06-07-followup-hardening/snapshots/test-cases.snapshot.md",
  "docs/work-items/2026-06-07-followup-hardening/deltas/testing-guide.delta.md",
  "docs/work-items/2026-06-07-followup-hardening/deltas/operator-manual.delta.md",
  "docs/work-items/2026-06-07-followup-hardening/deltas/architecture-summary.delta.md"
) + $Script:CanonicalReferences + $Script:TemplateFiles

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

function Assert-PathExists {
  param(
    [Parameter(Mandatory = $true)][string]$CheckId,
    [Parameter(Mandatory = $true)][string]$Path
  )
  if (-not (Test-Path -LiteralPath (Join-RepoPath $Path))) {
    Add-Failure $CheckId "Missing path: $Path"
  }
}

function Assert-PathAbsent {
  param(
    [Parameter(Mandatory = $true)][string]$CheckId,
    [Parameter(Mandatory = $true)][string]$Path
  )
  if (Test-Path -LiteralPath (Join-RepoPath $Path)) {
    Add-Failure $CheckId "Unexpected path exists: $Path"
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

function Get-ConcreteIds {
  param([Parameter(Mandatory = $true)][string]$Text)
  $matches = [regex]::Matches($Text, '\b(?:module|rule|schema|scenario|metric):[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?')
  return @($matches | ForEach-Object { $_.Value } | Sort-Object -Unique)
}

function Convert-ToRepoRelativePath {
  param([Parameter(Mandatory = $true)][string]$FullPath)
  $root = $Script:RepoRoot.Path.TrimEnd("\", "/")
  $normalizedFullPath = $FullPath
  if ($normalizedFullPath.StartsWith($root, [System.StringComparison]::OrdinalIgnoreCase)) {
    $normalizedFullPath = $normalizedFullPath.Substring($root.Length).TrimStart("\", "/")
  }
  return ($normalizedFullPath -replace '\\', '/')
}

function Add-Owner {
  param(
    [Parameter(Mandatory = $true)][hashtable]$Owners,
    [Parameter(Mandatory = $true)][string]$Id,
    [Parameter(Mandatory = $true)][string]$Path,
    [string]$Heading = ""
  )
  if (-not $Owners.ContainsKey($Id)) {
    $Owners[$Id] = @()
  }
  $Owners[$Id] += [PSCustomObject]@{
    Path = $Path
    Heading = $Heading
  }
}

function Get-OwnerGraph {
  $owners = @{
    module = @{}
    rule = @{}
    schema = @{}
    scenario = @{}
    metric = @{}
  }
  $ownerRows = @()

  foreach ($path in $Script:CanonicalReferences) {
    $text = Read-RepoText $path
    foreach ($match in [regex]::Matches($text, '(?:Module:|owns)\s+`(module:[a-z0-9][a-z0-9.-]*)`')) {
      Add-Owner $owners.module $match.Groups[1].Value $path ""
    }

    foreach ($line in ($text -split "`r?`n")) {
      $rowMatch = [regex]::Match($line, '^\|\s*`(rule:[a-z0-9][a-z0-9.-]*)`\s*\|\s*(.+?)\s*\|')
      if ($rowMatch.Success) {
        $ruleId = $rowMatch.Groups[1].Value
        $ownerCell = $rowMatch.Groups[2].Value
        Add-Owner $owners.rule $ruleId $path $ownerCell
        $ownerRows += [PSCustomObject]@{
          Path = $path
          Id = $ruleId
          OwnerCell = $ownerCell
        }
      }
    }
  }

  foreach ($path in $Script:TemplateFiles) {
    $text = Read-RepoText $path
    foreach ($match in [regex]::Matches($text, 'Schema:\s+`(schema:[a-z0-9][a-z0-9.-]*)`')) {
      Add-Owner $owners.schema $match.Groups[1].Value $path ""
    }
  }

  $scenarioMetricOwnerFiles = @(
    "docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md",
    "docs/work-items/2026-06-05-refactor-as-code/snapshots/test-cases.snapshot.md",
    "docs/work-items/2026-06-07-followup-hardening/snapshots/architecture.snapshot.md",
    "docs/work-items/2026-06-07-followup-hardening/snapshots/test-cases.snapshot.md",
    "docs/work-items/2026-06-07-release-versioning/snapshots/test-cases.snapshot.md"
  )
  foreach ($path in $scenarioMetricOwnerFiles) {
    $text = Read-RepoText $path
    foreach ($id in (Get-ConcreteIds $text)) {
      if ($id.StartsWith("scenario:")) {
        Add-Owner $owners.scenario $id $path ""
      } elseif ($id.StartsWith("metric:")) {
        Add-Owner $owners.metric $id $path ""
      }
    }
  }

  return [PSCustomObject]@{
    Owners = $owners
    OwnerRows = $ownerRows
  }
}

function Get-ReferenceRecords {
  $records = @()
  foreach ($path in $Script:CurrentSurfaceFiles) {
    $text = Read-RepoText $path
    foreach ($id in (Get-ConcreteIds $text)) {
      $records += [PSCustomObject]@{
        Path = $path
        Id = $id
      }
    }
  }
  return $records
}

function Get-OwnerTableHeadingNames {
  param([Parameter(Mandatory = $true)][string]$OwnerCell)
  $names = @()
  foreach ($match in [regex]::Matches($OwnerCell, '##\s*([^`|]+?)(?:\s+and\s+|$)')) {
    $names += "## " + $match.Groups[1].Value.Trim()
  }
  return $names
}

function Assert-GraphReferences {
  param(
    [Parameter(Mandatory = $true)]$Graph,
    [Parameter(Mandatory = $true)][object[]]$References
  )
  foreach ($record in $References) {
    if ($record.Path -match '/snapshots/test-cases\.snapshot\.md$' -and $record.Id -match ('^rule' + ':test\.')) {
      continue
    }
    $parts = $record.Id.Split(":", 2)
    $kind = $parts[0]
    if ($Graph.Owners.ContainsKey($kind) -and -not $Graph.Owners[$kind].ContainsKey($record.Id)) {
      Add-Failure "graph.references" "Dangling $kind reference '$($record.Id)' in $($record.Path)"
    }
  }

  foreach ($kind in @("module", "rule", "schema")) {
    foreach ($id in $Graph.Owners[$kind].Keys) {
      $paths = @($Graph.Owners[$kind][$id] | ForEach-Object { $_.Path } | Sort-Object -Unique)
      if ($paths.Count -gt 1) {
        Add-Failure "graph.references" "Duplicate $kind owner for '$id': $($paths -join ', ')"
      }
    }
  }
}

function Assert-OwnerHeadings {
  param([Parameter(Mandatory = $true)]$Graph)
  foreach ($row in $Graph.OwnerRows) {
    $text = Read-RepoText $row.Path
    $headings = Get-OwnerTableHeadingNames $row.OwnerCell
    foreach ($heading in $headings) {
      if ($text -notmatch "(?m)^$([regex]::Escape($heading))\s*$") {
        Add-Failure "graph.owner-headings" "Owner heading '$heading' for $($row.Id) is missing in $($row.Path)"
      }
    }
  }
}

function Get-PolicyReferences {
  param([Parameter(Mandatory = $true)][string]$Path)
  $text = Read-RepoText $Path
  $line = ($text -split "`r?`n" | Where-Object { $_ -match '^Policy references:' } | Select-Object -First 1)
  if (-not $line) {
    return @()
  }
  return @(Get-ConcreteIds $line)
}

function Assert-TemplateRoutes {
  $operationRequirements = @{
    "small-medium" = @("module:lifecycle", "module:quality", "module:models")
    "large-anchor" = @("module:lifecycle", "module:quality", "module:models")
    "phase-plan" = @("module:lifecycle", "module:quality", "module:models")
    "amendment" = @("module:lifecycle", "module:freeze-gate")
  }
  $operationTemplates = @{
    "small-medium" = @(
      ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
      ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md"
    )
    "large-anchor" = @(".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md")
    "phase-plan" = @(".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md")
    "amendment" = @(".agents/skills/dev-doc-harness/assets/templates/plan-amendment.md")
  }

  foreach ($operation in $operationRequirements.Keys) {
    $combined = @()
    foreach ($template in $operationTemplates[$operation]) {
      $combined += Get-PolicyReferences $template
    }
    $combined = @($combined | Sort-Object -Unique)
    foreach ($required in $operationRequirements[$operation]) {
      if ($combined -notcontains $required) {
        Add-Failure "graph.template-routes" "Template set for '$operation' is missing policy reference '$required'"
      }
    }
  }
}

function Assert-RouteContains {
  param(
    [Parameter(Mandatory = $true)][string]$Operation,
    [Parameter(Mandatory = $true)][string[]]$RequiredPatterns,
    [string]$CheckId = "router.required-routes"
  )
  $path = ".agents/skills/dev-doc-harness/SKILL.md"
  $text = Read-RepoText $path
  $routeLine = ($text -split "`r?`n" | Where-Object { $_ -match [regex]::Escape($Operation) } | Select-Object -First 1)
  if (-not $routeLine) {
    Add-Failure $CheckId "Missing operation route: $Operation"
    return
  }
  foreach ($pattern in $RequiredPatterns) {
    if ($routeLine -notmatch $pattern) {
      Add-Failure $CheckId "Route '$Operation' is missing target pattern: $pattern"
    }
  }
}

function Assert-RouteBudgets {
  $path = ".agents/skills/dev-doc-harness/SKILL.md"
  $text = Read-RepoText $path
  $budgets = @{
    "Classify work size" = 1
    "Draft or review small/medium specs and plans" = 3
    "Draft or review large anchor specs" = 3
    "Draft or review phase plans" = 3
    "Freeze planning packages" = 4
    "Execute approved work and record variance" = 4
    "Use or review sub-agent strategy" = 2
    "Evidence-heavy review or reports" = 1
    "Release, package, or team adoption work" = 1
    "Validate current harness surfaces" = 2
    "Update templates or router guidance" = 3
    "Superpowers or spec-kit compatibility" = 3
  }

  foreach ($operation in $budgets.Keys) {
    $routeLine = ($text -split "`r?`n" | Where-Object { $_ -match "^\|\s*$([regex]::Escape($operation))\s*\|" } | Select-Object -First 1)
    if (-not $routeLine) {
      Add-Failure "router.route-budget" "Missing route for budget check: $operation"
      continue
    }
    $rawCells = @($routeLine -split '\|')
    if ($rawCells.Count -lt 5) {
      Add-Failure "router.route-budget" "Malformed route row for budget check: $operation"
      continue
    }
    $cells = @()
    for ($i = 1; $i -lt ($rawCells.Count - 1); $i++) {
      $cells += $rawCells[$i].Trim()
    }
    if ($cells.Count -lt 2) {
      Add-Failure "router.route-budget" "Malformed route row for budget check: $operation"
      continue
    }
    $requiredCell = $cells[1]
    $moduleCount = @([regex]::Matches($requiredCell, 'module:[a-z0-9][a-z0-9.-]*') | ForEach-Object { $_.Value } | Sort-Object -Unique).Count
    if ($moduleCount -gt $budgets[$operation]) {
      Add-Failure "router.route-budget" "Route '$operation' requires $moduleCount modules, budget is $($budgets[$operation])"
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

function Get-NormalizedParagraphs {
  param([Parameter(Mandatory = $true)][string]$Path)
  $text = Read-RepoText $Path
  $paragraphs = @()
  $current = @()
  $inFence = $false
  foreach ($line in ($text -split "`r?`n")) {
    if ($line -match '^\s*```') {
      $inFence = -not $inFence
      continue
    }
    if ($inFence -or $line -match '^\s*\|' -or $line -match '^\s*#' -or $line -match '^\s*[-*]\s' -or $line -match '^\s*\d+\.') {
      if ($current.Count -gt 0) {
        $paragraphs += ($current -join " ")
        $current = @()
      }
      continue
    }
    if ([string]::IsNullOrWhiteSpace($line)) {
      if ($current.Count -gt 0) {
        $paragraphs += ($current -join " ")
        $current = @()
      }
      continue
    }
    $current += $line.Trim()
  }
  if ($current.Count -gt 0) {
    $paragraphs += ($current -join " ")
  }

  $normalized = @()
  foreach ($paragraph in $paragraphs) {
    $words = @([regex]::Matches($paragraph.ToLowerInvariant(), '[a-z0-9]+') | ForEach-Object { $_.Value })
    if ($words.Count -ge 55) {
      $normalized += [PSCustomObject]@{
        Path = $Path
        Text = ($words -join " ")
      }
    }
  }
  return $normalized
}

function Assert-DuplicateBlocks {
  $targets = @(
    "AGENTS.md",
    "README.md",
    ".agents/skills/dev-doc-harness/SKILL.md"
  ) + $Script:CanonicalReferences + $Script:TemplateFiles

  $seen = @{}
  foreach ($target in $targets) {
    foreach ($paragraph in (Get-NormalizedParagraphs $target)) {
      if ($seen.ContainsKey($paragraph.Text) -and $seen[$paragraph.Text] -ne $target) {
        Add-Failure "phrases.duplicate-blocks" "Duplicate broad policy block in $($seen[$paragraph.Text]) and $target"
      } elseif (-not $seen.ContainsKey($paragraph.Text)) {
        $seen[$paragraph.Text] = $target
      }
    }
  }
}

function Assert-WorkItemTracking {
  Assert-PathAbsent "tracking.work-items" "docs/work-items/AGENTS.md"
  $ignore = & git -C $Script:RepoRoot check-ignore -v "docs/work-items/2026-06-07-followup-hardening/spec-followup-hardening.md" 2>$null
  if ($LASTEXITCODE -eq 0 -and $ignore) {
    Add-Failure "tracking.work-items" "Work-item docs are still ignored: $ignore"
  }

  $markdownFiles = Get-ChildItem -LiteralPath (Join-RepoPath "docs/work-items") -Recurse -File -Filter "*.md" |
    ForEach-Object { Convert-ToRepoRelativePath $_.FullName }
  $tracked = @(& git -C $Script:RepoRoot ls-files "docs/work-items")
  foreach ($path in $markdownFiles) {
    if ($tracked -notcontains $path) {
      Add-Failure "tracking.work-items" "Untracked work-item Markdown artifact: $path"
    }
  }
}

function Assert-ReleaseIdentity {
  $checkId = "release.identity"
  $versionPath = ".agents/skills/dev-doc-harness/VERSION"
  $versionText = Read-RepoText $versionPath
  if ($versionText -notmatch '\A0\.3\.0\r?\n?\z') {
    Add-Failure $checkId "$versionPath must contain exactly 0.3.0 plus an optional trailing newline"
    return
  }

  $version = $versionText.TrimEnd("`r", "`n")
  Assert-PathExists $checkId ".agents/skills/dev-doc-harness/docs/releases/$version.md"
}

function Assert-ReleaseNotes {
  $checkId = "release.notes"
  $releaseNotesPath = ".agents/skills/dev-doc-harness/docs/releases/0.3.0.md"
  $releaseNotes = Read-RepoText $releaseNotesPath
  $changelog = Read-RepoText "CHANGELOG.md"
  $requiredHeadings = @(
    "# Dev Doc Harness 0.3.0",
    "## Release",
    "## Package Contents",
    "## Added",
    "## Changed",
    "## Compatibility",
    "## Team Adoption",
    "## Rollback",
    "## Source Changelog Entries"
  )

  foreach ($heading in $requiredHeadings) {
    if ($releaseNotes -notmatch "(?m)^$([regex]::Escape($heading))\s*$") {
      Add-Failure $checkId "Missing release-note heading '$heading'"
    }
  }

  $sourceMatch = [regex]::Match($releaseNotes, '(?ms)^## Source Changelog Entries\s*(?<body>.*?)(?=^##\s+|\z)')
  if (-not $sourceMatch.Success) {
    Add-Failure $checkId "Missing Source Changelog Entries section body"
    return
  }

  $sourceEntries = @([regex]::Matches($sourceMatch.Groups["body"].Value, '`(2026-06-07-release-versioning: [^`]+)`') | ForEach-Object { $_.Groups[1].Value })
  if ($sourceEntries.Count -eq 0) {
    Add-Failure $checkId "No source changelog entries listed in release notes"
  }

  foreach ($entry in $sourceEntries) {
    if ($changelog -notmatch "(?m)^##\s+$([regex]::Escape($entry))\s*$") {
      Add-Failure $checkId "Release-note source entry is missing from CHANGELOG.md: $entry"
    }
  }
}

function Get-ChangelogSections {
  $text = Read-RepoText "CHANGELOG.md"
  $sections = @()
  foreach ($match in [regex]::Matches($text, '(?ms)^##\s+(?<heading>2026-06-07-release-versioning:[^\r\n]+)\r?\n(?<body>.*?)(?=^##\s+|\z)')) {
    $sections += [PSCustomObject]@{
      Heading = $match.Groups["heading"].Value.Trim()
      Body = $match.Groups["body"].Value
    }
  }
  return $sections
}

function Assert-ReleaseChangelogSchema {
  $checkId = "release.changelog-schema"
  $sections = @(Get-ChangelogSections)
  if ($sections.Count -eq 0) {
    Add-Failure $checkId "No current release-versioning changelog entries found"
    return
  }

  foreach ($section in $sections) {
    $releaseTargetLines = @([regex]::Matches($section.Body, '(?m)^Release target:\s+`([^`]+)`\s*$'))
    $packageImpactLines = @([regex]::Matches($section.Body, '(?m)^Package impact:\s+`([^`]+)`\s*$'))
    $releaseNoteLines = @([regex]::Matches($section.Body, '(?m)^Release-note:\s+`([^`]+)`\s*$'))

    if ($releaseTargetLines.Count -ne 1) {
      Add-Failure $checkId "$($section.Heading) must contain exactly one Release target field"
    } elseif ($releaseTargetLines[0].Groups[1].Value -ne "0.3.0") {
      Add-Failure $checkId "$($section.Heading) has invalid Release target '$($releaseTargetLines[0].Groups[1].Value)'"
    }

    if ($packageImpactLines.Count -ne 1) {
      Add-Failure $checkId "$($section.Heading) must contain exactly one Package impact field"
    } elseif (@("distributable", "repository-only", "planning-only") -notcontains $packageImpactLines[0].Groups[1].Value) {
      Add-Failure $checkId "$($section.Heading) has invalid Package impact '$($packageImpactLines[0].Groups[1].Value)'"
    }

    if ($releaseNoteLines.Count -ne 1) {
      Add-Failure $checkId "$($section.Heading) must contain exactly one Release-note field"
    } elseif (@("include", "source-only", "omit") -notcontains $releaseNoteLines[0].Groups[1].Value) {
      Add-Failure $checkId "$($section.Heading) has invalid Release-note '$($releaseNoteLines[0].Groups[1].Value)'"
    }
  }
}

function Assert-ReleasePackageBoundary {
  $checkId = "release.package-boundary"
  $releasePolicy = ".agents/skills/dev-doc-harness/references/release-policy.md"
  $releaseNotes = ".agents/skills/dev-doc-harness/docs/releases/0.3.0.md"

  Assert-TextContains $checkId $releasePolicy 'distributable harness package is root `AGENTS\.md` plus `\.agents/`' "release policy package boundary"
  Assert-TextContains $checkId $releaseNotes 'distributable package is root `AGENTS\.md` plus `\.agents/`' "release notes package boundary"
  Assert-TextContains $checkId "README.md" 'copyable distributable package is\s+the root `AGENTS\.md` file plus the `\.agents/` folder' "README package boundary"
  Assert-TextContains $checkId $releasePolicy 'Do not copy this repository''s `docs/work-items/`' "release policy work-item exclusion"
  Assert-TextContains $checkId "README.md" 'Do not copy this repository''s `docs/work-items/` folder' "README work-item exclusion"
  Assert-TextContains $checkId $releasePolicy '(?i)rollback.+revert' "release policy rollback"
  Assert-TextContains $checkId $releaseNotes '(?i)revert.+dedicated harness update' "release notes rollback"
  Assert-TextContains $checkId "README.md" '(?i)roll back by reverting' "README rollback"
}

function Assert-ReleaseTemplateContext {
  $checkId = "release.template-context"
  $fieldLiteral = [string]::Concat("Harness release: ", [char]96, "<version or unknown>", [char]96)
  $fieldPattern = "(?m)^" + [regex]::Escape($fieldLiteral) + "\s*$"
  foreach ($template in $Script:TemplateFiles) {
    $text = Read-RepoText $template
    $count = @([regex]::Matches($text, $fieldPattern)).Count
    if ($count -ne 1) {
      Add-Failure $checkId "$template must contain exactly one Harness release field; found $count"
    }
  }
}

function Assert-ReleaseScenarios {
  $checkId = "release.notes"
  $snapshotPath = "docs/work-items/2026-06-07-release-versioning/snapshots/test-cases.snapshot.md"
  $scenarioIds = @(
    "scenario:release.package-identity",
    "scenario:release.release-notes-source",
    "scenario:release.changelog-schema",
    "scenario:release.package-boundary",
    "scenario:release.template-context",
    "scenario:release.team-adoption-rollback"
  )

  foreach ($scenarioId in $scenarioIds) {
    Assert-TextContains $checkId $snapshotPath ([regex]::Escape($scenarioId)) "$scenarioId snapshot row"
  }
}

$requiredFiles = @(
  "AGENTS.md",
  "README.md",
  "CHANGELOG.md",
  ".agents/skills/dev-doc-harness/SKILL.md",
  ".agents/skills/dev-doc-harness/VERSION",
  ".agents/skills/dev-doc-harness/references/policy-architecture.md",
  ".agents/skills/dev-doc-harness/references/artifact-contract.md",
  ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md",
  ".agents/skills/dev-doc-harness/references/subagent-model-policy.md",
  ".agents/skills/dev-doc-harness/references/durable-planning-quality.md",
  ".agents/skills/dev-doc-harness/references/release-policy.md",
  ".agents/skills/dev-doc-harness/docs/releases/0.3.0.md",
  ".agents/skills/dev-doc-harness/references/context-and-quality-gates.md",
  ".agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md",
  ".agents/skills/dev-doc-harness/references/subagent-role-examples.md",
  ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md",
  ".agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md",
  ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md",
  ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md",
  ".agents/skills/dev-doc-harness/assets/templates/plan-amendment.md",
  ".agents/skills/dev-doc-harness/assets/templates/variance-log.md",
  "docs/work-items/2026-06-05-refactor-as-code/snapshots/test-cases.snapshot.md",
  "docs/work-items/2026-06-05-refactor-as-code/deltas/testing-guide.delta.md",
  "docs/work-items/2026-06-05-refactor-as-code/deltas/operator-manual.delta.md",
  "docs/work-items/2026-06-05-refactor-as-code/deltas/architecture-summary.delta.md",
  "docs/work-items/2026-06-07-followup-hardening/snapshots/test-cases.snapshot.md",
  "docs/work-items/2026-06-07-followup-hardening/snapshots/architecture.snapshot.md",
  "docs/work-items/2026-06-07-followup-hardening/deltas/testing-guide.delta.md",
  "docs/work-items/2026-06-07-followup-hardening/deltas/operator-manual.delta.md",
  "docs/work-items/2026-06-07-followup-hardening/deltas/architecture-summary.delta.md",
  "docs/work-items/2026-06-07-release-versioning/snapshots/test-cases.snapshot.md"
)

foreach ($path in $requiredFiles) {
  Assert-PathExists "paths.required-files" $path
}
Write-CheckResult "paths.required-files"

$graph = Get-OwnerGraph
$references = Get-ReferenceRecords
Assert-GraphReferences $graph $references
Write-CheckResult "graph.references"

Assert-OwnerHeadings $graph
Write-CheckResult "graph.owner-headings"

Assert-TemplateRoutes
Write-CheckResult "graph.template-routes"

Assert-RouteContains "Classify work size" @("module:lifecycle", "rule:lifecycle.work-sizing")
Assert-RouteContains "Draft or review small/medium specs and plans" @("module:lifecycle", "module:quality", "module:models")
Assert-RouteContains "Draft or review large anchor specs" @("module:lifecycle", "module:quality", "module:models")
Assert-RouteContains "Draft or review phase plans" @("module:quality", "module:lifecycle", "module:models")
Assert-RouteContains "Freeze planning packages" @("module:freeze-gate", "module:lifecycle")
Assert-RouteContains "Execute approved work and record variance" @("module:lifecycle", "module:execution-quality")
Assert-RouteContains "Use or review sub-agent strategy" @("module:models", "rule:models.strategy-required")
Assert-RouteContains "Evidence-heavy review or reports" @("module:evidence")
Assert-RouteContains "Release, package, or team adoption work" @("module:release")
Assert-RouteContains "Update templates or router guidance" @("module:architecture")
Assert-RouteContains "Superpowers or spec-kit compatibility" @("module:lifecycle")
Write-CheckResult "router.required-routes"

Assert-RouteBudgets
Write-CheckResult "router.route-budget"

Assert-RouteContains "Release, package, or team adoption work" @("module:release") "release.route"
Write-CheckResult "release.route"

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
  @{ Path = ".agents/skills/dev-doc-harness/references/policy-architecture.md"; Pattern = "Historical artifacts are tracked documentation"; Label = "historical artifact handling" }
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
  "After this .*approved, frozen, and followed",
  "module:models.*when model or sub-agent strategy is assessed"
)
foreach ($target in $duplicatePhraseTargets) {
  foreach ($phrase in $disallowedPhrases) {
    Assert-TextNotContains "phrases.duplicated-policy" $target $phrase $phrase
  }
}
Write-CheckResult "phrases.duplicated-policy"

Assert-DuplicateBlocks
Write-CheckResult "phrases.duplicate-blocks"

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
  "docs/work-items/2026-06-05-refactor-as-code/deltas/architecture-summary.delta.md",
  "docs/work-items/2026-06-07-followup-hardening/snapshots/test-cases.snapshot.md",
  "docs/work-items/2026-06-07-followup-hardening/snapshots/architecture.snapshot.md",
  "docs/work-items/2026-06-07-followup-hardening/deltas/testing-guide.delta.md",
  "docs/work-items/2026-06-07-followup-hardening/deltas/operator-manual.delta.md",
  "docs/work-items/2026-06-07-followup-hardening/deltas/architecture-summary.delta.md"
)
$placeholderPatterns = @("Status:[ ]Draft", "T[D]B", "T[O]DO", "R[e]place", "blank u[n]less", "unresolved d[e]cision")
foreach ($target in $placeholderTargets) {
  foreach ($pattern in $placeholderPatterns) {
    Assert-TextNotContains "placeholders.current-surfaces" $target $pattern $pattern
  }
}
Write-CheckResult "placeholders.current-surfaces"

Assert-WorkItemTracking
Write-CheckResult "tracking.work-items"

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
  @{ Path = ".agents/skills/dev-doc-harness/references/artifact-contract.md"; Pattern = "rule:lifecycle.large-phase-orchestration"; Label = "large phase orchestration rule owner" },
  @{ Path = ".agents/skills/dev-doc-harness/references/artifact-contract.md"; Pattern = "Large or phased planning orchestration"; Label = "large phase orchestration heading" },
  @{ Path = ".agents/skills/dev-doc-harness/SKILL.md"; Pattern = "rule:lifecycle.large-phase-orchestration"; Label = "large route orchestration rule" },
  @{ Path = ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md"; Pattern = "rule:lifecycle.large-phase-orchestration"; Label = "large spec orchestration rule" },
  @{ Path = ".agents/skills/dev-doc-harness/references/artifact-contract.md"; Pattern = "anchor-spec-only"; Label = "anchor spec only package" },
  @{ Path = ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md"; Pattern = "combined planning"; Label = "combined planning exception" },
  @{ Path = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"; Pattern = "Approval freeze checkpoint"; Label = "freeze owner" }
)
Assert-ScenarioEvidence "scenario:planning.phase-plan-freeze" @(
  @{ Path = ".agents/skills/dev-doc-harness/SKILL.md"; Pattern = "Draft or review phase plans"; Label = "phase plan route" },
  @{ Path = ".agents/skills/dev-doc-harness/references/durable-planning-quality.md"; Pattern = "rule:quality.phase-plan-fresh-thread"; Label = "fresh thread rule" },
  @{ Path = ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md"; Pattern = "schema:plan.phase"; Label = "phase schema" },
  @{ Path = ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md"; Pattern = "rule:lifecycle.large-phase-orchestration"; Label = "phase plan orchestration rule" },
  @{ Path = ".agents/skills/dev-doc-harness/references/planning-freeze-gates.md"; Pattern = "phase-plan drafting resumes only after fresh operator instruction"; Label = "post anchor phase planning authorization" },
  @{ Path = ".agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md"; Pattern = "approved anchor spec"; Label = "approved anchor input" },
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
  @{ Path = ".agents/skills/dev-doc-harness/references/subagent-model-policy.md"; Pattern = "curated-artifact sub-agent"; Label = "curated artifact phase planning" },
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
  @{ Path = ".agents/skills/dev-doc-harness/references/policy-architecture.md"; Pattern = "Historical artifacts are tracked documentation"; Label = "historical handling" },
  @{ Path = "docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md"; Pattern = "scenario:history.historical-artifact-handling"; Label = "source scenario" }
)
Write-CheckResult "scenarios.golden-traversal"

Assert-ReleaseIdentity
Write-CheckResult "release.identity"

Assert-ReleaseNotes
Assert-ReleaseScenarios
Write-CheckResult "release.notes"

Assert-ReleaseChangelogSchema
Write-CheckResult "release.changelog-schema"

Assert-ReleasePackageBoundary
Write-CheckResult "release.package-boundary"

Assert-ReleaseTemplateContext
Write-CheckResult "release.template-context"

if ($Script:Failures.Count -gt 0) {
  exit 1
}
exit 0
