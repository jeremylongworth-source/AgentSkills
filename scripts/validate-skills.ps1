param(
  [string]$RepoRoot = '',
  [string]$Validator = ''
)

$ErrorActionPreference = 'Stop'
# Check native exit codes ourselves, including when the caller enables PS7's
# native-command error preference. This variable is harmless in Windows PS5.1.
$PSNativeCommandUseErrorActionPreference = $false

if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
  $scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
  $RepoRoot = (Resolve-Path (Join-Path $scriptDir '..')).Path
}

if ([string]::IsNullOrWhiteSpace($Validator)) {
  $homeDir = if ($env:USERPROFILE) { $env:USERPROFILE } else { $HOME }
  $Validator = Join-Path $homeDir '.codex/skills/.system/skill-creator/scripts/quick_validate.py'
}

$skillsDir = Join-Path $RepoRoot 'skills'
$skills = Get-ChildItem -Path $skillsDir -Directory | Sort-Object Name

function Invoke-PythonValidator {
  param(
    [string[]]$Arguments,
    [string]$Name,
    [switch]$Quiet
  )

  if ($Quiet) {
    $output = & python @Arguments
  } else {
    & python @Arguments
  }
  $exitCode = $LASTEXITCODE
  if ($exitCode -ne 0) {
    if ($Quiet) { $output | ForEach-Object { Write-Host $_ } }
    throw "$Name failed with exit code $exitCode."
  }
}

if (Test-Path $Validator) {
  foreach ($skill in $skills) {
    Invoke-PythonValidator @($Validator, $skill.FullName) "External skill validator ($($skill.Name))" -Quiet
  }
} else {
  Write-Host "External skill validator not found; using repo-local skill checks."
}

foreach ($script in @('validate-skill-files.py', 'validate-skillsets.py', 'validate-scenarios.py', 'validate-docs.py')) {
  Invoke-PythonValidator @((Join-Path $RepoRoot "scripts/$script"), '--repo-root', $RepoRoot) $script
}
