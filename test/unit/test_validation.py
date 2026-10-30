# """Tests for input and format validation."""

# import pytest

# from filex.core.validation import validate_input, validate_target_format
# from filex.exceptions import FileXError


# @pytest.mark.parametrize("extension", ["png", "jpg", "docx", "pdf", "odt", "rtf", "txt"])
# def test_validate_supported_input_formats(tmp_path, extension):
#     path = tmp_path / f"sample.{extension}"
#     path.write_bytes(b"test")
#     assert validate_input(path) == extension


# def test_reject_missing_file(tmp_path):
#     with pytest.raises(FileXError, match="does not exist"):
#         validate_input(tmp_path / "missing.png")


# def test_reject_unsupported_input_format(tmp_path):
#     path = tmp_path / "document.csv"
#     path.write_bytes(b"test")
#     with pytest.raises(FileXError, match="Unsupported input format"):
#         validate_input(path)


# def test_normalize_jpeg_target():
#     assert validate_target_format("JPEG") == "jpg"


# @pytest.mark.parametrize("extension", ["docx", "pdf", "odt", "rtf", "txt"])
# def test_validate_supported_document_targets(extension):
#     assert validate_target_format(extension.upper()) == extension


# def test_reject_unsupported_target():
#     with pytest.raises(FileXError, match="Unsupported target format"):
#         validate_target_format("csv")



"""Tests for input and format validation."""

import pytest

from filex.core.validation import validate_input, validate_target_format
from filex.exceptions import FileXError


@pytest.mark.parametrize("extension", ["png", "jpg", "docx", "pdf", "odt", "rtf", "txt", "pptx", "xlsx", "ods"])
def test_validate_supported_input_formats(tmp_path, extension):
    path = tmp_path / f"sample.{extension}"
    path.write_bytes(b"test")
    assert validate_input(path) == extension


def test_reject_missing_file(tmp_path):
    with pytest.raises(FileXError, match="does not exist"):
        validate_input(tmp_path / "missing.png")


def test_reject_unsupported_input_format(tmp_path):
    path = tmp_path / "document.csv"
    path.write_bytes(b"test")
    with pytest.raises(FileXError, match="Unsupported input format"):
        validate_input(path)


def test_normalize_jpeg_target():
    assert validate_target_format("JPEG") == "jpg"


@pytest.mark.parametrize("extension", ["docx", "pdf", "odt", "rtf", "txt", "pptx", "xlsx", "ods"])
def test_validate_supported_document_targets(extension):
    assert validate_target_format(extension.upper()) == extension


def test_reject_unsupported_target():
    with pytest.raises(FileXError, match="Unsupported target format"):
        validate_target_format("csv")
