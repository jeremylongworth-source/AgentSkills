#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
validator="${HOME}/.codex/skills/.system/skill-creator/scripts/quick_validate.py"

if [[ ! -f "$validator" ]]; then
  echo "Skill validator not found: $validator" >&2
  exit 1
fi

count=0
for skill in "$repo_root"/skills/*; do
  [[ -d "$skill" ]] || continue
  python "$validator" "$skill" >/dev/null
  [[ -f "$skill/SKILL.md" ]] || { echo "Missing SKILL.md: $skill" >&2; exit 1; }
  [[ -f "$skill/agents/openai.yaml" ]] || { echo "Missing agents/openai.yaml: $skill" >&2; exit 1; }
  [[ -d "$skill/references" ]] || { echo "Missing references/: $skill" >&2; exit 1; }
  grep -q '## References' "$skill/SKILL.md" || { echo "Missing References section: $skill" >&2; exit 1; }
  count=$((count + 1))
done

echo "Validated $count skills."

