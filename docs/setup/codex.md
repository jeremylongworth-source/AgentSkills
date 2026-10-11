# Codex Setup

Keep global instructions universal and install domain workflows in the
repositories that use them. These examples use the local development adapter;
older published tags do not include the new scope options.

For model selection, instruction tuning, and verification with `gpt-6-astra`,
see [AgentSkills with Astra](astra.md). Selecting a model is separate from
installing skills; the adapter does not change the model or reasoning setting.

## Global Foundation

```powershell
.\scripts\install-skillset.ps1 global-foundation -Scope user -DryRun
.\scripts\install-skillset.ps1 global-foundation -Scope user
```

This installs 13 custom skills. Codex-managed `openai-docs` and `skill-creator`
complete the 15-skill foundation and are left untouched. Frequent skill authors
can add the evaluation extension:

```powershell
.\scripts\install-skillset.ps1 agentops-evaluation -Scope user
```

Together these manifests install 17 unique custom skills. User scope preserves
this adapter's existing `$CODEX_HOME/skills` layout (`~/.codex/skills` by default).
Use `-CodexHome` to select another home. Existing skills with the same names are
replaced; unrelated skills are preserved. Back up local modifications first.

## Project Skills

Choose an existing repository directory explicitly:

```powershell
.\scripts\install-skillset.ps1 game-dev -Scope project -ProjectRoot ../MyGame -DryRun
.\scripts\install-skillset.ps1 game-dev -Scope project -ProjectRoot ../MyGame
```

Project skills go to `<project>/.agents/skills`. User scope remains the default
for compatibility with older callers; always spell out scope in new setup.
Use `all` only when the full catalog is explicitly needed for development or
testing. For one atomic skill, use a supported host installer or copy its
complete folder to the appropriate skill directory.

## Optional MCP and Routing

Skills install without changing MCP configuration or instruction files.
After reviewing the manifest's presets and routing template, opt in separately:

```powershell
.\scripts\install-skillset.ps1 game-dev -Scope project -ProjectRoot ../MyGame -WithMcp -WithAgents -DryRun
```

Remove `-DryRun` to apply the reviewed install. Project MCP snippets are added
to `<project>/.codex/config.toml`; routing is appended once to the project's
`AGENTS.md`, preserving existing text. Existing MCP server entries are retained.
Review project trust and tool access in Codex before using configured tools.

`-WithMcp` in user scope adds snippets to `$CODEX_HOME/config.toml` only when
explicitly requested. `-WithAgents` is rejected in user scope: the installer
never writes global `AGENTS.md`. Manifests can omit both presets and routing.
Old global routing blocks are not removed automatically; review and back them
up before a separate cleanup.

## Python and Bash

The Python adapter accepts `--scope`, `--project-root`, `--codex-home`,
`--with-mcp`, `--with-agents`, and `--dry-run`. The Bash wrapper forwards these
options and uses `python3` (or the `PYTHON` environment override):

```bash
./scripts/install-skillset.sh global-foundation --scope user --dry-run
./scripts/install-skillset.sh game-dev --scope project --project-root ../MyGame
```

## Verify

Start a fresh Codex task in the repository and inspect its available skills.
Invoke one intended skill and confirm the matching instructions are read.
Check global `AGENTS.md` is unchanged and domain skills are scoped correctly.
Dry-run and filesystem checks verify installation, not model routing behavior.

## References

- [OpenAI skill discovery and scope](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)
- [Global Foundation brief](../bundles/global-foundation.md)
