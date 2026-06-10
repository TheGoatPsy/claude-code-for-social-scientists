"""Command line installer for the Claude Code for Social Scientists project skills.

The skills are bundled into this package at build time from the repository's
``.claude/skills`` directory. ``social-cc install`` copies them into a Claude
configuration directory so they are discoverable as project or user skills.
"""

from __future__ import annotations

import argparse
import contextlib
import shutil
import sys
from collections.abc import Iterator
from importlib import resources
from pathlib import Path

from . import __version__

SKILLS_PACKAGE = "social_cc_plugin"
SKILLS_DIRNAME = "skills"


def _emit(message: str) -> None:
    """Write a line of user-facing output. CLI output is the tool's interface."""
    print(message)


@contextlib.contextmanager
def _bundled_source() -> Iterator[Path | None]:
    """Yield a real path to the bundled skills directory, or ``None`` if absent.

    When the package is run from a source checkout (skills not yet bundled by
    the build), the directory does not exist and ``None`` is yielded.
    """
    root = resources.files(SKILLS_PACKAGE).joinpath(SKILLS_DIRNAME)
    if not root.is_dir():
        yield None
        return
    with resources.as_file(root) as real:
        yield Path(real)


def list_skill_names(source: Path) -> list[str]:
    """Return the sorted names of skill directories under ``source``."""
    return sorted(entry.name for entry in source.iterdir() if entry.is_dir())


def install_skills(
    source: Path,
    target_root: Path,
    *,
    force: bool,
    dry_run: bool,
) -> tuple[int, int]:
    """Copy each skill directory from ``source`` into ``target_root``.

    Returns a ``(installed, skipped)`` count. Existing skills are skipped unless
    ``force`` is set. With ``dry_run`` nothing is written.
    """
    installed = 0
    skipped = 0
    for name in list_skill_names(source):
        dest = target_root / name
        if dest.exists() and not force:
            _emit(f"skip    {name} (exists, use --force to overwrite)")
            skipped += 1
            continue
        if dry_run:
            _emit(f"plan    {name}")
            installed += 1
            continue
        if dest.exists():
            shutil.rmtree(dest)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source / name, dest)
        _emit(f"install {name}")
        installed += 1
    return installed, skipped


def _target_root(project: bool) -> Path:
    base = Path.cwd() if project else Path.home()
    return base / ".claude" / "skills"


def _run_install(*, project: bool, force: bool, dry_run: bool) -> int:
    with _bundled_source() as source:
        if source is None:
            _emit("No bundled skills found. The package may be installed incorrectly.")
            return 1
        target_root = _target_root(project)
        _emit(f"Target: {target_root}")
        installed, skipped = install_skills(
            source, target_root, force=force, dry_run=dry_run
        )
        verb = "would install" if dry_run else "installed"
        _emit(f"{verb} {installed}, skipped {skipped}")
        return 0


def _run_list() -> int:
    with _bundled_source() as source:
        if source is None:
            _emit("No bundled skills found.")
            return 1
        names = list_skill_names(source)
        _emit(f"{len(names)} bundled skills:")
        for name in names:
            _emit(f"  {name}")
        return 0


def doctor_report(
    target_root: Path,
    bundled: list[str] | None,
    tools: dict[str, str | None],
    *,
    python_ok: bool,
) -> tuple[list[str], int]:
    """Build the doctor report lines and an exit code.

    ``tools`` maps tool names to resolved paths or ``None``. The exit code is 1
    when a required check fails. Missing optional tools are reported as
    warnings and do not fail the run.
    """
    lines: list[str] = []
    exit_code = 0
    if python_ok:
        lines.append("ok    python 3.9 or newer")
    else:
        lines.append("FAIL  python 3.9 or newer is required")
        exit_code = 1
    hints = {
        "claude": "install Claude Code, see booklet 001-01-0003",
        "git": "version control for reproducible research",
        "node": "needed only for repository validation work",
    }
    for tool, hint in hints.items():
        if tools.get(tool):
            lines.append(f"ok    {tool} on PATH")
        else:
            lines.append(f"warn  {tool} not found ({hint})")
    if target_root.is_dir():
        installed = sorted(p.name for p in target_root.iterdir() if p.is_dir())
    else:
        installed = []
    if bundled is None:
        lines.append("warn  bundled skills not found (source checkout?)")
        lines.append(f"info  {len(installed)} skills present at the target")
    else:
        missing = [name for name in bundled if name not in installed]
        if missing:
            lines.append(
                f"warn  {len(missing)} of {len(bundled)} bundled skills not installed,"
                " run social-cc install"
            )
        else:
            lines.append(f"ok    all {len(bundled)} bundled skills installed")
    return lines, exit_code


def _run_doctor(*, project: bool) -> int:
    with _bundled_source() as source:
        bundled = list_skill_names(source) if source is not None else None
    target_root = _target_root(project)
    tools: dict[str, str | None] = {
        name: shutil.which(name) for name in ("claude", "git", "node")
    }
    lines, exit_code = doctor_report(
        target_root, bundled, tools, python_ok=sys.version_info >= (3, 9)
    )
    _emit(f"Target: {target_root}")
    for line in lines:
        _emit(line)
    return exit_code


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="social-cc",
        description="Install the Claude Code for Social Scientists project skills.",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    install_parser = sub.add_parser(
        "install", help="Copy the bundled skills into a Claude configuration."
    )
    install_parser.add_argument(
        "--project",
        action="store_true",
        help="Install into ./.claude/skills instead of the user home configuration.",
    )
    install_parser.add_argument(
        "--force", action="store_true", help="Overwrite existing skill directories."
    )
    install_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be installed without writing.",
    )

    sub.add_parser("list", help="List the bundled skills.")

    doctor_parser = sub.add_parser(
        "doctor", help="Check the environment the guide's workflows expect."
    )
    doctor_parser.add_argument(
        "--project",
        action="store_true",
        help="Check ./.claude/skills instead of the user home configuration.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "install":
        return _run_install(
            project=args.project, force=args.force, dry_run=args.dry_run
        )
    if args.command == "doctor":
        return _run_doctor(project=args.project)
    return _run_list()


if __name__ == "__main__":
    raise SystemExit(main())
