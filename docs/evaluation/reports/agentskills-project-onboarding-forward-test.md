# Before/After Report: agentskills-project-onboarding

Date: 2026-05-02
Reviewer: Codex
Skill or bundle: `agentskills-project-onboarding`
Scenarios:

- frontend app onboarding
- backend/API repo onboarding
- docs-heavy OSS repo onboarding

Source material:

- `skills/agentskills-project-onboarding/SKILL.md`
- `skills/agentskills-project-onboarding/references/onboarding-checklist.md`
- `tests/scenarios/agentskills-project-onboarding.md`
- `docs/setup/README.md`
- `docs/compatibility.md`
- `docs/examples/before-after-agent-behavior.md`

## Decision

Decision: keep and refine

Reason: the skill fills a real gap between setup docs and repo-specific
configuration. It correctly emphasizes focused installs, project scope, short
project instructions, and verification before install commands. The initial
gap was that the checklist did not give enough concrete mapping from repo
signals to likely AgentSkills profiles.

## Target Artifact

Artifact expected: focused AgentSkills onboarding plan for one repository
Audience: maintainers, founders, developers, and operators adding AgentSkills
to a new or existing repo
High-risk boundaries: install commands, MCP enablement, project instruction
overwrites, broad `all` installs, secrets, production credentials, and invented
build/test commands

## Acceptance Criteria

- Inspects repo files before recommending skills.
- Recommends the smallest useful skillset or atomic skill list.
- Explains project versus user scope.
- Preserves existing project instruction files and proposes patches.
- Recommends MCP only when the workflow needs it.
- Provides verification and rollback steps.
- Avoids broad `all` installs unless explicitly requested.

## Baseline Result

Setup: user asks for AgentSkills setup in a new repo without the onboarding
skill.

Output summary: likely to point to generic setup docs, `gh skill install`, or a
large skillset without inspecting repo signals.

What worked: can provide valid install commands and mention `AGENTS.md`.

What failed: less likely to choose a minimal profile, distinguish project/user
scope, preserve existing instruction files, or include a skill-trigger
verification prompt.

Safety issues: higher risk of recommending broad installs, enabling MCP without
need, or overwriting existing project guidance.

Reviewer edits required: moderate.

## Skill-Enabled Result

Setup: scenario prompt routed through `agentskills-project-onboarding`.

Output summary by scenario:

- Frontend app: recommend `frontend-product` first; add `quality-testing` only
  if release coverage is needed; include browser QA only when screenshots or UI
  inspection matter.
- Backend/API repo: recommend `backend-api` plus `engineering-delivery` when
  issue planning, PR review, or release risk is in scope.
- Docs-heavy OSS repo: recommend `technical-documentation`, with
  `engineering-delivery` only when code changes and release checks are part of
  the workflow.

What improved: skill creates a repo readout, focused recommendation, install
scope rationale, `AGENTS.md` patch plan, MCP rationale, verification prompt,
and rollback notes.

What regressed: no blocker found. The workflow is more deliberate than a quick
install answer, which is appropriate because the goal is focused repo setup.

Safety issues: no blocker found. The skill keeps install and MCP actions
approval-gated.

Reviewer edits required: light after adding the common profile map.

## Score

| Criterion | Baseline | Skill-enabled | Notes |
|---|---:|---:|---|
| Trigger fit | 1 | 3 | The trigger now covers repo onboarding, skillset choice, project instructions, scope, MCP, and verification. |
| Artifact usefulness | 1 | 3 | Produces a focused setup plan instead of generic install steps. |
| Correctness and evidence | 1 | 2 | Requires repo inspection; host-specific commands still need current docs when exact behavior matters. |
| Procedural value | 1 | 3 | Adds profile selection, scope decision, instruction patching, verification, and rollback. |
| Safety boundaries | 1 | 3 | Keeps installs, MCP enablement, and instruction overwrites approval-gated. |
| Context efficiency | 2 | 3 | One concise skill plus one checklist; no script until repeated evidence justifies it. |
| Validation behavior | 1 | 2 | Scenario routing and release gate validate structure; future real-repo traces would improve confidence. |
| Vendor neutrality | 2 | 3 | Skill is host-neutral and verifies current host facts when needed. |
| Maintainability | 2 | 3 | Profile map lives in the reference file and can evolve without expanding SKILL.md. |

## Follow-Up Changes

- Added a common profile map to `references/onboarding-checklist.md`.
- Added a before/after example for focused AgentSkills repo setup.
- Keep script automation deferred until repeated real-repo tests show the same
  inspection logic being rewritten.

## Evidence Links

- `skills/agentskills-project-onboarding/SKILL.md`
- `skills/agentskills-project-onboarding/references/onboarding-checklist.md`
- `tests/scenarios/agentskills-project-onboarding.md`
