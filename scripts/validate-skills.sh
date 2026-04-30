#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
validator="${HOME}/.codex/skills/.system/skill-creator/scripts/quick_validate.py"

if [[ -f "$validator" ]]; then
  for skill in "$repo_root"/skills/*; do
    [[ -d "$skill" ]] || continue
    python "$validator" "$skill" >/dev/null
  done
else
  echo "External skill validator not found; using repo-local skill checks."
fi

python "$repo_root/scripts/validate-skill-files.py" --repo-root "$repo_root"
python "$repo_root/scripts/validate-skillsets.py" --repo-root "$repo_root"
python "$repo_root/scripts/validate-scenarios.py" --repo-root "$repo_root"
python "$repo_root/scripts/validate-docs.py" --repo-root "$repo_root"
