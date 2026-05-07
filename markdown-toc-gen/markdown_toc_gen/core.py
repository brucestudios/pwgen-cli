import re
from typing import List, Tuple, Optional


def generate_toc(
    filepath: str,
    indent: int = 2,
    marker: Optional[str] = None,
) -> str:
    """
    Generate a table of contents for a Markdown file.

    Args:
        filepath: Path to the Markdown file.
        indent: Number of spaces for each indentation level (default: 2).
        marker: If provided, the TOC will replace this line in the file.
                If not provided, the TOC is prepended to the file.

    Returns:
        The generated TOC as a string (with optional marker replacement logic
        handled by the caller if needed). This function only generates the TOC
        content; it does not read or write the file.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Extract headings
    headings: List[Tuple[int, str]] = []  # (level, text)
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("#"):
            # Count leading #
            level = 0
            for ch in stripped:
                if ch == "#":
                    level += 1
                else:
                    break
            # Ensure there's a space after the #s
            if level > 0 and len(stripped) > level and stripped[level] == " ":
                heading_text = stripped[level + 1 :].strip()
                # Remove any trailing inline HTML or markdown links? Keep simple.
                headings.append((level, heading_text))

    if not headings:
        return ""

    # Determine indent string
    indent_str = " " * indent

    # Build TOC lines
    toc_lines: List[str] = []
    toc_lines.append("## Table of Contents")
    for level, text in headings:
        # Create anchor: lowercase, replace spaces with hyphens, remove punctuation
        anchor = re.sub(r"[^\w\s-]", "", text).strip().lower()
        anchor = re.sub(r"[-\s]+", "-", anchor)
        # Indentation: (level-1) * indent_str
        if level == 1:
            indent_level = 0
        else:
            indent_level = level - 1
        line_indent = indent_str * indent_level
        toc_lines.append(f"{line_indent}- [{text}](#{anchor})")

    return "\n".join(toc_lines) + "\n"


def insert_toc(
    filepath: str,
    toc: str,
    marker: Optional[str] = None,
) -> None:
    """
    Insert the generated TOC into the file.

    Args:
        filepath: Path to the Markdown file.
        toc: The generated TOC string.
        marker: If provided, replace this line with the TOC.
                If not provided, prepend the TOC to the file.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines: List[str] = []
    if marker is not None:
        # Find the marker line and replace it
        for line in lines:
            if line.strip() == marker.strip():
                new_lines.append(toc)
                # Do not keep the original marker line
            else:
                new_lines.append(line)
    else:
        # Prepend TOC
        new_lines.append(toc)
        new_lines.extend(lines)

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)


if __name__ == "__main__":
    # Simple CLI for testing
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Generate TOC for a Markdown file.")
    parser.add_argument("file", help="Markdown file to process")
    parser.add_argument(
        "-o",
        "--output",
        help="Output file (default: overwrite input)",
    )
    parser.add_argument(
        "--indent",
        type=int,
        default=2,
        help="Number of spaces for indentation (default: 2)",
    )
    parser.add_argument(
        "--marker",
        help="If present, TOC will replace this line; otherwise appended at top",
    )

    args = parser.parse_args()

    toc = generate_toc(args.file, indent=args.indent, marker=args.marker)
    if not toc:
        print("No headings found.", file=sys.stderr)
        sys.exit(1)

    if args.output:
        # Write toc to output file (without inserting into original)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(toc)
    else:
        insert_toc(args.file, toc, marker=args.marker)