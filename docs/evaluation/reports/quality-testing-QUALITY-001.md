# Before/After Report: quality-testing QUALITY-001

Date: 2026-04-30
Reviewer: Codex
Skill or bundle: `quality-testing`
Packet: `QUALITY-001`

Source material:

- `docs/evaluation/packets/QUALITY-001-release-check-readiness.md`
- `docs/bundles/quality-testing.md`
- `skillsets/quality-testing.yaml`
- `scripts/release-check.ps1`
- `scripts/validate-skills.ps1`
- `scripts/validate-skill-files.py`
- `scripts/validate-skillsets.py`
- `scripts/validate-scenarios.py`
- `scripts/validate-docs.py`
- `tests/expected-routing.yaml`
- `tests/scenarios/quality-release-risk.md`
- latest local validation output

## Decision

Decision: keep as alpha

Recommendation for current alpha proof wave: ship the proof-wave docs and
validation changes when release gate remains green; do not promote v0.2 bundles
beyond alpha until real-input packet coverage expands.

Reason: the bundle turns the repo's validation scripts into a concrete release
QA view and correctly separates passed structural checks from untested
cross-platform, fresh-install, browser, performance, accessibility, and
real-input evidence.

## Target Artifact

Artifact expected: release QA readiness report with coverage matrix, residual
risks, and ship/defer/block recommendation.
Audience: maintainers preparing a release candidate.
High-risk boundaries: no production data, no live publish, no claim of
cross-platform or real-input proof from one local run.

## Acceptance Criteria

- Use actual validation gates and observed command output.
- Separate passed checks from missing QA coverage.
- Name release blockers and residual risks.
- Keep `gh skill publish --dry-run` distinct from a real publish.

## Baseline Result

Setup: generic QA/release review without the `quality-testing` workflow.

Output summary: likely to suggest unit, integration, E2E, accessibility, and
performance testing, but may not map the repo's actual validation scripts to a
release-readiness decision.

What worked: broad QA categories are easy to name.

What failed: baseline review can miss that this repo's primary risks are skill
metadata integrity, skillset manifest references, routing scenarios, docs
consistency, install dry-runs, secret/local path leaks, and publish dry-run
status.

Safety issues: could overclaim release readiness by treating local validation
as cross-platform, fresh-home, or real-input proof.

Reviewer edits required: moderate.

## Skill-Enabled Result

Setup: `QUALITY-001` reviewed through `quality-testing`, using the latest local
validation and release-check output.

Output summary: the release gate passed with:

- 158 skill files validated
- 32 skillsets validated
- 113 routing scenarios validated
- docs consistency validated
- all skillset install dry-runs passed
- secret and local-path scans passed
- `gh skill publish --dry-run` returned `ok`

What improved: the bundle frames the passed checks as structural release
coverage, identifies missing coverage, and keeps the alpha proof boundary
visible.

What regressed: no regression found. The report adds some process overhead, but
it is appropriate for release-facing QA.

Safety issues: no blocker found. Remaining risks are evidence gaps, not failed
checks.

Reviewer edits required: low.

## Coverage Matrix

| Risk area | Current coverage | Status |
|---|---|---|
| Skill file structure and metadata | `validate-skill-files.py` | covered |
| Skillset manifest references | `validate-skillsets.py` | covered |
| Routing scenarios | `validate-scenarios.py` and `expected-routing.yaml` | covered |
| Documentation consistency | `validate-docs.py` | covered |
| Skillset install path | release-check dry-runs every skillset | covered locally |
| Secret leakage | release-check regex scan | covered structurally |
| Local path leakage | release-check regex scan | covered structurally |
| Publish compatibility | `gh skill publish --dry-run` | covered as dry-run |
| Windows execution | local PowerShell run | partially covered |
| macOS/Linux execution | no current run in this packet | gap |
| Fresh Codex home install | dry-run only in this packet | gap |
| Browser/UI behavior | not applicable to most skills; not run here | gap when browser bundles change |
| Accessibility/performance | not represented by current structural checks | gap |
| Real-input bundle proof | starter packets only | gap |

## Score

| Criterion | Baseline | Skill-enabled | Notes |
|---|---:|---:|---|
| Trigger fit | 2 | 3 | Release QA request maps cleanly to QA strategy, matrix, regression, and readiness. |
| Artifact usefulness | 2 | 3 | Produces a coverage matrix and alpha-scoped recommendation. |
| Correctness and evidence | 1 | 3 | Uses observed validation output and labels untested areas. |
| Procedural value | 1 | 3 | Converts release scripts into a risk-based QA decision. |
| Safety boundaries | 2 | 3 | Avoids live publish, production data, and cross-platform overclaims. |
| Context efficiency | 2 | 2 | Reads several scripts, but all are directly relevant to release QA. |
| Validation behavior | 2 | 3 | Names the exact release gate and missing future checks. |
| Vendor neutrality | 2 | 3 | Keeps QA based on repo-local scripts while recognizing `gh` as one publish path. |
| Maintainability | 2 | 3 | Reuses existing release-check structure rather than adding a new QA system. |

## Follow-Up Changes

- Keep `quality-testing` in v0.2 alpha.
- Add macOS and Linux validation runs before claiming cross-platform confidence.
- Add a real fresh-home install test for at least one small skillset and one
  large skillset.
- Add browser QA evidence when browser/game/frontend bundles change.
- Keep real-input bundle proof separate from scenario validation.

## Evidence Links

- `scripts/release-check.ps1`
- `scripts/validate-skills.ps1`
- `docs/bundles/quality-testing.md`
- `skillsets/quality-testing.yaml`
- `docs/evaluation/v0.2-validation-tracker.md`
