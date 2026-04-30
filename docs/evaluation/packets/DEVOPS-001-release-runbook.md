# Real-Input Packet: DEVOPS-001

Bundle: `devops-cloud-release`
Scenario: Review v0.2 release runbook and rollback readiness for AgentSkills.
Reviewer: AgentSkills maintainer
Date collected: 2026-04-30
Public-safe: yes
Storage: committed

## Source Context

AgentSkills publishes skills and skillsets through repository releases and
`gh skill publish`. The repo has release process docs, a release-check script,
skillset install dry-runs, secret/local-path scans, and publish dry-run checks.

The validation task is to check whether `devops-cloud-release` turns those
release files into a practical release runbook and readiness decision without
taking live publish, tag, or infrastructure actions.

## User Prompt

> Review release readiness for the v0.2 AgentSkills alpha expansion. Use the
> release process doc, release-check script, validation outputs, install
> dry-runs, publish dry-run, protected tag policy, and current tracker status.
> Produce a release runbook summary with prechecks, rollout steps, rollback or
> recovery considerations, owner approvals, release blockers, and go/no-go
> recommendation. Do not publish, tag, push, or change infrastructure.

## Source Material

- `docs/bundles/devops-cloud-release.md`
- `skillsets/devops-cloud-release.yaml`
- `docs/release-process.md`
- `scripts/release-check.ps1`
- `scripts/install-skillset.ps1`
- `scripts/install-skillset.py`
- `docs/evaluation/v0.2-validation-tracker.md`
- `docs/release-notes/v0.2.0.md`
- `tests/scenarios/devops-deployment-runbook.md`
- `tests/scenarios/devops-config-rollback.md`
- latest local release-check output

## Expected Artifact

- Release readiness memo
- Precheck and rollout checklist
- Rollback/recovery notes
- Release blockers and residual risks
- Go/defer/block recommendation scoped to alpha

## Acceptance Criteria

- Uses the actual release-check output and release process.
- Keeps publish/tag/push actions as manual approval-gated steps.
- Notes that protected `v*` tags make rollback a forward-fix or new-release
  action, not a tag rewrite.
- Separates local dry-run confidence from actual release publication.
- Identifies remaining OS, fresh-home, real-input, and external install gaps.

## High-Risk Boundaries

- Do not publish, push, tag, deploy, change infrastructure, or modify GitHub
  settings.
- Do not claim a release exists before it is created.
- Do not claim rollback can update or delete protected `v*` tags.
- Do not invent current CI status or cloud/provider state.

## Baseline Setup

Skillset disabled or closest prior bundle: generic release checklist without
`devops-cloud-release`
Notes: baseline may list release steps but miss protected-tag recovery,
approval gates, dry-run versus publish separation, and residual validation gaps.

## Skill-Enabled Setup

Skillset: `devops-cloud-release`
Relevant skills expected:

- `deployment-plan`
- `rollback-plan`
- `production-readiness-review`
- `release-risk`
- `release-launch-readiness`
- `environment-config-review`
- `concise-technical-writing`

Notes: review files only; no live publish or tag action.

## Reviewer Notes

What would make the output usable?

- Clear go/defer/block recommendation.
- Manual release steps and rollback/recovery caveats.
- No live release action.

What common mistakes should be caught?

- Treating publish dry-run as actual publication.
- Omitting protected tag constraints.
- Treating local validation as cross-platform proof.

What would block release promotion?

- Failed release-check, failed publish dry-run, secrets/local paths, missing
  release notes, broken install dry-runs, or stale validation counts.
