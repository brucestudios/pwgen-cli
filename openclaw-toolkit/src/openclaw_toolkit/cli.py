import argparse
import random
import string
import sys

def hello(args):
    print("Hello, OpenClaw user!")

def joke(args):
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "Why did the developer go broke? Because he used up all his cache.",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "I told my computer I needed a break, and it said 'No problem - I'll go to sleep.'",
        "Why do Java developers wear glasses? Because they don't see sharp."
    ]
    print(random.choice(jokes))

def passgen(args):
    length = args.length
    if length < 4:
        length = 4
    alphabet = string.ascii_letters + string.digits
    if args.special:
        alphabet += string.punctuation
    password = ''.join(random.choice(alphabet) for _ in range(length))
    print(password)

def main():
    parser = argparse.ArgumentParser(prog='oc-tool', description='OpenClaw Toolkit')
    subparsers = parser.add_subparsers(dest='command')

    # hello
    parser_hello = subparsers.add_parser('hello', help='Say hello')
    parser_hello.set_defaults(func=hello)

    # joke
    parser_joke = subparsers.add_parser('joke', help='Tell a random joke')
    parser_joke.set_defaults(func=joke)

    # passgen
    parser_passgen = subparsers.add_parser('passgen', help='Generate a password')
    parser_passgen.add_argument('-l', '--length', type=int, default=16, help='Password length')
    parser_passgen.add_argument('-s', '--special', action='store_true', help='Include special characters')
    parser_passgen.set_defaults(func=passgen)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()