from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def clean_scalar(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def parse_manifest(path: Path) -> dict[str, object]:
    result: dict[str, object] = {
        "name": None,
        "description": None,
        "skills": [],
        "mcp_presets": [],
        "agents_file": None,
    }
    current: str | None = None

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue

        scalar = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$", line)
        if scalar:
            key, value = scalar.group(1), scalar.group(2).strip()
            if key in ("skills", "mcp_presets") and not value:
                current = key
            elif key in ("name", "description", "agents_file"):
                result[key] = clean_scalar(value)
                current = None
            else:
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


def find_duplicates(items: list[str]) -> list[str]:
    seen: set[str] = set()
    duplicates: list[str] = []
    for item in items:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    return duplicates


LEGACY_SKILLSETS = {
    "all",
    "frontend-product",
    "game-dev",
    "html5-game-publishing",
    "llm-skill-authoring",
    "research-validation",
    "sales-marketing",
}

REQUIRED_BUNDLE_BRIEF_HEADINGS = (
    "## Problem",
    "## Target User",
    "## Included Skills",
    "## Context Files",
    "## Safety Rules",
    "## Pilot Metrics",
    "## Acceptance Criteria",
)


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    skillsets_dir = repo_root / "skillsets"
    skills_dir = repo_root / "skills"
    presets_dir = repo_root / "mcp" / "presets"
    servers_dir = repo_root / "mcp" / "servers"
    bundle_docs_dir = repo_root / "docs" / "bundles"

    manifests = sorted(skillsets_dir.glob("*.yaml"))
    if not manifests:
        return [f"No skillset manifests found: {skillsets_dir}"]

    for manifest_path in manifests:
        manifest = parse_manifest(manifest_path)
        label = manifest_path.name
        name = manifest["name"]
        description = manifest["description"]
        skills: list[str] = manifest["skills"]  # type: ignore[assignment]
        presets: list[str] = manifest["mcp_presets"]  # type: ignore[assignment]
        agents_file = manifest["agents_file"]

        if not name:
            errors.append(f"{label}: missing name")
        elif name != manifest_path.stem:
            errors.append(f"{label}: name '{name}' does not match filename")

        if not description:
            errors.append(f"{label}: missing description")

        if not skills:
            errors.append(f"{label}: missing skills")

        if name == "all":
            actual_skills = sorted(
                path.name for path in skills_dir.iterdir() if (path / "SKILL.md").exists()
            )
            missing_from_all = sorted(set(actual_skills) - set(skills))
            extra_in_all = sorted(set(skills) - set(actual_skills))
            for skill in missing_from_all:
                errors.append(f"{label}: missing skill from all bundle '{skill}'")
            for skill in extra_in_all:
                errors.append(f"{label}: unknown skill in all bundle '{skill}'")

        for duplicate in find_duplicates(skills):
            errors.append(f"{label}: duplicate skill '{duplicate}'")

        for skill in skills:
            if not (skills_dir / skill / "SKILL.md").exists():
                errors.append(f"{label}: unknown skill '{skill}'")

        for duplicate in find_duplicates(presets):
            errors.append(f"{label}: duplicate MCP preset '{duplicate}'")

        for preset in presets:
            preset_path = presets_dir / f"{preset}.toml"
            if not preset_path.exists():
                errors.append(f"{label}: unknown MCP preset '{preset}'")
                continue

            servers = parse_preset_servers(preset_path)
            if not servers:
                errors.append(f"{label}: MCP preset '{preset}' has no servers")
                continue

            for server in servers:
                if not (servers_dir / f"{server}.toml").exists():
                    errors.append(
                        f"{label}: MCP preset '{preset}' references unknown server '{server}'"
                    )

        if agents_file and not (repo_root / str(agents_file)).exists():
            errors.append(f"{label}: unknown agents_file '{agents_file}'")

        if name and name not in LEGACY_SKILLSETS:
            brief_path = bundle_docs_dir / f"{name}.md"
            if not brief_path.exists():
                errors.append(f"{label}: missing bundle brief '{brief_path}'")
            else:
                brief_text = brief_path.read_text(encoding="utf-8")
                for heading in REQUIRED_BUNDLE_BRIEF_HEADINGS:
                    if heading not in brief_text:
                        errors.append(f"{label}: bundle brief missing heading '{heading}'")

    if bundle_docs_dir.exists():
        manifest_names = {path.stem for path in manifests}
        for brief_path in sorted(bundle_docs_dir.glob("*.md")):
            if brief_path.name == "README.md":
                continue
            if brief_path.stem not in manifest_names:
                errors.append(
                    f"docs/bundles/{brief_path.name}: no matching skillset manifest"
                )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    errors = validate(repo_root)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    count = len(list((repo_root / "skillsets").glob("*.yaml")))
    print(f"Validated {count} skillsets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
