"""Output path handling."""

from pathlib import Path

from filex.exceptions import FileXError


def get_output_path(
    input_path: Path,
    target_format: str,
    output_path: Path | None = None,
    output_dir: Path | None = None,
) -> Path:
    """Determine the output path without overwriting existing files."""
    input_path = input_path.resolve()

    if output_path is not None and output_dir is not None:
        raise FileXError("Use either --output or --output-dir, not both.")

    if output_path is not None:
        result = output_path.resolve()

        if result.suffix.lower() != f".{target_format}":
            raise FileXError(
                f"Output extension must be .{target_format}."
            )

    elif output_dir is not None:
        directory = output_dir.resolve()

        if not directory.is_dir():
            raise FileXError(
                f"Output directory does not exist: {directory}"
            )

        result = directory / f"{input_path.stem}.{target_format}"

    else:
        result = input_path.with_suffix(f".{target_format}")

    if result == input_path:
        raise FileXError("Output path must differ from the input path.")

    if not result.parent.is_dir():
        raise FileXError(
            f"Output directory does not exist: {result.parent}"
        )

    if result.exists():
        raise FileXError(
            f"Output file already exists: {result}. "
            "Choose another output path."
        )

    return result