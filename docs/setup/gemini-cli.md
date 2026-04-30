# Gemini CLI Setup

Gemini CLI supports agent skills, hierarchical `GEMINI.md` context files, and
MCP servers. Use `gh skill install` for host-specific AgentSkills installs, or
use Gemini CLI's own `gemini skills` commands for local links and management.

## Install One Skill

Preview the skill:

```powershell
gh skill preview jeremylongworth-source/AgentSkills product-brainstorming-planning
```

Install it for all Gemini CLI projects:

```powershell
gh skill install jeremylongworth-source/AgentSkills product-brainstorming-planning --agent gemini-cli --scope user --pin v0.1.1
```

Install it for the current repository instead:

```powershell
gh skill install jeremylongworth-source/AgentSkills product-brainstorming-planning --agent gemini-cli --scope project --pin v0.1.1
```

List discovered skills:

```powershell
gemini skills list
```

## Add Project Context

Gemini CLI uses `GEMINI.md` for persistent project context. If your repository
already has `AGENTS.md`, create a small `GEMINI.md` wrapper:

```md
@AGENTS.md

## Gemini CLI

Use installed AgentSkills when a task matches a skill description. Keep
`GEMINI.md` for project facts and use skills for repeatable procedures.
```

Use `/memory show` inside Gemini CLI to confirm which context files are loaded.
Use `/skills reload` after changing skills during a session.

## MCP

Gemini CLI can configure MCP servers from the terminal:

```powershell
gemini mcp add context7 npx -y @upstash/context7-mcp
gemini mcp list
```

You can also configure MCP in `.gemini/settings.json` for a project or
`~/.gemini/settings.json` for your user. Translate the AgentSkills Codex TOML
snippets into Gemini CLI's `mcpServers` JSON shape before using them.

## Verify

Run:

```powershell
gemini skills list
```

Then ask for a task that matches the installed skill description. Gemini CLI
loads skill metadata first and activates the full skill when the request
matches, subject to user approval.

## References

- [Gemini CLI skills](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/skills.md)
- [Gemini CLI configuration](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/reference/configuration.md)
- [Gemini CLI MCP tutorial](https://google-gemini.github.io/gemini-cli/docs/cli/tutorials.html)
- [GitHub CLI `gh skill install`](https://cli.github.com/manual/gh_skill_install)
