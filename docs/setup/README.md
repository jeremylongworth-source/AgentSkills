# Setup Guides

Use these guides to install AgentSkills into a specific AI coding agent.

For task-oriented examples, see [examples](../examples/README.md).
For host path details, see [compatibility](../compatibility.md).
For common setup failures, see [troubleshooting](../troubleshooting.md).
For portability rules, see [vendor neutrality](../vendor-neutrality.md).
For Astra-specific instruction review and evaluation, see
[AgentSkills with GPT-6 Astra](astra.md).

## Choose an install path

If you are setting up AgentSkills in a new repository, use
`agentskills-project-onboarding` first. It should inspect the repo, recommend a
focused skillset or small set of atomic skills, decide project versus user
scope, draft project routing guidance, and define verification steps before
install commands are run.

Use `gh skill install` when you want a convenient host-specific installer for
one or more atomic skills. You can also copy skill folders manually into a
host-supported skill path.

Use the repository skillset scripts when you want one of the curated
AgentSkills skillsets. The PowerShell installer currently targets Codex by
copying selected skills. MCP snippets are opt-in (`-WithMcp`), and routing
templates can only be appended explicitly in project scope (`-WithAgents`).
Global `AGENTS.md` is never changed. Use `global-foundation` for user scope;
choose focused domain bundles for project scope.

Use `agents/AGENTS.*.md` when the host needs a project instruction file instead
of, or in addition to, native skills.

## Prerequisites

- GitHub CLI 2.90.0 or later with `gh skill` support.
- A cloned copy of this repository for local skillset installs.
- Python on `PATH` for the PowerShell skillset installer.
- The target agent host installed and signed in.

## Preview before installing

Skills are instructions and may include scripts or references. Inspect a skill
before installing it:

```powershell
gh skill preview jeremylongworth-source/AgentSkills game-threejs-development
```

Install a pinned skill into a host-specific location:

```powershell
gh skill install jeremylongworth-source/AgentSkills game-threejs-development --agent codex --scope user --pin v0.1.1
```

Install from the repository interactively:

```powershell
gh skill install jeremylongworth-source/AgentSkills --agent github-copilot --scope project
```

## Host Guides

| Host | Guide | Best first install |
|---|---|---|
| Codex | [Codex](codex.md) | `gh skill install ... --agent codex`, or `.\scripts\install-skillset.ps1 game-dev -Scope project -ProjectRoot ../MyGame` |
| GitHub Copilot | [GitHub Copilot](github-copilot.md) | `gh skill install ... --agent github-copilot --scope project` |
| Cursor | [Cursor](cursor.md) | `gh skill install ... --agent cursor --scope project` |
| Claude Code | [Claude Code](claude-code.md) | `gh skill install ... --agent claude-code --scope user` |
| Gemini CLI | [Gemini CLI](gemini-cli.md) | `gh skill install ... --agent gemini-cli --scope user` |

## Skillsets

Skillset manifests live in `skillsets/`. Use them as curated bundles or as a
shopping list for hosts where you install skills one by one.

```powershell
.\scripts\install-skillset.ps1 game-dev -Scope project -ProjectRoot ../MyGame
.\scripts\install-skillset.ps1 html5-game-publishing -Scope project -ProjectRoot ../MyGame
.\scripts\install-skillset.ps1 sales-marketing -Scope project -ProjectRoot ../MyBusiness
```

Available skillsets:

See the [Skillset Catalog](https://github.com/jeremylongworth-source/AgentSkills/wiki/Skillset-Catalog)
for the current list, or run:

```powershell
.\scripts\list-skillsets.ps1
```

## MCP Presets

MCP presets and server snippets live in `mcp/`. The included snippets are TOML
for Codex. Other hosts usually need their own MCP command or JSON format, so
translate the server entries rather than pasting the TOML directly.

See [MCP setup](../mcp-setup.md) for the current preset list.

## References

- [GitHub CLI `gh skill install`](https://cli.github.com/manual/gh_skill_install)
- [GitHub Copilot agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- [OpenAI Codex agent skills](https://developers.openai.com/codex/skills)
