#!/usr/bin/env python3
"""
UUID Tool - Generate UUIDs (version 4) from the command line.

Usage:
    python uuid.py          # Generate one UUID
    python uuid.py -n 5     # Generate 5 UUIDs
    python uuid.py --help   # Show help
"""

import argparse
import uuid
import sys


def generate_uuid(count=1):
    """Generate one or more UUIDs."""
    uuids = [str(uuid.uuid4()) for _ in range(count)]
    return uuids if count > 1 else uuids[0]


def main():
    parser = argparse.ArgumentParser(
        description="Generate UUIDs (version 4).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Example:\n  python uuid.py -n 5"
    )
    parser.add_argument(
        "-n", "--number",
        type=int,
        default=1,
        help="Number of UUIDs to generate (default: 1)"
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version="UUID Tool 1.0.0"
    )

    args = parser.parse_args()

    if args.number < 1:
        print("Error: Number of UUIDs must be at least 1.", file=sys.stderr)
        sys.exit(1)

    result = generate_uuid(args.number)
    if isinstance(result, list):
        for uid in result:
            print(uid)
    else:
        print(result)


if __name__ == "__main__":
    main()