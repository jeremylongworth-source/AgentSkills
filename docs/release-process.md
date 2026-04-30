# Release Process

1. Update or add skills.
2. Run `scripts/validate-skills.ps1`.
3. Run scenario checks from `tests/scenarios/` for affected skillsets.
4. Update bundle manifests if skills are added or renamed.
5. Update `agents/` routing templates if globally relevant.
6. Run a public-safety scan before publishing:
   - no API keys, tokens, passwords, private keys, or local auth files
   - no personal machine paths or temporary test directories
   - no generated caches, logs, local databases, or build output
7. Smoke-test at least one representative install into a temporary Codex home.
8. Confirm the README, release notes, and repository structure match the actual files.
9. Tag the release with a semver tag such as `v0.1.0`.
10. If an additional descriptive tag is useful, keep it pointing at the same commit.
11. Publish the GitHub release from the intended primary tag.
12. Confirm the GitHub release state matches the launch decision:
   - normal release for stable public releases
   - prerelease only when the release should be explicitly marked as early or unstable
13. Verify the published tag, release page, and default branch all point at the intended commit.
