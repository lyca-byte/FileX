
"""Select the appropriate converter."""

from filex.converters.image import ImageConverter
from filex.converters.office import OfficeConverter
from filex.core.validation import IMAGE_FORMATS
from filex.exceptions import FileXError


def get_converter(source_format: str, target_format: str):
    """Return a converter for the requested format pair."""
    if source_format in IMAGE_FORMATS and target_format in IMAGE_FORMATS:
        return ImageConverter()

    if {source_format, target_format} == {"docx", "pdf"}:
        return OfficeConverter()

    raise FileXError(
        f"Conversion from {source_format} to {target_format} "
        "is not supported."
    )
