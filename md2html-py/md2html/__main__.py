import sys
from .core import markdown_to_html

def main() -> None:
    if len(sys.argv) > 1:
        # Read from file
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        # Read from stdin
        text = sys.stdin.read()
    
    html = markdown_to_html(text)
    sys.stdout.write(html)

if __name__ == "__main__":
    main()