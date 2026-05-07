#!/usr/bin/env python3
"""
Ultimate Password Generator
A powerful and flexible command-line tool for generating secure, random passwords.
"""

import argparse
import sys
import random
import string
try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False


def generate_pronounceable(length):
    """Generate a pronounceable password using consonant-vowel patterns."""
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    password = []
    for i in range(length):
        if i % 2 == 0:
            # Even positions: consonant
            password.append(random.choice(consonants))
        else:
            # Odd positions: vowel
            password.append(random.choice(vowels))
    
    return ''.join(password)


def generate_password(length, use_upper, use_lower, use_numbers, use_symbols, 
                     exclude_ambiguous, pronounceable):
    """Generate a random password based on the given criteria."""
    
    if pronounceable:
        return generate_pronounceable(length)
    
    # Define character sets
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    
    # Remove ambiguous characters if requested
    if exclude_ambiguous:
        uppercase = uppercase.replace('O', '').replace('I', '')
        lowercase = lowercase.replace('l', '').replace('o', '')
        numbers = numbers.replace('0', '').replace('1', '')
    
    # Build the character set based on options
    charset = ''
    if use_upper:
        charset += uppercase
    if use_lower:
        charset += lowercase
    if use_numbers:
        charset += numbers
    if use_symbols:
        charset += symbols
    
    # If no character types selected, use all (excluding ambiguous if set)
    if not charset:
        charset = uppercase + lowercase + numbers + symbols
        if exclude_ambiguous:
            charset = ''.join(c for c in charset if c not in 'OIl01o')
    
    # Generate password
    password = ''.join(random.choice(charset) for _ in range(length))
    return password


def main():
    parser = argparse.ArgumentParser(
        description='Generate secure passwords.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  upg                           # Generate a 16-character password
  upg -l 20 -n -s              # Generate a 20-character password with numbers and symbols
  upg -c 5 -l 12 --no-ambiguous # Generate 5 passwords, each 12 characters, excluding ambiguous
  upg --pronounceable          # Generate a pronounceable password
  upg -c 10 -l 16 -o passwords.txt # Save 10 passwords to a file
        '''
    )
    
    parser.add_argument('-l', '--length', type=int, default=16,
                        help='Length of each password (default: 16)')
    parser.add_argument('-c', '--count', type=int, default=1,
                        help='Number of passwords to generate (default: 1)')
    parser.add_argument('-u', '--uppercase', action='store_true',
                        help='Include uppercase letters (A-Z)')
    parser.add_argument('-l', '--lowercase', action='store_true',
                        help='Include lowercase letters (a-z)')
    parser.add_argument('-n', '--numbers', action='store_true',
                        help='Include numbers (0-9)')
    parser.add_argument('-s', '--symbols', action='store_true',
                        help='Include symbols (!@#$%^&* etc.)')
    parser.add_argument('--no-ambiguous', action='store_true',
                        help='Exclude ambiguous characters (0Oql1)')
    parser.add_argument('--pronounceable', action='store_true',
                        help='Generate pronounceable passwords')
    parser.add_argument('-o', '--output', type=str,
                        help='Output file to save passwords')
    parser.add_argument('--clipboard', action='store_true',
                        help='Copy result to clipboard (requires pyperclip)')
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.length < 1:
        parser.error('Password length must be at least 1')
    if args.count < 1:
        parser.error('Password count must be at least 1')
    if args.pronounceable and args.length < 2:
        parser.error('Pronounceable passwords require length of at least 2')
    if args.clipboard and not CLIPBOARD_AVAILABLE:
        print('Warning: pyperclip not installed. Clipboard functionality disabled.', 
              file=sys.stderr)
    
    # If no character types selected, select all by default
    if not (args.uppercase or args.lowercase or args.numbers or args.symbols):
        args.uppercase = args.lowercase = args.numbers = args.symbols = True
    
    # Generate passwords
    passwords = []
    for _ in range(args.count):
        password = generate_password(
            length=args.length,
            use_upper=args.uppercase,
            use_lower=args.lowercase,
            use_numbers=args.numbers,
            use_symbols=args.symbols,
            exclude_ambiguous=args.no_ambiguous,
            pronounceable=args.pronounceable
        )
        passwords.append(password)
    
    # Output results
    output = '\n'.join(passwords)
    
    if args.output:
        try:
            with open(args.output, 'w') as f:
                f.write(output)
            print(f'Saved {len(passwords)} password(s) to {args.output}')
        except IOError as e:
            print(f'Error writing to file: {e}', file=sys.stderr)
            sys.exit(1)
    else:
        print(output)
    
    # Copy to clipboard if requested
    if args.clipboard and CLIPBOARD_AVAILABLE and len(passwords) == 1:
        try:
            pyperclip.copy(passwords[0])
            print('Password copied to clipboard.')
        except Exception as e:
            print(f'Warning: Could not copy to clipboard: {e}', file=sys.stderr)
    elif args.clipboard and len(passwords) > 1:
        print('Warning: Clipboard copying only works for single password generation.', 
              file=sys.stderr)


if __name__ == '__main__':
    main()