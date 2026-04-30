from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


PRESET_SERVERS = {
    "docs-research": ["context7", "openaiDeveloperDocs"],
    "browser-qa": ["playwright", "chrome-devtools"],
    "full": ["context7", "openaiDeveloperDocs", "playwright", "chrome-devtools"],
}


def parse_manifest(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    result: dict[str, object] = {"skills": [], "mcp_presets": [], "agents_file": None}
    current: str | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if re.match(r"^skills\s*:", line):
            current = "skills"
            continue
        if re.match(r"^mcp_presets\s*:", line):
            current = "mcp_presets"
            continue
        scalar = re.match(r"^agents_file\s*:\s*(.+)\s*$", line)
        if scalar:
            result["agents_file"] = scalar.group(1).strip()
            current = None
            continue
        if re.match(r"^[A-Za-z_][A-Za-z0-9_ -]*\s*:", line):
            current = None
            continue
        item = re.match(r"^\s*-\s*(.+?)\s*$", line)
        if item and current in ("skills", "mcp_presets"):
            result[current].append(item.group(1).strip())  # type: ignore[index]
    return result


def append_once(path: Path, marker: str, content: str) -> None:
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    if marker in existing:
        return
    with path.open("a", encoding="utf-8", newline="\n") as f:
        if existing and not existing.endswith("\n"):
            f.write("\n")
        f.write(content)
        if not content.endswith("\n"):
            f.write("\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skillset", required=True)
    parser.add_argument("--repo-root", required=True)
    parser.add_argument("--codex-home", required=True)
    args = parser.parse_args()

    repo_root = Path(args.repo_root)
    codex_home = Path(args.codex_home)
    manifest_path = repo_root / "skillsets" / f"{args.skillset}.yaml"
    if not manifest_path.exists():
        raise SystemExit(f"Unknown skillset: {args.skillset}")

    manifest = parse_manifest(manifest_path)
    skills: list[str] = manifest["skills"]  # type: ignore[assignment]
    presets: list[str] = manifest["mcp_presets"]  # type: ignore[assignment]
    agents_file = manifest["agents_file"]

    target_skills = codex_home / "skills"
    target_skills.mkdir(parents=True, exist_ok=True)

    for skill in skills:
        src = repo_root / "skills" / skill
        if not (src / "SKILL.md").exists():
            raise SystemExit(f"Missing skill folder: {src}")
        dst = target_skills / skill
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)

    config_path = codex_home / "config.toml"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.touch(exist_ok=True)

    server_names: list[str] = []
    for preset in presets:
        server_names.extend(PRESET_SERVERS.get(preset, []))
    for server in dict.fromkeys(server_names):
        snippet = repo_root / "mcp" / "servers" / f"{server}.toml"
        if not snippet.exists():
            raise SystemExit(f"Missing MCP server snippet: {snippet}")
        marker = f"[mcp_servers.{server}]"
        append_once(config_path, marker, "\n" + snippet.read_text(encoding="utf-8").strip() + "\n")

    if agents_file:
        agent_src = repo_root / str(agents_file)
        if not agent_src.exists():
            raise SystemExit(f"Missing agents file: {agent_src}")
        agents_path = codex_home / "AGENTS.md"
        marker = f"AgentSkills skillset: {args.skillset}"
        content = f"\n# {marker}\n{agent_src.read_text(encoding='utf-8').strip()}\n"
        append_once(agents_path, marker, content)

    print(f"Installed skillset '{args.skillset}' with {len(skills)} skills.")
    if presets:
        print("MCP config changed or verified. Restart Codex if new MCP servers do not appear immediately.")


if __name__ == "__main__":
    main()

