import re
from typing import List


def slugify(text: str) -> str:
    """Convert a string to a URL-friendly slug."""
    # Convert to lowercase
    text = text.lower()
    # Replace non-alphanumeric characters (except spaces) with hyphens
    text = re.sub(r'[^a-z0-9\s]', '-', text)
    # Replace spaces and multiple hyphens with single hyphen
    text = re.sub(r'[\s-]+', '-', text)
    # Remove leading/trailing hyphens
    return text.strip('-')


def truncate(text: str, length: int, suffix: str = '...') -> str:
    """Truncate text to a given length, adding a suffix if truncated."""
    if len(text) <= length:
        return text
    return text[:length - len(suffix)] + suffix


def title_case(text: str) -> str:
    """Convert string to title case (first letter of each word capitalized)."""
    return text.title()


def word_count(text: str) -> int:
    """Count the number of words in text."""
    # Split by whitespace and filter out empty strings
    words = [w for w in text.split() if w]
    return len(words)


def sentence_count(text: str) -> int:
    """Count the number of sentences in text."""
    # Simple sentence ending detection
    sentences = re.split(r'[.!?]+', text)
    # Filter out empty strings
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)


def char_count(text: str, include_spaces: bool = True) -> int:
    """Count characters in text."""
    if include_spaces:
        return len(text)
    return len(text.replace(' ', ''))


def remove_extra_whitespace(text: str) -> str:
    """Remove leading/trailing whitespace and reduce internal whitespace to single spaces."""
    return re.sub(r'\s+', ' ', text).strip()