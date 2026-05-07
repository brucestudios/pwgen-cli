import os
import sys
import yaml
import argparse
from pathlib import Path

def load_config(config_path):
    """Load configuration from YAML file."""
    if config_path and os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    return {}

def check_file(filepath, required_fields):
    """Check a single markdown file for frontmatter."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return f"Error reading {filepath}: {e}"

    # Check for frontmatter delimiters
    if not content.startswith('---\n'):
        return f"Missing frontmatter delimiter at start: {filepath}"

    # Find the end delimiter
    end_idx = content.find('\n---\n', 4)
    if end_idx == -1:
        return f"Missing closing frontmatter delimiter: {filepath}"

    # Extract frontmatter
    frontmatter = content[4:end_idx]
    try:
        data = yaml.safe_load(frontmatter)
    except yaml.YAMLError as e:
        return f"Invalid YAML in frontmatter: {filepath} - {e}"

    if data is None:
        return f"Empty frontmatter: {filepath}"

    # Check required fields
    missing = []
    for field in required_fields:
        if field not in data:
            missing.append(field)

    if missing:
        return f"Missing required fields {missing} in {filepath}"

    return None  # No error

def main():
    parser = argparse.ArgumentParser(description='Check Jekyll markdown files for proper frontmatter.')
    parser.add_argument('directory', help='Directory to scan for .md files')
    parser.add_argument('--config', '-c', help='Path to configuration YAML file', default='.jekyll-checker.yml')
    parser.add_argument('--required', '-r', nargs='*', help='Required fields (overrides config)', default=[])
    args = parser.parse_args()

    # Load config
    config = load_config(args.config)
    required_fields = args.required if args.required else config.get('required_fields', ['title', 'date'])

    # Walk directory
    errors = []
    for root, dirs, files in os.walk(args.directory):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                error = check_file(filepath, required_fields)
                if error:
                    errors.append(error)

    # Report
    if errors:
        print("Frontmatter check failed:", file=sys.stderr)
        for err in errors:
            print(err, file=sys.stderr)
        sys.exit(1)
    else:
        print(f"All {len([f for r, d, files in os.walk(args.directory) for f in files if f.endswith('.md')])} markdown files passed frontmatter check.")
        sys.exit(0)

if __name__ == '__main__':
    main()