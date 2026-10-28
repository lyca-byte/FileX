
"""Tests for document conversion routing."""

import pytest

from filex.converters.office import OfficeConverter
from filex.core.router import get_converter
from filex.exceptions import FileXError

from pathlib import Path
from unittest.mock import patch


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


def test_pdf_to_docx_defaults_to_editable():
    converter = OfficeConverter()

    with patch.object(
        converter,
        "_pdf_to_docx",
    ) as editable, patch.object(
        converter,
        "_pdf_to_docx_visual",
    ) as visual:
        converter.convert(
            Path("input.pdf"),
            Path("output.docx"),
            "docx",
        )

    editable.assert_called_once_with(
        Path("input.pdf").resolve(),
        Path("output.docx").resolve(),
    )
    visual.assert_not_called()


def test_pdf_to_docx_visual_mode():
    converter = OfficeConverter()

    with patch.object(
        converter,
        "_pdf_to_docx",
    ) as editable, patch.object(
        converter,
        "_pdf_to_docx_visual",
    ) as visual:
        converter.convert(
            Path("input.pdf"),
            Path("output.docx"),
            "docx",
            mode="visual",
        )

    visual.assert_called_once_with(
        Path("input.pdf").resolve(),
        Path("output.docx").resolve(),
    )
    editable.assert_not_called()


def test_pdf_to_docx_rejects_unknown_mode():
    converter = OfficeConverter()

    with pytest.raises(
        FileXError,
        match="Unsupported PDF-to-DOCX mode",
    ):
        converter.convert(
            Path("input.pdf"),
            Path("output.docx"),
            "docx",
            mode="unknown",
        )
