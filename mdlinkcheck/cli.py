"""Command-line interface for mdlinkcheck."""

from __future__ import annotations

import argparse
import sys
from typing import List, Tuple

from .checker import check_links_in_path


def main(argv: List[str] | None = None) -> int:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Check for broken links in Markdown files."
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="Markdown files or directories to check"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=10,
        help="HTTP request timeout in seconds (default: 10)"
    )
    parser.add_argument(
        "--user-agent",
        default="mdlinkcheck/0.1.0",
        help="User-Agent string for HTTP requests"
    )
    parser.add_argument(
        "--ignore-local",
        action="store_true",
        help="Skip checking local file links"
    )
    parser.add_argument(
        "--ignore-remote",
        action="store_true",
        help="Skip checking HTTP(S) links"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output"
    )
    parser.add_argument(
        "--version",
        action="version",
        version="mdlinkcheck 0.1.0"
    )

    args = parser.parse_args(argv)

    all_valid = True
    for path in args.paths:
        if args.verbose:
            print(f"Checking {path}...", file=sys.stderr)
        
        valid, broken = check_links_in_path(
            path,
            timeout=args.timeout,
            user_agent=args.user_agent,
            ignore_local=args.ignore_local,
            ignore_remote=args.ignore_remote
        )
        
        if not valid:
            all_valid = False
            for file_path, link, error in broken:
                print(f"{file_path}: {link} - {error}", file=sys.stderr)
        elif args.verbose and not broken:
            print(f"✓ All links are valid.", file=sys.stderr)

    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())