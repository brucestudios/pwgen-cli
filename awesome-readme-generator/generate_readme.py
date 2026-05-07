#!/usr/bin/env python3
"""
Awesome README Generator
A simple CLI tool to generate high-quality README.md files from templates.
"""

import argparse
import os
import sys

def generate_readme(args):
    """Generate README content based on arguments."""
    # Table of contents
    toc = []
    if args.installation:
        toc.append("- [Installation](#installation)")
    if args.usage:
        toc.append("- [Usage](#usage)")
    if args.license:
        toc.append("- [License](#license)")
    if args.contributing:
        toc.append("- [Contributing](#contributing)")
    if args.tests:
        toc.append("- [Tests](#tests)")
    if args.changelog:
        toc.append("- [Changelog](#changelog)")

    toc_str = "\n".join(toc) if toc else ""

    # Sections
    sections = []
    sections.append(f"# {args.project_name}\n")
    sections.append(f"{args.description}\n")

    if toc_str:
        sections.append(f"## Table of Contents\n{toc_str}\n")

    if args.installation:
        sections.append("## Installation\n")
        sections.append(f"```bash\n{args.installation_command}\n```\n")

    if args.usage:
        sections.append("## Usage\n")
        sections.append(f"```bash\n{args.usage_example}\n```\n")

    if args.license:
        sections.append(f"## License\n")
        sections.append(f"This project is licensed under the {args.license} License.\n")

    if args.contributing:
        sections.append("## Contributing\n")
        sections.append(f"{args.contributing}\n")

    if args.tests:
        sections.append("## Tests\n")
        sections.append(f"{args.tests}\n")

    if args.changelog:
        sections.append("## Changelog\n")
        sections.append(f"{args.changelog}\n")

    return "".join(sections)

def main():
    parser = argparse.ArgumentParser(description="Generate a high-quality README.md file.")
    parser.add_argument("--project-name", required=True, help="Project name")
    parser.add_argument("--description", required=True, help="Project description")
    parser.add_argument("--author", help="Author name (for reference)")
    parser.add_argument("--version", help="Project version")
    parser.add_argument("--license", default="MIT", help="License type (default: MIT)")
    parser.add_argument("--installation", action="store_true", help="Include installation section")
    parser.add_argument("--installation-command", default="pip install your-package", help="Installation command")
    parser.add_argument("--usage", action="store_true", help="Include usage section")
    parser.add_argument("--usage-example", default="your-command --help", help="Usage example")
    parser.add_argument("--contributing", help="Contributing guidelines")
    parser.add_argument("--tests", help="Testing instructions")
    parser.add_argument("--changelog", help="Changelog information")

    args = parser.parse_args()

    readme_content = generate_readme(args)

    # Write to README.md
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("README.md generated successfully!")

if __name__ == "__main__":
    main()