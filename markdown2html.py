#!/usr/bin/python3
"""
markdown2html.py

docs
"""

import sys
from pathlib import Path


def main() -> int:
    """Entry point"""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        return 1

    input_path = Path(sys.argv[1])
    output_path = sys.argv[2]

    if not input_path.is_file():
        print(f"Missing {input_path.name}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
