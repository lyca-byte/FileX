"""Tests for the FileX CLI."""

import sys

import pytest

from filex import __version__
from filex.cli import main


def test_help_option(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["filex", "--help"])

    with pytest.raises(SystemExit) as exc:
        main()

    assert exc.value.code == 0
    assert "Offline multi-format file converter" in capsys.readouterr().out


def test_version_option(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["filex", "--version"])

    with pytest.raises(SystemExit) as exc:
        main()

    assert exc.value.code == 0
    assert __version__ in capsys.readouterr().out


def test_missing_required_arguments(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["filex"])

    assert main() == 2
    assert "--file" in capsys.readouterr().err