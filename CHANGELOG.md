# Changelog

This project follows semver-style release tags. Dates are added when a release
is cut.

## Unreleased

No unreleased changes.

## v0.2.2 - 2026-05-05

- Added `agentskills-project-onboarding` for focused AgentSkills setup in new
  or existing repositories.
- Added a forward-test report and before/after example for focused AgentSkills
  project onboarding.
- Added `customer-health-review` for customer success account health, renewal
  risk, QBR, adoption, and success-plan workflows.
- Strengthened `revenue-growth` with sales pipeline management and added
  pipeline/customer-health routing scenarios.
- Added a lean-company operating model roadmap note for the first-five-hires
  expansion lens.

## v0.2.1 - 2026-04-30

- Added a stable release plan that separates distribution stability from alpha
  bundle maturity.
- Expanded GitHub Actions validation to run the release gate on Windows, macOS,
  and Linux.
- Made release-gate scripts use the available PowerShell host instead of
  assuming Windows PowerShell.

## v0.2.0 - 2026-04-30

- Expanded from 42 to 166 validated skill files.
- Expanded from 7 to 33 validated skillsets.
- Added 26 role-based alpha bundles across executive, creator, engineering,
  business analysis, documentation, AgentOps, security, data, and operations
  workflows.
- Added 123 routing scenarios and expected-routing validation.
- Added bundle briefs, setup guides, compatibility docs, examples, and
  vendor-neutrality guidance.
- Added evaluation templates, proof packets, before/after reports, quality
  rubrics, and security review templates.
- Added a stronger release gate with all-skillset dry-runs, fresh Codex home
  smoke tests, secret/local-path scans, and publish dry-run support.
- Added GitHub Actions validation for push, pull request, and manual runs.
- Added v0.2 release-candidate checklist and prerelease recommendation.
- Added v0.2 release handoff for final maintainer review before tagging.
- Added public collaboration docs, pull request template, issue templates, and
  code of conduct.

## v0.1.1

- Published the official `gh skill publish` release.
- Added `license: MIT` metadata to all skills.
- Kept `gh skill publish --dry-run` green before publishing.

## v0.1.0

- Published the initial public AgentSkills release.
- Included the first 42 validated skills and 7 skillsets.
- Added initial setup, validation, and release documentation.
