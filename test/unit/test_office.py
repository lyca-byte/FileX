
"""Tests for document conversion routing."""

import pytest

from filex.converters.office import OfficeConverter
from filex.core.router import get_converter
from filex.exceptions import FileXError


@pytest.mark.parametrize(
    ("source", "target"),
    [("docx", "pdf"), ("pdf", "docx")],
)
def test_office_converter_is_selected(source, target):
    assert isinstance(
        get_converter(source, target),
        OfficeConverter,
    )


def test_image_to_pdf_is_not_supported():
    with pytest.raises(FileXError, match="not supported"):
        get_converter("png", "pdf")


def test_pdf_to_image_is_not_supported():
    with pytest.raises(FileXError, match="not supported"):
        get_converter("pdf", "png")
