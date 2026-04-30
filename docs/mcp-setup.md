# MCP Setup

MCP presets are portable tool-group definitions. Server snippets live in
`mcp/servers/`.

Current server snippets:

- `context7`: current library/framework documentation
- `openaiDeveloperDocs`: official OpenAI documentation
- `playwright`: browser automation and screenshots
- `chrome-devtools`: Chrome DevTools inspection

On Windows, package-based servers use `npx.cmd` instead of `npx` to avoid PowerShell execution policy blocking `.ps1` shims.

Security note: package-based snippets that use `npx` may download and execute
third-party package code when the host starts that MCP server. Review the server
package before enabling it in sensitive workspaces, and pin package versions in
controlled environments instead of relying on floating latest versions.

The snippets are currently written for Codex `config.toml`. For Cursor, Claude
Code, Gemini CLI, and other hosts, translate the command, arguments, and
environment settings into that host's MCP configuration format.

For host-specific setup, see [setup guides](setup/README.md).
