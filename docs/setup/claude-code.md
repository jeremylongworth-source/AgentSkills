# Claude Code Setup

Claude Code supports native skills, `CLAUDE.md` project memory, path-scoped
rules, and MCP servers. Use `gh skill install` to place AgentSkills in the
right Claude Code skill directory.

## Install One Skill

Preview the skill:

```powershell
gh skill preview jeremylongworth-source/AgentSkills qa-test-strategy
```

Install it for all Claude Code projects:

```powershell
gh skill install jeremylongworth-source/AgentSkills qa-test-strategy --agent claude-code --scope user --pin v0.1.1
```

Install it for the current repository instead:

```powershell
gh skill install jeremylongworth-source/AgentSkills qa-test-strategy --agent claude-code --scope project --pin v0.1.1
```

Claude can invoke a skill automatically from its description, or you can invoke
it directly as a slash command:

```text
/qa-test-strategy create a release smoke test plan
```

## Add Project Instructions

Claude Code reads `CLAUDE.md`, not `AGENTS.md`. If your repository already has
an AgentSkills `AGENTS.md`, create a small `CLAUDE.md` wrapper:

```md
@AGENTS.md

## Claude Code

Use installed AgentSkills when a task matches a skill description. Keep
`CLAUDE.md` for project facts and use skills for repeatable procedures.
```

For larger projects, place focused Markdown rules in `.claude/rules/` and keep
`CLAUDE.md` under 200 lines when practical.

## MCP

Use Claude Code's MCP commands rather than the Codex TOML snippets directly.
For local stdio servers:

```powershell
claude mcp add context7 -- cmd /c npx -y @upstash/context7-mcp
```

On native Windows, use the `cmd /c` wrapper for `npx` based MCP servers.

## Verify

Run Claude Code from the repository root and use `/memory` to confirm the
expected `CLAUDE.md` files are loaded. Then invoke one installed skill directly
or ask for a task that matches the skill description.

## References

- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code memory](https://code.claude.com/docs/en/memory)
- [Claude Code MCP](https://code.claude.com/docs/en/mcp)
- [GitHub CLI `gh skill install`](https://cli.github.com/manual/gh_skill_install)
