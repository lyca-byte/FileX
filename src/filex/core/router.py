# """Select the appropriate converter."""

# from filex.converters.image import ImageConverter
# from filex.converters.office import OfficeConverter
# from filex.core.validation import DOCUMENT_FORMATS, IMAGE_FORMATS
# from filex.exceptions import FileXError


# def get_converter(source_format: str, target_format: str):
#     """Return a converter for the requested format pair."""
#     if source_format in IMAGE_FORMATS and target_format in IMAGE_FORMATS:
#         return ImageConverter()

#     if source_format in DOCUMENT_FORMATS and target_format in DOCUMENT_FORMATS:
#         return OfficeConverter()

#     raise FileXError(
#         f"Conversion from {source_format} to {target_format} "
#         "is not supported."
#     )


"""Select the appropriate converter."""

from filex.converters.image import ImageConverter
from filex.converters.office import OfficeConverter
from filex.core.validation import DOCUMENT_FORMATS, IMAGE_FORMATS
from filex.exceptions import FileXError


def get_converter(source_format: str, target_format: str):
    """Return a converter for the requested format pair."""
    if source_format in IMAGE_FORMATS and target_format in IMAGE_FORMATS:
        return ImageConverter()

    if source_format in DOCUMENT_FORMATS and target_format in DOCUMENT_FORMATS:
        return OfficeConverter()

    raise FileXError(
        f"Conversion from {source_format} to {target_format} "
        "is not supported."
    )
