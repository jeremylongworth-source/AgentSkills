from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


def clean_scalar(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


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
            result["agents_file"] = clean_scalar(scalar.group(1))
            current = None
            continue
        if re.match(r"^[A-Za-z_][A-Za-z0-9_ -]*\s*:", line):
            current = None
            continue
        item = re.match(r"^\s*-\s*(.+?)\s*$", line)
        if item and current in ("skills", "mcp_presets"):
            result[current].append(clean_scalar(item.group(1)))  # type: ignore[index]
    return result


def parse_preset_servers(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"servers\s*=\s*\[(.*?)\]", text, re.S)
    if not match:
        return []
    return [
        clean_scalar(item)
        for item in (part.strip() for part in match.group(1).split(","))
        if item
    ]


def unique(items: list[str]) -> list[str]:
    return list(dict.fromkeys(items))


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
    parser.add_argument("--dry-run", action="store_true")
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
    if not args.dry_run:
        target_skills.mkdir(parents=True, exist_ok=True)

    for skill in skills:
        src = repo_root / "skills" / skill
        if not (src / "SKILL.md").exists():
            raise SystemExit(f"Missing skill folder: {src}")
        dst = target_skills / skill
        if not args.dry_run:
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)

    config_path = codex_home / "config.toml"
    if not args.dry_run:
        config_path.parent.mkdir(parents=True, exist_ok=True)
        config_path.touch(exist_ok=True)

    server_names: list[str] = []
    for preset in presets:
        preset_path = repo_root / "mcp" / "presets" / f"{preset}.toml"
        if not preset_path.exists():
            raise SystemExit(f"Missing MCP preset: {preset_path}")
        servers = parse_preset_servers(preset_path)
        if not servers:
            raise SystemExit(f"MCP preset has no servers: {preset_path}")
        server_names.extend(servers)

    for server in unique(server_names):
        snippet = repo_root / "mcp" / "servers" / f"{server}.toml"
        if not snippet.exists():
            raise SystemExit(f"Missing MCP server snippet: {snippet}")
        if not args.dry_run:
            marker = f"[mcp_servers.{server}]"
            append_once(
                config_path,
                marker,
                "\n" + snippet.read_text(encoding="utf-8").strip() + "\n",
            )

    if agents_file:
        agent_src = repo_root / str(agents_file)
        if not agent_src.exists():
            raise SystemExit(f"Missing agents file: {agent_src}")
        if not args.dry_run:
            agents_path = codex_home / "AGENTS.md"
            marker = f"AgentSkills skillset: {args.skillset}"
            content = f"\n# {marker}\n{agent_src.read_text(encoding='utf-8').strip()}\n"
            append_once(agents_path, marker, content)

    if args.dry_run:
        print(f"Dry run for skillset '{args.skillset}'.")
        print(f"Codex home: {codex_home}")
        print("Skills:")
        for skill in skills:
            print(f"  - {skill} -> {target_skills / skill}")
        if presets:
            print("MCP presets:")
            for preset in presets:
                print(f"  - {preset}")
            print("MCP servers:")
            for server in unique(server_names):
                print(f"  - {server} -> {config_path}")
        if agents_file:
            print(f"Agents file: {agents_file} -> {codex_home / 'AGENTS.md'}")
        return

    print(f"Installed skillset '{args.skillset}' with {len(skills)} skills.")
    if presets:
        print("MCP config changed or verified. Restart Codex if new MCP servers do not appear immediately.")


if __name__ == "__main__":
    main()
