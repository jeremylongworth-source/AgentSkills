# Technical Documentation Bundle Brief

## Problem

Teams need agents to produce documentation that is accurate, navigable, and
useful to real readers. Generic writing help is not enough; docs need source
grounding, structure, validation, version awareness, and clear next actions.

## Target User

Developers, maintainers, DevRel teams, technical writers, founders, and teams
shipping software, APIs, libraries, skillsets, or internal tools.

## Included Skills

- `readme-upgrade`: improve README structure, setup, examples, and trust proof.
- `api-doc-writing`: document endpoints, SDKs, schemas, auth, errors, and
  examples.
- `release-notes`: draft user-facing release notes.
- `changelog-maintenance`: maintain release history and Unreleased sections.
- `architecture-docs`: document system structure, tradeoffs, and ADRs.
- `migration-guide`: write upgrade and breaking-change guides.
- `developer-onboarding`: document setup, verification, workflows, and
  contribution paths.
- `tutorial-writing`: create task-focused walkthroughs and quickstarts.
- `concise-technical-writing`: tighten docs without losing required facts.

## Context Files

- `README.md`: current project positioning and install path.
- `docs/release-process.md`: release workflow and validation gate.
- `docs/compatibility.md`: host and platform compatibility notes.
- `docs/vendor-neutrality.md`: portable core and adapter boundaries.
- `docs/evaluation/`: proof and review templates for docs quality.

## MCP Preset Intent

Use documentation research for current platform, framework, API, and host facts.
Prefer source files, official docs, generated schemas, tests, and release
artifacts over memory.

## Safety Rules

- Do not invent commands, compatibility claims, release dates, API behavior,
  status codes, security posture, or performance claims.
- Do not expose secrets, private endpoints, customer data, or unreleased
  vulnerabilities in docs.
- Verify current external platform or API facts from official sources when
  they may have changed.
- Keep host-specific setup details in adapter docs when possible.

## Pilot Metrics

- Operational: time from source changes to reviewed docs draft.
- Quality: reviewer edit rate and command/link correction rate.
- Adoption: docs accepted without major rewrite.
- Economic: reduction in maintainer support time.

## Acceptance Criteria

- The bundle installs with a dry run.
- README, API docs, release notes, and migration/onboarding scenarios route to
  the intended skills.
- Documentation outputs identify source material, assumptions, validation, and
  open gaps.
- Commands, links, version names, and compatibility claims are checked or
  marked unverified.
