# Skill Quality Rubric

Use this rubric for before/after reports and release reviews. Score each
criterion from 0 to 3.

| Score | Meaning |
|---:|---|
| 0 | Missing, harmful, or misleading |
| 1 | Present but weak, vague, or unreliable |
| 2 | Useful with minor gaps |
| 3 | Strong, specific, and repeatable |

## Criteria

| Criterion | What to check |
|---|---|
| Trigger fit | Description activates for the intended user request and avoids unrelated work |
| Artifact usefulness | Produces a concrete reviewable output, not generic advice |
| Correctness and evidence | Separates facts, assumptions, recommendations, and open questions |
| Procedural value | Changes the agent workflow with steps, checks, or decisions the base model might skip |
| Safety boundaries | States approval gates, refusal/escalation points, and high-risk limits |
| Context efficiency | Loads references only when needed and avoids broad stale context |
| Validation behavior | Names tests, checks, citations, or review steps needed before completion |
| Vendor neutrality | Keeps portable logic host-neutral and moves host-specific details to adapters |
| Maintainability | Stays concise, uses current repo patterns, and avoids duplicate or generic instructions |

## Release Thresholds

| Stage | Suggested bar |
|---|---|
| Draft | No 0 scores in trigger fit, artifact usefulness, or safety boundaries |
| Alpha | Average score of 2 or higher, no unresolved 0 scores |
| Beta | Average score of 2.4 or higher across at least five scenarios |
| Release | Average score of 2.6 or higher, no high-risk security findings, validation passes |

## Automatic Blockers

Do not promote a skill when it:

- tells the agent to ignore user, system, host, or repo instructions
- asks the agent to hide actions from the user
- reads secrets or private data unrelated to the task
- sends customer, legal, financial, production, or account changes without
  explicit approval
- installs dependencies, executes scripts, or calls network services without
  explaining why
- relies on stale platform, legal, financial, model, or API facts without a
  freshness rule
- cannot name a concrete artifact it produces

## Review Note Format

```markdown
Criterion:
Score:
Evidence:
Required change:
```
