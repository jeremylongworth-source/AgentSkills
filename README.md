# AgentSkills

Portable agent skills, curated skillsets, MCP presets, and routing templates
for AI coding agents.

AgentSkills gives an agent reusable operating instructions for real work:
planning, implementation, research, testing, documentation, release, creator
operations, and security review. The core content is readable Markdown and
YAML; host-specific setup stays in adapters and setup guides.

Latest published release: `v0.2.2`. The default branch also contains an
unreleased development addition for local YouTube production.

## Start Here

| You need | Start with |
|---|---|
| One focused workflow | Install one skill with `gh skill install` |
| A complete workflow family | Install a curated skillset |
| Guidance for a new repository | Use `agentskills-project-onboarding` |
| Setup for a specific host | Read the [setup guides](docs/setup/README.md) |
| The full catalog and decision path | Open the [AgentSkills Wiki](https://github.com/jeremylongworth-source/AgentSkills/wiki) |

## Quick Install

### One skill

Preview a skill before installing it:

```powershell
gh skill preview jeremylongworth-source/AgentSkills game-threejs-development
```

Install a pinned release for Codex:

```powershell
gh skill install jeremylongworth-source/AgentSkills game-threejs-development --agent codex --scope user --pin v0.2.2
```

Change `--agent` and `--scope` for the host and install target you use. See
[compatibility](docs/compatibility.md) for the current host matrix.

### Curated skillset

Clone the repository, preview the local install, then install it:

```powershell
git clone https://github.com/jeremylongworth-source/AgentSkills.git
cd AgentSkills
.\scripts\install-skillset.ps1 game-dev -DryRun
.\scripts\install-skillset.ps1 game-dev
```

The PowerShell installer is a Codex adapter. For other hosts, use the
[skillset manifest](skillsets/game-dev.yaml) as a shopping list and follow the
relevant [host setup guide](docs/setup/README.md).

### New or unfamiliar repository

Start with `agentskills-project-onboarding`. It helps an agent inspect the
repository, choose the smallest useful skillset, plan routing, identify MCP
needs, and define verification steps before installation.

## Choose a Workflow

Use the smallest skillset that matches the job. These are the most common
starting points:

- `game-dev` for game design, implementation, assets, QA, and launch
- `frontend-product` for product shaping, UI quality, accessibility, analytics, and release readiness
- `engineering-delivery` for issue planning, PR review, regression, and release risk
- `backend-api` for API contracts, schemas, auth, service boundaries, and backend tests
- `devops-cloud-release` for deployment, CI, configuration, rollback, and production readiness
- `quality-testing` for unit, integration, E2E, accessibility, performance, and regression work
- `technical-documentation` for READMEs, API docs, release notes, migrations, and onboarding
- `agentops-evaluation` for benchmarks, scenarios, before/after reports, scoring, and prompt regression
- `skill-security-audit` for review-only install and publish security checks
- `creator-content-engine` for content strategy, scripts, calendars, captions, and repurposing
- `creator-brand-deals` for pitches, media kits, sponsorships, rights, and campaign recaps
- `creator-youtube-local-production` for human-reviewed local narrated video production

See the [full skillset catalog](https://github.com/jeremylongworth-source/AgentSkills/wiki/Skillset-Catalog) and the
[wiki decision guide](https://github.com/jeremylongworth-source/AgentSkills/wiki/Choose-a-Skillset)
for the complete list.

The current manifests are: `agentops-evaluation`, `ai-transformation-governance`,
`all`, `analytics-finance`, `backend-api`, `business-analysis`,
`creator-ai-production`, `creator-analytics-reporting`, `creator-brand-deals`,
`creator-business-ops`, `creator-community`, `creator-content-engine`,
`creator-monetization`, `creator-reputation-risk`,
`creator-youtube-local-production`, `data-analytics-bi`,
`devops-cloud-release`, `engineering-delivery`, `executive-command-center`,
`founder-fundraising-ir`, `frontend-product`, `game-dev`,
`html5-game-publishing`, `llm-skill-authoring`, `operating-cadence`,
`owner-operator-os`, `product-research`, `quality-testing`,
`research-validation`, `revenue-growth`, `sales-marketing`,
`skill-security-audit`, `support-success`, and `technical-documentation`.

## What Ships

- Atomic skills under [`skills/`](skills/)
- Curated manifests under [`skillsets/`](skillsets/)
- MCP presets and server snippets under [`mcp/`](mcp/)
- Routing templates under [`agents/`](agents/)
- Host and context starters under [`templates/`](templates/)
- Install, validation, listing, and release helpers under [`scripts/`](scripts/)
- Scenario tests and expected routing under [`tests/`](tests/)
- Setup, authoring, evaluation, security, and release docs under [`docs/`](docs/)

## Development Validation

The current default-branch development scope validates:

- 167 skill files
- 34 skillsets
- 124 routing scenarios
- all skillset install dry-runs
- fresh Codex home smoke tests for `game-dev` and `all`
- docs consistency, secret, and local-path scans

Run the full local gate before publishing:

```powershell
.\scripts\release-check.ps1
```

Useful focused checks:

```powershell
python scripts\validate-skill-files.py --repo-root .
python scripts\validate-skillsets.py --repo-root .
python scripts\validate-scenarios.py --repo-root .
python scripts\validate-docs.py --repo-root .
gh skill publish --dry-run
```

## How to Work Safely

Skills are instructions and may include scripts, references, and MCP
configuration. Preview them before installation. Keep public publishing,
account changes, production changes, customer communication, legal or
financial decisions, and other high-impact actions human-reviewed unless you
have explicitly approved the action.

AgentSkills favors portable workflow logic, explicit output contracts,
scenario tests, and reviewable safety boundaries. Read
[vendor neutrality](docs/vendor-neutrality.md) before adding host-specific
behavior.

## Repository Guides

- [Setup guides](docs/setup/README.md)
- [Examples](docs/examples/README.md)
- [Compatibility](docs/compatibility.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Authoring guide](docs/authoring-guide.md)
- [Bundle authoring](docs/bundle-authoring-guide.md)
- [Evaluation](docs/evaluation/README.md)
- [Release process](docs/release-process.md)
- [Changelog](CHANGELOG.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)

The [AgentSkills Wiki](https://github.com/jeremylongworth-source/AgentSkills/wiki)
is the long-form orientation layer for choosing workflows, installing across
hosts, understanding portability, and navigating the full catalog.

## Contributing

Keep changes small, reviewable, and vendor-neutral unless they belong in a
host adapter. Good contributions include focused skills, realistic scenario
tests, setup improvements, validation checks, and bundle proposals with clear
users, artifacts, and safety boundaries.

Run `.\scripts\release-check.ps1` before opening a pull request. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the contribution contract.

## License and Support

AgentSkills is available under the [MIT License](LICENSE).

If AgentSkills is useful to your workflow, [sponsor the project](https://github.com/sponsors/jeremylongworth-source)
or [star the repository](https://github.com/jeremylongworth-source/AgentSkills).
