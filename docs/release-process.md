# Release Process

1. Update or add skills.
2. Run `scripts/validate-skills.ps1`.
3. Run scenario checks from `tests/scenarios/` for affected skillsets.
4. Update bundle manifests if skills are added or renamed.
5. Update `agents/` routing templates if globally relevant.
6. Tag the repo release.

