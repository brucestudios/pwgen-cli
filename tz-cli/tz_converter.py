#!/usr/bin/env python3
"""
Timezone Converter CLI Tool

Convert times between different timezones.
"""

import argparse
import sys
from datetime import datetime
from zoneinfo import ZoneInfo
import tzdata  # pylint: disable=unused-import


def parse_time(time_str: str) -> datetime:
    """Parse a time string in ISO format."""
    try:
        return datetime.fromisoformat(time_str)
    except ValueError as e:
        print(f"Error: Invalid time format. Use ISO format (YYYY-MM-DDTHH:MM:SS).", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert times between different timezones."
    )
    parser.add_argument(
        "--time",
        help="Time to convert (ISO format, default: now)",
        default=None,
    )
    parser.add_argument(
        "--from",
        dest="from_tz",
        help="Source timezone (default: UTC)",
        default="UTC",
    )
    parser.add_argument(
        "--to",
        dest="to_tz",
        help="Target timezone (required)",
        required=True,
    )

    args = parser.parse_args()

    # Get the current time if not provided
    if args.time is None:
        dt = datetime.now()
    else:
        dt = parse_time(args.time)

    # Attach source timezone if the datetime is naive
    if dt.tzinfo is None:
        try:
            dt = dt.replace(tzinfo=ZoneInfo(args.from_tz))
        except Exception as e:
            print(f"Error: Unknown source timezone '{args.from_tz}'.", file=sys.stderr)
            sys.exit(1)

    # Convert to target timezone
    try:
        target_tz = ZoneInfo(args.to_tz)
    except Exception as e:
        print(f"Error: Unknown target timezone '{args.to_tz}'.", file=sys.stderr)
        sys.exit(1)

    converted_dt = dt.astimezone(target_tz)

    # Output the result
    print(converted_dt.isoformat())


if __name__ == "__main__":
    main()