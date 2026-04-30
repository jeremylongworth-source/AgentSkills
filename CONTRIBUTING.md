# Contributing

Thanks for improving AgentSkills. Keep contributions small, reviewable, and
vendor-neutral unless the change is explicitly for one host adapter.

## Good Contributions

- Improve an existing skill's trigger, workflow, safety rule, or deliverable.
- Add a focused scenario test for a real workflow.
- Improve setup, compatibility, troubleshooting, or release docs.
- Add a small validation check that catches a concrete release risk.
- Propose a new bundle with a clear user, artifact, and safety boundary.

## Before Opening a PR

Run the standard release gate:

```powershell
.\scripts\release-check.ps1
```

For CI-like local checks that skip publish auth, run:

```powershell
.\scripts\release-check.ps1 -SkipPublishDryRun
```

## Skill Guidelines

- Keep `SKILL.md` concise and procedural.
- Use concrete artifacts: briefs, memos, checklists, plans, scorecards,
  reports, runbooks, or review tables.
- Add freshness rules for current platform, legal, model, API, pricing, or
  compliance claims.
- Keep high-risk actions draft-first, read-first, or approval-gated.
- Do not include secrets, private customer data, local machine paths, logs,
  generated caches, or temporary output.

## Bundle Guidelines

- Compose existing skills before adding new ones.
- Add a bundle brief under `docs/bundles/`.
- Add route scenarios under `tests/scenarios/`.
- Update `tests/expected-routing.yaml`.
- Keep host-specific behavior in setup guides, templates, or adapter scripts.

## Review Checklist

- Validation passes.
- Docs and counts are current.
- New public files are safe to publish.
- The change avoids unnecessary host lock-in.
- The release notes or changelog are updated when the change affects users.
