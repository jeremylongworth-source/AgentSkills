# Scenario: AgentOps Skill Chaining Overhead Review

Prompt:

> Review whether this multi-step research skill should stay monolithic or be
> split into composed skills. Compare baseline versus skill-enabled behavior,
> repeated-run context growth, loaded files, command/script output, MCP tool
> use, host-specific adapter options such as Claude Code forked skills, and a
> keep/split/compose decision rule.

Expected routing:

- skill-token-overhead-review
- skill-benchmark-design
- skill-evaluation-iteration
- before-after-evaluation
- scenario-test-authoring

Future bundle:

- agentops-evaluation
