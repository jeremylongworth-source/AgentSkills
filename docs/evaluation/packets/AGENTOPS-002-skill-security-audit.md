# Real-Input Packet: AGENTOPS-002

Bundle: `agentops-evaluation`
Scenario: Evaluate the `skill-security-audit` bundle after two public-safe
security reviews.
Reviewer: AgentSkills maintainer
Date collected: 2026-04-30
Public-safe: yes
Storage: committed

## Source Context

The repo now has two public-safe security packets:

- `SECURITY-001`: instruction-only review of `ai-media-prompt-brief`
- `SECURITY-002`: installer and MCP snippet review covering scripts, file
  writes, config appends, and `npx` package-execution risk

The validation task is to check whether `skill-security-audit` produces more
useful security decisions than ad hoc review and whether it is ready to remain
in v0.2 alpha.

## User Prompt

> Evaluate the `skill-security-audit` alpha bundle using `SECURITY-001` and
> `SECURITY-002`. Compare ad hoc/manual review against the skill-enabled audit
> workflow. Score whether the bundle catches instruction-only risk, script and
> install risk, MCP/package-execution risk, secrets handling, host lock-in, and
> approval boundaries. Recommend keep, revise, split, merge, defer, or retire.

## Source Material

- `docs/evaluation/packets/SECURITY-001-ai-media-prompt-brief.md`
- `docs/evaluation/packets/SECURITY-002-local-install-mcp.md`
- `docs/evaluation/reports/skill-security-audit-SECURITY-001.md`
- `docs/evaluation/reports/skill-security-audit-SECURITY-002.md`
- `docs/bundles/skill-security-audit.md`
- `docs/evaluation/security-review-template.md`
- `docs/evaluation/skill-quality-rubric.md`

## Expected Artifact

- Before/after evaluation report
- Skill quality score table
- Promotion decision and required follow-up evidence

## Acceptance Criteria

- Compares instruction-only skill review and installer/MCP review.
- Identifies that no actual script execution, MCP launch, or third-party
  package review occurred.
- Separates mitigated findings from residual risks.
- Requires at least one third-party or scripted-skill packet before promotion.

## High-Risk Boundaries

- Do not claim third-party MCP packages are safe from config review alone.
- Do not launch MCP servers or run installer scripts in non-dry-run mode.
- Do not claim security approval for private user environments.

## Baseline Setup

Skillset disabled or closest prior bundle: manual security review without
`skill-security-audit`
Notes: baseline may find obvious scripts but may miss hidden instruction,
MCP/package, host adapter, or approval-boundary issues.

## Skill-Enabled Setup

Skillset: `agentops-evaluation`
Relevant skills expected:

- `before-after-evaluation`
- `skill-output-scoring`
- `acceptance-criteria-mapper`
- `skill-token-overhead-review`
- `concise-technical-writing`

Notes: use existing security packets and reports only.

## Reviewer Notes

What would make the output usable?

- Clear keep/revise/defer decision for `skill-security-audit`.
- Specific evidence gaps before promotion.
- No overclaiming from local public-safe files.

What common mistakes should be caught?

- Treating no secrets as no risk.
- Treating config append as harmless because MCP servers are not launched
  during install.
- Treating one instruction-only audit as enough proof for a security bundle.

What would block release promotion?

- Any report that approves scripts, package execution, broad MCP scopes, or
  install-time writes without naming review conditions and residual risk.
