"""Installation boundary tests; no access to the real Codex home."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
INSTALLER = REPO / "scripts" / "install-skillset.py"


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="agentskills-scope-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.home = self.root / "home"
        self.project = self.root / "project"
        self.project.mkdir()

    def run_install(self, skillset="global-foundation", *options, source=REPO):
        return subprocess.run(
            [sys.executable, str(INSTALLER), "--repo-root", str(source),
             "--skillset", skillset, "--codex-home", str(self.home), *options],
            text=True, capture_output=True,
        )

    def assert_ok(self, result):
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_user_preserves_instructions_config_and_managed_skills(self):
        self.home.mkdir()
        (self.home / "AGENTS.md").write_bytes(b"Universal contract\r\n")
        (self.home / "config.toml").write_bytes(b'model = "existing"\r\n')
        managed = self.home / "skills" / ".system"
        managed.mkdir(parents=True)
        (managed / "sentinel").write_bytes(b"managed")
        for _ in range(2):
            self.assert_ok(self.run_install())
            self.assertEqual((self.home / "AGENTS.md").read_bytes(), b"Universal contract\r\n")
            self.assertEqual((self.home / "config.toml").read_bytes(), b'model = "existing"\r\n')
            self.assertEqual((managed / "sentinel").read_bytes(), b"managed")
            self.assertEqual(len(list((self.home / "skills").glob("*/SKILL.md"))), 13)
        self.assert_ok(self.run_install("agentops-evaluation"))
        self.assertEqual(len(list((self.home / "skills").glob("*/SKILL.md"))), 17)

    def test_defaults_do_not_enable_mcp_or_routing(self):
        self.assert_ok(self.run_install("game-dev"))
        self.assertFalse((self.home / "config.toml").exists())
        self.assertFalse((self.home / "AGENTS.md").exists())

    def test_dry_run_has_no_side_effects(self):
        self.assert_ok(self.run_install("game-dev", "--dry-run", "--with-mcp"))
        self.assertFalse(self.home.exists())
        self.assert_ok(self.run_install("game-dev", "--scope", "project", "--project-root", str(self.project), "--with-mcp", "--with-agents", "--dry-run"))
        self.assertEqual(list(self.project.iterdir()), [])

    def test_user_routing_rejected(self):
        result = self.run_install("game-dev", "--with-agents")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.home.exists())

    def test_project_install_and_opt_ins_are_isolated_and_idempotent(self):
        args = ("--scope", "project", "--project-root", str(self.project))
        self.assert_ok(self.run_install("game-dev", *args))
        self.assertTrue((self.project / ".agents/skills/game-3d-development/SKILL.md").exists())
        self.assertFalse((self.project / ".codex").exists())
        (self.project / "AGENTS.md").write_text("Project contract\n", encoding="utf-8")
        for _ in range(2):
            self.assert_ok(self.run_install("game-dev", *args, "--with-mcp", "--with-agents"))
        text = (self.project / "AGENTS.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("Project contract\n"))
        self.assertEqual(text.count("# AgentSkills skillset: game-dev"), 1)
        config = (self.project / ".codex/config.toml").read_text(encoding="utf-8")
        self.assertEqual(config.count("[mcp_servers.playwright]"), 1)
        self.assertFalse(self.home.exists())

    def test_missing_source_fails_before_existing_skill_is_changed(self):
        source = self.root / "source"
        (source / "skillsets").mkdir(parents=True)
        shutil.copytree(REPO / "skills/pr-review", source / "skills/pr-review")
        (source / "skillsets/broken.yaml").write_text("skills:\n  - pr-review\n  - missing-skill\n", encoding="utf-8")
        sentinel = self.home / "skills/pr-review/SKILL.md"
        sentinel.parent.mkdir(parents=True)
        sentinel.write_bytes(b"local edits")
        result = self.run_install("broken", source=source)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(sentinel.read_bytes(), b"local edits")

    def test_path_traversal_rejected_without_writes(self):
        result = self.run_install("../all")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.home.exists())


if __name__ == "__main__":
    unittest.main()
