param(
  [string]$RepoRoot = '',
  [string]$GhPath = '',
  [switch]$SkipPublishDryRun
)

$ErrorActionPreference = 'Stop'
# Native status is checked explicitly below. In particular, rg exit 1 means
# a successful scan with no matches, even if the caller enables PS7's preference.
$PSNativeCommandUseErrorActionPreference = $false

if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
  $scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
  $RepoRoot = (Resolve-Path (Join-Path $scriptDir '..')).Path
} else {
  $RepoRoot = (Resolve-Path $RepoRoot).Path
}

function Find-PowerShellHost {
  $pwsh = Get-Command pwsh -ErrorAction SilentlyContinue
  if ($pwsh) { return $pwsh.Source }

  $windowsPowerShell = Get-Command powershell.exe -ErrorAction SilentlyContinue
  if ($windowsPowerShell) { return $windowsPowerShell.Source }

  throw "PowerShell host not found. Install PowerShell 7 or Windows PowerShell."
}

function Test-IsWindowsPlatform {
  return ($PSVersionTable.PSVersion.Major -lt 6) -or
    [System.Runtime.InteropServices.RuntimeInformation]::IsOSPlatform(
      [System.Runtime.InteropServices.OSPlatform]::Windows
    )
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

$PowerShellHost = Find-PowerShellHost

function Invoke-PowerShellFile {
  param(
    [string]$Path,
    [string[]]$Arguments = @()
  )

  $psArgs = @('-NoProfile')
  if (Test-IsWindowsPlatform) {
    $psArgs += @('-ExecutionPolicy', 'Bypass')
  }
  $psArgs += @('-File', $Path)
  $psArgs += $Arguments
  & $PowerShellHost @psArgs
  $exitCode = $LASTEXITCODE
  if ($exitCode -ne 0) {
    throw "Child PowerShell script '$Path' failed with exit code $exitCode."
  }
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
    throw "$Name could not run: rg not found."
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
  $exitCode = $LASTEXITCODE
  if ($exitCode -ne 0) { throw "git diff whitespace failed with exit code $exitCode." }
}

Invoke-Check "skill and skillset validation" {
  Invoke-PowerShellFile (Join-Path $RepoRoot 'scripts/validate-skills.ps1') @('-RepoRoot', $RepoRoot)
}

Invoke-Check "skillset install dry runs" {
  $dryRunHome = Join-Path ([System.IO.Path]::GetTempPath()) 'agentskills-release-check-codex-home'
  $skillsets = Get-ChildItem -Path (Join-Path $RepoRoot 'skillsets') -Filter '*.yaml' -File | Sort-Object Name
  foreach ($skillset in $skillsets) {
    $name = [System.IO.Path]::GetFileNameWithoutExtension($skillset.Name)
    Write-Host "Dry run: $name"
    python (Join-Path $RepoRoot 'scripts/install-skillset.py') --skillset $name --repo-root $RepoRoot --codex-home $dryRunHome --dry-run | Out-Null
    $exitCode = $LASTEXITCODE
    if ($exitCode -ne 0) { throw "Skillset '$name' install dry run failed with exit code $exitCode." }
  }
}

Invoke-Check "fresh Codex home install smoke" {
  Invoke-PowerShellFile (Join-Path $RepoRoot 'scripts/test-fresh-codex-home.ps1') @('-RepoRoot', $RepoRoot)
}

Invoke-Check "installer scope and preservation regression tests" {
  python (Join-Path $RepoRoot 'tests/test_install_skillset.py')
  if ($LASTEXITCODE -ne 0) { throw "Installer regression tests failed." }
}

Invoke-Check "skillset listing" {
  Invoke-PowerShellFile (Join-Path $RepoRoot 'scripts/list-skillsets.ps1') @('-RepoRoot', $RepoRoot, '-Markdown')
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
    $exitCode = $LASTEXITCODE
    if ($exitCode -ne 0) { throw "gh skill publish dry run failed with exit code $exitCode." }
  }
}

Invoke-Check "git status summary" {
  $status = git -C $RepoRoot status --short
  $exitCode = $LASTEXITCODE
  if ($exitCode -ne 0) { throw "git status summary failed with exit code $exitCode." }
  if ($status) {
    Write-Host "Working tree has changes:"
    $status | ForEach-Object { Write-Host $_ }
  } else {
    Write-Host "Working tree is clean."
  }
}

Write-Host "Release check complete."
