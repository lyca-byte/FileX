# """Tests for document conversion routing."""

# import pytest

# from filex.converters.office import OfficeConverter
# from filex.core.router import get_converter
# from filex.exceptions import FileXError


# @pytest.mark.parametrize(
#     ("source", "target"),
#     [
#         ("docx", "pdf"), ("pdf", "docx"),
#         ("docx", "odt"), ("odt", "docx"),
#         ("rtf", "txt"), ("txt", "rtf"),
#         ("pdf", "txt"), ("odt", "pdf"),
#     ],
# )
# def test_office_converter_is_selected_for_document_pairs(source, target):
#     assert isinstance(get_converter(source, target), OfficeConverter)


# def test_image_to_pdf_is_not_supported():
#     with pytest.raises(FileXError, match="not supported"):
#         get_converter("png", "pdf")


# def test_pdf_to_image_is_not_supported():
#     with pytest.raises(FileXError, match="not supported"):
#         get_converter("pdf", "png")



"""Tests for document conversion routing."""

import pytest

from filex.converters.office import OfficeConverter
from filex.core.router import get_converter
from filex.exceptions import FileXError


@pytest.mark.parametrize(
    ("source", "target"),
    [
        ("docx", "pdf"), ("pdf", "docx"),
        ("docx", "odt"), ("odt", "docx"),
        ("rtf", "txt"), ("txt", "rtf"),
        ("pdf", "txt"), ("odt", "pdf"),
        ("pptx", "pdf"), ("pdf", "pptx"),
        ("xlsx", "ods"), ("ods", "xlsx"),
        ("docx", "xlsx"), ("pptx", "txt"),
    ],
)
def test_office_converter_is_selected_for_document_pairs(source, target):
    assert isinstance(get_converter(source, target), OfficeConverter)


def test_image_to_pdf_is_not_supported():
    with pytest.raises(FileXError, match="not supported"):
        get_converter("png", "pdf")


def test_pdf_to_image_is_not_supported():
    with pytest.raises(FileXError, match="not supported"):
        get_converter("pdf", "png")
