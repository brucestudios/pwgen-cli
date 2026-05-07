"""Command-line interface for Textura."""

import argparse
import sys
from . import transform

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Textura - A versatile command-line tool for text transformation and manipulation."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Case conversion
    case_parser = subparsers.add_parser("upper", help="Convert text to uppercase")
    case_parser.add_argument(
        "-i", "--input", type=argparse.FileType("r"), default=sys.stdin,
        help="Input file (default: stdin)"
    )
    case_parser.add_argument(
        "-o", "--output", type=argparse.FileType("w"), default=sys.stdout,
        help="Output file (default: stdout)"
    )

    lower_parser = subparsers.add_parser("lower", help="Convert text to lowercase")
    lower_parser.add_argument("-i", "--input", type=argparse.FileType("r"), default=sys.stdin)
    lower_parser.add_argument("-o", "--output", type=argparse.FileType("w"), default=sys.stdout)

    title_parser = subparsers.add_parser("title", help="Convert text to title case")
    title_parser.add_argument("-i", "--input", type=argparse.FileType("r"), default=sys.stdin)
    title_parser.add_argument("-o", "--output", type=argparse.FileType("w"), default=sys.stdout)

    sentence_parser = subparsers.add_parser("sentence", help="Convert text to sentence case")
    sentence_parser.add_argument("-i", "--input", type=argparse.FileType("r"), default=sys.stdin)
    sentence_parser.add_argument("-o", "--output", type=argparse.FileType("w"), default=sys.stdout)

    alternating_parser = subparsers.add_parser("alternating", help="Convert text to alternating case")
    alternating_parser.add_argument("-i", "--input", type=argparse.FileType("r"), default=sys.stdin)
    alternating_parser.add_argument("-o", "--output", type=argparse.FileType("w"), default=sys.stdout)

    # Sorting
    sort_parser = subparsers.add_parser("sort", help="Sort lines alphabetically")
    sort_parser.add_argument("-r", "--reverse", action="store_true", help="Sort in reverse order")
    sort_parser.add_argument("-i", "--input", type=argparse.FileType("r"), default=sys.stdin)
    sort_parser.add_argument("-o", "--output", type=argparse.FileType("w"), default=sys.stdout)

    reverse_parser = subparsers.add_parser("reverse", help="Reverse the order of lines")
    reverse_parser.add_argument("-i", "--input", type=argparse.FileType("r"), default=sys.stdin)
    reverse_parser.add_argument("-o", "--output", type=argparse.FileType("w"), default=sys.stdout)

    random_parser = subparsers.add_parser("random", help="Shuffle lines randomly")
    random_parser.add_argument("-i", "--input", type=argparse.FileType("r"), default=sys.stdin)
    random_parser.add_argument("-o", "--output", type=argparse.FileType("w"), default=sys.stdout)

    length_parser = subparsers.add_parser("length", help="Sort lines by length")
    length_parser.add_argument("-r", "--reverse", action="store_true", help="Sort in reverse order (longest first)")
    length_parser.add_argument("-i", "--input", type=argparse.FileType("r"), default=sys.stdin)
    length_parser.add_argument("-o", "--output", type=argparse.FileType("w"), default=sys.stdout)

    # Deduplication
    dedup_lines_parser = subparsers.add_parser("dedup-lines", help="Remove duplicate lines")
    dedup_lines_parser.add_argument("-i", "--input", type=argparse.FileType("r"), default=sys.stdin)
    dedup_lines_parser.add_argument("-o", "--output", type=argparse.FileType("w"), default=sys.stdout)

    dedup_words_parser = subparsers.add_parser("dedup-words", help="Remove duplicate words")
    dedup_words_parser.add_argument("-i", "--input", type=argparse.FileType("r"), default=sys.stdin)
    dedup_words_parser.add_argument("-o", "--output", type=argparse.FileType("w"), default=sys.stdout)

    # Filtering
    grep_parser = subparsers.add_parser("grep", help="Filter lines matching a pattern")
    grep_parser.add_argument("pattern", help="Regex pattern to match")
    grep_parser.add_argument("-i", "--ignore-case", action="store_true", help="Ignore case")
    grep_parser.add_argument("-i", "--input", type=argparse.FileType("r"), default=sys.stdin)
    grep_parser.add_argument("-o", "--output", type=argparse.FileType("w"), default=sys.stdout)

    grep_v_parser = subparsers.add_parser("grep-v", help="Filter lines NOT matching a pattern")
    grep_v_parser.add_argument("pattern", help="Regex pattern to match")
    grep_v_parser.add_argument("-i", "--ignore-case", action="store_true", help="Ignore case")
    grep_v_parser.add_argument("-i", "--input", type=argparse.FileType("r"), default=sys.stdin)
    grep_v_parser.add_argument("-o", "--output", type=argparse.FileType("w"), default=sys.stdout)

    # Wrapping
    wrap_parser = subparsers.add_parser("wrap", help="Wrap text to a given width")
    wrap_parser.add_argument("-w", "--width", type=int, default=70, help="Width (default: 70)")
    wrap_parser.add_argument("-i", "--input", type=argparse.FileType("r"), default=sys.stdin)
    wrap_parser.add_argument("-o", "--output", type=argparse.FileType("w"), default=sys.stdout)

    unwrap_parser = subparsers.add_parser("unwrap", help="Unwrap text (join wrapped lines)")
    unwrap_parser.add_argument("-i", "--input", type=argparse.FileType("r"), default=sys.stdin)
    unwrap_parser.add_argument("-o", "--output", type=argparse.FileType("w"), default=sys.stdout)

    # Column extraction
    column_parser = subparsers.add_parser("column", help="Extract a column from delimited text")
    column_parser.add_argument("column", type=int, help="Column index (0-based)")
    column_parser.add_argument("-d", "--delimiter", help="Delimiter (default: whitespace)")
    column_parser.add_argument("-i", "--input", type=argparse.FileType("r"), default=sys.stdin)
    column_parser.add_argument("-o", "--output", type=argparse.FileType("w"), default=sys.stdout)

    # Join/Split
    join_parser = subparsers.add_parser("join", help="Join lines with a separator")
    join_parser.add_argument("-s", "--separator", default=" ", help="Separator (default: space)")
    join_parser.add_argument("-i", "--input", type=argparse.FileType("r"), default=sys.stdin)
    join_parser.add_argument("-o", "--output", type=argparse.FileType("w"), default=sys.stdout)

    split_parser = subparsers.add_parser("split", help="Split text into lines (output as JSON-like list)")
    split_parser.add_argument("-i", "--input", type=argparse.FileType("r"), default=sys.stdin)
    split_parser.add_argument("-o", "--output", type=argparse.FileType("w"), default=sys.stdout)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    # Read input
    with args.input as f:
        text = f.read()

    # Process based on command
    result = None
    if args.command == "upper":
        result = transform.upper(text)
    elif args.command == "lower":
        result = transform.lower(text)
    elif args.command == "title":
        result = transform.title(text)
    elif args.command == "sentence":
        result = transform.sentence(text)
    elif args.command == "alternating":
        result = transform.alternating(text)
    elif args.command == "sort":
        result = transform.sort_lines(text, reverse=args.reverse)
    elif args.command == "reverse":
        result = transform.reverse_lines(text)
    elif args.command == "random":
        result = transform.random_lines(text)
    elif args.command == "length":
        result = transform.sort_by_length(text, reverse=args.reverse)
    elif args.command == "dedup-lines":
        result = transform.dedup_lines(text)
    elif args.command == "dedup-words":
        result = transform.dedup_words(text)
    elif args.command == "grep":
        result = transform.grep_lines(text, args.pattern, ignore_case=args.ignore_case)
    elif args.command == "grep-v":
        result = transform.grep_v_lines(text, args.pattern, ignore_case=args.ignore_case)
    elif args.command == "wrap":
        result = transform.wrap_text(text, width=args.width)
    elif args.command == "unwrap":
        result = transform.unwrap_text(text)
    elif args.command == "column":
        result = transform.extract_column(text, column=args.column, delimiter=args.delimiter)
    elif args.command == "join":
        result = transform.join_lines(text, separator=args.separator)
    elif args.command == "split":
        lines = transform.split_lines(text)
        # Output as a Python-like list for simplicity
        result = "\n".join(lines)  # Actually, we want one line per element? Let's output each line as is? Wait, split_lines returns list, we want to output each line? Actually, the command "split" should output the lines, one per line? That's just the input. Let's think: maybe we want to output as a JSON array? For simplicity, we'll output each line as is (which is the same as input). Let's change: we'll output each element on a new line, which is the same as the input if the input was already lines. So maybe this command is useless. Let's instead output as a JSON list to a file.
        import json
        result = json.dumps(lines)
    else:
        parser.print_help()
        sys.exit(1)

    # Write output
    with args.output as f:
        f.write(result)
        if not result.endswith('\n'):
            f.write('\n')

if __name__ == "__main__":
    main()