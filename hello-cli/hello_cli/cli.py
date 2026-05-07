import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Say hello to someone.")
    parser.add_argument(
        "name",
        nargs="?",
        default="World",
        help="The name to greet (default: World)"
    )
    parser.add_argument(
        "-u",
        "--uppercase",
        action="store_true",
        help="Output in uppercase"
    )
    args = parser.parse_args()

    greeting = f"Hello, {args.name}!"
    if args.uppercase:
        greeting = greeting.upper()

    print(greeting)
    sys.exit(0)

if __name__ == "__main__":
    main()