"""Tests for the social-cc-plugin installer business logic."""

from __future__ import annotations

import re
from pathlib import Path

import pytest

import social_cc_plugin
from social_cc_plugin import cli


def _make_source(tmp_path: Path) -> Path:
    source = tmp_path / "skills"
    for name in ("alpha-skill", "beta-skill"):
        skill_dir = source / name
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text("# test skill\n", encoding="utf-8")
    return source


def test_list_skill_names_sorted(tmp_path: Path) -> None:
    source = _make_source(tmp_path)
    assert cli.list_skill_names(source) == ["alpha-skill", "beta-skill"]


def test_install_copies_all(tmp_path: Path) -> None:
    source = _make_source(tmp_path)
    target = tmp_path / "out"
    installed, skipped = cli.install_skills(source, target, force=False, dry_run=False)
    assert (installed, skipped) == (2, 0)
    assert (target / "alpha-skill" / "SKILL.md").read_text(encoding="utf-8") == "# test skill\n"


def test_install_skips_existing(tmp_path: Path) -> None:
    source = _make_source(tmp_path)
    target = tmp_path / "out"
    cli.install_skills(source, target, force=False, dry_run=False)
    installed, skipped = cli.install_skills(source, target, force=False, dry_run=False)
    assert (installed, skipped) == (0, 2)


def test_install_force_overwrites(tmp_path: Path) -> None:
    source = _make_source(tmp_path)
    target = tmp_path / "out"
    cli.install_skills(source, target, force=False, dry_run=False)
    installed, skipped = cli.install_skills(source, target, force=True, dry_run=False)
    assert (installed, skipped) == (2, 0)


def test_dry_run_writes_nothing(tmp_path: Path) -> None:
    source = _make_source(tmp_path)
    target = tmp_path / "out"
    installed, skipped = cli.install_skills(source, target, force=False, dry_run=True)
    assert (installed, skipped) == (2, 0)
    assert not target.exists()


def test_main_list_without_bundle_returns_one() -> None:
    # In the source checkout the skills are not bundled, so list reports nothing.
    assert cli.main(["list"]) == 1


def test_main_version_exits_zero() -> None:
    with pytest.raises(SystemExit) as exc:
        cli.main(["--version"])
    assert exc.value.code == 0


def test_version_matches_pyproject() -> None:
    # Guards against the package version drifting from the release cascade.
    pyproject = Path(__file__).resolve().parents[1] / "pyproject.toml"
    match = re.search(r'^version = "(.+)"$', pyproject.read_text(encoding="utf-8"), re.M)
    assert match is not None
    assert social_cc_plugin.__version__ == match.group(1)


def test_doctor_report_all_ok(tmp_path: Path) -> None:
    target = tmp_path / "skills"
    for name in ("alpha-skill", "beta-skill"):
        (target / name).mkdir(parents=True)
    tools = {"claude": "/usr/bin/claude", "git": "/usr/bin/git", "node": "/usr/bin/node"}
    lines, exit_code = cli.doctor_report(
        target, ["alpha-skill", "beta-skill"], tools, python_ok=True
    )
    assert exit_code == 0
    assert "ok    all 2 bundled skills installed" in lines


def test_doctor_report_missing_skills_warns(tmp_path: Path) -> None:
    target = tmp_path / "skills"
    tools = {"claude": None, "git": "/usr/bin/git", "node": None}
    lines, exit_code = cli.doctor_report(
        target, ["alpha-skill", "beta-skill"], tools, python_ok=True
    )
    assert exit_code == 0
    assert any(line.startswith("warn  2 of 2 bundled skills not installed") for line in lines)
    assert any(line.startswith("warn  claude not found") for line in lines)


def test_doctor_report_old_python_fails(tmp_path: Path) -> None:
    lines, exit_code = cli.doctor_report(tmp_path, None, {}, python_ok=False)
    assert exit_code == 1
    assert lines[0].startswith("FAIL")


def test_main_doctor_runs_from_source_checkout(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    # No bundle in the source checkout: doctor still reports and exits zero.
    monkeypatch.setattr(cli.Path, "home", classmethod(lambda cls: tmp_path))
    assert cli.main(["doctor"]) == 0
