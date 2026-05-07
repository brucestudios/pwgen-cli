"""Text utility library."""

from .core import (
    camel_to_snake,
    snake_to_camel,
    reverse_string,
    is_palindrome,
    count_vowels,
    count_consonants,
    remove_punctuation,
    capitalize_words,
    truncate_string,
    wrap_text,
)

__all__ = [
    "camel_to_snake",
    "snake_to_camel",
    "reverse_string",
    "is_palindrome",
    "count_vowels",
    "count_consonants",
    "remove_punctuation",
    "capitalize_words",
    "truncate_string",
    "wrap_text",
    "__version__",
]

__version__ = "1.0.0"