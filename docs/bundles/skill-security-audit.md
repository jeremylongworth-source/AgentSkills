# Skill Security Audit Bundle Brief

## Problem

Agent skills can contain instructions, references, scripts, dependencies, and
install steps that agents may trust too much. Teams need a review-only workflow
for deciding whether a skill is safe to install, publish, or run with elevated
permissions.

## Target User

Skill authors, maintainers, security reviewers, AI engineers, enterprise teams,
and operators installing third-party skills.

## Included Skills

- `skill-threat-model`: map assets, trust boundaries, permissions, and threat
  paths.
- `prompt-injection-review`: inspect instructions, examples, and references for
  prompt injection or instruction override risk.
- `data-exfiltration-review`: review data sources, sinks, logs, and network
  movement.
- `script-permission-review`: inspect scripts, command examples, file writes,
  network calls, and destructive operations.
- `supply-chain-review`: review sources, dependencies, version pins, install
  steps, and provenance.
- `secrets-handling-review`: review credentials, env vars, redaction, storage,
  and exposure paths.
- `safe-install-checklist`: produce least-privilege install recommendations and
  approval gates.
- `concise-technical-writing`: make audit findings clear and actionable.

## Context Files

- `docs/evaluation/security-review-template.md`: security review report format.
- `docs/vendor-neutrality.md`: portable core versus host adapter boundaries.
- `docs/compatibility.md`: host and MCP setup differences.

## MCP Preset Intent

Use documentation research for public source verification when needed. Keep
audits review-only unless the user explicitly approves an install, script run,
network call, or permission change.

## Safety Rules

- Do not run unreviewed scripts to determine whether they are safe.
- Do not access, print, copy, transmit, or commit secrets.
- Do not approve hidden instruction overrides, concealed activity, data
  exfiltration paths, unexplained network calls, or broad permissions.
- Treat executable scripts, package install hooks, remote downloads, and broad
  MCP scopes as higher risk than instruction-only skills.
- Require explicit approval before installing third-party skills, enabling
  write scopes, running scripts, or using customer/production data.

## Pilot Metrics

- Operational: time from skill receipt to approve/block/defer recommendation.
- Quality: reviewer agreement with severity and required mitigations.
- Adoption: percent of new skills audited before release.
- Economic: avoided rework from unsafe install or publish decisions.

## Acceptance Criteria

- The bundle installs with a dry run.
- Third-party install, script review, publish review, and MCP scope scenarios
  route to the intended skills.
- Audit outputs include scope, capability inventory, risk matrix, findings,
  required mitigations, approval conditions, and recommendation.
- No audit workflow requires a single vendor or host-specific security service.
