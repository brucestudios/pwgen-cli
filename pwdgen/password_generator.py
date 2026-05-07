#!/usr/bin/env python3
"""
pwdgen - A simple, secure password generator.

Generates strong random passwords with customizable length and character sets.
"""

import argparse
import secrets
import string
import sys


def generate_password(length: int = 16,
                      use_upper: bool = True,
                      use_lower: bool = True,
                      use_digits: bool = True,
                      use_symbols: bool = True) -> str:
    """Generate a random password."""
    if length < 4:
        raise ValueError("Password length must be at least 4")

    characters = ''
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected")

    # Ensure at least one character from each selected set
    password = []
    if use_lower:
        password.append(secrets.choice(string.ascii_lowercase))
    if use_upper:
        password.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        password.append(secrets.choice(string.digits))
    if use_symbols:
        password.append(secrets.choice(string.punctuation))

    # Fill the rest with random choices from the combined set
    for _ in range(length - len(password)):
        password.append(secrets.choice(characters))

    # Shuffle the list to avoid predictable patterns
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a secure random password."
    )
    parser.add_argument(
        '-l', '--length', type=int, default=16,
        help='Length of the password (default: 16)'
    )
    parser.add_argument(
        '--no-upper', action='store_true',
        help='Exclude uppercase letters'
    )
    parser.add_argument(
        '--no-lower', action='store_true',
        help='Exclude lowercase letters'
    )
    parser.add_argument(
        '--no-digits', action='store_true',
        help='Exclude digits'
    )
    parser.add_argument(
        '--no-symbols', action='store_true',
        help='Exclude symbols'
    )
    args = parser.parse_args()

    try:
        password = generate_password(
            length=args.length,
            use_upper=not args.no_upper,
            use_lower=not args.no_lower,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols
        )
        print(password)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()