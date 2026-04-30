#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: ./scripts/install-skillset.sh <skillset>" >&2
  exit 1
fi

skillset="$1"
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
codex_home="${CODEX_HOME:-$HOME/.codex}"
manifest="$repo_root/skillsets/$skillset.yaml"

if [[ ! -f "$manifest" ]]; then
  echo "Unknown skillset: $skillset" >&2
  exit 1
fi

mkdir -p "$codex_home/skills"

awk '/^skills:/{flag=1; next} /^[A-Za-z_].*:/{flag=0} flag && /^\s*-/{gsub(/^[ \t]*-[ \t]*/, ""); print}' "$manifest" |
while read -r skill; do
  [[ -n "$skill" ]] || continue
  cp -R "$repo_root/skills/$skill" "$codex_home/skills/"
done

echo "Installed skillset '$skillset'."

