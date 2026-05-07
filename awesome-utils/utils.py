#!/usr/bin/env python3
"""
Awesome Utils - A collection of helpful utility functions.
"""

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def factorial(n: int) -> int:
    """Calculate factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def format_bytes(size: int) -> str:
    """Convert bytes to human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"

if __name__ == "__main__":
    # Simple demo
    print("Awesome Utils Demo")
    print("-" * 20)
    print(f"Is 'Racecar' a palindrome? {is_palindrome('Racecar')}")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Format 1024 bytes: {format_bytes(1024)}")