import sys
import markdown
from .extensions.footnote import FootnoteExtension
from .extensions.tasklist import TaskListExtension

def main():
    if len(sys.argv) < 2:
        print("Usage: markdown-utils <command> [options]")
        print("Commands:")
        print("  footnote   - Process footnotes in a Markdown file")
        print("  tasklist   - Process task lists in a Markdown file")
        sys.exit(1)

    command = sys.argv[1]
    if command == "footnote":
        if len(sys.argv) < 3:
            print("Usage: markdown-utils footnote <input_file> [output_file]")
            sys.exit(1)
        input_file = sys.argv[2]
        output_file = sys.argv[3] if len(sys.argv) > 3 else None
        with open(input_file, 'r') as f:
            text = f.read()
        html = markdown.markdown(text, extensions=[FootnoteExtension()])
        if output_file:
            with open(output_file, 'w') as f:
                f.write(html)
        else:
            print(html)
    elif command == "tasklist":
        if len(sys.argv) < 3:
            print("Usage: markdown-utils tasklist <input_file> [output_file]")
            sys.exit(1)
        input_file = sys.argv[2]
        output_file = sys.argv[3] if len(sys.argv) > 3 else None
        with open(input_file, 'r') as f:
            text = f.read()
        html = markdown.markdown(text, extensions=[TaskListExtension()])
        if output_file:
            with open(output_file, 'w') as f:
                f.write(html)
        else:
            print(html)
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
