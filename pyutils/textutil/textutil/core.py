"""Core text processing functions."""

import re
import textwrap
from typing import List


def camel_to_snake(s: str) -> str:
    """Convert a camelCase string to snake_case."""
    # Insert underscore before uppercase letters and convert to lowercase
    s = re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
    return s


def snake_to_camel(s: str) -> str:
    """Convert a snake_case string to camelCase."""
    components = s.split('_')
    # Capitalize the first letter of each component except the first
    return components[0] + ''.join(x.title() for x in components[1:])


def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome (ignoring case and non-alphanumeric)."""
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]


def count_vowels(s: str) -> int:
    """Count the number of vowels in a string."""
    return sum(1 for char in s.lower() if char in 'aeiou')


def count_consonants(s: str) -> int:
    """Count the number of consonants in a string."""
    return sum(1 for char in s.lower() if char in 'bcdfghjklmnpqrstvwxyz')


def remove_punctuation(s: str) -> str:
    """Remove punctuation from a string."""
    return re.sub(r'[^\w\s]', '', s)


def capitalize_words(s: str) -> str:
    """Capitalize the first letter of each word in a string."""
    return ' '.join(word.capitalize() for word in s.split())


def truncate_string(s: str, max_length: int, suffix: str = '...') -> str:
    """Truncate a string to a maximum length and add a suffix if truncated."""
    if len(s) <= max_length:
        return s
    return s[:max_length - len(suffix)] + suffix


def wrap_text(text: str, width: int = 70) -> str:
    """Wrap text to a specified width."""
    return textwrap.fill(text, width=width)