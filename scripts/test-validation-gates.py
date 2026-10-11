#!/usr/bin/env python3
"""Exercise actual PowerShell gates with disposable, synthetic command results.

No network, installation, Git mutation, credentials or user configuration is used.
All available PowerShell hosts are tested; a missing host is an error, not a pass.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile

VALIDATORS = (
    "validate-skill-files.py", "validate-skillsets.py",
    "validate-scenarios.py", "validate-docs.py",
)
CHILDREN = ("validate-skills.ps1", "test-fresh-codex-home.ps1", "list-skillsets.ps1")
RELEASE_OK = "Release check complete."


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def ps_quote(value):
    return "'" + str(value).replace("'", "''") + "'"


def shim(path, executable, arguments=()):
    if os.name == "nt":
        path = path.with_suffix(".cmd")
        command = subprocess.list2cmdline([str(executable), *map(str, arguments)])
        write(path, "@echo off\n" + command + " %*\nexit /b %errorlevel%\n")
    else:
        command = " ".join(shlex.quote(str(x)) for x in (executable, *arguments))
        write(path, '#!/bin/sh\nexec ' + command + ' "$@"\n')
        path.chmod(0o700)
    return path


def windows_native_stub(root):
    """Build one synthetic native process with Windows PowerShell's built-in .NET.

    A batch-file rg stub is unsafe: cmd.exe can reinterpret regex pipes before
    the batch file starts. This process accepts the actual argv without a shell.
    """
    compiler_host = shutil.which("powershell.exe")
    if not compiler_host:
        raise RuntimeError("Windows PowerShell is required to build native test fixtures")
    source, executable = root / "command.cs", root / "command.exe"
    write(source, """using System;
using System.IO;
using System.Reflection;
public static class SyntheticCommand {
    public static int Main(string[] args) {
        string name = Path.GetFileNameWithoutExtension(Assembly.GetExecutingAssembly().Location);
        string variable;
        string fallback = "0";
        if (name == "git") {
            string operation = args.Length > 2 ? args[2].ToUpperInvariant() : "";
            variable = "GATE_GIT_" + operation + "_EXIT";
        } else if (name == "rg") {
            variable = "GATE_RG_EXIT";
            fallback = "1";
        } else if (name == "gh") {
            variable = "GATE_GH_EXIT";
        } else { return 99; }
        int code = Int32.Parse(Environment.GetEnvironmentVariable(variable) ?? fallback);
        if (name == "rg" && code == 0) Console.WriteLine("synthetic scan match");
        return code;
    }
}
""")
    command = "Add-Type -Path " + ps_quote(source) + " -OutputAssembly " + ps_quote(executable) + " -OutputType ConsoleApplication -ErrorAction Stop"
    result = subprocess.run([compiler_host, "-NoProfile", "-Command", command], capture_output=True, text=True, errors="replace", timeout=90)
    if result.returncode or not executable.is_file():
        raise RuntimeError("Native fixture compilation failed: " + result.stdout + result.stderr)
    return executable


def fixture(root, scripts, host, changes, native_stub=None):
    repo, bin_dir = root / "repo", root / "bin"
    bin_dir.mkdir(parents=True)
    (repo / "skills" / "synthetic-skill").mkdir(parents=True)
    write(repo / "skillsets" / "synthetic.yaml", "skills:\n  - synthetic-skill\n")
    for name in ("validate-skills.ps1", "release-check.ps1"):
        write(repo / "scripts" / name, (scripts / name).read_text(encoding="utf-8-sig"))
    validator = (
        "import os\nfrom pathlib import Path\nimport sys\n"
        "name = Path(__file__).name\nprint('validated: ' + name)\n"
        "sys.exit(23 if os.environ.get('GATE_FAIL_VALIDATOR') == name else 0)\n"
    )
    for name in (*VALIDATORS, "install-skillset.py"):
        write(repo / "scripts" / name, validator)
    write(repo / "tests" / "test_install_skillset.py", validator)
    for name in CHILDREN[1:] + ("install-skillset.ps1",):
        write(repo / "scripts" / name, "param([Parameter(ValueFromRemainingArguments=$true)][object[]]$Rest)\nexit 0\n")
    command = root / "command.py"
    write(command, """import os
import sys
name, args = sys.argv[1], sys.argv[2:]
if name == 'git':
    action = args[2] if len(args) > 2 else (args[0] if args else '')
    code = int(os.environ.get('GATE_GIT_' + action.upper() + '_EXIT', '0'))
elif name == 'rg':
    code = int(os.environ.get('GATE_RG_EXIT', '1'))
    if code == 0:
        print('synthetic scan match')
elif name == 'gh':
    code = int(os.environ.get('GATE_GH_EXIT', '0'))
else:
    raise SystemExit('unexpected synthetic command')
