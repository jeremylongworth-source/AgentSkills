# Real-Input Packet: SECURITY-002

Bundle: `skill-security-audit`
Scenario: Security review of local skillset install scripts and MCP snippets.
Reviewer: AgentSkills maintainer
Date collected: 2026-04-30
Public-safe: yes
Storage: committed

## Source Context

The repository includes local skillset installer scripts and MCP preset/server
snippets. Unlike an instruction-only skill, this layer can copy files into a
user's Codex home directory and append MCP server config. Package-based MCP
servers may be launched later by the host through `npx`.

## User Prompt

> Audit the local skillset installer and MCP snippets before v0.2 publication.
> Review file writes, destructive operations, shell command construction,
> network/package-fetch behavior, dependency execution, secrets handling,
> host lock-in, broad permissions, and whether docs clearly tell users to
> preview and review install changes before enabling MCP servers. Produce a
> security review with approve, approve with changes, block, or defer.

## Source Material

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

## Expected Artifact

- Install and MCP security review
- Capability inventory
- Risk matrix
- Required mitigations, if any
- Approve/approve with changes/block/defer recommendation

## Acceptance Criteria

- Identifies file writes to Codex home, skill folder replacement, config append,
  and AGENTS instruction append behavior.
- Distinguishes installer dry-run behavior from real install behavior.
- Flags `npx`-based MCP snippets as package execution that should be reviewed
  and pinned in controlled environments.
- Confirms that no secrets are requested and no MCP server is launched by the
  installer itself.
- Keeps recommendations vendor-neutral and adapter-scoped.

## High-Risk Boundaries

- Do not run installer scripts in non-dry-run mode.
- Do not launch MCP servers to prove they are safe.
- Do not claim third-party package security or current platform compliance.
- Do not make Codex the only supported host path.

## Baseline Setup

Skillset disabled or closest prior bundle: manual install review without
`skill-security-audit`
Notes: baseline may inspect scripts but may miss the later package-execution
risk from MCP snippets.

## Skill-Enabled Setup

Skillset: `skill-security-audit`
Relevant skills expected:

- `skill-threat-model`
- `script-permission-review`
- `supply-chain-review`
- `secrets-handling-review`
- `safe-install-checklist`
- `concise-technical-writing`

Notes: review files only; use dry-run behavior as the safe validation path.

## Reviewer Notes

What would make the output usable?

- Clear approve/approve with changes/block/defer recommendation.
- Concrete mitigation if docs or snippets understate package execution risk.
- No recommendation that requires a new security platform.

What common mistakes should be caught?

- Treating config append as harmless because it does not launch the server.
- Missing that `npx -y` can fetch and execute packages later.
- Ignoring that local installers are Codex adapters, not the portable contract.

What would block release promotion?

- Hidden script execution, secret access, network calls during install,
  destructive writes outside the target skill home, or unreviewed MCP servers
  being launched automatically.
