#!/usr/bin/env python3
import argparse
import string
import secrets
import sys

def generate_password(length=16, use_digits=False, use_punctuation=False, use_letters=True, exclude_ambiguous=False):
    """Generate a secure password."""
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    ambiguous = set('0OoIl1')  # 0, O, o, I, l, 1

    # Build the character set
    chars = ''
    if use_letters:
        chars += letters
    if use_digits:
        chars += digits
    if use_punctuation:
        chars += punctuation

    # Remove ambiguous characters if requested
    if exclude_ambiguous:
        chars = ''.join(c for c in chars if c not in ambiguous)

    if not chars:
        raise ValueError("No characters available for password generation.")

    # Generate password
    return ''.join(secrets.choice(chars) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description="Generate a secure password.")
    parser.add_argument('-l', '--length', type=int, default=16, help='Length of the password (default: 16)')
    parser.add_argument('-d', '--digits', action='store_true', help='Include digits (0-9)')
    parser.add_argument('-p', '--punctuation', action='store_true', help='Include punctuation characters')
    parser.add_argument('-a', '--letters', action='store_true', help='Include letters (both uppercase and lowercase, default)')
    parser.add_argument('-e', '--exclude-ambiguous', action='store_true', help='Exclude ambiguous characters (0, O, l, 1)')
    args = parser.parse_args()

    # If no character set is explicitly chosen, default to letters
    if not (args.digits or args.punctuation or args.letters):
        args.letters = True

    try:
        password = generate_password(
            length=args.length,
            use_digits=args.digits,
            use_punctuation=args.punctuation,
            use_letters=args.letters,
            exclude_ambiguous=args.exclude_ambiguous
        )
        print(password)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()