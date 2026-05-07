#!/usr/bin/env python3
"""
A simple UUID generator.
Generates UUIDs (version 4) and prints them to stdout.
"""

import uuid
import sys

def generate_uuid(count=1):
    """Generate a specified number of UUIDs."""
    for _ in range(count):
        print(uuid.uuid4())

def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
            if count < 1:
                raise ValueError
        except ValueError:
            print("Error: Please provide a positive integer for the number of UUIDs to generate.", file=sys.stderr)
            sys.exit(1)
    else:
        count = 1

    generate_uuid(count)

if __name__ == "__main__":
    main()
