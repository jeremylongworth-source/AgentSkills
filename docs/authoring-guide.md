# Skill Authoring Guide

Create focused skills that change workflow quality, not just writing style.

## Repository Required Files

`SKILL.md` is the portable skill contract. This repository also requires
`agents/openai.yaml` as host adapter metadata so current Codex/OpenAI surfaces
can display and wire skills consistently.

```text
skill-name/
  SKILL.md
  agents/openai.yaml
  references/checklist.md
```

## SKILL.md Requirements

- YAML frontmatter with `name`, `description`, and `license: MIT`
- concise core workflow
- domain-specific priorities
- deliverable shape or output contract
- references section
- freshness rule when external facts change quickly

## Naming

- lowercase letters, digits, and hyphens
- short and specific
- one folder per atomic skill

## Bundles

For curated multi-skill installs, use the
[bundle authoring guide](bundle-authoring-guide.md).

Keep portable skill logic in `SKILL.md`, references, and scripts. Keep
host-specific setup in adapter metadata and setup docs.

## Validation

Run:

```powershell
.\scripts\validate-skills.ps1
```

The validator uses the local Codex skill-creator validator when it is available
and falls back to repo-local structural checks otherwise.
