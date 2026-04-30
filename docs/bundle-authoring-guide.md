# Bundle Authoring Guide

Use bundles when a user goal needs several skills to work together. In this
repository, bundles are skillset manifests under `skillsets/`.

Bundles should be vendor-neutral by default. Put host-specific installation
paths, commands, and config formats in setup guides, templates, or adapter
scripts.

For the current expansion sequence, see
[scope broadening roadmap](scope-broadening-roadmap.md).

Use [the bundle brief template](../templates/bundles/bundle-brief.md) before
adding a new bundle. Completed bundle briefs can live under `docs/bundles/`.
When reviewing a large expansion document, use the
[bundle expansion map](bundle-expansion-map.md) and
`templates/bundles/expansion-proposal-map.md`.

## When to Add a Bundle

Add a bundle when:

- a recurring workflow spans multiple atomic skills
- users need a clear install target such as `game-dev` or `sales-marketing`
- the skills share routing guidance, MCP needs, or validation scenarios

Do not add a bundle for one narrow task. Add or improve an atomic skill instead.

## Manifest Shape

Current skillset manifests use this shape:

```yaml
name: example-bundle
description: Short description of the workflow this bundle supports.
skills:
  - product-brainstorming-planning
  - qa-test-strategy
mcp_presets:
  - docs-research
agents_file: agents/AGENTS.full.md
```

Required fields:

- `name`: must match the filename without `.yaml`
- `description`: one sentence that explains who should install the bundle
- `skills`: ordered list of existing skill directories

Optional fields:

- `mcp_presets`: preset names from `mcp/presets/`
- `agents_file`: routing template from `agents/`

Future metadata such as `category`, `hosts`, `recommended_for`, or `includes`
can be added after the tooling and docs agree on the schema.

Do not add host-specific metadata until there is a concrete consumer for it.
Prefer a small, portable manifest and host-specific docs at the edge.

## Naming

Use lowercase letters, digits, and hyphens.

Good names:

- `backend-api-development`
- `data-analytics-engineering`
- `devops-release-engineering`

Avoid names that are too broad, overloaded, or tied to one company.

## Skill Selection

Order skills by how the agent should usually route work:

1. orchestration or planning skills
2. domain implementation skills
3. evidence, research, or analytics skills
4. QA, accessibility, release, and writing skills

Keep each bundle coherent. A bundle should answer "what job does this install
prepare the agent to do?"

## MCP Presets

Use existing presets when possible:

- `docs-research` for current documentation and API research
- `browser-qa` for browser screenshots and UI inspection
- `full` for broad workflows that need both

If a new preset is needed:

1. add `mcp/presets/<name>.toml`
2. list servers with `servers = ["server-name"]`
3. add each server snippet under `mcp/servers/`
4. run validation

The Codex installer reads preset server lists dynamically from
`mcp/presets/*.toml`, so new presets do not require installer code changes.
Other hosts should translate the same preset server list into their own MCP
format.

## Routing Templates

Reuse existing routing templates unless a bundle has distinct routing rules:

- `agents/AGENTS.full.md` for broad product, frontend, research, and authoring
  bundles
- `agents/AGENTS.game-dev.md` for game and browser-game bundles
- `agents/AGENTS.sales-marketing.md` for revenue and GTM bundles

Add a new `agents/AGENTS.<bundle>.md` only when the bundle needs routing that
would be noisy or misleading for other bundles.

If a host does not read `AGENTS.md`, provide a thin host wrapper such as
`CLAUDE.md`, `GEMINI.md`, or a Cursor rule that points back to the same portable
routing guidance.

## Examples and Docs

After adding a bundle:

- add it to the README skillset table
- add or update a bundle brief under `docs/bundles/`
- add install examples when it represents a new workflow category
- update `docs/compatibility.md` only if host behavior changes
- update `docs/examples/` when the bundle needs a new scenario
- keep vendor-specific instructions out of the manifest when docs or templates
  can carry them

List current bundles:

```powershell
.\scripts\list-skillsets.ps1
```

Generate a Markdown table:

```powershell
.\scripts\list-skillsets.ps1 -Markdown
```

## Validation

Run:

```powershell
.\scripts\validate-skills.ps1
.\scripts\install-skillset.ps1 example-bundle -DryRun
.\scripts\release-check.ps1
```

Validation checks that manifest skills, MCP presets, preset server snippets,
and agents files exist.

## Acceptance Criteria

A new bundle is ready when:

- the manifest name matches the filename
- every listed skill exists and has a valid `SKILL.md`
- every MCP preset and server snippet exists
- the routing template exists and matches the bundle's workflow
- `install-skillset.ps1 <bundle> -DryRun` shows the expected install plan
- `release-check.ps1` passes
