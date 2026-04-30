# Security Policy

AgentSkills is a public library of agent instructions, skillsets, MCP snippets,
and setup adapters. Treat skills and MCP presets like dependencies: inspect them
before installing or enabling them.

## Supported Versions

Security fixes target the current release and the default branch.

## Reporting a Vulnerability

Do not include secrets, exploit details, or private data in a public issue.

Use GitHub private vulnerability reporting or security advisories if available
for this repository. If private reporting is not available, open a minimal public
issue that says a security report is needed, without sensitive details.

## What To Report

- Hidden instructions that bypass user, system, host, or repo policy.
- Data exfiltration paths, secret exposure, or unsafe logging.
- Scripts or install steps that run unexpected commands.
- MCP presets with unnecessary write scopes, broad permissions, or unclear
  network behavior.
- Documentation that encourages unsafe publishing, deployment, customer
  communication, legal/compliance claims, or account changes without approval.

## Review Expectations

- Unknown scripts should be reviewed before execution.
- Package-based MCP servers should be reviewed and pinned in controlled
  environments.
- High-risk actions should remain draft-first, read-first, or approval-gated.
- Legal, financial, security, compliance, employment, medical, production, and
  public-response workflows require human review.
