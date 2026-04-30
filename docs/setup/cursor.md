# Cursor Setup

Cursor can use project rules, user rules, root `AGENTS.md`, MCP servers, and
agent skills installed by `gh skill`.

## Install One Skill

Preview the skill:

```powershell
gh skill preview jeremylongworth-source/AgentSkills visual-ui-ux-audit
```

Install it for the current repository:

```powershell
gh skill install jeremylongworth-source/AgentSkills visual-ui-ux-audit --agent cursor --scope project --pin v0.1.1
```

Install it for all Cursor projects:

```powershell
gh skill install jeremylongworth-source/AgentSkills visual-ui-ux-audit --agent cursor --scope user --pin v0.1.1
```

## Add Project Routing

For simple routing, put an `AGENTS.md` file in the project root. Start from one
of the templates in `agents/`.

For Cursor-specific rules, create a project rule under `.cursor/rules/`.

Example `.cursor/rules/agent-skills.mdc`:

```md
---
alwaysApply: true
---

Use installed AgentSkills when the user request matches a skill description.
Read the matching `SKILL.md` first, then load referenced files only when needed.
```

Use root `AGENTS.md` for straightforward shared instructions. Use
`.cursor/rules` when you need multiple rules, path scoping, or Cursor-specific
behavior.

## MCP

Cursor uses JSON MCP configuration. Create `.cursor/mcp.json` for project tools
or `~/.cursor/mcp.json` for global tools.

The AgentSkills MCP snippets in `mcp/servers/` are Codex TOML. Translate the
server command and arguments into Cursor's `mcpServers` JSON shape before using
them in Cursor.

## Verify

Open Cursor in the repository and confirm the project rule or `AGENTS.md`
appears in the agent context. If using Cursor CLI MCP, list configured servers:

```powershell
cursor-agent mcp list
```

Ask for a task that should trigger the installed skill, such as a screenshot
grounded UI audit for `visual-ui-ux-audit`.

## References

- [Cursor rules](https://docs.cursor.com/context/rules)
- [Cursor MCP](https://docs.cursor.com/advanced/model-context-protocol)
- [Cursor CLI MCP](https://docs.cursor.com/cli/mcp)
- [GitHub CLI `gh skill install`](https://cli.github.com/manual/gh_skill_install)
