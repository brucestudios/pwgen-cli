#!/usr/bin/env python3
import argparse
import uuid
import sys

def generate_uuid(count=1, no_hyphens=False, uppercase=False):
    """Generate UUIDs."""
    uuids = []
    for _ in range(count):
        u = uuid.uuid4()
        if no_hyphens:
            u_str = str(u).replace('-', '')
        else:
            u_str = str(u)
        if uppercase:
            u_str = u_str.upper()
        uuids.append(u_str)
    return uuids

def main():
    parser = argparse.ArgumentParser(description='Generate UUIDs.')
    parser.add_argument('-n', '--count', type=int, default=1, help='Number of UUIDs to generate (default: 1)')
    parser.add_argument('--no-hyphens', action='store_true', help='Output UUIDs without hyphens')
    parser.add_argument('--uppercase', action='store_true', help='Output UUIDs in uppercase letters')
    args = parser.parse_args()

    if args.count < 1:
        print('Error: count must be at least 1', file=sys.stderr)
        sys.exit(1)

    uuids = generate_uuid(args.count, args.no_hyphens, args.uppercase)
    for u in uuids:
        print(u)

if __name__ == '__main__':
    main()