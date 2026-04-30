# Install One Skill

Use this when you want one focused workflow without installing a full skillset.
`gh skill install` is a convenient path, not the only path. Hosts that support
local skill folders can also consume the same skill directory directly.

## Preview

Inspect the skill before installing:

```powershell
gh skill preview jeremylongworth-source/AgentSkills concise-technical-writing
```

## Install for a Host

Install the skill for Codex at user scope:

```powershell
gh skill install jeremylongworth-source/AgentSkills concise-technical-writing --agent codex --scope user --pin v0.1.1
```

Install the same skill for GitHub Copilot in the current repository:

```powershell
gh skill install jeremylongworth-source/AgentSkills concise-technical-writing --agent github-copilot --scope project --pin v0.1.1
```

Install for another host by changing `--agent`:

```powershell
gh skill install jeremylongworth-source/AgentSkills concise-technical-writing --agent cursor --scope user --pin v0.1.1
gh skill install jeremylongworth-source/AgentSkills concise-technical-writing --agent claude-code --scope user --pin v0.1.1
gh skill install jeremylongworth-source/AgentSkills concise-technical-writing --agent gemini-cli --scope user --pin v0.1.1
```

## Verify

Ask for a task that matches the skill:

```text
Use concise technical writing to tighten this PR description.
```

Expected behavior:

- The agent identifies `concise-technical-writing`.
- The agent reads the skill's `SKILL.md`.
- The output leads with the final concise text.

## When to Use a Skillset Instead

Use a skillset when the work spans multiple disciplines. For example, an HTML5
game launch usually needs game implementation, UI, browser QA, pricing,
analytics, and release-readiness skills.
