param(
  [Parameter(Mandatory = $true)]
  [string]$Skillset,
  [string]$RepoRoot = '',
  [string]$CodexHome = '',
  [ValidateSet('user', 'project')]
  [string]$Scope = 'user',
  [string]$ProjectRoot = '',
  [switch]$WithMcp,
  [switch]$WithAgents,
  [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
  $scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
  $RepoRoot = (Resolve-Path (Join-Path $scriptDir '..')).Path
}

if ([string]::IsNullOrWhiteSpace($CodexHome)) {
  $homeDir = if ($env:USERPROFILE) { $env:USERPROFILE } else { $HOME }
  $CodexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $homeDir '.codex' }
}

$argsList = @(
  (Join-Path $RepoRoot 'scripts/install-skillset.py'),
  '--skillset', $Skillset,
  '--repo-root', $RepoRoot,
  '--scope', $Scope,
  '--codex-home', $CodexHome
)

if ($ProjectRoot) { $argsList += @('--project-root', $ProjectRoot) }
if ($WithMcp) { $argsList += '--with-mcp' }
if ($WithAgents) { $argsList += '--with-agents' }
if ($DryRun) {
  $argsList += '--dry-run'
}

python @argsList
if ($LASTEXITCODE -ne 0) { throw "Skillset installation failed (exit $LASTEXITCODE)." }
