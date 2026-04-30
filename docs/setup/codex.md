# Codex Setup

Codex has native support for agent skills. Use `gh skill install` for portable
atomic skill installs, or use the repository skillset installer when you want a
curated AgentSkills bundle with Codex routing and MCP snippets.

## Install One Skill

Preview the skill:

```powershell
gh skill preview jeremylongworth-source/AgentSkills game-threejs-development
```

Install it for all Codex projects:

```powershell
gh skill install jeremylongworth-source/AgentSkills game-threejs-development --agent codex --scope user --pin v0.1.1
```

Install it into the current repository instead:

```powershell
gh skill install jeremylongworth-source/AgentSkills game-threejs-development --agent codex --scope project --pin v0.1.1
```

## Install a Skillset

From the repository root, install a curated skillset:

```powershell
.\scripts\install-skillset.ps1 game-dev
```

The PowerShell installer:

- copies the skillset's skills into the Codex home skills directory
- appends MCP server snippets from the skillset presets to Codex config
- appends the skillset routing template to the Codex home `AGENTS.md`

Useful first skillsets:

```powershell
.\scripts\install-skillset.ps1 game-dev
.\scripts\install-skillset.ps1 html5-game-publishing
.\scripts\install-skillset.ps1 frontend-product
```

Restart Codex after installing a skillset if new MCP servers or skills do not
appear immediately.

## Add Project Routing

For project-specific routing, copy the closest template from `agents/` into the
project root as `AGENTS.md`.

Examples:

- `agents/AGENTS.game-dev.md` for game projects
- `agents/AGENTS.sales-marketing.md` for GTM and revenue workflows
- `agents/AGENTS.full.md` for broad AgentSkills routing

Keep project routing short. Put reusable procedures in skills, not in
`AGENTS.md`.

## Verify

Start Codex from the repository root and check that the skill appears in the
skills list. You can also explicitly invoke a skill by name, for example:

```text
$game-threejs-development review this scene architecture
```

For implicit routing, ask for a task that matches the skill description and
confirm that Codex reads the matching `SKILL.md`.

## References

- [OpenAI Codex agent skills](https://developers.openai.com/codex/skills)
- [GitHub CLI `gh skill install`](https://cli.github.com/manual/gh_skill_install)
