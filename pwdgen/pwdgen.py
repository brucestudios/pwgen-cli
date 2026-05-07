#!/usr/bin/env python3
import argparse
import secrets
import string

def generate_password(length=16, no_ambiguous=False, letters_only=False, numbers_only=False, special=False):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    # Ambiguous characters: 0 O 1 l I (and maybe others?)
    ambiguous = set('0O1lI')

    # Build the character set based on options
    chars = ''
    if letters_only:
        chars = letters
    elif numbers_only:
        chars = digits
    else:
        chars = letters + digits
        if special:
            chars += special_chars

    # Remove ambiguous characters if requested
    if no_ambiguous:
        chars = ''.join(c for c in chars if c not in ambiguous)

    # Ensure we have at least one character to choose from
    if not chars:
        raise ValueError("No characters available for password generation.")

    # Generate password
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description='Generate a secure random password.')
    parser.add_argument('-l', '--length', type=int, default=16, help='Password length (default: 16)')
    parser.add_argument('--no-ambiguous', action='store_true', help='Exclude ambiguous characters (0, O, 1, l, I)')
    parser.add_argument('--letters-only', action='store_true', help='Generate only letters (both cases)')
    parser.add_argument('--numbers-only', action='store_true', help='Generate only numbers')
    parser.add_argument('--special', action='store_true', help='Include special characters')
    args = parser.parse_args()

    # Validate options
    if args.letters_only and args.numbers_only:
        parser.error("Cannot specify both --letters-only and --numbers-only")
    if args.letters_only and args.special:
        parser.error("Cannot specify both --letters-only and --special")
    if args.numbers_only and args.special:
        parser.error("Cannot specify both --numbers-only and --special")

    try:
        password = generate_password(
            length=args.length,
            no_ambiguous=args.no_ambiguous,
            letters_only=args.letters_only,
            numbers_only=args.numbers_only,
            special=args.special
        )
        print(password)
    except ValueError as e:
        parser.error(str(e))

if __name__ == '__main__':
    main()