# Vendor Neutrality

AgentSkills should stay useful across agent hosts. The portable core is:

- `skills/*/SKILL.md`
- `skills/*/references/`
- `skills/*/scripts/`
- `skillsets/*.yaml`
- `mcp/presets/*.toml`

Host-specific files are adapters around that core:

- `skills/*/agents/openai.yaml`
- `agents/AGENTS.*.md`
- `templates/hosts/`
- `docs/setup/*`
- `scripts/install-skillset.ps1`

## Principles

- Keep skill instructions host-neutral unless a skill is explicitly about one
  vendor or product.
- Put vendor-specific commands, paths, and config formats in setup guides,
  compatibility docs, templates, or adapter scripts.
- Prefer open formats: Markdown, YAML, TOML, JSON, and plain shell commands.
- Keep bundle manifests data-only. Do not encode host behavior in skillset
  names or descriptions.
- Treat MCP presets as logical tool groups. Translate them into each host's MCP
  config format at the edge.
- Avoid making GitHub CLI, Codex, or any single host the only path to use the
  repository. They can be supported paths, not the portable contract.

## Naming

Use domain and workflow names:

- `backend-api-development`
- `data-analytics-engineering`
- `devops-release-engineering`

Avoid host-bound names unless the bundle is actually host-specific:

- `codex-backend`
- `cursor-frontend`
- `claude-writing`

## Documentation Pattern

When adding a host-specific instruction, name the host and keep the portable
alternative nearby.

Good:

```text
Use `gh skill install` for host-specific installs, or copy the skill directory
manually into a host-supported skill path.
```

Avoid:

```text
Use GitHub CLI to install AgentSkills.
```

## Current Host Adapters

The local skillset installer is a Codex adapter. It copies selected skills into
Codex home, appends Codex TOML MCP snippets, and appends a Codex-readable
`AGENTS.md` routing block.

Other hosts should consume the same skill and skillset content through their
own skill directories, instruction files, and MCP config formats.
