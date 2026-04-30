# Real-Input Packet: BACKEND-001

Bundle: `backend-api`
Scenario: Review internal script interfaces and manifest contracts.
Reviewer: AgentSkills maintainer
Date collected: 2026-04-30
Public-safe: yes
Storage: committed

## Source Context

AgentSkills does not expose a network API, but it does have internal command
interfaces and data contracts used by installers and validators. Skillset
manifests, MCP presets, server snippets, route scenarios, and release scripts
act as the repo's backend-like integration surface.

The validation task is to check whether `backend-api` can produce a useful API
contract and service-boundary review from these local script interfaces.

## User Prompt

> Review the internal command and manifest contracts for AgentSkills. Treat
> skillset YAML, MCP preset TOML, server snippets, scenario routing, install
> scripts, and validation scripts as the integration surface. Produce an API
> contract review with inputs, outputs, error behavior, boundaries, test
> coverage, compatibility risks, and follow-up recommendations. Do not rewrite
> the scripts unless a concrete blocker appears.

## Source Material

- `docs/bundles/backend-api.md`
- `skillsets/backend-api.yaml`
- `scripts/install-skillset.py`
- `scripts/install-skillset.ps1`
- `scripts/validate-skillsets.py`
- `scripts/validate-scenarios.py`
- `scripts/validate-docs.py`
- `scripts/list-skillsets.ps1`
- `skillsets/*.yaml`
- `mcp/presets/*.toml`
- `mcp/servers/*.toml`
- `tests/expected-routing.yaml`
- `tests/scenarios/backend-api-contract.md`
- `tests/scenarios/backend-service-boundary.md`

## Expected Artifact

- Internal API/contract review
- Service boundary memo
- Compatibility and error-behavior notes
- Backend test coverage gaps
- Keep/revise/defer recommendation

## Acceptance Criteria

- Names the script commands, manifest fields, and config formats as contracts.
- Distinguishes portable core contracts from Codex adapter behavior.
- Identifies duplicate parsing or drift risk without forcing a refactor.
- Uses existing validation as evidence.
- Does not invent network APIs, databases, auth systems, or production traffic.

## High-Risk Boundaries

- Do not run non-dry-run install actions.
- Do not change user home config, credentials, or MCP settings.
- Do not claim this validates real backend APIs, databases, auth, or production
  services.

## Baseline Setup

Skillset disabled or closest prior bundle: generic script review without
`backend-api`
Notes: baseline may inspect implementation but may not name contracts,
boundaries, error behavior, or compatibility risks.

## Skill-Enabled Setup

Skillset: `backend-api`
Relevant skills expected:

- `api-contract-design`
- `service-boundary-design`
- `error-handling-contracts`
- `api-doc-writing`
- `backend-test-plan`
- `skill-threat-model`
- `concise-technical-writing`

Notes: review local scripts and manifest formats only.

## Reviewer Notes

What would make the output usable?

- Clear contract map for installers, validators, manifests, and MCP snippets.
- Specific compatibility risks and tests.
- No unnecessary refactor.

What common mistakes should be caught?

- Treating the PowerShell installer as the portable core.
- Ignoring duplicate manifest parsing across scripts.
- Ignoring dry-run and error-message behavior as part of the contract.

What would block release promotion?

- Unknown manifest references, broken dry-runs, unstable command inputs,
  destructive non-dry-run behavior, or docs that misrepresent host boundaries.
