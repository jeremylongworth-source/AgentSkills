# AgentSkills

Portable Agent Skills, skillsets, MCP presets, and routing templates for AI coding agents.

Reusable AI-agent workflows for builders, operators, and executive teams.

## Why this exists

Most AI coding agents improve when they are given reusable domain-specific operating instructions. AgentSkills packages those instructions into installable skillsets for Codex, GitHub Copilot, Cursor, Claude Code, Gemini CLI, and related tools.

The portable core is vendor-neutral Markdown skills, YAML skillsets, MCP
presets, and routing templates. Host-specific setup lives at the edges in setup
guides, templates, and adapter scripts.

AgentSkills prioritizes clear output contracts, scenario tests, and reviewable
safety boundaries over bulk-generated skill lists.

## Quick install

Install a discoverable skill with GitHub CLI:

```powershell
gh skill install jeremylongworth-source/AgentSkills
```

Pin a specific skill to the current release:

```powershell
gh skill install jeremylongworth-source/AgentSkills game-threejs-development --pin v0.1.1
```

Install a local Codex skillset from a cloned repo:

```powershell
.\scripts\install-skillset.ps1 game-dev
```

## Available skillsets

| Skillset | Best for |
|---|---|
| `game-dev` | Game design, implementation, QA, launch |
| `html5-game-publishing` | Phaser, Three.js, itch.io, browser QA |
| `executive-command-center` | Executive briefs, decisions, risks, action tracking |
| `founder-fundraising-ir` | Investor updates, fundraising narrative, data rooms, diligence |
| `ai-transformation-governance` | AI use cases, pilots, governance, vendors, adoption |
| `owner-operator-os` | Owner dashboards, cash-flow triage, pricing, vendors, ops |
| `operating-cadence` | Leadership meetings, OKRs, decisions, MBRs, follow-up |
| `engineering-delivery` | Issue planning, PR review, regression, release risk |
| `support-success` | Support triage, safe replies, escalations, KB drafts |
| `revenue-growth` | Account research, approved outreach, campaigns, funnel |
| `sales-marketing` | GTM, positioning, paid media, lifecycle |
| `frontend-product` | React, Tailwind, UX, accessibility |
| `product-research` | Feedback synthesis, PRDs, experiments, analytics |
| `analytics-finance` | KPI narratives, variance commentary, close checklists |
| `research-validation` | Competitive research, experiments, analytics |
| `llm-skill-authoring` | Creating and validating new agent skills |
| `agentops-evaluation` | Skill benchmarks, scenarios, before/after reports, scoring |
| `skill-security-audit` | Skill threat models, prompt-injection review, safe install checks |
| `technical-documentation` | READMEs, API docs, release notes, changelogs, migrations |
| `backend-api` | API contracts, schemas, auth flows, service boundaries, backend tests |
| `devops-cloud-release` | Deployment, CI, containers, config, rollback, cloud cost, readiness |
| `quality-testing` | Unit, integration, E2E, bug reproduction, QA, accessibility, performance |
| `data-analytics-bi` | Metrics, dashboards, funnels, cohorts, retention, SQL plans, experiments |
| `creator-content-engine` | Content pillars, hooks, scripts, calendars, captions, repurposing |
| `creator-brand-deals` | Media kits, pitches, sponsorship packages, rate cards, recaps, renewals |
| `creator-analytics-reporting` | Sponsor reports, content analytics, affiliate reporting, dashboards, experiments |
| `creator-monetization` | Offer ladders, owned-product launches, pricing, affiliates, dashboards |
| `creator-business-ops` | Weekly ops, sponsor pipeline, invoices, production handoffs, asset checks |
| `creator-community` | Comment and DM triage, moderation briefs, feedback, polls, engagement plans |
| `creator-reputation-risk` | Disclosure, rights, AI-labeling, brand-safety, platform-policy, response review |
| `creator-ai-production` | AI media prompt briefs, synthetic characters, provenance, disclosure, review gates |
| `all` | Every included skill and MCP preset |

## Who this is for

