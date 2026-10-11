# Global Foundation Bundle Brief

## Problem

Installing broad domain bundles globally exposes unrelated workflows in every
repository and can accumulate routing instructions and MCP registrations.

## Target User

Maintainers working across multiple repositories who need a small, durable
personal set of planning, review, validation, and skill-authoring workflows.

## Included Skills

The [manifest](../../skillsets/global-foundation.yaml) installs 13 portable
AgentSkills workflows. Codex-managed `openai-docs` and `skill-creator` complete
the 15-skill foundation; this bundle does not copy or replace managed skills.

For frequent skill-authoring work, optionally add `skill-benchmark-design`,
`before-after-evaluation`, `skill-output-scoring`, and
`skill-token-overhead-review`. They are an explicit personal extension, not
required dependencies. The `agentops-evaluation` manifest includes these four
and five skills already in the foundation; installing both remains 17 unique
custom skills.

## Context Files

- Global `AGENTS.md`: universal execution and authority contract.
- Repository `AGENTS.md`: project truth, validation and review boundaries.
- Repository skills and references: focused procedures and domain knowledge.
- Task prompt: current objective, constraints and acceptance criteria.

## Safety Rules

- Never append domain routing to global `AGENTS.md` during installation.
- Preserve managed system skills and unrelated configuration.
- Install skills only by default; MCP setup and project routing are opt-in.
- Back up existing installations before pruning; do not infer project targets.
- Use `all` only for explicit full-catalog development or testing.

## Pilot Metrics

- Number of custom globally discoverable skills.
- Unrelated skill activations in representative repository tasks.
- Repeated installation preserves global instructions and configuration.

## Acceptance Criteria

- User installation provides exactly the 13 manifest skills in a fresh home.
- No global `AGENTS.md` or MCP configuration is created or changed by default.
- Project installation writes skills under `.agents/skills` in the target repo.
- Routing is available only through an explicit project-scope option.
- Dry runs have no filesystem side effects; invalid input fails before copying.
- The optional evaluation extension results in 17 unique custom skills.
