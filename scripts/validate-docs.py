from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


LEGACY_SKILLSETS = {
    "all",
    "frontend-product",
    "game-dev",
    "html5-game-publishing",
    "llm-skill-authoring",
    "research-validation",
    "sales-marketing",
}


def skillset_names(repo_root: Path) -> set[str]:
    return {path.stem for path in (repo_root / "skillsets").glob("*.yaml")}


def skill_names(repo_root: Path) -> set[str]:
    return {
        path.name
        for path in (repo_root / "skills").iterdir()
        if path.is_dir() and (path / "SKILL.md").exists()
    }


def scenario_names(repo_root: Path) -> set[str]:
    return {path.stem for path in (repo_root / "tests" / "scenarios").glob("*.md")}


def markdown_links(path: Path) -> set[str]:
    if not path.exists():
        return set()
    text = path.read_text(encoding="utf-8")
    return set(re.findall(r"\]\(([^)]+)\)", text))


def linked_bundle_briefs(repo_root: Path) -> set[str]:
    readme = repo_root / "docs" / "bundles" / "README.md"
    if not readme.exists():
        return set()
    text = readme.read_text(encoding="utf-8")
    return {
        Path(match).stem
        for match in re.findall(r"\]\(([^)]+\.md)\)", text)
        if not match.startswith("../")
    }


def require_file(errors: list[str], repo_root: Path, relative_path: str) -> Path:
    path = repo_root / relative_path
    if not path.exists():
        errors.append(f"Missing file: {relative_path}")
    return path


def require_text(
    errors: list[str], path: Path, label: str, required: str, text: str | None = None
) -> None:
    content = path.read_text(encoding="utf-8") if text is None and path.exists() else text
    if content is None or required not in content:
        errors.append(f"{label}: missing '{required}'")


