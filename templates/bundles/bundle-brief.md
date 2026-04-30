# Bundle Brief Template

Use this template before adding a new skillset under `skillsets/`.

## Problem

Describe the recurring workflow problem this bundle solves.

## Target User

Name the role or team that would install the bundle.

## Included Skills

- `skill-name`: why it belongs in this bundle

## Context Files

- `CONTEXT_FILE.md`: what the user should put here

## MCP Preset Intent

State which logical tool groups the bundle expects, such as documentation
research, browser QA, repository inspection, or read-only business systems.

## Safety Rules

- Default action mode:
- Actions requiring approval:
- Facts the agent must not invent:
- When to escalate:

## Pilot Metrics

- Operational:
- Quality:
- Adoption:
- Economic:

## Acceptance Criteria

- The manifest name matches the filename.
- Every listed skill exists and validates.
- Routing scenarios cover the main workflow.
- The bundle can be installed with a dry run.
- High-risk actions require human approval.

## Install Notes

Keep this section vendor-neutral. Link host-specific setup guides instead of
embedding host-only paths or commands.
