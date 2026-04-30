# Before/After Report: devops-cloud-release DEVOPS-001

Date: 2026-04-30
Reviewer: Codex
Skill or bundle: `devops-cloud-release`
Packet: `DEVOPS-001`

Source material:

- `docs/evaluation/packets/DEVOPS-001-release-runbook.md`
- `docs/bundles/devops-cloud-release.md`
- `skillsets/devops-cloud-release.yaml`
- `docs/release-process.md`
- `scripts/release-check.ps1`
- `scripts/install-skillset.ps1`
- `scripts/install-skillset.py`
- `docs/evaluation/v0.2-validation-tracker.md`
- `docs/release-notes/v0.2.0.md`
- latest local release-check output

## Decision

Decision: keep as alpha

Go/defer/block recommendation for the current proof wave: go for continued
alpha proof development while the release gate is green; defer public v0.2
release promotion until remaining real-input, cross-platform, and fresh-install
evidence is collected.

Reason: the bundle produces a useful release-readiness memo and keeps live
release actions approval-gated. It correctly treats `gh skill publish
--dry-run` as evidence, not publication, and names protected-tag recovery
constraints.

## Target Artifact

Artifact expected: release readiness memo with prechecks, rollout steps,
rollback/recovery notes, blockers, and go/defer/block recommendation.
Audience: maintainers and release owners.
High-risk boundaries: no publish, push, tag, infrastructure, migration, or
settings changes.

## Acceptance Criteria

- Use actual release-check output and release process docs.
- Keep all live release actions manual and approval-gated.
- Note protected `v*` tag rollback constraints.
- Separate local dry-run confidence from actual release publication.

## Baseline Result

Setup: generic release checklist without the `devops-cloud-release` workflow.

Output summary: likely to list validation, release notes, tagging, and publish
steps, but may not distinguish dry-run from release, tag protection from
rollback, or alpha proof evidence from release proof.

What worked: the repo already has a clear release process and release-check
script.

What failed: baseline review can miss operational risk boundaries and recovery
constraints.

Safety issues: medium risk of implying that dry-run success is enough to tag or
publish without a release owner decision.

Reviewer edits required: moderate.

## Skill-Enabled Result

Setup: `DEVOPS-001` reviewed through `devops-cloud-release`, using release
process docs and latest release-check output.

Output summary: the release gate passed with skill validation, skillset
validation, scenario validation, docs consistency, all skillset install
dry-runs, skillset listing, secret scan, local-path scan, and `gh skill publish
--dry-run`.

What improved: the bundle turns those checks into a release memo with prechecks,
manual rollout steps, recovery notes, release blockers, and explicit defer
criteria for promotion beyond alpha.

What regressed: no regression found. The bundle adds release process structure,
which is appropriate for publish/tag decisions.

Safety issues: no blocker found. Residual risk remains around OS coverage,
fresh-home install behavior, external install paths, and real-input validation.

Reviewer edits required: low.

## Release Readiness Matrix

| Area | Current evidence | Status |
|---|---|---|
| Skill and skillset validation | release-check passed | go |
| Scenario routing | 113 scenarios validated | go |
| Docs consistency | release-check passed | go |
| Skillset install dry-runs | all 32 skillsets dry-run successfully | go locally |
| Secret scan | release-check passed | go structurally |
| Local path scan | release-check passed | go structurally |
| Publish compatibility | `gh skill publish --dry-run` returned `ok` | go as dry-run |
| Release notes | draft exists and has current proof-wave additions | go for alpha |
| Protected tag recovery | `v*` tags cannot be updated or deleted | forward-fix/new release required |
| Cross-platform validation | not run in this packet | gap |
| Fresh-home install | dry-run only | gap |
| Real-input promotion proof | starter packets only | gap |

## Rollout Notes

- Run `scripts/release-check.ps1` immediately before any release tag.
- Confirm release notes, README counts, validation tracker, and bundle lists are
  current.
- Have the maintainer explicitly approve tag and publish actions.
- Treat a bad protected `v*` release as a forward-fix: publish a corrected
  patch release rather than attempting to rewrite the protected tag.

## Score

| Criterion | Baseline | Skill-enabled | Notes |
|---|---:|---:|---|
| Trigger fit | 2 | 3 | Release readiness maps to deployment, rollback, readiness, and release-risk workflows. |
| Artifact usefulness | 2 | 3 | Produces release matrix, rollout notes, and defer criteria. |
| Correctness and evidence | 1 | 3 | Uses release-check output and avoids claiming actual publication. |
| Procedural value | 1 | 3 | Adds prechecks, manual approvals, recovery notes, and blockers. |
| Safety boundaries | 2 | 3 | Keeps tag, publish, and infrastructure actions approval-gated. |
| Context efficiency | 2 | 2 | Reads release scripts/docs directly relevant to the decision. |
| Validation behavior | 2 | 3 | Names release-check and remaining validation gaps. |
| Vendor neutrality | 2 | 3 | Keeps core release readiness repo-local while treating `gh` as publish-path evidence. |
| Maintainability | 2 | 3 | Reuses existing release-process docs instead of adding a new release system. |

## Follow-Up Changes

- Keep `devops-cloud-release` in v0.2 alpha.
- Add macOS/Linux release-check runs before cross-platform claims.
- Add a non-destructive fresh-home install test.
- Add a release owner checklist before tagging v0.2.

## Evidence Links

- `docs/release-process.md`
- `scripts/release-check.ps1`
- `docs/bundles/devops-cloud-release.md`
- `skillsets/devops-cloud-release.yaml`
- `docs/evaluation/v0.2-validation-tracker.md`
