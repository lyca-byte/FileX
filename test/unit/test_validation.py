
"""Tests for input and format validation."""

import pytest

from filex.core.validation import (
    validate_input,
    validate_target_format,
)
from filex.exceptions import FileXError


def test_validate_existing_png(tmp_path):
    image_path = tmp_path / "sample.png"
    image_path.write_bytes(b"test")

    assert validate_input(image_path) == "png"


def test_reject_missing_file(tmp_path):
    with pytest.raises(FileXError, match="does not exist"):
        validate_input(tmp_path / "missing.png")


def test_reject_unsupported_input_format(tmp_path):
    path = tmp_path / "document.txt"
    path.write_bytes(b"test")

    with pytest.raises(FileXError, match="Unsupported input format"):
        validate_input(path)


def test_normalize_jpeg_target():
    assert validate_target_format("JPEG") == "jpg"


def test_reject_unsupported_target():
    with pytest.raises(FileXError, match="Unsupported target format"):
        validate_target_format("txt")


def test_validate_docx_input(tmp_path):
    path = tmp_path / "document.docx"
    path.write_bytes(b"test")

    assert validate_input(path) == "docx"


def test_validate_pdf_target():
    assert validate_target_format("PDF") == "pdf"
