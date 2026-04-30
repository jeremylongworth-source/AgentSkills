# GitHub Copilot Setup

GitHub Copilot supports agent skills for Copilot cloud agent, GitHub Copilot
CLI, and agent mode in Visual Studio Code. Use `gh skill install` to place
AgentSkills in the correct Copilot directory.

## Install One Skill

Preview the skill:

```powershell
gh skill preview jeremylongworth-source/AgentSkills concise-technical-writing
```

Install it for the current repository:

```powershell
gh skill install jeremylongworth-source/AgentSkills concise-technical-writing --agent github-copilot --scope project --pin v0.1.1
```

Install it for your user account instead:

```powershell
gh skill install jeremylongworth-source/AgentSkills concise-technical-writing --agent github-copilot --scope user --pin v0.1.1
```

You can also browse this repository's skills interactively:

```powershell
gh skill install jeremylongworth-source/AgentSkills --agent github-copilot --scope project
```

## Add Project Instructions

For broad repository guidance, create `.github/copilot-instructions.md`.

For agent routing, add an `AGENTS.md` file. Copilot uses the nearest
`AGENTS.md` file in the repository tree when working as an agent.

Recommended starting point:

1. Choose a routing template from `agents/`.
2. Copy it to the repository root as `AGENTS.md`.
3. Add project-specific build, test, and review commands above or below the
   AgentSkills routing section.

Use `.github/instructions/*.instructions.md` only when instructions should
apply to specific paths.

## Verify

Ask Copilot for a task that matches the installed skill description. Copilot
decides when to load a skill based on the prompt and the `description` field in
`SKILL.md`.

For custom instructions, check the response references when your Copilot
surface shows them, or ask a repository-specific question that should depend on
the new instructions.

## References

- [GitHub Copilot agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- [GitHub Copilot repository custom instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)
- [GitHub CLI `gh skill install`](https://cli.github.com/manual/gh_skill_install)
