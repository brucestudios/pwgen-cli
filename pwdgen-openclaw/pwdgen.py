#!/usr/bin/env python3
"""
A simple yet powerful password generator.

Features:
- Generate passwords of variable length
- Include/exclude uppercase, lowercase, digits, and special characters
- Ensure at least one character from each selected category
- Optionally exclude ambiguous characters (like 'l', '1', 'I', 'O', '0')
- Copy to clipboard (if pyperclip is installed) or print to stdout

Usage:
    python pwdgen.py [options]

Options:
    -l, --length LENGTH       Length of the password (default: 16)
    --no-upper                Exclude uppercase letters
    --no-lower                Exclude lowercase letters
    --no-digits               Exclude digits
    --no-special              Exclude special characters
    --no-ambiguous            Exclude ambiguous characters (l, 1, I, O, 0)
    -c, --clipboard           Copy the password to the clipboard (requires pyperclip)
    -h, --help                Show this help message

Example:
    python pwdgen.py -l 20 --no-ambiguous -c
"""

import argparse
import random
import string
import sys

try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False


def build_charsets(use_upper=True, use_lower=True, use_digits=True, use_special=True, no_ambiguous=False):
    """Build character sets based on options."""
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    if no_ambiguous:
        ambiguous = 'l1IO0'
        upper = ''.join(c for c in upper if c not in ambiguous)
        lower = ''.join(c for c in lower if c not in ambiguous)
        digits = ''.join(c for c in digits if c not in ambiguous)

    charset = ''
    if use_upper:
        charset += upper
    if use_lower:
        charset += lower
    if use_digits:
        charset += digits
    if use_special:
        charset += special

    # Ensure we have at least one character from each selected category
    required = []
    if use_upper:
        required.append(random.choice(upper))
    if use_lower:
        required.append(random.choice(lower))
    if use_digits:
        required.append(random.choice(digits))
    if use_special:
        required.append(random.choice(special))

    return charset, required


def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_special=True, no_ambiguous=False):
    """Generate a password."""
    if length < 4:
        raise ValueError("Password length must be at least 4 to include one of each character type.")

    charset, required = build_charsets(use_upper, use_lower, use_digits, use_special, no_ambiguous)

    if not charset:
        raise ValueError("At least one character set must be selected.")

    # Generate the remaining characters
    remaining_length = length - len(required)
    if remaining_length < 0:
        # This happens if length is less than the number of required categories (should be caught by length<4)
        remaining_length = 0

    password_chars = required + [random.choice(charset) for _ in range(remaining_length)]
    random.shuffle(password_chars)
    return ''.join(password_chars)


def main():
    parser = argparse.ArgumentParser(description="Generate a strong password.")
    parser.add_argument('-l', '--length', type=int, default=16, help='Length of the password (default: 16)')
    parser.add_argument('--no-upper', action='store_true', help='Exclude uppercase letters')
    parser.add_argument('--no-lower', action='store_true', help='Exclude lowercase letters')
    parser.add_argument('--no-digits', action='store_true', help='Exclude digits')
    parser.add_argument('--no-special', action='store_true', help='Exclude special characters')
    parser.add_argument('--no-ambiguous', action='store_true', help='Exclude ambiguous characters (l, 1, I, O, 0)')
    parser.add_argument('-c', '--clipboard', action='store_true', help='Copy the password to the clipboard (requires pyperclip)')
    args = parser.parse_args()

    # Validate options
    if args.length < 4:
        parser.error("Password length must be at least 4.")
    if not (args.no_upper or args.no_lower or args.no_digits or args.no_special):
        # If none of the exclusions are set, we use all categories.
        pass
    # Actually, we want to allow the user to exclude any combination, but we must ensure at least one category remains.
    use_upper = not args.no_upper
    use_lower = not args.no_lower
    use_digits = not args.no_digits
    use_special = not args.no_special
    if not any([use_upper, use_lower, use_digits, use_special]):
        parser.error("At least one character set must be selected.")

    try:
        password = generate_password(
            length=args.length,
            use_upper=use_upper,
            use_lower=use_lower,
            use_digits=use_digits,
            use_special=use_special,
            no_ambiguous=args.no_ambiguous
        )
    except ValueError as e:
        parser.error(str(e))

    if args.clipboard:
        if CLIPBOARD_AVAILABLE:
            pyperclip.copy(password)
            print(f"Password copied to clipboard: {password}")
        else:
            print("Warning: pyperclip not installed. Install with 'pip install pyperclip' to use clipboard feature.")
            print(f"Generated password: {password}")
    else:
        print(password)


if __name__ == '__main__':
    main()