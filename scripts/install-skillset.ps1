param(
  [Parameter(Mandatory = $true)]
  [string]$Skillset,
  [string]$RepoRoot = '',
  [string]$CodexHome = '',
  [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
  $scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
  $RepoRoot = (Resolve-Path (Join-Path $scriptDir '..')).Path
}

if ([string]::IsNullOrWhiteSpace($CodexHome)) {
  $homeDir = if ($env:USERPROFILE) { $env:USERPROFILE } else { $HOME }
  $CodexHome = Join-Path $homeDir '.codex'
}

$argsList = @(
  (Join-Path $RepoRoot 'scripts/install-skillset.py'),
  '--skillset', $Skillset,
  '--repo-root', $RepoRoot,
  '--codex-home', $CodexHome
)

if ($DryRun) {
  $argsList += '--dry-run'
}

python @argsList
