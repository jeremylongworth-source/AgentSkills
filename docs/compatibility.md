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

## Portable Skill Design

Keep the main AgentSkills content portable by default:

- Put reusable workflow guidance in `SKILL.md`.
- Move detailed reference material into `references/` and load it only when the
  task needs it.
- Put deterministic repeat work in `scripts/` when a host can execute scripts.
- Keep host-specific frontmatter or shell interpolation out of portable skills
  unless the skill is intentionally host-specific.

The Agent Skills specification supports progressive disclosure: skill metadata
is available first, the full `SKILL.md` loads only after activation, and bundled
resources load as needed. Use host adapters for features outside that portable
core.

## Claude Code Optimization Notes

Verified against Claude Code docs on 2026-05-02.

Claude Code follows the Agent Skills standard and adds host-specific features
that can reduce context or isolate work for complex skills:

- `context: fork` runs a skill in an isolated subagent context. Use it for
  task-like skills with explicit instructions, not for passive guidelines.
- `agent` selects the subagent type when `context: fork` is set.
- `disable-model-invocation: true` keeps a skill manual-only and removes its
  description from the model-invoked skill list.
- `allowed-tools` can pre-approve tools while the skill is active, but host
  permission settings still control tool access.
- Inline `!command` placeholders and fenced shell-injection blocks insert shell
  output before the rendered prompt reaches Claude. This saves model work, but
  the command output still enters the prompt, so keep output small and
  structured.
- `shell: powershell` can be used for Claude Code skill shell injection on
  Windows when the host is configured for PowerShell.
- MCP Tool Search is enabled by default in supported Claude Code setups. Tool
  definitions are deferred and discovered on demand, which reduces the context
  cost of large MCP configurations.

Do not copy these Claude Code fields into portable skill frontmatter unless the
skill or generated adapter is specifically for Claude Code. For portable
AgentSkills, document the behavior as an adapter note or generate a host-specific
variant during installation.

Sources:

- [Agent Skills specification](https://agentskills.io/specification)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code MCP Tool Search](https://code.claude.com/docs/en/mcp)

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
