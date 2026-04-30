param(
  [string]$RepoRoot = '',
  [string[]]$Skillsets = @('game-dev', 'all'),
  [switch]$KeepTemp
)

$ErrorActionPreference = 'Stop'

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

function Read-ListValue {
  param(
    [string]$Path,
    [string]$Key
  )

  $values = @()
  $inList = $false
  foreach ($raw in Get-Content -Path $Path) {
    $line = ($raw -split '#', 2)[0].TrimEnd()
    if ($line -match "^$([regex]::Escape($Key))\s*:") {
      $inList = $true
      continue
    }
    if ($inList -and $line -match '^\s*-\s*(.+?)\s*$') {
      $values += $matches[1].Trim().Trim('"', "'")
      continue
    }
    if ($inList -and $line -match '^[A-Za-z_][A-Za-z0-9_-]*\s*:') {
      break
    }
  }
  return $values
}

function Read-ScalarValue {
  param(
    [string]$Path,
    [string]$Key
  )

  foreach ($raw in Get-Content -Path $Path) {
    $line = ($raw -split '#', 2)[0].TrimEnd()
    if ($line -match "^$([regex]::Escape($Key))\s*:\s*(.+?)\s*$") {
      return $matches[1].Trim().Trim('"', "'")
    }
  }
  return ''
}

function Read-PresetServers {
  param([string]$Path)

  $text = Get-Content -Raw -Path $Path
  $match = [regex]::Match($text, 'servers\s*=\s*\[(.*?)\]', [System.Text.RegularExpressions.RegexOptions]::Singleline)
  if (-not $match.Success) { return @() }

  $servers = @()
  foreach ($part in $match.Groups[1].Value.Split(',')) {
    $name = $part.Trim().Trim('"', "'")
    if (-not [string]::IsNullOrWhiteSpace($name)) {
      $servers += $name
    }
  }
  return $servers
}

$tempBase = [System.IO.Path]::GetTempPath()
$tempRoot = Join-Path $tempBase ('agentskills-fresh-home-' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $tempRoot | Out-Null
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
}

try {
  foreach ($skillset in $Skillsets) {
    $manifestPath = Join-Path $RepoRoot "skillsets/$skillset.yaml"
    if (-not (Test-Path $manifestPath)) {
      throw "Unknown skillset: $skillset"
    }

    $codexHome = Join-Path $tempRoot $skillset
    Invoke-PowerShellFile (Join-Path $RepoRoot 'scripts/install-skillset.ps1') @($skillset, '-RepoRoot', $RepoRoot, '-CodexHome', $codexHome) | Out-Null

    $skills = Read-ListValue -Path $manifestPath -Key 'skills'
    foreach ($skill in $skills) {
      $skillFile = Join-Path $codexHome "skills/$skill/SKILL.md"
      if (-not (Test-Path $skillFile)) {
        throw "${skillset}: missing installed skill file: $skill"
      }
    }

    $presets = Read-ListValue -Path $manifestPath -Key 'mcp_presets'
    $servers = @()
    foreach ($preset in $presets) {
      $presetPath = Join-Path $RepoRoot "mcp/presets/$preset.toml"
      if (-not (Test-Path $presetPath)) {
        throw "${skillset}: missing MCP preset: $preset"
      }
      $servers += Read-PresetServers -Path $presetPath
    }

    $configPath = Join-Path $codexHome 'config.toml'
    foreach ($server in ($servers | Select-Object -Unique)) {
      if (-not (Test-Path $configPath)) {
        throw "${skillset}: missing config.toml for MCP server '$server'"
      }
      $marker = "[mcp_servers.$server]"
      if (-not (Select-String -Path $configPath -SimpleMatch $marker -Quiet)) {
        throw "${skillset}: missing MCP marker '$marker'"
      }
    }

    $agentsFile = Read-ScalarValue -Path $manifestPath -Key 'agents_file'
    if (-not [string]::IsNullOrWhiteSpace($agentsFile)) {
      $agentsPath = Join-Path $codexHome 'AGENTS.md'
      $marker = "AgentSkills skillset: $skillset"
      if (-not (Test-Path $agentsPath)) {
        throw "${skillset}: missing AGENTS.md"
      }
      if (-not (Select-String -Path $agentsPath -SimpleMatch $marker -Quiet)) {
        throw "${skillset}: missing AGENTS marker"
      }
    }

    Write-Host "ok: $skillset fresh-home install ($($skills.Count) skills)"
  }
}
finally {
  if ($KeepTemp) {
    Write-Host "Kept temp Codex home root: $tempRoot"
  } else {
    $resolvedTempBase = (Resolve-Path $tempBase).Path.TrimEnd('\', '/')
    $resolvedTempRoot = (Resolve-Path $tempRoot).Path
    $comparison = if (Test-IsWindowsPlatform) { [System.StringComparison]::OrdinalIgnoreCase } else { [System.StringComparison]::Ordinal }
    if (-not $resolvedTempRoot.StartsWith($resolvedTempBase, $comparison)) {
      throw "Refusing to remove temp root outside temp base: $resolvedTempRoot"
    }
    if ((Split-Path -Leaf $resolvedTempRoot) -notmatch '^agentskills-fresh-home-[a-f0-9]{32}$') {
      throw "Refusing to remove unexpected temp root: $resolvedTempRoot"
    }
    Remove-Item -LiteralPath $resolvedTempRoot -Recurse -Force
  }
}