- Developers using Codex, GitHub Copilot, Cursor, Claude Code, Gemini CLI, or similar AI coding agents
- Builders who want reusable AI-agent workflows instead of rewriting the same instructions for every project
- Teams experimenting with MCP-backed specialist agents
- Skill authors and maintainers who want scenario-tested, reviewable skills
- Game, engineering, frontend, support, product, marketing, and research workflows
- Creator, influencer, and founder-led content workflows

## What is included

- Atomic skills under `skills/`
- Installable skillsets under `skillsets/`
- MCP presets for tool-aware workflows
- `AGENTS.md` routing templates
- Host starter templates under `templates/`
- Host-specific setup adapters and docs
- Validation scripts
- Scenario tests
- Evaluation templates for before/after reports, quality rubrics, and security
  reviews
- Documentation and examples for setup, use, and skillset authoring

## Validation Status

Current v0.2 development gate:

- 158 validated skill files
- 32 validated skillsets
- 113 routing scenarios
- all skillset install dry-runs pass
- fresh Codex home install smoke passes for `game-dev` and `all`
- `gh skill publish --dry-run` returns `ok`

## Example use cases

Use AgentSkills when you want an AI coding agent to behave more like a specialist:

- Build and QA an HTML5 game
- Prepare a weekly executive brief and decision memo
- Draft investor updates and fundraising readiness artifacts
- Map AI use cases and pilot governance before rollout
- Create a small-business owner dashboard and cash action list
- Run a weekly leadership cadence with decisions, risks, and actions
- Turn engineering issues into scoped plans and release checks
- Plan and implement a Three.js interactive page
- Prepare a product launch workflow
- Synthesize product feedback into a reviewed PRD
- Triage support tickets and draft reviewed customer replies
- Draft KPI narratives and variance commentary for review
- Run structured competitive research
- Create a repeatable frontend/product implementation workflow
- Author new reusable agent skills
- Benchmark, score, and improve skills with before/after reports
- Audit skills before installing or publishing them
- Improve READMEs, API docs, release notes, and migration guides
- Design backend APIs, schemas, auth flows, and service boundaries
- Plan deployments, CI workflows, rollback, and production readiness
- Build focused test plans, QA matrices, bug reproductions, and release gates
- Turn analytics questions into metric definitions, dashboards, and read-only analysis plans
- Build creator content pillars, hooks, scripts, calendars, captions, and repurposing plans
- Prepare creator media kits, sponsor pitches, campaign proposals, rate cards, and recap reports
- Turn creator analytics exports into sponsor reports, content learnings, affiliate reports, and dashboard specs
- Map creator monetization options into offer ladders, launch plans, pricing reviews, and owned-revenue dashboards
- Run creator business ops reviews for sponsor pipeline, invoice readiness, production handoffs, and asset systems
- Triage creator comments and DMs into reviewed replies, moderation briefs, feedback themes, polls, and engagement plans
- Review creator reputation risks for disclosures, rights, AI labeling, brand safety, platform policy, and public responses
- Plan AI-assisted creator production with prompt packs, synthetic character bibles, provenance notes, rights checks, and human-review gates

## Repository structure

```text
AgentSkills/
|-- skills/
|-- skillsets/
|-- mcp/
|-- agents/
|-- templates/
|-- scripts/
|-- tests/
`-- docs/
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

## Host setup guides

Use the host-specific guides when installing AgentSkills into a particular
coding agent:

- [Codex](docs/setup/codex.md)
- [GitHub Copilot](docs/setup/github-copilot.md)
- [Cursor](docs/setup/cursor.md)
- [Claude Code](docs/setup/claude-code.md)
- [Gemini CLI](docs/setup/gemini-cli.md)

Start with [setup guides](docs/setup/README.md) if you are choosing between
`gh skill install`, local skillset scripts, project instruction files, and MCP
presets.

See [examples](docs/examples/README.md) for single-skill installs, skillset
installs, MCP preset usage, and before/after agent behavior.

See [compatibility](docs/compatibility.md) for host paths and MCP formats, and
[troubleshooting](docs/troubleshooting.md) for common setup failures.

