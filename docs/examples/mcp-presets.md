# Use MCP Presets

MCP presets group tool servers that support common workflows. Treat presets as
portable intent, then translate each server into the target host's MCP config
format.

## Included Presets

| Preset | Servers | Use |
|---|---|---|
| `docs-research` | `context7`, `openaiDeveloperDocs` | current documentation and API research |
| `browser-qa` | `playwright`, `chrome-devtools` | browser checks, screenshots, and UI inspection |
| `full` | all included servers | broad workflows that need docs and browser QA |

Preset files live in `mcp/presets/`. Server snippets live in `mcp/servers/`.

## Codex Skillset Install

For Codex, the local skillset installer appends the required server snippets:

```powershell
.\scripts\install-skillset.ps1 frontend-product
```

The `frontend-product` skillset includes `docs-research` and `browser-qa`.

## Manual Codex Setup

Copy a server snippet from `mcp/servers/` into Codex `config.toml`.

Example:

```toml
[mcp_servers.context7]
command = "npx.cmd"
args = ["-y", "@upstash/context7-mcp"]
```

## Other Hosts

The included snippets are Codex TOML. Translate them for other hosts.

Cursor project example:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    }
  }
}
```

Gemini CLI example:

```powershell
gemini mcp add context7 npx -y @upstash/context7-mcp
```

Claude Code on native Windows needs a command wrapper for `npx` based servers:

```powershell
claude mcp add context7 -- cmd /c npx -y @upstash/context7-mcp
```

## Verify

Ask the host to list configured MCP servers or use a prompt that requires the
server, such as current framework documentation lookup or browser screenshot
inspection.
