# Stable Release Plan

Use this plan to move AgentSkills from a prerelease expansion to a normal
GitHub release without overstating the maturity of every alpha bundle.

## Release Stability vs Bundle Maturity

Release stability is separate from bundle maturity.

- A normal release means the library can be installed, validated, updated, and
  documented through stable public paths.
- An alpha bundle means the workflow is scenario-tested and review-gated, but
  still needs more real-input evidence before it should be called proven.

The next non-prerelease release can still include alpha bundles if the release
notes clearly say which bundles are alpha and what evidence remains.

## Stable Release Gate

Before removing prerelease status from a future release, require:

- Windows, macOS, and Linux GitHub Actions release gates pass.
- Local Windows release gate passes with `gh skill publish --dry-run`.
- A published-tag install smoke test passes for at least one representative
  skill from the current release.
- README, changelog, release notes, validation tracker, release handoff, and
  bundle counts match the repo.
- Secret and local-path scans pass.
- High-risk bundles still advertise human review, draft-first, read-first, or
  approval-gated behavior.
- Release notes distinguish stable distribution from alpha workflow maturity.

## Evidence Required Before Bundle Promotion

These evidence gaps block promoting the related bundles beyond alpha. They do
not block a stable distribution release if the alpha labels remain clear.

- Real or anonymized creator and sponsor packets.
- Real application API contract packets.
- Third-party scripted skill audit packets.
- Source-grounded data and finance packets.
- Leadership-review packets for executive bundles.
- Reviewer packets for owner, operating, product, revenue, engineering, and
  support bundles.

## Recommended Next Release Shape

Use a patch release, such as `v0.2.1`, for the first normal release if the only
changes are validation, documentation, release notes, install proof, and stable
release positioning.

Use a minor release, such as `v0.3.0`, if the work also adds or substantially
changes skillsets, output contracts, routing behavior, or bundle scope.

## Go/No-Go For Normal Release

Go as a normal release when the stable release gate is green and the release
notes clearly state:

- the distribution and install path are stable
- newly expanded role bundles remain alpha unless separately promoted
- scenario validation is not the same as real-world adoption proof
- high-risk outputs require human review

Hold as prerelease if cross-platform validation fails, install smoke tests fail,
counts drift, release notes imply alpha bundles are proven, or any security or
local-path scan fails.