For new multi-skill bundles, see the
[bundle authoring guide](docs/bundle-authoring-guide.md).
For the first expanded business bundle, see the
[support success brief](docs/bundles/support-success.md).
For skill and bundle evaluation workflows, see the
[agentops evaluation brief](docs/bundles/agentops-evaluation.md).
For skill install and publish review workflows, see the
[skill security audit brief](docs/bundles/skill-security-audit.md).
For documentation workflows, see the
[technical documentation brief](docs/bundles/technical-documentation.md).
For backend and API design workflows, see the
[backend API brief](docs/bundles/backend-api.md).
For DevOps, cloud, and release workflows, see the
[DevOps cloud release brief](docs/bundles/devops-cloud-release.md).
For quality and testing workflows, see the
[quality testing brief](docs/bundles/quality-testing.md).
For data analytics and BI workflows, see the
[data analytics BI brief](docs/bundles/data-analytics-bi.md).
For creator content workflows, see the
[creator content engine brief](docs/bundles/creator-content-engine.md).
For creator sponsorship workflows, see the
[creator brand deals brief](docs/bundles/creator-brand-deals.md).
For creator analytics and reporting workflows, see the
[creator analytics reporting brief](docs/bundles/creator-analytics-reporting.md).
For creator monetization workflows, see the
[creator monetization brief](docs/bundles/creator-monetization.md).
For creator business operations workflows, see the
[creator business ops brief](docs/bundles/creator-business-ops.md).
For creator community workflows, see the
[creator community brief](docs/bundles/creator-community.md).
For creator reputation risk workflows, see the
[creator reputation risk brief](docs/bundles/creator-reputation-risk.md).
For creator AI production workflows, see the
[creator AI production brief](docs/bundles/creator-ai-production.md).
For portability rules, see [vendor neutrality](docs/vendor-neutrality.md).
For expansion planning, see the
[scope broadening roadmap](docs/scope-broadening-roadmap.md).
For mapping new bundle proposals, see the
[bundle expansion map](docs/bundle-expansion-map.md).
For current scope decisions, see
[bundle expansion decisions](docs/bundle-expansion-decisions.md).
For the executive bundle expansion, see
[executive skillsets roadmap](docs/executive-skillsets-roadmap.md).
For the creator and influencer expansion, see
[creator skillsets roadmap](docs/creator-skillsets-roadmap.md).
For the active research and development backlog, see the
[roadmap research plan](docs/roadmap-research-plan.md).
For skill proof, before/after checks, and security review templates, see
[evaluation](docs/evaluation/README.md).
For v0.2 promotion checks, see the
[alpha validation plan](docs/evaluation/v0.2-alpha-validation-plan.md).
For validation status, see the
[v0.2 validation tracker](docs/evaluation/v0.2-validation-tracker.md).
For v0.2 release-candidate scope and prerelease decision support, see
[v0.2 release candidate checklist](docs/release-candidate-v0.2.md).
For maintainer handoff before tagging, see the
[v0.2 release handoff](docs/v0.2-release-handoff.md).
For the path from prerelease to normal release, see the
[stable release plan](docs/stable-release-plan.md).
For release details, see
[v0.2.1 release notes](docs/release-notes/v0.2.1.md).

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

- Forward-testing for AgentOps evaluation and skill security audit bundles
- More forward-test reports and expanded vertical bundles
- Additional executive, owner-operator, customer success, and vertical bundles
- Creator platform expansion, live/event, and additional vertical bundles
- More scenario tests, before/after reports, and security review examples
- More MCP presets and host setup examples where they improve portability

## Contributing

Contributions are welcome.

Good first contributions include:

- Adding setup instructions for your preferred coding agent
- Improving install scripts
- Adding examples
- Adding tests
- Proposing new skillsets
- Improving existing skill instructions

See [Contributing](CONTRIBUTING.md), [Changelog](CHANGELOG.md),
[Security](SECURITY.md), and [Code of Conduct](CODE_OF_CONDUCT.md) for
contribution, release, vulnerability reporting, and community guidance.

## License

MIT

## Star the repo

If AgentSkills helps your AI development workflow, star the repo so other builders can find it.
