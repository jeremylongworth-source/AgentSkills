# v0.2 Release Candidate Checklist

Use this checklist to decide whether the expanded v0.2 portfolio is ready to
tag and publish.

For final maintainer handoff before tagging, see
[v0.2 release handoff](v0.2-release-handoff.md).

For the path from prerelease to normal release, see
[stable release plan](stable-release-plan.md).

## Release Shape

Recommended release type: prerelease

Reason: v0.2 adds a large alpha bundle portfolio. The core repo validation,
install checks, docs, and publish dry-run are green, but several new business
and creator bundles still need real or anonymized input packets before they
should be described as proven workflows.

## Included Scope

- 166 validated skill files.
- 33 validated skillsets.
- 123 routing scenarios.
- 26 new role-based alpha bundles.
- Evaluation proof layer with packets, reports, quality rubric, and security
  review template.
- Release gate with all skillset dry-runs, fresh Codex home smoke test,
  secret/local-path scans, and publish dry-run support.
- GitHub Actions validation for push, pull request, and manual runs.
- Public repo hygiene docs: changelog, contributing guide, security policy,
  code of conduct, pull request template, and issue templates.

## Must Pass Before Tagging

- `.\scripts\release-check.ps1`
- Latest GitHub Actions validation run, unless the release owner records why
  local validation is being used instead.
- README, changelog, release notes, and validation tracker counts match
  the repo.
- No private packets, secrets, local paths, logs, caches, or generated temp
  output are included.
- Release owner confirms whether the GitHub release should be marked
  prerelease.

## Alpha Boundaries

- Scenario validation proves routing and structure, not real-world adoption.
- Public-safe packets prove review workflow shape, not full domain proof.
- Real-input packets remain deferred until suitable public-safe, anonymized, or
  private-local material is available.
- High-risk legal, financial, security, compliance, employment, production,
  public-response, and platform-policy decisions remain human-reviewed.

## Deferred Before Promotion Beyond Alpha

- Real creator and sponsor packets.
- Real application API contract packets.
- Third-party scripted skill audit packets.
- Source-grounded data/finance packets.
- Leadership-review packets for executive bundles.
- macOS and Linux release-check runs before cross-platform claims.

## Stable Release Path

A future normal release does not need every alpha bundle to be proven, but it
does need stable install, validation, and documentation paths. Use the stable
release plan to decide whether the release itself is stable while keeping
newly expanded role bundles labeled alpha until real-input evidence supports
promotion.

## Go/No-Go

Go as prerelease when the release gate and CI are green and the release owner
accepts the alpha boundaries.

Hold if validation fails, CI fails without explanation, counts drift, public
docs are stale, or the release notes imply the new bundles are proven beyond
their current evidence.
