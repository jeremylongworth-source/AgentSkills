# Real-Input Packet: QUALITY-001

Bundle: `quality-testing`
Scenario: Review v0.2 release-check readiness using the repo validation gate.
Reviewer: AgentSkills maintainer
Date collected: 2026-04-30
Public-safe: yes
Storage: committed

## Source Context

The repo has a release gate that validates skill files, skillsets, routing
scenarios, documentation consistency, all skillset install dry-runs, secret
scan, local-path scan, skillset listing, and `gh skill publish --dry-run`.

The validation task is to check whether the `quality-testing` bundle turns that
release gate into a useful QA decision, including what remains untested before
v0.2 promotion.

## User Prompt

> Review test readiness for the v0.2 AgentSkills release candidate. Use the
> current validation scripts, scenario coverage, install dry-runs, secret/local
> path scans, and publish dry-run as source material. Identify covered risks,
> missing QA coverage, release blockers, and give a ship/defer/block
> recommendation for the current alpha proof wave.

## Source Material

- `docs/bundles/quality-testing.md`
- `skillsets/quality-testing.yaml`
- `scripts/validate-skills.ps1`
- `scripts/validate-skill-files.py`
- `scripts/validate-skillsets.py`
- `scripts/validate-scenarios.py`
- `scripts/validate-docs.py`
- `scripts/release-check.ps1`
- `tests/expected-routing.yaml`
- `tests/scenarios/quality-release-risk.md`
- `tests/scenarios/quality-e2e-qa-matrix.md`
- `docs/evaluation/v0.2-validation-tracker.md`
- latest local validation output

## Expected Artifact

- Release QA readiness report
- Coverage matrix
- Missing test coverage and residual risk list
- Ship/defer/block recommendation for the alpha proof wave

## Acceptance Criteria

- Uses actual validation gates rather than generic QA advice.
- Separates checks that passed from checks not represented in the repo.
- Does not claim tests passed without command output.
- Identifies OS, fresh-home, external install, browser, and real-input packet
  gaps where applicable.
- Keeps production, customer, and private data out of QA.

## High-Risk Boundaries

- Do not claim v0.2 is release-ready from local validation alone.
- Do not use production data or private user material.
- Do not run live publishing commands.
- Do not claim accessibility, performance, or cross-platform compatibility
  from structural validation.

## Baseline Setup

Skillset disabled or closest prior bundle: generic release QA review without
`quality-testing`
Notes: baseline may list broad test categories but may not map them to the
actual AgentSkills release gate.

## Skill-Enabled Setup

Skillset: `quality-testing`
Relevant skills expected:

- `qa-test-strategy`
- `qa-matrix`
- `regression-check`
- `release-launch-readiness`
- `performance-test-plan`
- `accessibility-test-plan`
- `concise-technical-writing`

Notes: use local validation outputs and repo scripts only.

## Reviewer Notes

What would make the output usable?

- Clear release-risk matrix.
- Ship/defer/block recommendation scoped to the alpha proof wave.
- Concrete missing coverage rather than generic test advice.

What common mistakes should be caught?

- Treating scenario validation as real-input validation.
- Treating local Windows validation as cross-platform proof.
- Treating `gh skill publish --dry-run` as an actual release.

What would block release promotion?

- Failing validation, failing publish dry-run, broken install dry-runs, secret
  leaks, local path leaks, stale docs counts, or missing high-risk safety gates.
