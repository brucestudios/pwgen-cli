#!/usr/bin/env python3
"""Command-line interface for temperature converter."""

import argparse
import sys
from .converter import convert

def main():
    parser = argparse.ArgumentParser(
        description="Convert temperatures between Celsius and Fahrenheit."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # convert command
    convert_parser = subparsers.add_parser("convert", help="Convert a temperature")
    convert_parser.add_argument("value", type=float, help="Temperature value")
    convert_parser.add_argument(
        "conversion",
        choices=["CtoF", "FtoC"],
        help="Conversion type: CtoF or FtoC",
    )

    # interactive command
    subparsers.add_parser("interactive", help="Run in interactive mode")

    # batch command
    batch_parser = subparsers.add_parser("batch", help="Convert temperatures from a file")
    batch_parser.add_argument(
        "filename", type=str, help="File containing lines of '<value> <unit>'"
    )

    args = parser.parse_args()

    if args.command == "convert":
        from_unit = args.conversion[0]  # 'C' or 'F'
        to_unit = args.conversion[-1]   # 'C' or 'F'
        result = convert(args.value, from_unit, to_unit)
        print(f"{args.value}°{from_unit} = {result}°{to_unit}")

    elif args.command == "interactive":
        print("Temperature Converter Interactive Mode")
        print("Enter 'quit' to exit.")
        while True:
            try:
                line = input("Enter temperature and unit (e.g., 25 C): ").strip()
                if line.lower() in ("quit", "exit"):
                    break
                parts = line.split()
                if len(parts) != 2:
                    print("Please enter a value and a unit (C or F).")
                    continue
                value = float(parts[0])
                unit = parts[1].upper()
                if unit not in ("C", "F"):
                    print("Unit must be C or F.")
                    continue
                target = "F" if unit == "C" else "C"
                result = convert(value, unit, target)
                print(f"{value}°{unit} = {result}°{target}")
            except ValueError as e:
                print(f"Invalid input: {e}")
            except KeyboardInterrupt:
                print("\nExiting...")
                break

    elif args.command == "batch":
        try:
            with open(args.filename, "r") as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split()
                    if len(parts) != 2:
                        print(
                            f"Line {line_num}: invalid format, skipping: {line}",
                            file=sys.stderr,
                        )
                        continue
                    try:
                        value = float(parts[0])
                        unit = parts[1].upper()
                        if unit not in ("C", "F"):
                            print(
                                f"Line {line_num}: unit must be C or F, skipping: {line}",
                                file=sys.stderr,
                            )
                            continue
                        target = "F" if unit == "C" else "C"
                        result = convert(value, unit, target)
                        print(f"{value}°{unit} = {result}°{target}")
                    except ValueError:
                        print(
                            f"Line {line_num}: invalid number, skipping: {line}",
                            file=sys.stderr,
                        )
        except FileNotFoundError:
            print(f"File not found: {args.filename}", file=sys.stderr)
            sys.exit(1)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()