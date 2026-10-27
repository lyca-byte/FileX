
"""Allow FileX to run with python -m filex."""

import sys

from filex.cli import main


if __name__ == "__main__":
    sys.exit(main())
