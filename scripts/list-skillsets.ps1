param(
  [string]$RepoRoot = '',
  [switch]$Markdown
)

$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
  $scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
  $RepoRoot = (Resolve-Path (Join-Path $scriptDir '..')).Path
} else {
  $RepoRoot = (Resolve-Path $RepoRoot).Path
}

function Clean-Scalar {
  param([string]$Value)

  $clean = $Value.Trim()
  if (($clean.StartsWith('"') -and $clean.EndsWith('"')) -or ($clean.StartsWith("'") -and $clean.EndsWith("'"))) {
    return $clean.Substring(1, $clean.Length - 2)
  }
  return $clean
}

function Read-SkillsetManifest {
  param([string]$Path)

  $manifest = [ordered]@{
    Name = $null
    Description = $null
    Skills = @()
    McpPresets = @()
    AgentsFile = $null
  }
  $current = $null

  foreach ($raw in Get-Content -Path $Path) {
    $line = ($raw -split '#', 2)[0].TrimEnd()
    if ([string]::IsNullOrWhiteSpace($line)) { continue }

    if ($line -match '^([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$') {
      $key = $Matches[1]
      $value = $Matches[2].Trim()
      switch ($key) {
        'name' {
          $manifest.Name = Clean-Scalar $value
          $current = $null
        }
        'description' {
          $manifest.Description = Clean-Scalar $value
          $current = $null
        }
        'agents_file' {
          $manifest.AgentsFile = Clean-Scalar $value
          $current = $null
        }
        'skills' {
          $current = 'skills'
        }
        'mcp_presets' {
          $current = 'mcp_presets'
        }
        default {
          $current = $null
        }
      }
      continue
    }

    if ($line -match '^\s*-\s*(.+?)\s*$') {
      $item = Clean-Scalar $Matches[1]
      if ($current -eq 'skills') {
        $manifest.Skills += $item
      } elseif ($current -eq 'mcp_presets') {
        $manifest.McpPresets += $item
      }
    }
  }

  return [pscustomobject]$manifest
}

function Escape-MarkdownCell {
  param([string]$Value)

  if ($null -eq $Value -or $Value -eq '') { return '' }
  return $Value.Replace('|', '\|')
}

$skillsetsDir = Join-Path $RepoRoot 'skillsets'
$manifests = Get-ChildItem -Path $skillsetsDir -Filter '*.yaml' -File | Sort-Object Name

$rows = foreach ($file in $manifests) {
  $manifest = Read-SkillsetManifest $file.FullName
  [pscustomobject]@{
    Name = $manifest.Name
    Description = $manifest.Description
    Skills = $manifest.Skills.Count
    McpPresets = ($manifest.McpPresets -join ', ')
    AgentsFile = $manifest.AgentsFile
  }
}

if ($Markdown) {
  Write-Output '| Skillset | Description | Skills | MCP presets | Agents file |'
  Write-Output '|---|---|---:|---|---|'
  foreach ($row in $rows) {
    $name = Escape-MarkdownCell $row.Name
    $description = Escape-MarkdownCell $row.Description
    $presets = Escape-MarkdownCell $row.McpPresets
    $agentsFile = Escape-MarkdownCell $row.AgentsFile
    Write-Output ('| `{0}` | {1} | {2} | {3} | `{4}` |' -f $name, $description, $row.Skills, $presets, $agentsFile)
  }
  return
}

$rows
