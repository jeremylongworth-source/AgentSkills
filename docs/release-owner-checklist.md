# Release Owner Checklist

Use this before tagging or publishing a release. It is a release-owner review
aid, not an automated release system.

## Prechecks

- Confirm the release version and intended tag.
- For a normal release, review `docs/stable-release-plan.md` and confirm
  release stability is not being confused with alpha bundle promotion.
- Review `docs/v0.2-release-handoff.md` for the latest local gate result,
  known evidence gaps, and final release-owner actions.
- Review `docs/release-candidate-v0.2.md` for scope, alpha boundaries, and the
  prerelease recommendation.
- Confirm release notes match the actual repo state.
- Confirm the latest CI validation run passed, or record why local validation is
  being used instead.
- Run `scripts/release-check.ps1`.
- Confirm `gh skill publish --dry-run` returns `ok`.
- Confirm the validation tracker reflects the latest gate.
- Confirm no private packets, customer data, secrets, local paths, logs, caches,
  or generated temp output are included.
- Confirm `v*` tag protection is understood: a bad protected release should be
  corrected with a forward patch release, not a tag rewrite.
- Confirm the GitHub release is marked prerelease unless the release owner
  explicitly accepts the remaining alpha evidence gaps.

## Evidence Review

- Scenario validation may support alpha inclusion.
- Public-safe packets may support proof workflow shape.
- Real-input packets are required before promoting high-risk bundles beyond
  alpha.
- Cross-platform claims require macOS, Linux, and Windows runs.
- Normal release status requires Windows, macOS, and Linux GitHub Actions
  release gates unless an exception is recorded.
- Fresh-home install claims require the fresh-home smoke test or an equivalent
  manual install record.

## Manual Release Steps

1. Run the release gate from a clean intended release branch.
2. Review the final diff and release notes.
3. Create the tag only after maintainer approval.
4. Publish from the intended tag.
5. Verify the release page, tag, default branch, and install path.

## Hold Conditions

- Any release-check failure.
- Any failed skillset install dry-run or fresh-home smoke test.
- Any secret or local path scan finding.
- Any stale count in README, release notes, or validation tracker.
- Any unreviewed live publish, tag, infrastructure, or account change.
