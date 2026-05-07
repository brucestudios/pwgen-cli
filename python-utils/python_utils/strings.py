def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word in the text."""
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string(text: str) -> str:
    """Reverse the input string."""
    return text[::-1]

def is_palindrome(text: str) -> bool:
    """Check if the text is a palindrome (ignoring case and non-alphanumeric)."""
    cleaned = ''.join(filter(str.isalnum, text)).lower()
    return cleaned == cleaned[::-1]

def remove_whitespace(text: str) -> str:
    """Remove all whitespace from the text."""
    return ''.join(text.split())