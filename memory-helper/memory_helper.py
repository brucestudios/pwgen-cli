#!/usr/bin/env python3
"""
Memory Helper - A CLI tool to manage OpenClaw memory files.

Features:
  - List daily memory files and MEMORY.md
  - Search within memory files
  - Add a new daily memory file with a template
  - View a specific memory file

Usage:
  memory_helper list          # List all memory files
  memory_helper search <term> # Search for term in memory files
  memory_helper add           # Create a new daily memory file
  memory_helper view <file>   # View a specific memory file
"""

import os
import sys
import argparse
from datetime import datetime
from pathlib import Path

# Constants
MEMORY_DIR = Path.home() / '.openclaw' / 'workspace' / 'memory'
MEMORY_FILE = Path.home() / '.openclaw' / 'workspace' / 'MEMORY.md'

def list_memory_files():
    """List all memory files (daily and MEMORY.md)."""
    print("Memory files:")
    if MEMORY_FILE.exists():
        print(f"  {MEMORY_FILE}")
    daily_files = sorted(MEMORY_DIR.glob('*.md')) if MEMORY_DIR.exists() else []
    for f in daily_files:
        print(f"  {f}")

def search_memory(term):
    """Search for term in memory files."""
    files_to_search = []
    if MEMORY_FILE.exists():
        files_to_search.append(MEMORY_FILE)
    if MEMORY_DIR.exists():
        files_to_search.extend(MEMORY_DIR.glob('*.md'))
    
    found = False
    for file_path in files_to_search:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f, 1):
                    if term.lower() in line.lower():
                        print(f"{file_path}:{i}: {line.rstrip()}")
                        found = True
        except Exception as e:
            print(f"Error reading {file_path}: {e}", file=sys.stderr)
    
    if not found:
        print(f"No matches found for '{term}'.")

def add_daily_memory():
    """Create a new daily memory file with a template."""
    if not MEMORY_DIR.exists():
        MEMORY_DIR.mkdir(parents=True)
    
    today = datetime.now().strftime('%Y-%m-%d')
    filename = MEMORY_DIR / f"{today}.md"
    
    if filename.exists():
        print(f"File {filename} already exists.")
        return
    
    template = f"""# Memory for {today}

- **Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Events
- 

## Thoughts & Insights
- 

## Todos
- [ ] 

## Notes
- 
"""
    filename.write_text(template, encoding='utf-8')
    print(f"Created {filename}")

def view_memory(file_path):
    """View a specific memory file."""
    path = Path(file_path)
    if not path.exists():
        # Try to find in memory directory or as a relative path
        alt_path = MEMORY_DIR / file_path
        if alt_path.exists():
            path = alt_path
        else:
            alt_path = Path.home() / '.openclaw' / 'workspace' / file_path
            if alt_path.exists():
                path = alt_path
            else:
                print(f"File not found: {file_path}")
                return
    
    try:
        content = path.read_text(encoding='utf-8')
        print(content)
    except Exception as e:
        print(f"Error reading {path}: {e}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description='Manage OpenClaw memory files.')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # list command
    subparsers.add_parser('list', help='List all memory files')
    
    # search command
    search_parser = subparsers.add_parser('search', help='Search for term in memory files')
    search_parser.add_argument('term', help='Term to search for')
    
    # add command
    subparsers.add_parser('add', help='Create a new daily memory file')
    
    # view command
    view_parser = subparsers.add_parser('view', help='View a specific memory file')
    view_parser.add_argument('file', help='Memory file to view (e.g., 2026-05-05.md or MEMORY.md)')
    
    args = parser.parse_args()
    
    if args.command == 'list':
        list_memory_files()
    elif args.command == 'search':
        search_memory(args.term)
    elif args.command == 'add':
        add_daily_memory()
    elif args.command == 'view':
        view_memory(args.file)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()