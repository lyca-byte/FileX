"""Command-line interface for FileX."""

import argparse
import sys
from pathlib import Path

from filex import __version__
from filex.core.conversion import convert_file
from filex.exceptions import FileXError


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="filex",
        description="Offline multi-format file converter.",
        epilog="Example: filex --file photo.png --to webp",
    )

    parser.add_argument(
        "--file",
        type=Path,
        metavar="PATH",
        help="Path to the input file.",
    )
    parser.add_argument(
        "--to",
        dest="target_format",
        metavar="FORMAT",
        help="Target format: png, jpg, webp, docx, or pdf.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        metavar="PATH",
        help="Optional output file path.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        metavar="DIR",
        help="Optional output directory.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    return parser


def run(args: argparse.Namespace) -> int:
    """Validate arguments and run the conversion."""
    if args.file is None:
        raise FileXError("Missing required argument: --file")

    if args.target_format is None:
        raise FileXError("Missing required argument: --to")

    result = convert_file(
        input_path=args.file,
        target_format=args.target_format,
        output_path=args.output,
        output_dir=args.output_dir,
    )

    print(f"Conversion successful: {result}")
    return 0


def main() -> int:
    """Run the FileX CLI."""
    parser = build_parser()
    args = parser.parse_args()

    try:
        return run(args)
    except FileXError as exc:
        print(f"filex: error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())