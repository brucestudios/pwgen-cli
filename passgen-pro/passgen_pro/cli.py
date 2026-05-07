#!/usr/bin/env python3
"""
PassGen Pro - A modern password generator CLI.
"""

import argparse
import sys
import secrets
import string

def generate_password(length=16, use_digits=True, use_upper=True, use_lower=True, use_symbols=True, exclude_ambiguous=False):
    """Generate a random password."""
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    # Build the character set
    chars = ''
    if use_lower:
        chars += lower
    if use_upper:
        chars += upper
    if use_digits:
        chars += digits
    if use_symbols:
        chars += symbols

    # Remove ambiguous characters if requested
    if exclude_ambiguous:
        ambiguous = '0OIl1'
        chars = ''.join(c for c in chars if c not in ambiguous)

    if not chars:
        raise ValueError("No characters available to generate password.")

    # Generate password
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate strong, random passwords.")
    parser.add_argument('-l', '--length', type=int, default=16, help='Length of the password (default: 16)')
    parser.add_argument('-n', '--num', type=int, default=1, help='Number of passwords to generate (default: 1)')
    parser.add_argument('--no-digits', action='store_false', dest='digits', help='Exclude digits')
    parser.add_argument('--no-upper', action='store_false', dest='upper', help='Exclude uppercase letters')
    parser.add_argument('--no-lower', action='store_false', dest='lower', help='Exclude lowercase letters')
    parser.add_argument('--no-symbols', action='store_false', dest='symbols', help='Exclude symbols')
    parser.add_argument('--exclude-ambiguous', action='store_true', help='Exclude ambiguous characters (0, O, I, l, 1)')
    parser.add_argument('--copy', action='store_true', help='Copy the password to clipboard (requires pyperclip)')

    args = parser.parse_args()

    # Validate arguments
    if args.length < 1:
        parser.error("Length must be at least 1.")
    if args.num < 1:
        parser.error("Number of passwords must be at least 1.")

    try:
        passwords = []
        for _ in range(args.num):
            password = generate_password(
                length=args.length,
                use_digits=args.digits,
                use_upper=args.upper,
                use_lower=args.lower,
                use_symbols=args.symbols,
                exclude_ambiguous=args.exclude_ambiguous
            )
            passwords.append(password)

        # Output
        for pwd in passwords:
            print(pwd)

        # Copy to clipboard if requested
        if args.copy and args.num == 1:
            try:
                import pyperclip
                pyperclip.copy(passwords[0])
                print("(Copied to clipboard)", file=sys.stderr)
            except ImportError:
                print("Warning: pyperclip not installed. Install with: pip install pyperclip", file=sys.stderr)
            except Exception as e:
                print(f"Warning: Could not copy to clipboard: {e}", file=sys.stderr)

    except ValueError as e:
        parser.error(str(e))

if __name__ == '__main__':
    main()