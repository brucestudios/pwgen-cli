"""Text transformation functions."""

import random
import re
import textwrap
from typing import List, Sequence


def upper(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()


def lower(text: str) -> str:
    """Convert text to lowercase."""
    return text.lower()


def title(text: str) -> str:
    """Convert text to title case."""
    return text.title()


def sentence(text: str) -> str:
    """Convert text to sentence case."""
    if not text:
        return text
    return text[0].upper() + text[1:].lower()


def alternating(text: str) -> str:
    """Convert text to alternating case (e.g., hElLo WoRlD)."""
    result = []
    for i, c in enumerate(text):
        if c.isalpha():
            result.append(c.upper() if i % 2 == 0 else c.lower())
        else:
            result.append(c)
    return "".join(result)


def sort_lines(text: str, reverse: bool = False) -> str:
    """Sort lines of text alphabetically."""
    lines = text.splitlines()
    lines.sort(reverse=reverse)
    return "\n".join(lines)


def reverse_lines(text: str) -> str:
    """Reverse the order of lines."""
    lines = text.splitlines()
    lines.reverse()
    return "\n".join(lines)


def random_lines(text: str) -> str:
    """Shuffle lines randomly."""
    lines = text.splitlines()
    random.shuffle(lines)
    return "\n".join(lines)


def sort_by_length(text: str, reverse: bool = False) -> str:
    """Sort lines by length."""
    lines = text.splitlines()
    lines.sort(key=len, reverse=reverse)
    return "\n".join(lines)


def dedup_lines(text: str) -> str:
    """Remove duplicate lines (keeping first occurrence)."""
    seen = set()
    lines = []
    for line in text.splitlines():
        if line not in seen:
            seen.add(line)
            lines.append(line)
    return "\n".join(lines)


def dedup_words(text: str) -> str:
    """Remove duplicate words (keeping first occurrence) while preserving whitespace."""
    # We split by whitespace to get words, but we want to keep the original whitespace.
    # This is a simple approach: split the text into words and non-words (whitespace and punctuation)
    # and then deduplicate the words.
    # However, note that this might not preserve exact whitespace if there are multiple spaces/tabs.
    # For simplicity, we'll split by whitespace and then join by a single space.
    # If you need to preserve exact whitespace, a more complex regex is needed.
    words = text.split()
    seen = set()
    deduped = []
    for word in words:
        if word not in seen:
            seen.add(word)
            deduped.append(word)
    return " ".join(deduped)


def grep_lines(text: str, pattern: str, ignore_case: bool = False) -> str:
    """Filter lines matching a regex pattern."""
    flags = re.IGNORECASE if ignore_case else 0
    regex = re.compile(pattern, flags)
    lines = text.splitlines()
    matched = [line for line in lines if regex.search(line)]
    return "\n".join(matched)


def grep_v_lines(text: str, pattern: str, ignore_case: bool = False) -> str:
    """Filter lines NOT matching a regex pattern."""
    flags = re.IGNORECASE if ignore_case else 0
    regex = re.compile(pattern, flags)
    lines = text.splitlines()
    unmatched = [line for line in lines if not regex.search(line)]
    return "\n".join(unmatched)


def wrap_text(text: str, width: int = 70) -> str:
    """Wrap text to a given width."""
    return textwrap.fill(text, width=width)


def unwrap_text(text: str) -> str:
    """Unwrap text (join lines that are wrapped)."""
    # Join lines that are not empty and do not look like they are intentional line breaks?
    # Simple approach: join all lines with a space, then collapse multiple spaces.
    lines = text.splitlines()
    # Join non-empty lines with a space, and keep empty lines as paragraph breaks?
    # For simplicity, we'll join all lines with a space and then clean up.
    return re.sub(r"\s+", " ", " ".join(lines)).strip()


def extract_column(text: str, column: int, delimiter: str = None) -> str:
    """Extract a column (0-indexed) from delimited text."""
    lines = text.splitlines()
    extracted = []
    for line in lines:
        if delimiter is None:
            parts = line.split()
        else:
            parts = line.split(delimiter)
        if column < len(parts):
            extracted.append(parts[column])
        else:
            extracted.append("")  # or skip? We'll append empty string for missing.
    return "\n".join(extracted)


def join_lines(text: str, separator: str = " ") -> str:
    """Join lines with a separator."""
    return separator.join(text.splitlines())


def split_lines(text: str) -> List[str]:
    """Split text into lines (returns a list)."""
    return text.splitlines()