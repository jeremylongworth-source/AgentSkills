param(
  [string]$RepoRoot = '',
  [string]$GhPath = '',
  [switch]$SkipPublishDryRun
)

$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
  $scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
  $RepoRoot = (Resolve-Path (Join-Path $scriptDir '..')).Path
} else {
  $RepoRoot = (Resolve-Path $RepoRoot).Path
}

function Find-GitHubCli {
  if (-not [string]::IsNullOrWhiteSpace($GhPath)) {
    if (-not (Test-Path $GhPath)) { throw "GitHub CLI not found: $GhPath" }
    return (Resolve-Path $GhPath).Path
  }

  $command = Get-Command gh -ErrorAction SilentlyContinue
  if ($command) { return $command.Source }

  $fallback = 'C:\Program Files\GitHub CLI\gh.exe'
  if (Test-Path $fallback) { return $fallback }

  throw "GitHub CLI not found. Install gh or pass -GhPath."
}

function Invoke-Check {
  param(
    [string]$Name,
    [scriptblock]$Script
  )

  Write-Host "==> $Name"
  & $Script
  Write-Host "ok: $Name"
}

function Invoke-RgNoMatches {
  param(
    [string]$Name,
    [string]$Pattern
  )

  $rg = Get-Command rg -ErrorAction SilentlyContinue
  if (-not $rg) {
    Write-Host "skip: $Name (rg not found)"
    return
  }

  $output = & rg --hidden --glob '!.git/**' --glob '!**/.git/**' --glob '!**/node_modules/**' --glob '!**/.venv/**' --glob '!**/__pycache__/**' --line-number --pcre2 -- $Pattern $RepoRoot
  $exitCode = $LASTEXITCODE
  if ($exitCode -eq 0) {
    $output | ForEach-Object { Write-Host $_ }
    throw "$Name found matches."
  }
  if ($exitCode -ne 1) {
    throw "$Name scan failed with exit code $exitCode."
  }
}

Invoke-Check "git diff whitespace" {
  git -C $RepoRoot diff --check
}

Invoke-Check "skill and skillset validation" {
  powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $RepoRoot 'scripts/validate-skills.ps1') -RepoRoot $RepoRoot
}

Invoke-Check "skillset install dry runs" {
  $dryRunHome = Join-Path $env:TEMP 'agentskills-release-check-codex-home'
  $skillsets = Get-ChildItem -Path (Join-Path $RepoRoot 'skillsets') -Filter '*.yaml' -File | Sort-Object Name
  foreach ($skillset in $skillsets) {
    $name = [System.IO.Path]::GetFileNameWithoutExtension($skillset.Name)
    Write-Host "Dry run: $name"
    powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $RepoRoot 'scripts/install-skillset.ps1') $name -RepoRoot $RepoRoot -CodexHome $dryRunHome -DryRun | Out-Null
  }
}

Invoke-Check "fresh Codex home install smoke" {
  powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $RepoRoot 'scripts/test-fresh-codex-home.ps1') -RepoRoot $RepoRoot
}

Invoke-Check "skillset listing" {
  powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $RepoRoot 'scripts/list-skillsets.ps1') -RepoRoot $RepoRoot -Markdown
}

Invoke-Check "secret scan" {
  $secretPattern = '-----BEGIN (RSA|OPENSSH|DSA|EC|PGP) PRIVATE KEY-----|ghp_[A-Za-z0-9_]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-proj-[A-Za-z0-9_-]{20,}|sk-[A-Za-z0-9]{32,}|xox[baprs]-[A-Za-z0-9-]{20,}'
  Invoke-RgNoMatches "secret scan" $secretPattern
}

Invoke-Check "local path scan" {
  $pathPattern = 'C:\\Users\\[A-Za-z0-9._-]+|/Users/[A-Za-z0-9._-]+|/home/[A-Za-z0-9._-]+|D:\\CodexProject'
  Invoke-RgNoMatches "local path scan" $pathPattern
}

if (-not $SkipPublishDryRun) {
  Invoke-Check "gh skill publish dry run" {
    $gh = Find-GitHubCli
    & $gh skill publish --dry-run
  }
}

Invoke-Check "git status summary" {
  $status = git -C $RepoRoot status --short
  if ($status) {
    Write-Host "Working tree has changes:"
    $status | ForEach-Object { Write-Host $_ }
  } else {
    Write-Host "Working tree is clean."
  }
}

Write-Host "Release check complete."
