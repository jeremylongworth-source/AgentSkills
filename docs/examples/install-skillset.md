# Install a Skillset

Use a skillset when you want a curated group of skills plus routing guidance.
Skillset manifests are portable. The repository skillset installer is the
current Codex adapter.

## Install

From the repository root:

```powershell
.\scripts\install-skillset.ps1 game-dev
```

Preview the install first:

```powershell
.\scripts\install-skillset.ps1 game-dev -DryRun
```

Other useful bundles:

```powershell
.\scripts\install-skillset.ps1 html5-game-publishing
.\scripts\install-skillset.ps1 executive-command-center
.\scripts\install-skillset.ps1 founder-fundraising-ir
.\scripts\install-skillset.ps1 ai-transformation-governance
.\scripts\install-skillset.ps1 owner-operator-os
.\scripts\install-skillset.ps1 operating-cadence
.\scripts\install-skillset.ps1 engineering-delivery
.\scripts\install-skillset.ps1 support-success
.\scripts\install-skillset.ps1 frontend-product
.\scripts\install-skillset.ps1 product-research
.\scripts\install-skillset.ps1 revenue-growth
.\scripts\install-skillset.ps1 analytics-finance
.\scripts\install-skillset.ps1 sales-marketing
.\scripts\install-skillset.ps1 research-validation
```

## What the Installer Does

The installer reads `skillsets/<name>.yaml`, then:

- copies the listed skills into the Codex home skills directory
- appends required MCP server snippets to Codex `config.toml`
- appends the matching routing template to Codex `AGENTS.md`

Restart Codex if new skills or MCP servers do not appear immediately.

## Verify in a Temporary Codex Home

Use a temporary Codex home when testing the installer without touching your
normal setup:

```powershell
$tempHome = Join-Path $env:TEMP "agentskills-codex-home"
Remove-Item -Recurse -Force $tempHome -ErrorAction SilentlyContinue
.\scripts\install-skillset.ps1 game-dev -CodexHome $tempHome
Get-ChildItem "$tempHome\skills"
```

Expected result:

- the selected skills appear under `$tempHome\skills`
- `$tempHome\config.toml` contains MCP snippets for the skillset presets
- `$tempHome\AGENTS.md` contains the matching routing template

## For Non-Codex Hosts

Use `skillsets/<name>.yaml` as a shopping list, then install the listed skills
with `gh skill install --agent <host>` or by copying skill folders into that
host's supported skill path.
