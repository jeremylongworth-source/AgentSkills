param(
  [Parameter(Mandatory = $true)]
  [string]$Skillset,
  [string]$RepoRoot = '',
  [string]$CodexHome = "$env:USERPROFILE\.codex"
)

$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
  $scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
  $RepoRoot = (Resolve-Path (Join-Path $scriptDir '..')).Path
}

python (Join-Path $RepoRoot 'scripts/install-skillset.py') --skillset $Skillset --repo-root $RepoRoot --codex-home $CodexHome

