# Compatibility Matrix

Use this matrix when choosing where to install skills and where to put routing
instructions.

This table describes host adapters. The portable content remains the same
skill folders, skillset manifests, and MCP presets.

| Host | User skills | Project skills | Project instructions | MCP format | Verify |
|---|---|---|---|---|---|
| Codex | `~/.codex/skills` | `.agents/skills` | `AGENTS.md` | `~/.codex/config.toml` TOML | check skills list or invoke `$skill-name` |
| GitHub Copilot | `~/.copilot/skills` | `.agents/skills` or `.github/skills` | `.github/copilot-instructions.md`, `AGENTS.md` | host-dependent | ask for a task matching the skill |
| Cursor | `~/.cursor/skills` | `.agents/skills` | root `AGENTS.md`, `.cursor/rules/*.mdc` | `.cursor/mcp.json` JSON | `cursor-agent mcp list` for MCP |
| Claude Code | `~/.claude/skills` | `.claude/skills` | `CLAUDE.md` | `claude mcp add ...` or Claude settings | `/memory`, then invoke `/skill-name` |
| Gemini CLI | `~/.gemini/skills` | `.agents/skills` or `.gemini/skills` | `GEMINI.md` | `.gemini/settings.json` or `gemini mcp add ...` | `gemini skills list`, `/memory show` |

## Install with GitHub CLI

Use `gh skill install` as one host-specific atomic skill install path:

```powershell
gh skill install jeremylongworth-source/AgentSkills qa-test-strategy --agent codex --scope user --pin v0.1.1
```

Change `--agent` for another host:

- `github-copilot`
- `cursor`
- `claude-code`
- `gemini-cli`

## Install a Codex Skillset

Use the local installer for curated Codex bundles:

```powershell
.\scripts\install-skillset.ps1 game-dev
```

Preview changes first:

```powershell
.\scripts\install-skillset.ps1 game-dev -DryRun
```

## Notes for Future Skillsets

Skillsets are data-driven manifests under `skillsets/`. Add new bundles by
creating a manifest that references existing skills, MCP presets, and optional
agents files.

The validator checks that each manifest reference exists. The Codex installer
reads MCP preset server lists from `mcp/presets/*.toml`, so new presets do not
need Python changes when they follow the existing `servers = [...]` format.

Keep new skillsets host-neutral unless the workflow itself is host-specific.
