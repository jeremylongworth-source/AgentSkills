#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: ./scripts/install-skillset.sh <skillset> [--scope user|project] [options]" >&2
  exit 1
fi

skillset="$1"
shift
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
codex_home="${CODEX_HOME:-$HOME/.codex}"
exec "${PYTHON:-python3}" "$repo_root/scripts/install-skillset.py" --skillset "$skillset" --repo-root "$repo_root" --codex-home "$codex_home" "$@"
