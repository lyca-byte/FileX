"""Tests for output path handling."""

import pytest

from filex.core.output import get_output_path
from filex.exceptions import FileXError


def test_default_output_path(tmp_path):
    source = tmp_path / "photo.png"
    source.write_bytes(b"input")

    result = get_output_path(source, "webp")

    assert result == source.with_suffix(".webp")


def test_output_directory(tmp_path):
    source = tmp_path / "photo.png"
    source.write_bytes(b"input")

    output_dir = tmp_path / "output"
    output_dir.mkdir()

    result = get_output_path(
        source,
        "webp",
        output_dir=output_dir,
    )

    assert result == output_dir / "photo.webp"


def test_reject_existing_output(tmp_path):
    source = tmp_path / "photo.png"
    source.write_bytes(b"input")

    destination = tmp_path / "photo.webp"
    destination.write_bytes(b"existing")

    with pytest.raises(FileXError, match="already exists"):
        get_output_path(source, "webp")


def test_reject_wrong_output_extension(tmp_path):
    source = tmp_path / "photo.png"
    source.write_bytes(b"input")

    with pytest.raises(FileXError, match="extension"):
        get_output_path(
            source,
            "webp",
            output_path=tmp_path / "result.png",
        )