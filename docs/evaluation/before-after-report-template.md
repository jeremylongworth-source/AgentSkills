# Before/After Report Template

Use this template to document whether a skill or bundle improved a realistic
agent output. Keep reports short enough that maintainers will read them.

```markdown
# Before/After Report: <skill or bundle>

Date:
Reviewer:
Skill or bundle:
Scenario:
Source material:

## Decision

Decision: keep | revise | split | merge | defer | retire

Reason:

## Target Artifact

Artifact expected:
Audience:
High-risk boundaries:

## Acceptance Criteria

- <criterion>
- <criterion>
- <criterion>

## Baseline Result

Setup:
Output summary:
What worked:
What failed:
Safety issues:
Reviewer edits required:

## Skill-Enabled Result

Setup:
Output summary:
What improved:
What regressed:
Safety issues:
Reviewer edits required:

## Score

| Criterion | Baseline | Skill-enabled | Notes |
|---|---:|---:|---|
| Trigger fit |  |  |  |
| Artifact usefulness |  |  |  |
| Correctness and evidence |  |  |  |
| Procedural value |  |  |  |
| Safety boundaries |  |  |  |
| Context efficiency |  |  |  |
| Validation behavior |  |  |  |

## Overhead

Extra files loaded:
Extra tools/scripts used:
Approximate extra turns or time:
Token or trace link if available:

## Follow-Up Changes

- <patch or doc update>
- <scenario to add>
- <risk to review>

## Evidence Links

- <scenario file>
- <source input>
- <baseline output>
- <skill-enabled output>
- <validation output>
```

## Reporting Rules

- Report regressions. A skill that helps one criterion but hurts safety,
  correctness, or maintainability is not ready.
- Separate missing context from skill failure. If the prompt lacked required
  source material, say so.
- Do not use private customer data in public reports.
- Keep vendor-specific traces optional. Link them when available, but do not
  require one host or observability vendor to run the evaluation.
