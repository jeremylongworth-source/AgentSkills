param(
  [string]$RepoRoot = '',
  [string]$Validator = "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py"
)

$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
  $scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
  $RepoRoot = (Resolve-Path (Join-Path $scriptDir '..')).Path
}

$skillsDir = Join-Path $RepoRoot 'skills'
$skills = Get-ChildItem -Path $skillsDir -Directory | Sort-Object Name

if (Test-Path $Validator) {
  foreach ($skill in $skills) {
    python $Validator $skill.FullName | Out-Null
  }
} else {
  Write-Host "External skill validator not found; using repo-local skill checks."
}

python (Join-Path $RepoRoot 'scripts/validate-skill-files.py') --repo-root $RepoRoot
python (Join-Path $RepoRoot 'scripts/validate-skillsets.py') --repo-root $RepoRoot
python (Join-Path $RepoRoot 'scripts/validate-scenarios.py') --repo-root $RepoRoot
python (Join-Path $RepoRoot 'scripts/validate-docs.py') --repo-root $RepoRoot
