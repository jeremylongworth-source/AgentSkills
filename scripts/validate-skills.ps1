param(
  [string]$RepoRoot = '',
  [string]$Validator = "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py"
)

$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
  $scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
  $RepoRoot = (Resolve-Path (Join-Path $scriptDir '..')).Path
}

if (-not (Test-Path $Validator)) {
  throw "Skill validator not found: $Validator"
}

$skillsDir = Join-Path $RepoRoot 'skills'
$skills = Get-ChildItem -Path $skillsDir -Directory | Sort-Object Name

foreach ($skill in $skills) {
  python $Validator $skill.FullName | Out-Null
  $skillMd = Join-Path $skill.FullName 'SKILL.md'
  $agentYaml = Join-Path $skill.FullName 'agents/openai.yaml'
  $refsDir = Join-Path $skill.FullName 'references'

  if (-not (Test-Path $skillMd)) { throw "Missing SKILL.md: $($skill.Name)" }
  if (-not (Test-Path $agentYaml)) { throw "Missing agents/openai.yaml: $($skill.Name)" }
  if (-not (Test-Path $refsDir)) { throw "Missing references/: $($skill.Name)" }

  $text = Get-Content -Raw -Path $skillMd
  if ($text -notmatch '## References') { throw "Missing References section: $($skill.Name)" }
  if ($text -notmatch '## Output Contract|## Deliverable Shape|## Multi-Discipline Output Contract') {
    throw "Missing output contract/deliverable shape: $($skill.Name)"
  }
  if ($text -match '\[TODO|TODO:|Structuring This Skill|Examples from other skills') {
    throw "Scaffold placeholder remains: $($skill.Name)"
  }
}

Write-Host "Validated $($skills.Count) skills."
