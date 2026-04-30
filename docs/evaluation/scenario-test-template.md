# Scenario Test Template

Copy this template into `tests/scenarios/<scenario-name>.md` when a new bundle
or skill needs routing coverage. Keep the prompt realistic and compact.

```markdown
# Scenario: <Human-readable scenario name>

Prompt:

> <User prompt exactly as the agent should receive it. Include enough context to
> route correctly, but do not include the expected answer.>

Expected routing:

- <skill-name>
- <skill-name>

Future bundle:

- <bundle-name>
```

Then add the matching key to `tests/expected-routing.yaml`:

```yaml
<scenario-name>:
  - <skill-name>
  - <skill-name>
```

## Scenario Quality Checks

- The prompt names a real user job, not an internal implementation detail.
- The expected routing uses existing skill folder names unless the scenario is
  explicitly documenting planned work.
- The scenario can run without private credentials, customer data, or live
  production systems.
- The prompt is specific enough to activate the intended skill, but not so
  specific that it gives away the output.
- The expected output can be reviewed as an artifact: memo, checklist, runbook,
  plan, risk register, scorecard, or draft.
- High-risk workflows include an approval or review expectation in the prompt.

## Examples

Good:

```markdown
> Review this proposed API change and produce an OpenAPI outline, error
> contract, and backend test checklist.
```

Weak:

```markdown
> Use the backend-api skill.
```

Good:

```markdown
> Audit this skill folder before publication and identify prompt-injection,
> script-permission, secrets-handling, and supply-chain risks.
```

Weak:

```markdown
> Make this secure.
```
