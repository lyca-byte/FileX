"""Tests for the FileX CLI."""

import sys

import pytest

from filex import __version__
from filex.cli import main, build_parser


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


def test_mode_defaults_to_editable():
    parser = build_parser()
    args = parser.parse_args(
        ["--file", "input.pdf", "--to", "docx"]
    )

    assert args.mode == "editable"


@pytest.mark.parametrize("mode", ["editable", "visual"])
def test_valid_mode_options(mode):
    parser = build_parser()
    args = parser.parse_args(
        [
            "--file", "input.pdf",
            "--to", "docx",
            "--mode", mode,
        ]
    )

    assert args.mode == mode


def test_invalid_mode_is_rejected():
    parser = build_parser()

    with pytest.raises(SystemExit) as exc:
        parser.parse_args(
            [
                "--file", "input.pdf",
                "--to", "docx",
                "--mode", "unknown",
            ]
        )

    assert exc.value.code == 2
