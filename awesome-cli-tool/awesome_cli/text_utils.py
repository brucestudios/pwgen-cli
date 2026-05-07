"""Text processing utilities for awesome-cli-tool."""

import string
from typing import List


def upper(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()


def lower(text: str) -> str:
    """Convert text to lowercase."""
    return text.lower()


def title(text: str) -> str:
    """Convert text to title case."""
    return text.title()


def snake_case(text: str) -> str:
    """Convert text to snake_case."""
    # Replace spaces and hyphens with underscores, then convert to lowercase
    text = text.replace(' ', '_').replace('-', '_')
    # Remove any non-alphanumeric characters (except underscores)
    text = ''.join(c if c.isalnum() or c == '_' else '_' for c in text)
    # Convert to lowercase
    return text.lower()


def kebab_case(text: str) -> str:
    """Convert text to kebab-case."""
    # Replace spaces and underscores with hyphens, then convert to lowercase
    text = text.replace(' ', '-').replace('_', '-')
    # Remove any non-alphanumeric characters (except hyphens)
    text = ''.join(c if c.isalnum() or c == '-' else '-' for c in text)
    # Convert to lowercase
    return text.lower()


def camel_case(text: str) -> str:
    """Convert text to camelCase."""
    # Split by spaces, underscores, and hyphens
    words = text.replace('_', ' ').replace('-', ' ').split()
    # Lowercase the first word, capitalize the rest
    if not words:
        return ''
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])


def pascal_case(text: str) -> str:
    """Convert text to PascalCase."""
    # Split by spaces, underscores, and hyphens
    words = text.replace('_', ' ').replace('-', ' ').split()
    # Capitalize each word and join
    return ''.join(word.capitalize() for word in words)


def count_words(text: str) -> int:
    """Count the number of words in text."""
    return len(text.split())


def count_lines(text: str) -> int:
    """Count the number of lines in text."""
    return len(text.splitlines())


def count_chars(text: str) -> int:
    """Count the number of characters in text."""
    return len(text)


def count_chars_no_spaces(text: str) -> int:
    """Count the number of characters in text excluding spaces."""
    return len(text.replace(' ', ''))


def reverse_text(text: str) -> str:
    """Reverse the text."""
    return text[::-1]


def remove_extra_spaces(text: str) -> str:
    """Remove extra spaces from text."""
    return ' '.join(text.split())


def to_list(text: str, separator: str = ',') -> List[str]:
    """Convert text to a list using a separator."""
    return [item.strip() for item in text.split(separator) if item.strip()]