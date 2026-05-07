#!/usr/bin/env python3
"""
passgen - A secure password generator.

Generate strong passwords with customizable options.
"""

import argparse
import os
import string
import sys
import secrets


def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True, exclude_ambiguous=False):
    """Generate a random password."""
    # Define character sets
    uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowers = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    symbols = '!@#$%^&*()-_=+[]{}|;:,.<>?/~`'

    # Optionally exclude ambiguous characters: il1Lo0O
    ambiguous = set('il1Lo0O')

    # Build the character set
    chars = ''
    if use_upper:
        uppers_filtered = ''.join(c for c in uppers if c not in ambiguous or not exclude_ambiguous)
        chars += uppers_filtered
    if use_lower:
        lowers_filtered = ''.join(c for c in lowers if c not in ambiguous or not exclude_ambiguous)
        chars += lowers_filtered
    if use_digits:
        digits_filtered = ''.join(c for c in digits if c not in ambiguous or not exclude_ambiguous)
        chars += digits_filtered
    if use_symbols:
        # Symbols are less likely to be ambiguous, but we can filter if needed
        symbols_filtered = ''.join(c for c in symbols if c not in ambiguous or not exclude_ambiguous)
        chars += symbols_filtered

    if not chars:
        raise ValueError("No characters available to generate password.")

    # Ensure at least one character from each requested set is included
    password_chars = []
    if use_upper:
        password_chars.append(secrets.choice(uppers_filtered if exclude_ambiguous else uppers))
    if use_lower:
        password_chars.append(secrets.choice(lowers_filtered if exclude_ambiguous else lowers))
    if use_digits:
        password_chars.append(secrets.choice(digits_filtered if exclude_ambiguous else digits))
    if use_symbols:
        password_chars.append(secrets.choice(symbols_filtered if exclude_ambiguous else symbols))

    # Fill the rest of the password length with random choices from the combined set
    for _ in range(length - len(password_chars)):
        password_chars.append(secrets.choice(chars))

    # Shuffle the list to avoid predictable patterns
    secrets.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)


def main():
    parser = argparse.ArgumentParser(
        description="Generate strong, secure passwords.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  passgen                    # Generate a 16-character password with all character types
  passgen -l 20              # Generate a 20-character password
  passgen --no-symbols       # Generate a password without symbols
  passgen --exclude-ambiguous # Exclude ambiguous characters (il1Lo0O)
  passgen -l 10 -ud          # Generate a 10-character password with only uppercase and digits
        """
    )
    parser.add_argument(
        '-l', '--length',
        type=int,
        default=16,
        help='Length of the password (default: 16)'
    )
    parser.add_argument(
        '--no-upper',
        action='store_false',
        dest='use_upper',
        help='Exclude uppercase letters'
    )
    parser.add_argument(
        '--no-lower',
        action='store_false',
        dest='use_lower',
        help='Exclude lowercase letters'
    )
    parser.add_argument(
        '--no-digits',
        action='store_false',
        dest='use_digits',
        help='Exclude digits'
    )
    parser.add_argument(
        '--no-symbols',
        action='store_false',
        dest='use_symbols',
        help='Exclude symbols'
    )
    parser.add_argument(
        '--exclude-ambiguous',
        action='store_true',
        help='Exclude ambiguous characters (il1Lo0O)'
    )

    args = parser.parse_args()

    # Validate length
    if args.length < 1:
        parser.error("Length must be at least 1.")
    if args.length < 4 and (args.use_upper + args.use_lower + args.use_digits + args.use_symbols) > args.length:
        parser.error("Length is too short for the selected character types.")

    try:
        password = generate_password(
            length=args.length,
            use_upper=args.use_upper,
            use_lower=args.use_lower,
            use_digits=args.use_digits,
            use_symbols=args.use_symbols,
            exclude_ambiguous=args.exclude_ambiguous
        )
        print(password)
    except ValueError as e:
        parser.error(str(e))


if __name__ == '__main__':
    main()