raise SystemExit(code)
""")
    python_shim = shim(bin_dir / "python", sys.executable)
    # Use a real native process on Windows so regex pipes reach argv unchanged.
    for name in ("git", "rg", "gh"):
        if native_stub:
            shutil.copyfile(native_stub, bin_dir / (name + ".exe"))
        else:
            shim(bin_dir / name, sys.executable, (command, name))
    shim(bin_dir / "pwsh", host)
    env = os.environ.copy()
    for name in tuple(env):
        if name.startswith("GATE_"):
            del env[name]
    # USERPROFILE takes precedence in validate-skills on every tested OS. Only
    # this child process receives the synthetic home; no real home is changed.
    env["USERPROFILE"] = str(root / "synthetic-profile")
    env["PATH"] = str(bin_dir)
    env["GATE_RG_EXIT"] = "1"
    for name, value in changes.get("env", {}).items():
        env[name] = str(value)
    if changes.get("missing_rg"):
        (bin_dir / ("rg.exe" if os.name == "nt" else "rg")).unlink()
    if changes.get("missing_python"):
        python_shim.unlink()
    if changes.get("external"):
        external = Path(env["USERPROFILE"]) / ".codex/skills/.system/skill-creator/scripts/quick_validate.py"
        content = "import agentskills_synthetic_unavailable_runtime\n" if changes["external"] == "missing-runtime" else "print('synthetic external validator failure')\nraise SystemExit(23)\n"
        write(external, content)
    if changes.get("child"):
        content = "throw 'synthetic child failure'\n" if changes.get("throw") else "exit 23\n"
        write(repo / "scripts" / changes["child"], content)
    return repo, env


def cases():
    result = [
        ("validators-positive-external-absent", "validate-skills.ps1", {}, True, "External skill validator not found", None),
        ("release-positive-rg1-preference-false", "release-check.ps1", {}, True, RELEASE_OK, None),
        ("release-positive-rg1-preference-true", "release-check.ps1", {"preference": True}, True, RELEASE_OK, None),
    ]
    for validator in VALIDATORS:
        change = {"env": {"GATE_FAIL_VALIDATOR": validator}}
        result.append(("validator-fails-" + validator, "validate-skills.ps1", change, False, validator, None))
        result.append(("parent-validator-fails-" + validator, "release-check.ps1", change, False, validator, "ok: skill and skillset validation"))
    result += [
        ("external-present-fails", "validate-skills.ps1", {"external": "fails"}, False, "External skill validator", None),
        ("external-present-runtime-missing", "validate-skills.ps1", {"external": "missing-runtime"}, False, "agentskills_synthetic_unavailable_runtime", None),
        ("external-present-python-missing", "validate-skills.ps1", {"external": "fails", "missing_python": True}, False, "python", None),
        ("parent-external-runtime-missing", "release-check.ps1", {"external": "missing-runtime"}, False, "agentskills_synthetic_unavailable_runtime", "ok: skill and skillset validation"),
        ("validator-fails-preference-true", "validate-skills.ps1", {"preference": True, "env": {"GATE_FAIL_VALIDATOR": VALIDATORS[0]}}, False, VALIDATORS[0], None),
        ("installer-native-fails", "release-check.ps1", {"env": {"GATE_FAIL_VALIDATOR": "install-skillset.py"}}, False, "install dry run", "ok: skillset install dry runs"),
        ("installer-regression-native-fails", "release-check.ps1", {"env": {"GATE_FAIL_VALIDATOR": "test_install_skillset.py"}}, False, "Installer regression tests failed", "ok: installer scope and preservation regression tests"),
    ]
    for child in CHILDREN:
        label = {"validate-skills.ps1": "skill and skillset validation", "test-fresh-codex-home.ps1": "fresh Codex home install smoke", "list-skillsets.ps1": "skillset listing"}[child]
        result.append(("child-exit23-" + child, "release-check.ps1", {"child": child}, False, "exit code 23", "ok: " + label))
    result += [
        ("child-throws", "release-check.ps1", {"child": CHILDREN[1], "throw": True}, False, "synthetic child failure", "ok: fresh Codex home install smoke"),
        ("git-diff-fails", "release-check.ps1", {"env": {"GATE_GIT_DIFF_EXIT": 23}}, False, "git diff whitespace failed", "ok: git diff whitespace"),
        ("git-status-fails", "release-check.ps1", {"env": {"GATE_GIT_STATUS_EXIT": 23}}, False, "git status summary failed", "ok: git status summary"),
        ("gh-native-fails", "release-check.ps1", {"publish": True, "env": {"GATE_GH_EXIT": 23}}, False, "gh skill publish dry run failed", "ok: gh skill publish dry run"),
        ("rg-match0-fails", "release-check.ps1", {"env": {"GATE_RG_EXIT": 0}}, False, "secret scan found matches", "ok: secret scan"),
        ("rg-error2-fails", "release-check.ps1", {"env": {"GATE_RG_EXIT": 2}}, False, "secret scan scan failed with exit code 2", "ok: secret scan"),
        ("rg-missing-blocks", "release-check.ps1", {"missing_rg": True}, False, "rg not found", "ok: secret scan"),
    ]
    return result


def run_case(root, scripts, host, case, legacy=False, native_stub=None):
    name, gate, changes, expected_success, required, forbidden = case
    repo, env = fixture(root, scripts, host, changes, native_stub)
    runner = root / "runner.ps1"
    preference = "$true" if changes.get("preference") else "$false"
    invoke = "& " + ps_quote(repo / "scripts" / gate) + " -RepoRoot " + ps_quote(repo)
    if gate == "release-check.ps1" and not changes.get("publish"):
        invoke += " -SkipPublishDryRun"
    write(runner, "$ErrorActionPreference = 'Stop'\n$PSNativeCommandUseErrorActionPreference = " + preference + "\n" + invoke + "\n")
    args = [str(host), "-NoProfile"]
    if os.name == "nt":
        args += ["-ExecutionPolicy", "Bypass"]
    args += ["-File", str(runner)]
    completed = subprocess.run(args, env=env, cwd=repo, capture_output=True, text=True, errors="replace", timeout=90)
    output = completed.stdout + completed.stderr
    if legacy:
        passed = completed.returncode == 0 and (gate != "release-check.ps1" or RELEASE_OK in output)
    else:
        passed = (completed.returncode == 0) == expected_success and required in output
        if forbidden:
            passed = passed and forbidden not in output
        if not expected_success and gate == "release-check.ps1":
            passed = passed and RELEASE_OK not in output
        if name == "validators-positive-external-absent":
            passed = passed and all("validated: " + validator in output for validator in VALIDATORS)
    record = {"case": name, "host": Path(host).name, "legacy_characterization": legacy, "expected": "legacy false pass" if legacy else ("pass" if expected_success else "failure"), "actual_exit": completed.returncode, "passed": passed, "stdout": completed.stdout, "stderr": completed.stderr}
    for stream in ("stdout", "stderr"):
        record[stream + "_sha256"] = hashlib.sha256(record[stream].encode("utf-8")).hexdigest()
    print(("PASS" if passed else "FAIL") + ": " + record["host"] + " / " + name + (" (legacy false pass reproduced)" if legacy else ""), flush=True)
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--powershell-host", action="append", default=[])
    parser.add_argument("--legacy-scripts-dir", type=Path)
    parser.add_argument("--temp-root", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    hosts = args.powershell_host or [path for name in ("pwsh", "powershell.exe") if (path := shutil.which(name))]
    hosts = list(dict.fromkeys(str(Path(host).resolve()) for host in hosts))
    if not hosts or any(not Path(host).is_file() for host in hosts):
        parser.error("A working PowerShell host is required; no host tests were performed.")
    scripts = Path(__file__).resolve().parent
    temp_base = (args.temp_root or Path(tempfile.gettempdir())).resolve()
    temp_base.mkdir(parents=True, exist_ok=True)
    root = Path(tempfile.mkdtemp(prefix="agentskills-gate-regression-", dir=temp_base)).resolve()
    records = []
    try:
        native_stub = windows_native_stub(root) if os.name == "nt" else None
        for host_index, host in enumerate(hosts):
            for index, case in enumerate(cases()):
                records.append(run_case(root / ("fixed-" + str(host_index) + "-" + str(index)), scripts, host, case, native_stub=native_stub))
            if args.legacy_scripts_dir:
                wanted = {"validator-fails-" + VALIDATORS[0], "parent-validator-fails-" + VALIDATORS[0], "child-exit23-" + CHILDREN[0], "git-diff-fails", "git-status-fails", "gh-native-fails", "rg-missing-blocks"}
                for index, case in enumerate(case for case in cases() if case[0] in wanted):
                    records.append(run_case(root / ("legacy-" + str(host_index) + "-" + str(index)), args.legacy_scripts_dir.resolve(), host, case, legacy=True, native_stub=native_stub))
    finally:
        # Delete only the exact disposable directory created above, after checking
        # its resolved parent and generated identity. No shell deletion is used.
        if root.parent != temp_base or not root.name.startswith("agentskills-gate-regression-"):
            raise RuntimeError("Refusing cleanup outside the exact disposable fixture root")
        shutil.rmtree(root)
    report = {"status": "PASS" if all(r["passed"] for r in records) else "FAIL", "power_shell_hosts": [Path(host).name for host in hosts], "cases_per_host": len(cases()), "executed_checks": len(records), "passed_checks": sum(r["passed"] for r in records), "legacy_false_passes_reproduced": sum(r["legacy_characterization"] and r["passed"] for r in records), "fixture_cleanup_verified": not root.exists(), "scope": "Synthetic gate exit propagation only; no real install, Git mutation, publication or cross-OS qualification.", "results": records}
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("Gate regression result: " + report["status"] + " (" + str(report["passed_checks"]) + "/" + str(report["executed_checks"]) + ")")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
