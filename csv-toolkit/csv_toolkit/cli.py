import argparse
import sys
from .core import read_csv, write_csv, filter_csv, convert_csv_delimiter

def main():
    parser = argparse.ArgumentParser(description="CSV Toolkit - A tool for CSV file operations")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Read command
    read_parser = subparsers.add_parser('read', help='Read a CSV file and display its contents')
    read_parser.add_argument('file', help='Path to the CSV file')
    read_parser.add_argument('-d', '--delimiter', default=',', help='Delimiter used in the CSV (default: comma)')
    read_parser.add_argument('--no-header', action='store_true', help='Specify if the CSV does not have a header')

    # Write command
    write_parser = subparsers.add_parser('write', help='Write data to a CSV file')
    write_parser.add_argument('file', help='Path to the output CSV file')
    write_parser.add_argument('-d', '--delimiter', default=',', help='Delimiter to use (default: comma)')
    write_parser.add_argument('--header', help='Comma-separated list of column names (if not provided, keys from first record are used)')

    # Filter command
    filter_parser = subparsers.add_parser('filter', help='Filter rows in a CSV file based on a condition')
    filter_parser.add_argument('input', help='Path to the input CSV file')
    filter_parser.add_argument('output', help='Path to the output CSV file')
    filter_parser.add_argument('-d', '--delimiter', default=',', help='Delimiter used in the CSV (default: comma)')
    filter_parser.add_argument('--condition', required=True, help='Condition to filter rows (e.g., "age>18") - note: this is a simple example, for complex conditions use a Python expression with the row as a dictionary)')

    # Convert delimiter command
    convert_parser = subparsers.add_parser('convert', help='Convert a CSV file from one delimiter to another')
    convert_parser.add_argument('input', help='Path to the input CSV file')
    convert_parser.add_argument('output', help='Path to the output CSV file')
    convert_parser.add_argument('-i', '--input-delimiter', default=',', help='Delimiter of the input CSV (default: comma)')
    convert_parser.add_argument('-o', '--output-delimiter', default=',', help='Delimiter for the output CSV (default: comma)')

    args = parser.parse_args()

    if args.command == 'read':
        data = read_csv(args.file, delimiter=args.delimiter, has_header=not args.no_header)
        for row in data:
            print(row)

    elif args.command == 'write':
        # For simplicity, we'll read from stdin in this example.
        # In a more advanced tool, we might read from a file or another source.
        print("Writing to CSV is not fully implemented in this example. Please provide data via stdin or extend the tool.", file=sys.stderr)
        sys.exit(1)

    elif args.command == 'filter':
        # This is a simplified example. In reality, we would need to parse the condition and apply it.
        # For the sake of this example, we'll just read and write without filtering.
        print("Filtering is not fully implemented in this example. Please extend the tool to handle conditions.", file=sys.stderr)
        sys.exit(1)

    elif args.command == 'convert':
        convert_csv_delimiter(args.input, args.output, args.input_delimiter, args.output_delimiter)
        print(f"Converted {args.input} from delimiter '{args.input_delimiter}' to '{args.output_delimiter}' and saved to {args.output}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()