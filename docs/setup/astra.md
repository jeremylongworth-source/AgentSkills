# AgentSkills with GPT-6 Astra

Use this guide to run AgentSkills with Astra in Codex. Reviewed against official
OpenAI documentation on 2026-09-17. Model availability and host behavior can
change; recheck the linked sources when updating your setup.

AgentSkills is a collection of workflow instructions, not a model runtime.
Select Astra in Codex and install the workflows your project needs. There is
no separate Astra skill format or required Astra-wide bundle in this repo.

## Choose the Model

In a Codex interface that offers Astra, select `gpt-6-astra`. The CLI supports
an explicit model choice for a session:

```sh
codex --model gpt-6-astra
```

Keep your established reasoning setting when comparing skill versions. Astra
does not support `none`; OpenAI recommends starting at `low` when migrating
from `none` or `minimal`. If Astra is unavailable, check the host version,
provider, and account access before changing the skills. A documented model
name does not establish access for a particular account.

See [OpenAI's Astra migration guidance](https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra.md#migration-quickstart).
AgentSkills installers do not select a model or change reasoning settings.

## Keep Discovery Focused

Use the [Codex setup guide](codex.md) for the current local adapter. The scope
options below are development changes and are not available in `v0.2.2`.
Run from the AgentSkills clone and replace `../MyProject` with an existing
project directory:

```powershell
.\scripts\install-skillset.ps1 engineering-delivery -Scope project -ProjectRoot ../MyProject -DryRun
.\scripts\install-skillset.ps1 engineering-delivery -Scope project -ProjectRoot ../MyProject
```

For a small personal set used across repositories, review `global-foundation`.
Reserve `all` for deliberate catalog testing. Project installs put skills in
`.agents/skills`; the local adapter retains its existing Codex user-scope path.
MCP and project routing are separate opt-ins, and the adapter leaves global
`AGENTS.md` unchanged.

Codex initially discovers skills through their metadata and loads the selected
instructions afterward. Large catalogs can shorten descriptions or omit
entries from the initial list. Check discovery in a fresh task; copying files
successfully does not prove the host exposed or used them. See
[OpenAI's skill discovery documentation](https://learn.chatgpt.com/docs/build-skills).

## Review Instructions Before Adding More

OpenAI's [Astra prompting guidance](https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra.md#prompting-best-practices)
identifies sensitivity to skill instructions, clarification pauses, response
formatting, delegation, and excessive testing as behaviors worth tuning.
The following are AgentSkills maintenance choices based on that guidance and
the source audit, not measured performance claims:

| Instruction issue | AgentSkills approach |
|---|---|
| A question quota blocks a sufficiently specified task | Ask about material unknowns and use evidence for routine gaps. |
| Brainstorming ends an authorized build at a handoff | Continue once direction is sufficient; preserve planning-only requests. |
| A setup plan repeats an approval already given | Apply and verify the requested install within its stated scope. |
| Every fix gets a broad test campaign | Run relevant checks and required gates; expand for identified risks. |
| Global routing lists duplicate the skill catalog | Use precise descriptions, focused scope, and on-demand references. |
| A source audit is described as a successful model test | Record the evaluation method and keep live-run claims separate. |

Adapt the [project instruction starter](../../templates/hosts/AGENTS.md) to the
repository's facts and validation commands. Merge useful clauses into existing
instructions instead of copying overlapping templates wholesale. The
[base routing guidance](../../agents/AGENTS.base.md) is another small reference;
neither file is automatically applied to existing projects.

When delegating is supported and authorized, define independent work and file
ownership, then integrate and verify the result. More agents are useful only
when they improve the task; selecting Astra does not enable delegation tools.

## Give Each Task a Clear Contract

Supply the outcome, relevant files, scope boundaries, and acceptance evidence.
For example:

```text
Fix the CSV export bug described in issue 42. Preserve the existing column
order and API. Inspect the current tests, add coverage for the failing case,
and run the relevant export checks plus the repository's required gates.
Use repository conventions for routine choices. Stop before publishing.
```

Use a planning-only request when you need a decision before implementation.
For an authorized build, preserve the objective when sending status questions
or corrections, and make changes in scope explicit.

## Verify the Change

Start with the [ASTRA-001 regression packet](../evaluation/packets/ASTRA-001-instruction-behavior.md).
It covers execution, planning, authorization, tests, discovery, and follow-up
steering. Compare skill versions with the same model, effort, inputs, tools,
and host instructions. Save the resulting transcripts and check observable
behavior rather than exact wording.

The [source review](../evaluation/reports/astra-instruction-review.md) records
the gaps addressed here. Repository validators check file structure and
consistency; they do not establish Astra routing quality, speed, token savings,
or superiority over another model. Run the packet on representative work
before making those claims.
