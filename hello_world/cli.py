import argparse
import sys
from . import __version__

def main():
    parser = argparse.ArgumentParser(
        description="Print a friendly greeting."
    )
    parser.add_argument(
        "--name",
        default="World",
        help="Name to greet (default: World)"
    )
    parser.add_argument(
        "--lang",
        choices=["en", "es", "fr"],
        default="en",
        help="Language for greeting (default: en)"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )

    args = parser.parse_args()

    greetings = {
        "en": f"Hello, {args.name}!",
        "es": f"¡Hola, {args.name}!",
        "fr": f"Bonjour, {args.name} !"
    }

    print(greetings[args.lang])

if __name__ == "__main__":
    sys.exit(main())