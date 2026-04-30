# Before/After Report: backend-api BACKEND-001

Date: 2026-04-30
Reviewer: Codex
Skill or bundle: `backend-api`
Packet: `BACKEND-001`

Source material:

- `docs/evaluation/packets/BACKEND-001-script-interface-contract.md`
- `docs/bundles/backend-api.md`
- `skillsets/backend-api.yaml`
- `scripts/install-skillset.py`
- `scripts/install-skillset.ps1`
- `scripts/validate-skillsets.py`
- `scripts/validate-scenarios.py`
- `scripts/validate-docs.py`
- `scripts/list-skillsets.ps1`
- `mcp/presets/*.toml`
- `mcp/servers/*.toml`
- `tests/expected-routing.yaml`

## Decision

Decision: keep as alpha

Reason: the bundle can review internal command/data contracts and produce a
useful boundary memo without pretending the repo has a production web API. It
still needs real application/API packets before promotion because this packet
covers script interfaces, not deployed backend services.

## Target Artifact

Artifact expected: internal API contract review and service-boundary memo.
Audience: maintainers changing installer, validator, skillset, MCP, or routing
interfaces.
High-risk boundaries: no non-dry-run install, no user-home config changes, no
claims about production APIs, auth, databases, or traffic.

## Acceptance Criteria

- Identify command interfaces, manifest fields, and config formats.
- Separate portable core contracts from Codex adapter behavior.
- Name error behavior, compatibility risks, and backend-style tests.
- Avoid unnecessary refactors.

## Baseline Result

Setup: generic script review without the `backend-api` workflow.

Output summary: likely to read the scripts and spot implementation details, but
less likely to document the manifest and command behavior as contracts.

What worked: script inputs and validation behavior are visible in local files.

What failed: baseline review can miss that skillset YAML, MCP presets, server
snippets, route scenarios, and installer arguments are external-facing
contracts for maintainers and host adapters.

Safety issues: low to medium risk of treating the Codex installer as the whole
portable system or making a refactor larger than the evidence justifies.

Reviewer edits required: moderate.

## Skill-Enabled Result

Setup: `BACKEND-001` reviewed through the `backend-api` bundle.

Output summary: the review maps the repo's internal integration surface:

- Skillset YAML fields: `name`, `description`, `skills`, `mcp_presets`,
  `agents_file`
- MCP preset contract: `servers = [...]` in TOML
- MCP server snippet contract: Codex TOML server blocks
- Installer command contract: `--skillset`, `--repo-root`, `--codex-home`,
  `--dry-run`
- Release/validation contract: validators fail with explicit messages and
  release-check composes them into one gate
- Routing contract: scenario files must match `tests/expected-routing.yaml`

What improved: the bundle produced a boundary view and named compatibility
risks instead of only reviewing code mechanics.

What regressed: no regression found. The report intentionally avoids refactoring
duplicate parsing logic because validation is green and the drift risk is
manageable at alpha scale.

Safety issues: no blocker found.

Reviewer edits required: low to moderate.

## Contract Map

| Contract | Producer | Consumer | Current evidence |
|---|---|---|---|
| Skillset manifest YAML | maintainers | validators, installer, list script | validated across 32 skillsets |
| Skill folder names | maintainers | manifests and installer | validated across 158 skills |
| MCP preset TOML | maintainers | installer parser | release-check dry-runs all presets used by skillsets |
| MCP server snippet TOML | maintainers | Codex config append path | snippet existence validated through presets |
| Scenario routing files | maintainers | route validator | 113 scenarios validated |
| Installer dry-run output | installer | maintainers/users | release-check runs every skillset dry-run |
| Publish dry-run | GitHub CLI | release owner | `gh skill publish --dry-run` returns `ok` |

## Compatibility Risks

- Manifest parsing logic exists in more than one script; future format changes
  should update installer and validators together.
- MCP server snippets are Codex TOML adapters; other hosts need translated
  config formats.
- The PowerShell installer is a Codex adapter, not the portable core.
- Dry-run validation covers command shape but does not prove a real fresh-home
  install.

## Score

| Criterion | Baseline | Skill-enabled | Notes |
|---|---:|---:|---|
| Trigger fit | 2 | 3 | Script interface and manifest review maps to API contract and service boundary work. |
| Artifact usefulness | 2 | 3 | Produces a contract map, boundary notes, and compatibility risks. |
| Correctness and evidence | 1 | 3 | Uses current validators, manifests, and release-check output. |
| Procedural value | 1 | 3 | Reviews inputs, outputs, errors, consumers, and tests as contracts. |
| Safety boundaries | 2 | 3 | Avoids non-dry-run install and production API claims. |
| Context efficiency | 2 | 2 | Reads several scripts because the contract is spread across repo tools. |
| Validation behavior | 2 | 3 | Ties contract health to existing validators and release-check. |
| Vendor neutrality | 2 | 3 | Separates portable Markdown/YAML/TOML core from Codex adapters. |
| Maintainability | 2 | 3 | Names drift risk without adding a premature abstraction. |

## Follow-Up Changes

- Keep `backend-api` in v0.2 alpha.
- Add a real API contract packet from an application repo before promotion.
- If manifest syntax expands, update installer and validator parsers in the
  same change.
- Add a fresh-home install test before treating installer behavior as proven.

## Evidence Links

- `scripts/install-skillset.py`
- `scripts/validate-skillsets.py`
- `scripts/validate-scenarios.py`
- `docs/bundles/backend-api.md`
- `skillsets/backend-api.yaml`
