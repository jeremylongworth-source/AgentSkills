# Skill Security Review: local installer and MCP snippets SECURITY-002

Date: 2026-04-30
Reviewer: Codex
Source: local install scripts and MCP snippets
Version or commit: current workspace
Install path: repo-local scripts and `mcp/`

## Summary

Recommendation: approve with changes
Risk level: medium
Reason: the PowerShell/Python installer has a dry-run path, checks manifest
references, copies only declared skill folders, and appends MCP/AGENTS config
without launching servers. The meaningful risk is that package-based MCP server
snippets use `npx`, which can download and execute third-party package code when
the host starts the server. That risk is acceptable for alpha after documenting
review and pinning guidance.

## Scope

Reviewed files:

- `scripts/install-skillset.ps1`
- `scripts/install-skillset.py`
- `scripts/install-skillset.sh`
- `mcp/presets/docs-research.toml`
- `mcp/presets/browser-qa.toml`
- `mcp/presets/full.toml`
- `mcp/servers/context7.toml`
- `mcp/servers/openaiDeveloperDocs.toml`
- `mcp/servers/playwright.toml`
- `mcp/servers/chrome-devtools.toml`
- `docs/mcp-setup.md`
- `docs/setup/README.md`
- `docs/compatibility.md`
- `docs/vendor-neutrality.md`

Not reviewed:

- Third-party package source code for MCP servers.
- Live host behavior after MCP servers are enabled.
- User-specific Codex home contents.

## Capability Inventory

| Capability | Present? | Notes |
|---|---|---|
| Instruction-only skill | no | This packet reviews install scripts and MCP snippets. |
| Executable scripts | yes | PowerShell, Python, and shell installer scripts are present. |
| External dependencies | yes | Installer uses Python; MCP snippets may use `npx` packages. |
| Network access | indirect | Installer does not call network; `npx` servers can fetch packages when launched by the host. |
| File read/write guidance | yes | Installer copies skill folders and appends config/AGENTS files. |
| Secret handling | no | No secrets are requested or printed. |
| MCP/tool permissions | yes | Presets list docs and browser QA server snippets. |
| Host-specific install steps | yes | Local installer is a Codex adapter, not the portable core. |

## Risk Checks

| Check | Result | Evidence |
|---|---|---|
| Prompt injection or instruction override | pass | AGENTS content is appended visibly with a skillset marker. |
| Hidden data exfiltration path | pass | Installer does not upload data or call network services. |
| Privilege escalation or broad permissions | warn | MCP snippets can give docs/browser tooling once enabled by the host. |
| Unsafe script execution | warn | Installer is explicit and has dry-run; MCP `npx` package execution needs review. |
| Unpinned or suspicious dependencies | warn | `npx` snippets use package names that resolve at runtime; controlled environments should pin versions. |
| Secrets requested or exposed | pass | No credential paths, env secret reads, or secret prints found. |
| Network calls without clear purpose | warn | Package fetch happens later through `npx` server startup, not during install. |
| Destructive file or git operations | warn | Python installer replaces existing target skill folders under the configured Codex home. |
| Legal, financial, medical, or compliance claims | pass | No regulated-advice claim found. |
| Host lock-in or hidden install behavior | pass | Docs identify the local installer as a Codex adapter and keep portable alternatives. |

## Findings

| Severity | Finding | File | Required fix |
|---|---|---|---|
| medium | MCP snippets understate that package-based servers may download and execute package code when started by the host. | `mcp/servers/context7.toml`, `mcp/servers/playwright.toml`, `mcp/servers/chrome-devtools.toml`, `docs/mcp-setup.md` | Add review/pinning guidance. |
| low | Setup docs listed only the original seven skillsets, which can mislead users during install review. | `docs/setup/README.md` | Replace the stale list with a dynamic reference. |

## Required Mitigations

- Document that package-based MCP server snippets use `npx` and should be
  reviewed and pinned in controlled environments.
- Keep dry-run install guidance visible before local install examples.
- Avoid maintaining a stale manual skillset list in setup docs.

## Approval Conditions

- The installer remains explicit and user-run; no automatic install or MCP
  launch is added.
- Non-dry-run installs remain scoped to declared skill folders, MCP snippets,
  and the target Codex home.
- Third-party MCP servers are reviewed before use in sensitive repositories.

## Follow-Up

- Add a future packet for a third-party skill folder with bundled scripts.
- Consider a later installer guardrail that prints target paths before deleting
  an existing installed skill folder in non-dry-run mode.
- Re-review if MCP snippets gain write scopes, credentials, custom env vars, or
  private network access.
