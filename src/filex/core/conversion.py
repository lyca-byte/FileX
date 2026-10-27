"""Coordinate the file conversion process."""

from pathlib import Path

from filex.core.output import get_output_path
from filex.core.router import get_converter
from filex.core.validation import (
    normalize_format,
    validate_input,
    validate_target_format,
)
from filex.exceptions import FileXError


def convert_file(
    input_path: Path,
    target_format: str,
    output_path: Path | None = None,
    output_dir: Path | None = None,
) -> Path:
    """Validate, route, and execute a file conversion."""
    source_format = validate_input(input_path)
    target_format = validate_target_format(target_format)

    if normalize_format(source_format) == target_format:
        raise FileXError(
            "Input and target formats are identical. "
            "Choose a different target format."
        )

    result_path = get_output_path(
        input_path=input_path,
        target_format=target_format,
        output_path=output_path,
        output_dir=output_dir,
    )

    converter = get_converter(source_format, target_format)
    converter.convert(input_path, result_path, target_format)

    return result_path