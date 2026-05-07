"""
Validation utility functions.
"""

import re
from typing import Union


def is_email(email: str) -> bool:
    """Validate email format using regex."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def is_url(url: str) -> bool:
    """Validate URL format using regex."""
    pattern = r'^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$'
    return bool(re.match(pattern, url))


def is_phone_number(phone: str) -> bool:
    """Validate phone number (simple: digits, optional +, spaces, dashes, parentheses)."""
    # Remove allowed characters
    cleaned = re.sub(r'[\+\s\-\(\)]', '', phone)
    return cleaned.isdigit() and len(cleaned) >= 10


def is_strong_password(password: str) -> bool:
    """Check password strength: at least 8 chars, contains upper, lower, digit, special."""
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        return False
    return True


def is_alpha(text: str) -> bool:
    """Check if string contains only letters (Unicode letters)."""
    return text.isalpha()


def is_alphanumeric(text: str) -> bool:
    """Check if string is alphanumeric (letters and digits only)."""
    return text.isalnum()