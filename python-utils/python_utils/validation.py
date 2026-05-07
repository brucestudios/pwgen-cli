import re

def is_email(email: str) -> bool:
    """Return True if the string is a valid email address."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_url(url: str) -> bool:
    """Return True if the string is a valid URL."""
    pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    return bool(re.match(pattern, url))

def is_alpha(text: str) -> bool:
    """Return True if the string contains only alphabetic characters."""
    return text.isalpha()

def is_alphanumeric(text: str) -> bool:
    """Return True if the string contains only alphanumeric characters."""
    return text.isalnum()

def is_strong_password(password: str) -> bool:
    """Return True if the password is strong (at least 8 chars, upper, lower, digit, special)."""
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True