def require_count(errors: list[str], label: str, text: str, count: int) -> None:
    if not re.search(rf"\b{count}\b", text):
        errors.append(f"{label}: missing current count '{count}'")


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    names = skillset_names(repo_root)
    expanded = names - LEGACY_SKILLSETS
    skill_count = len(skill_names(repo_root))
    skillset_count = len(names)
    scenario_count = len(scenario_names(repo_root))
    expanded_count = len(expanded)

    readme_path = repo_root / "README.md"

    if not readme_path.exists():
        return [f"Missing README: {readme_path}"]

    readme = readme_path.read_text(encoding="utf-8")
    for name in sorted(names):
        if f"`{name}`" not in readme:
            errors.append(f"README.md: missing skillset '{name}'")

    linked = linked_bundle_briefs(repo_root)
    for name in sorted(expanded):
        if name not in linked:
            errors.append(f"docs/bundles/README.md: missing bundle brief link '{name}'")

    public_docs = [
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "CODE_OF_CONDUCT.md",
    ]
    readme_links = markdown_links(readme_path)
    for relative_path in public_docs:
        require_file(errors, repo_root, relative_path)
        if relative_path not in readme_links:
            errors.append(f"README.md: missing link to '{relative_path}'")

    release_notes_path = require_file(
        errors, repo_root, "docs/release-notes/v0.2.0.md"
    )
    rc_checklist_path = require_file(
        errors, repo_root, "docs/release-candidate-v0.2.md"
    )
    handoff_path = require_file(errors, repo_root, "docs/v0.2-release-handoff.md")
    changelog_path = require_file(errors, repo_root, "CHANGELOG.md")

    count_docs = [
        ("README.md", readme_path, readme),
        (
            "docs/release-notes/v0.2.0.md",
            release_notes_path,
            release_notes_path.read_text(encoding="utf-8")
            if release_notes_path.exists()
            else "",
        ),
        (
            "CHANGELOG.md",
            changelog_path,
            changelog_path.read_text(encoding="utf-8")
            if changelog_path.exists()
            else "",
        ),
        (
            "docs/release-candidate-v0.2.md",
            rc_checklist_path,
            rc_checklist_path.read_text(encoding="utf-8")
            if rc_checklist_path.exists()
            else "",
        ),
        (
            "docs/v0.2-release-handoff.md",
            handoff_path,
            handoff_path.read_text(encoding="utf-8") if handoff_path.exists() else "",
        ),
    ]
    for label, _path, text in count_docs:
        require_count(errors, label, text, skill_count)
        require_count(errors, label, text, skillset_count)
        require_count(errors, label, text, scenario_count)

    release_notes = release_notes_path.read_text(encoding="utf-8") if release_notes_path.exists() else ""
    require_count(errors, "docs/release-notes/v0.2.0.md", release_notes, expanded_count)
    require_text(
        errors,
        release_notes_path,
        "docs/release-notes/v0.2.0.md",
        "fresh Codex home install smoke passes",
        release_notes,
    )
    require_text(
        errors,
        release_notes_path,
        "docs/release-notes/v0.2.0.md",
        "`gh skill publish --dry-run` returns `ok`",
        release_notes,
    )
    require_text(
        errors,
        release_notes_path,
        "docs/release-notes/v0.2.0.md",
        "secret and local-path scans pass",
        release_notes,
    )
    require_text(
        errors,
        release_notes_path,
        "docs/release-notes/v0.2.0.md",
        "Recommended release state: prerelease",
        release_notes,
    )

    rc_checklist = (
        rc_checklist_path.read_text(encoding="utf-8")
        if rc_checklist_path.exists()
        else ""
    )
    require_text(
        errors,
        rc_checklist_path,
        "docs/release-candidate-v0.2.md",
        "Recommended release type: prerelease",
        rc_checklist,
    )
    require_text(
        errors,
        rc_checklist_path,
        "docs/release-candidate-v0.2.md",
        "Real-input packets remain deferred",
        rc_checklist,
    )

    handoff = handoff_path.read_text(encoding="utf-8") if handoff_path.exists() else ""
    require_text(
        errors,
        handoff_path,
        "docs/v0.2-release-handoff.md",
        "Local release gate: passed",
        handoff,
    )
    require_text(
        errors,
        handoff_path,
        "docs/v0.2-release-handoff.md",
        "Recommended release state: prerelease",
        handoff,
    )
    require_text(
        errors,
        handoff_path,
        "docs/v0.2-release-handoff.md",
        "`gh skill publish --dry-run` returning `ok`",
        handoff,
    )
    require_text(
        errors,
        handoff_path,
        "docs/v0.2-release-handoff.md",
        "Remote CI has to run after the next push or pull request.",
        handoff,
    )

    evaluation_readme = require_file(errors, repo_root, "docs/evaluation/README.md")
    evaluation_links = markdown_links(evaluation_readme)
    packets_dir = repo_root / "docs" / "evaluation" / "packets"
    reports_dir = repo_root / "docs" / "evaluation" / "reports"
    for packet in sorted(packets_dir.glob("*.md")):
        if packet.name == "README.md":
            continue
        target = f"packets/{packet.name}"
        if target not in evaluation_links:
            errors.append(f"docs/evaluation/README.md: missing packet link '{target}'")
    for report in sorted(reports_dir.glob("*.md")):
        target = f"reports/{report.name}"
        if target not in evaluation_links:
            errors.append(f"docs/evaluation/README.md: missing report link '{target}'")

    workflow = require_file(errors, repo_root, ".github/workflows/validation.yml")
    workflow_text = workflow.read_text(encoding="utf-8") if workflow.exists() else ""
    require_text(
        errors,
        workflow,
        ".github/workflows/validation.yml",
        "scripts\\release-check.ps1",
        workflow_text,
    )
    require_text(
        errors,
        workflow,
        ".github/workflows/validation.yml",
        "-SkipPublishDryRun",
        workflow_text,
    )

    github_docs = [
        ".github/pull_request_template.md",
        ".github/ISSUE_TEMPLATE/bug_report.md",
        ".github/ISSUE_TEMPLATE/skill_proposal.md",
        ".github/ISSUE_TEMPLATE/bundle_proposal.md",
        ".github/ISSUE_TEMPLATE/docs_fix.md",
        ".github/ISSUE_TEMPLATE/config.yml",
    ]
    for relative_path in github_docs:
        require_file(errors, repo_root, relative_path)

    docs_to_check = [
        repo_root / "docs" / "bundle-expansion-map.md",
        repo_root / "docs" / "bundle-expansion-decisions.md",
        repo_root / "docs" / "scope-broadening-roadmap.md",
        repo_root / "docs" / "release-owner-checklist.md",
        repo_root / "docs" / "release-candidate-v0.2.md",
        repo_root / "docs" / "v0.2-release-handoff.md",
    ]
    for path in docs_to_check:
        if not path.exists():
            errors.append(f"Missing docs file: {path.relative_to(repo_root)}")

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

    print("Validated docs consistency.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
