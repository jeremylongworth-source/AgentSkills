# Astra Instruction Source Review

Date: 2026-09-17
Method: source audit and static scenario walkthrough
Target: `gpt-6-astra` in Codex
Decision: revise shared instructions; live effectiveness remains unmeasured

## Evidence and Scope

Reviewed the working-tree project starter, base routing, onboarding,
brainstorming, regression, and skill-evaluation instructions against
[OpenAI's Astra prompting guidance](https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra.md#prompting-best-practices)
and [skill discovery documentation](https://learn.chatgpt.com/docs/build-skills).
The input already included uncommitted Global Foundation and scoped-installer
work. That work was preserved; it is not a measured result of this review.

The [ASTRA-001 packet](../packets/ASTRA-001-instruction-behavior.md) defines the
test prompts and acceptance criteria. The source comparison below concerns
instruction text, not captured before/after model outputs. No independent
model calls, cross-model benchmark, or fresh-host discovery test was run.

## Findings and Changes

| Cases | Pre-change source finding | Revision |
|---|---|---|
| A1, A2 | Brainstorming preferred 3-7 questions and ended with a next-skill recommendation even when the request included implementation. | Questions depend on material unknowns; handoff continues authorized implementation while preserving planning-only boundaries. |
| A3, A4 | Onboarding ended in a setup plan and did not distinguish a requested install from a recommendation clearly enough. | Preview and apply the requested install within its authorized scope; recommendation-only work remains a plan. |
| A5 | Regression guidance listed broad coverage without a stopping rule. | Select checks for plausible effects and required gates, then stop unless new evidence justifies more. |
| A6, A7 | Project starter did not explain existing authorization, independent work during a gate, or follow-up steering. | Add those rules and require the exact blocking instruction to be identified. |
| A8 | Evaluation checklist and quality bar still recommended account-level routing despite the new focused-discovery direction. | Align references with metadata-driven discovery and require evidence for live-run claims. |

Static walkthrough result: the revised instructions now state the intended
behavior for these cases. They do not change the high-risk domain rules or
authorize bypassing host restrictions or required human review. This resolves
the identified text conflicts; it does not establish how consistently Astra
will follow them in new sessions.

## Validation Boundary

Structural checks passed on the working tree on 2026-09-17:

- Repository validators: 167 skill files, 35 skillsets, 125 routing scenarios,
  and documentation consistency.
- Official skill validator: onboarding, brainstorming, regression checking,
  and skill-evaluation iteration.
- Project-scope `engineering-delivery` installer dry run: eight skill targets;
  no files installed or configuration changed.
- `git diff --check`: no whitespace errors; Git reported existing line-ending
  normalization warnings.

The local Codex CLI (`0.153.4`) exposes `--model`; no Astra model invocation or
account-availability check was performed. Onboarding's `agents/openai.yaml`
now covers authorized execution and separate discovery verification. The
other edited skills retain their existing purpose and metadata.

Run ASTRA-001 in fresh tasks with the exact model, effort, host version, active
skills, and tools recorded before making claims about completion rate, fewer
questions, speed, token savings, or improvement over another model. Existing
historical forward-test reports were not relabeled as Astra evidence.
