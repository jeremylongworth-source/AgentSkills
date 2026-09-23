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
    parser.add_argument("--codex-home")
    parser.add_argument("--scope", choices=("user", "project"), default="user")
    parser.add_argument("--project-root")
    parser.add_argument("--with-mcp", action="store_true")
    parser.add_argument("--with-agents", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", args.skillset):
        parser.error("Invalid skillset name")
    if args.scope == "project":
        if not args.project_root:
            parser.error("Project scope requires --project-root")
        project_root = Path(args.project_root).resolve()
        if not project_root.is_dir():
            parser.error("Project root must be an existing directory")
        if args.codex_home and project_root == Path(args.codex_home).resolve():
            parser.error("Project root must not be the Codex home")
        target_skills = project_root / ".agents" / "skills"
        config_path = project_root / ".codex" / "config.toml"
        agents_path = project_root / "AGENTS.md"
        scope_root = project_root
    else:
        if not args.codex_home:
            parser.error("User scope requires --codex-home")
        if args.project_root or args.with_agents:
            parser.error("Project routing requires --scope project; global AGENTS.md is never changed")
        codex_home = Path(args.codex_home).resolve()
        target_skills = codex_home / "skills"
        config_path = codex_home / "config.toml"
        agents_path = None
        scope_root = codex_home
    manifest_path = repo_root / "skillsets" / f"{args.skillset}.yaml"
    if not manifest_path.exists():
        raise SystemExit(f"Unknown skillset: {args.skillset}")

    manifest = parse_manifest(manifest_path)
    skills: list[str] = manifest["skills"]  # type: ignore[assignment]
    presets: list[str] = manifest["mcp_presets"] if args.with_mcp else []  # type: ignore[assignment]
    agents_file = manifest["agents_file"] if args.with_agents else None

    # Validate every source and destination before changing the installation.
    destinations: list[tuple[Path, Path]] = []
    expected_root = target_skills.parent.resolve()
    if (not target_skills.resolve().is_relative_to(scope_root)
            or target_skills.resolve().parent != expected_root
            or target_skills.is_symlink()
            or getattr(target_skills, "is_junction", lambda: False)()):
        raise SystemExit(f"Refusing redirected skills directory: {target_skills}")
    for path in ([config_path] if args.with_mcp else []) + ([agents_path] if agents_file else []):
        if path is not None and (not path.resolve().is_relative_to(scope_root) or path.is_symlink()):
            raise SystemExit(f"Refusing redirected configuration destination: {path}")
    for skill in skills:
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", skill):
            raise SystemExit(f"Invalid skill name: {skill}")
        src = repo_root / "skills" / skill
        if not (src / "SKILL.md").exists():
            raise SystemExit(f"Missing skill folder: {src}")
        dst = target_skills / skill
        if dst.exists() and not dst.is_dir():
            raise SystemExit(f"Skill destination is not a directory: {dst}")
        if (dst.resolve().parent != target_skills.resolve() or dst.is_symlink()
                or getattr(dst, "is_junction", lambda: False)()):
            raise SystemExit(f"Refusing redirected skill destination: {dst}")
        if src.resolve() == dst.resolve() or src.resolve().is_relative_to(dst.resolve()):
            raise SystemExit(f"Installation would overwrite its source: {dst}")
        destinations.append((src, dst))

    server_names: list[str] = []
    for preset in presets:
        preset_path = repo_root / "mcp" / "presets" / f"{preset}.toml"
        if not preset_path.exists():
            raise SystemExit(f"Missing MCP preset: {preset_path}")
        servers = parse_preset_servers(preset_path)
        if not servers:
            raise SystemExit(f"MCP preset has no servers: {preset_path}")
        server_names.extend(servers)

    snippets: list[tuple[str, Path]] = []
    for server in unique(server_names):
        snippet = repo_root / "mcp" / "servers" / f"{server}.toml"
        if not snippet.exists():
            raise SystemExit(f"Missing MCP server snippet: {snippet}")
        snippets.append((server, snippet))

    if agents_file:
        agent_src = repo_root / str(agents_file)
        if not agent_src.exists():
            raise SystemExit(f"Missing agents file: {agent_src}")

    if args.dry_run:
        print(f"Dry run for skillset '{args.skillset}'.")
        print(f"Scope: {args.scope}; skills directory: {target_skills}")
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
            print(f"Project routing: {agents_file} -> {agents_path}")
        return

    target_skills.mkdir(parents=True, exist_ok=True)
    for src, dst in destinations:
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
    for server, snippet in snippets:
        config_path.parent.mkdir(parents=True, exist_ok=True)
        append_once(config_path, f"[mcp_servers.{server}]", "\n" + snippet.read_text(encoding="utf-8").strip() + "\n")
    if agents_file:
        assert agents_path is not None
        marker = f"AgentSkills skillset: {args.skillset}"
        content = f"\n# {marker}\n{agent_src.read_text(encoding='utf-8').strip()}\n"
        append_once(agents_path, marker, content)

    print(f"Installed skillset '{args.skillset}' with {len(skills)} skills.")
    if presets:
        print("MCP config changed or verified. Restart Codex if new MCP servers do not appear immediately.")


if __name__ == "__main__":
    main()
