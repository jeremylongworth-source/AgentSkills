# AgentSkills

Portable Codex skillsets for installing domain-specific agent capabilities.

This repo stores atomic skills under `skills/` and installable bundles under `skillsets/`. A user can install a single themed skillset, merge MCP server presets, and apply account-level routing instructions.

## Layout

```text
skills/       Atomic Codex skills. Each folder contains SKILL.md, agents/openai.yaml, and references/.
skillsets/    Bundle manifests that list skills, MCP presets, and routing templates.
mcp/          Reusable MCP server config snippets and presets.
agents/       Account-level AGENTS.md routing templates.
scripts/      Install and validation helpers.
tests/        Scenario prompts for evaluating routing and skill behavior.
docs/         Authoring and operating guidance.
```

## Install A Skillset

From PowerShell:

```powershell
.\scripts\install-skillset.ps1 game-dev
```

By default this copies skills into `$env:USERPROFILE\.codex\skills`, appends MCP config snippets to `$env:USERPROFILE\.codex\config.toml` if they are missing, and appends routing guidance to `$env:USERPROFILE\.codex\AGENTS.md`.

Validate the repo:

```powershell
.\scripts\validate-skills.ps1
```

## Skillsets

- `game-dev`: game design, implementation, assets, audio, UI, playtesting, publishing, QA, launch.
- `html5-game-publishing`: Phaser, Three.js, sprite design, itch.io publishing, browser QA.
- `sales-marketing`: GTM, positioning, pipeline, outbound, paid media, lifecycle, analytics, ABM.
- `frontend-product`: brainstorming, React/Next performance, Tailwind, visual audit, accessibility, analytics, QA, release.
- `research-validation`: customer research, competitive research, experiments, product analytics.
- `llm-skill-authoring`: skill creation, evaluation, iteration, concise writing, OpenAI docs routing.
- `all`: everything in the repo.

## Quality Bar

Each skill should have:

- precise frontmatter `description`
- concise `SKILL.md`
- `agents/openai.yaml`
- at least one reference/checklist
- output contract or deliverable shape
- freshness rule when platform, legal, model, or API guidance changes quickly
- no scaffold TODOs

