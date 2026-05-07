#!/usr/bin/env python3
"""
readme-gen: A tool to generate professional README.md files for GitHub projects.
"""

import argparse
import os
import sys
from datetime import datetime


def get_user_input():
    """Collect project details from user input."""
    print("📝 Let's generate a README.md for your project!")
    print("Please provide the following information (press Enter for defaults):\n")
    
    project_name = input("Project name: ").strip()
    if not project_name:
        project_name = "My Awesome Project"
    
    description = input("Project description: ").strip()
    if not description:
        description = "A brief description of the project."
    
    version = input("Version (default: 1.0.0): ").strip()
    if not version:
        version = "1.0.0"
    
    author = input("Author name: ").strip()
    if not author:
        author = "Your Name"
    
    license_choice = input("License (default: MIT): ").strip()
    if not license_choice:
        license_choice = "MIT"
    
    language = input("Primary programming language (optional): ").strip()
    
    return {
        "project_name": project_name,
        "description": description,
        "version": version,
        "author": author,
        "license": license_choice,
        "language": language,
        "year": datetime.now().year
    }


def generate_readme(data):
    """Generate README content based on provided data."""
    badges = []
    if data["language"]:
        badges.append(f"![{data['language']}](https://img.shields.io/badge/{data['language']}-blue)")
    badges.append(f"![License: {data['license']}](https://img.shields.io/badge/License-{data['license']}-yellow)")
    
    badges_line = " ".join(badges) if badges else ""
    
    content = f"""# {data['project_name']}

{badges_line}

## Description

{data['description']}

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

```bash
# Installation instructions
```

## Usage

```bash
# Usage examples
```

## License

This project is licensed under the {data['license']} License - see the [LICENSE](LICENSE) file for details.

## Author

{data['author']}

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

*Generated with [readme-gen](https://github.com/brucestudios/readme-gen) on {datetime.now().strftime('%Y-%m-%d')}*
"""
    return content


def main():
    parser = argparse.ArgumentParser(description="Generate a README.md file for your project.")
    parser.add_argument("--non-interactive", action="store_true", 
                        help="Use command line arguments instead of interactive prompts")
    parser.add_argument("--name", help="Project name")
    parser.add_argument("--description", help="Project description")
    parser.add_argument("--version", default="1.0.0", help="Project version")
    parser.add_argument("--author", help="Author name")
    parser.add_argument("--license", default="MIT", help="License type")
    parser.add_argument("--language", help="Primary programming language")
    parser.add_argument("--output", default="README.md", help="Output file path")
    
    args = parser.parse_args()
    
    if args.non_interactive:
        data = {
            "project_name": args.name or "My Awesome Project",
            "description": args.description or "A brief description of the project.",
            "version": args.version,
            "author": args.author or "Your Name",
            "license": args.license,
            "language": args.language,
            "year": datetime.now().year
        }
    else:
        data = get_user_input()
    
    readme_content = generate_readme(data)
    
    try:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(readme_content)
        print(f"\n✅ README.md generated successfully at {os.path.abspath(args.output)}")
    except Exception as e:
        print(f"\n❌ Error writing file: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()