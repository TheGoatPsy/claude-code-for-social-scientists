"""Installer for the Claude Code for Social Scientists project skills."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("social-cc-plugin")
except PackageNotFoundError:  # running from a source checkout
    __version__ = "3.0.0"
