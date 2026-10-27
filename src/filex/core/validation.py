
"""Input and format validation."""

from pathlib import Path

from filex.exceptions import FileXError


IMAGE_FORMATS = {"png", "jpg", "webp"}
DOCUMENT_FORMATS = {"docx", "pdf"}
SUPPORTED_INPUT_FORMATS = IMAGE_FORMATS | DOCUMENT_FORMATS
SUPPORTED_TARGET_FORMATS = IMAGE_FORMATS | DOCUMENT_FORMATS


def normalize_format(file_format: str) -> str:
    """Normalize a format name or extension."""
    normalized = file_format.lower().strip().lstrip(".")

    if normalized == "jpeg":
        return "jpg"

    return normalized


def validate_input(input_path: Path) -> str:
    """Validate the input file and return its normalized format."""
    if not input_path.is_file():
        raise FileXError(
            f"Input file does not exist or is not a file: {input_path}"
        )

    source_format = normalize_format(input_path.suffix)

    if source_format not in SUPPORTED_INPUT_FORMATS:
        raise FileXError(
            f"Unsupported input format: {input_path.suffix or '(none)'}. "
            "Supported formats: PNG, JPG, JPEG, WebP, DOCX, PDF."
        )

    return source_format


def validate_target_format(target_format: str) -> str:
    """Validate and normalize the requested target format."""
    normalized = normalize_format(target_format)

    if normalized not in SUPPORTED_TARGET_FORMATS:
        raise FileXError(
            f"Unsupported target format: {target_format}. "
            "Supported formats: PNG, JPG, JPEG, WebP, DOCX, PDF."
        )

    return normalized
