"""
String utility functions.
"""

def capitalize_words(text: str) -> str:
    """Capitalize first letter of each word in the string."""
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string(text: str) -> str:
    """Reverse the input string."""
    return text[::-1]

def is_palindrome(text: str) -> bool:
    """Check if the string is a palindrome (ignoring case and non-alphanumeric)."""
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

def count_vowels(text: str) -> int:
    """Count the number of vowels in the string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def remove_whitespace(text: str) -> str:
    """Remove all whitespace characters from the string."""
    return ''.join(text.split())

def truncate_string(text: str, max_length: int) -> str:
    """Truncate the string to max_length and add ellipsis if needed."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + '...'