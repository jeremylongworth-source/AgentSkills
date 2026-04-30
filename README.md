# AgentSkills

Portable Agent Skills, skillsets, MCP presets, and routing templates for AI coding agents.

## Why this exists

Most AI coding agents improve when they are given reusable domain-specific operating instructions. AgentSkills packages those instructions into installable skillsets for Codex, GitHub Copilot, Cursor, Claude Code, Gemini CLI, and related tools.

## Quick install

```powershell
.\scripts\install-skillset.ps1 game-dev
```

## Available skillsets

| Skillset | Best for |
|---|---|
| `game-dev` | Game design, implementation, QA, launch |
| `html5-game-publishing` | Phaser, Three.js, itch.io, browser QA |
| `sales-marketing` | GTM, positioning, paid media, lifecycle |
| `frontend-product` | React, Tailwind, UX, accessibility |
| `research-validation` | Competitive research, experiments, analytics |
| `llm-skill-authoring` | Creating and validating new agent skills |

## Who this is for

- Developers using Codex, GitHub Copilot, Cursor, Claude Code, Gemini CLI, or similar AI coding agents
- Builders who want reusable AI-agent workflows instead of rewriting the same instructions for every project
- Teams experimenting with MCP-backed specialist agents
- Game, frontend, product, marketing, and research workflows

## What is included

- Atomic skills under `skills/`
- Installable skillsets under `skillsets/`
- MCP presets for tool-aware workflows
- `AGENTS.md` routing templates
- Validation scripts
- Scenario tests
- Documentation for creating and extending skillsets

## Example use cases

Use AgentSkills when you want an AI coding agent to behave more like a specialist:

- Build and QA an HTML5 game
- Plan and implement a Three.js interactive page
- Prepare a product launch workflow
- Run structured competitive research
- Create a repeatable frontend/product implementation workflow
- Author new reusable agent skills

## Repository structure

```text
AgentSkills/
├─ skills/
├─ skillsets/
├─ mcp/
├─ agents/
├─ scripts/
├─ tests/
└─ docs/
```

## Getting started

1. Clone the repository.

```powershell
git clone https://github.com/jeremylongworth-source/AgentSkills.git
cd AgentSkills
```

2. Install a skillset.

```powershell
.\scripts\install-skillset.ps1 game-dev
```

3. Review the installed instructions before using them with your agent.

4. Start your coding agent with the relevant skillset active.

## Suggested first skillset

For game development or interactive browser work, start with:

```powershell
.\scripts\install-skillset.ps1 game-dev
```

For browser game publishing workflows, use:

```powershell
.\scripts\install-skillset.ps1 html5-game-publishing
```

## Supported agent workflows

AgentSkills is intended for workflows involving:

- OpenAI Codex
- GitHub Copilot
- Cursor
- Claude Code
- Gemini CLI
- MCP-enabled agent systems
- Other coding agents that can read project instructions and reusable skill files

Exact host support may vary depending on how each tool loads instructions, skills, and workspace context.

## Roadmap

Planned improvements include:

- More install examples for Windows, macOS, and Linux
- More host-specific setup guides
- Additional skillsets for game development, frontend apps, marketing, research, and product workflows
- More MCP presets
- Validation improvements
- Example projects showing before and after agent behavior

## Contributing

Contributions are welcome.

Good first contributions include:

- Adding setup instructions for your preferred coding agent
- Improving install scripts
- Adding examples
- Adding tests
- Proposing new skillsets
- Improving existing skill instructions

## License

MIT

## Star the repo

If AgentSkills helps your AI development workflow, star the repo so other builders can find it.
