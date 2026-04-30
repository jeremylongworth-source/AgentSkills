# Troubleshooting

Use this guide when setup or validation fails.

## PowerShell Blocks Scripts

Symptom:

```text
running scripts is disabled on this system
```

Run the script with a process-local execution policy bypass:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\validate-skills.ps1
```

This does not change the machine's permanent execution policy.

## `gh` Is Installed but Not on PATH

Symptom:

```text
gh is not recognized
```

Check the common Windows install path:

```powershell
& 'C:\Program Files\GitHub CLI\gh.exe' --version
```

Pass the explicit path to the release check:

```powershell
.\scripts\release-check.ps1 -GhPath 'C:\Program Files\GitHub CLI\gh.exe'
```

## Windows `npx` MCP Servers Fail

Codex snippets use `npx.cmd` on Windows to avoid PowerShell execution-policy
issues with `.ps1` shims.

Claude Code on native Windows usually needs a command wrapper:

```powershell
claude mcp add context7 -- cmd /c npx -y @upstash/context7-mcp
```

Other hosts may prefer `npx` or a full executable path depending on how they
start subprocesses.

## MCP Config Does Not Load

The included MCP snippets are Codex TOML. Do not paste them directly into
Cursor, Claude Code, or Gemini CLI.

Translate:

- server name
- command
- args
- environment variables
- URL, when using HTTP transport

See [MCP preset examples](examples/mcp-presets.md).

## A Skill Does Not Trigger

Check:

- the skill is installed in the host's expected user or project directory
- the skill has a clear `description` in `SKILL.md`
- the prompt uses words that match the skill's scope
- the host has reloaded skills or restarted after installation

For direct testing, invoke the skill by name when the host supports it.

## A Skillset Install Looks Risky

Preview the install before writing to Codex home:

```powershell
.\scripts\install-skillset.ps1 frontend-product -DryRun
```

For isolated tests, point the install at a temporary Codex home:

```powershell
$tempHome = Join-Path $env:TEMP "agentskills-codex-home"
.\scripts\install-skillset.ps1 frontend-product -CodexHome $tempHome
```

## Release Check Fails on Local Paths

`release-check.ps1` scans for personal machine paths before publish. Replace
machine-specific paths with placeholders such as:

- `%USERPROFILE%`
- `$HOME`
- `/path/to/repo`
- `C:\path\to\repo`

Use exact local paths only in local notes that are not committed.
