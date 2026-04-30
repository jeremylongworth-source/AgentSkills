# Release Process

1. Update or add skills.
2. Run `scripts/release-check.ps1` for the standard release gate.
3. Confirm scenario checks from `tests/scenarios/` are covered by validation.
4. Review `docs/release-owner-checklist.md` before tagging or publishing.
5. Update bundle manifests if skills are added or renamed.
6. Run `scripts/list-skillsets.ps1 -Markdown` when README or docs tables need to reflect bundle changes.
7. Update `agents/` routing templates if globally relevant.
8. Check vendor neutrality for new bundles and docs:
   - portable skill behavior stays in `SKILL.md`, references, and scripts
   - host-specific commands stay in setup guides, templates, or adapter scripts
   - new bundle manifests avoid host-specific fields unless required
9. If running checks manually, run a public-safety scan before publishing:
   - no API keys, tokens, passwords, private keys, or local auth files
   - no personal machine paths or temporary test directories
   - no generated caches, logs, local databases, or build output
10. Confirm every skillset dry-run install passes in the release check.
11. Confirm the fresh Codex home install smoke test passes in the release check.
12. Confirm the README, release notes, and repository structure match the actual files.
13. Tag the release with a semver tag such as `v0.1.0`.
14. If an additional descriptive tag is useful, keep it pointing at the same commit.
15. Publish the GitHub release from the intended primary tag.
16. Confirm the GitHub release state matches the launch decision:
   - normal release for stable public releases
   - prerelease only when the release should be explicitly marked as early or unstable
17. Verify the published tag, release page, and default branch all point at the intended commit.
