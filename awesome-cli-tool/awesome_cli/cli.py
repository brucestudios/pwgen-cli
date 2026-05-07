"""Command-line interface for awesome-cli-tool."""

import argparse
import sys
from .text_utils import (
    upper, lower, title, snake_case, kebab_case, camel_case, pascal_case,
    count_words, count_lines, count_chars, count_chars_no_spaces,
    reverse_text, remove_extra_spaces, to_list
)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Awesome CLI Tool - Text processing utilities",
        prog="awesome-text"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Case conversion commands
    case_parser = subparsers.add_parser('upper', help='Convert text to uppercase')
    case_parser.add_argument('text', nargs='?', help='Text to convert')
    case_parser.add_argument('--file', '-f', help='Read text from file')
    
    case_parser = subparsers.add_parser('lower', help='Convert text to lowercase')
    case_parser.add_argument('text', nargs='?', help='Text to convert')
    case_parser.add_argument('--file', '-f', help='Read text from file')
    
    case_parser = subparsers.add_parser('title', help='Convert text to title case')
    case_parser.add_argument('text', nargs='?', help='Text to convert')
    case_parser.add_argument('--file', '-f', help='Read text from file')
    
    case_parser = subparsers.add_parser('snake', help='Convert text to snake_case')
    case_parser.add_argument('text', nargs='?', help='Text to convert')
    case_parser.add_argument('--file', '-f', help='Read text from file')
    
    case_parser = subparsers.add_parser('kebab', help='Convert text to kebab-case')
    case_parser.add_argument('text', nargs='?', help='Text to convert')
    case_parser.add_argument('--file', '-f', help='Read text from file')
    
    case_parser = subparsers.add_parser('camel', help='Convert text to camelCase')
    case_parser.add_argument('text', nargs='?', help='Text to convert')
    case_parser.add_argument('--file', '-f', help='Read text from file')
    
    case_parser = subparsers.add_parser('pascal', help='Convert text to PascalCase')
    case_parser.add_argument('text', nargs='?', help='Text to convert')
    case_parser.add_argument('--file', '-f', help='Read text from file')
    
    # Counting commands
    count_parser = subparsers.add_parser('count', help='Count text statistics')
    count_parser.add_argument('text', nargs='?', help='Text to analyze')
    count_parser.add_argument('--file', '-f', help='Read text from file')
    count_parser.add_argument('--words', action='store_true', help='Count words')
    count_parser.add_argument('--lines', action='store_true', help='Count lines')
    count_parser.add_argument('--chars', action='store_true', help='Count characters')
    count_parser.add_argument('--chars-no-spaces', action='store_true', help='Count characters excluding spaces')
    
    # Other utilities
    subparsers.add_parser('reverse', help='Reverse text').add_argument('text', nargs='?', help='Text to reverse').add_argument('--file', '-f', help='Read text from file')
    subparsers.add_parser('clean-spaces', help='Remove extra spaces').add_argument('text', nargs='?', help='Text to clean').add_argument('--file', '-f', help='Read text from file')
    
    list_parser = subparsers.add_parser('list', help='Convert text to list')
    list_parser.add_argument('text', nargs='?', help='Text to convert')
    list_parser.add_argument('--file', '-f', help='Read text from file')
    list_parser.add_argument('--separator', '-s', default=',', help='Separator character (default: comma)')
    
    # Interactive mode
    subparsers.add_parser('interactive', help='Start interactive mode')
    
    args = parser.parse_args()
    
    # If no command provided, show help
    if not args.command:
        parser.print_help()
        return
    
    # Get text input
    text = None
    if args.command != 'interactive':
        if hasattr(args, 'file') and args.file:
            try:
                with open(args.file, 'r', encoding='utf-8') as f:
                    text = f.read()
            except FileNotFoundError:
                print(f"Error: File '{args.file}' not found.", file=sys.stderr)
                sys.exit(1)
            except Exception as e:
                print(f"Error reading file: {e}", file=sys.stderr)
                sys.exit(1)
        elif hasattr(args, 'text') and args.text:
            text = args.text
        else:
            # Try to read from stdin if not provided as argument
            if not sys.stdin.isatty():
                text = sys.stdin.read().rstrip('\n')
            else:
                print("Error: No text provided. Use --help for usage information.", file=sys.stderr)
                sys.exit(1)
    
    # Execute command
    try:
        if args.command == 'upper':
            result = upper(text)
            print(result)
        elif args.command == 'lower':
            result = lower(text)
            print(result)
        elif args.command == 'title':
            result = title(text)
            print(result)
        elif args.command == 'snake':
            result = snake_case(text)
            print(result)
        elif args.command == 'kebab':
            result = kebab_case(text)
            print(result)
        elif args.command == 'camel':
            result = camel_case(text)
            print(result)
        elif args.command == 'pascal':
            result = pascal_case(text)
            print(result)
        elif args.command == 'count':
            if args.words:
                print(count_words(text))
            elif args.lines:
                print(count_lines(text))
            elif args.chars:
                print(count_chars(text))
            elif args.chars_no_spaces:
                print(count_chars_no_spaces(text))
            else:
                # Default: show all counts
                print(f"Words: {count_words(text)}")
                print(f"Lines: {count_lines(text)}")
                print(f"Characters: {count_chars(text)}")
                print(f"Characters (no spaces): {count_chars_no_spaces(text)}")
        elif args.command == 'reverse':
            result = reverse_text(text)
            print(result)
        elif args.command == 'clean-spaces':
            result = remove_extra_spaces(text)
            print(result)
        elif args.command == 'list':
            result = to_list(text, args.separator)
            print(result)
        elif args.command == 'interactive':
            interactive_mode()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def interactive_mode():
    """Run interactive mode."""
    print("Awesome CLI Tool - Interactive Mode")
    print("Type 'help' for available commands, 'quit' to exit.")
    print()
    
    while True:
        try:
            command_input = input("awesome-text> ").strip()
            
            if not command_input:
                continue
                
            if command_input.lower() in ['quit', 'exit']:
                print("Goodbye!")
                break
                
            if command_input.lower() == 'help':
                print("Available commands:")
                print("  upper <text>     - Convert to uppercase")
                print("  lower <text>     - Convert to lowercase")
                print("  title <text>     - Convert to title case")
                print("  snake <text>     - Convert to snake_case")
                print("  kebab <text>     - Convert to kebab-case")
                print("  camel <text>     - Convert to camelCase")
                print("  pascal <text>    - Convert to PascalCase")
                print("  count <text>     - Count words, lines, characters")
                print("  reverse <text>   - Reverse text")
                print("  clean-spaces <text> - Remove extra spaces")
                print("  list <text>      - Convert to comma-separated list")
                print("  help             - Show this help")
                print("  quit/exit        - Exit interactive mode")
                continue
            
            parts = command_input.split(maxsplit=1)
            command = parts[0].lower()
            text = parts[1] if len(parts) > 1 else ""
            
            if not text:
                print("Error: No text provided for command.")
                continue
            
            # Execute command
            if command == 'upper':
                print(upper(text))
            elif command == 'lower':
                print(lower(text))
            elif command == 'title':
                print(title(text))
            elif command == 'snake':
                print(snake_case(text))
            elif command == 'kebab':
                print(kebab_case(text))
            elif command == 'camel':
                print(camel_case(text))
            elif command == 'pascal':
                print(pascal_case(text))
            elif command == 'count':
                print(f"Words: {count_words(text)}")
                print(f"Lines: {count_lines(text)}")
                print(f"Characters: {count_chars(text)}")
                print(f"Characters (no spaces): {count_chars_no_spaces(text)}")
            elif command == 'reverse':
                print(reverse_text(text))
            elif command == 'clean-spaces':
                print(remove_extra_spaces(text))
            elif command == 'list':
                print(to_list(text))
            else:
                print(f"Error: Unknown command '{command}'. Type 'help' for available commands.")
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()