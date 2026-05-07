#!/usr/bin/env python3
"""
Text Utilities - A collection of text processing tools

This module provides various text processing utilities for common string manipulation tasks.
"""

import re
import string
from typing import List, Dict, Tuple, Optional
from collections import Counter


def reverse_string(text: str) -> str:
    """
    Reverse a string.
    
    Args:
        text: Input string to reverse
        
    Returns:
        Reversed string
        
    Example:
        >>> reverse_string("hello")
        'olleh'
    """
    return text[::-1]


def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word in a string.
    
    Args:
        text: Input string
        
    Returns:
        String with each word capitalized
        
    Example:
        >>> capitalize_words("hello world")
        'Hello World'
    """
    return text.title()


def count_words(text: str) -> int:
    """
    Count the number of words in a string.
    
    Args:
        text: Input string
        
    Returns:
        Number of words
        
    Example:
        >>> count_words("Hello world, how are you?")
        5
    """
    # Split by whitespace and filter out empty strings
    words = [word for word in text.split() if word.strip()]
    return len(words)


def count_characters(text: str, include_spaces: bool = True) -> int:
    """
    Count characters in a string.
    
    Args:
        text: Input string
        include_spaces: Whether to count spaces (default: True)
        
    Returns:
        Character count
        
    Example:
        >>> count_characters("Hello World", include_spaces=False)
        10
    """
    if include_spaces:
        return len(text)
    else:
        return len([c for c in text if not c.isspace()])


def remove_punctuation(text: str) -> str:
    """
    Remove punctuation from a string.
    
    Args:
        text: Input string
        
    Returns:
        String without punctuation
        
    Example:
        >>> remove_punctuation("Hello, world!")
        'Hello world'
    """
    return text.translate(str.maketrans('', '', string.punctuation))


def is_palindrome(text: str) -> bool:
    """
    Check if a string is a palindrome (reads the same forwards and backwards).
    
    Args:
        text: Input string to check
        
    Returns:
        True if palindrome, False otherwise
        
    Example:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^A-Za-z0-9]', '', text.lower())
    return cleaned == cleaned[::-1]


def extract_emails(text: str) -> List[str]:
    """
    Extract email addresses from a string.
    
    Args:
        text: Input string
        
    Returns:
        List of email addresses found
        
    Example:
        >>> extract_emails("Contact us at info@example.com or support@test.org")
        ['info@example.com', 'support@test.org']
    """
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, text)


def extract_urls(text: str) -> List[str]:
    """
    Extract URLs from a string.
    
    Args:
        text: Input string
        
    Returns:
        List of URLs found
        
    Example:
        >>> extract_urls("Visit https://example.com or http://test.org")
        ['https://example.com', 'http://test.org']
    """
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    return re.findall(url_pattern, text)


def word_frequency(text: str) -> Dict[str, int]:
    """
    Calculate word frequency in a string.
    
    Args:
        text: Input string
        
    Returns:
        Dictionary with words as keys and their frequencies as values
        
    Example:
        >>> word_frequency("hello world hello")
        {'hello': 2, 'world': 1}
    """
    # Convert to lowercase and split into words
    words = re.findall(r'\b\w+\b', text.lower())
    return dict(Counter(words))


def find_longest_word(text: str) -> Tuple[str, int]:
    """
    Find the longest word in a string.
    
    Args:
        text: Input string
        
    Returns:
        Tuple of (longest_word, length)
        
    Example:
        >>> find_longest_word("The quick brown fox jumps over the lazy dog")
        ('jumps', 5)
    """
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return ("", 0)
    
    longest_word = max(words, key=len)
    return (longest_word, len(longest_word))


def convert_case(text: str, case_type: str = "lower") -> str:
    """
    Convert text to different cases.
    
    Args:
        text: Input string
        case_type: Type of case conversion ("lower", "upper", "title", "sentence")
        
    Returns:
        Converted string
        
    Example:
        >>> convert_case("Hello World", "upper")
        'HELLO WORLD'
    """
    case_type = case_type.lower()
    if case_type == "lower":
        return text.lower()
    elif case_type == "upper":
        return text.upper()
    elif case_type == "title":
        return text.title()
    elif case_type == "sentence":
        # Capitalize first letter of each sentence
        sentences = re.split(r'([.!?]+)', text)
        result = ""
        for i, part in enumerate(sentences):
            if i % 2 == 0:  # Actual sentence part
                result += part.strip().capitalize() + (" " if part.strip() else "")
            else:  # Punctuation
                result += part
        return result.strip()
    else:
        raise ValueError(f"Unsupported case type: {case_type}. Use 'lower', 'upper', 'title', or 'sentence'")


def remove_extra_whitespace(text: str) -> str:
    """
    Remove extra whitespace from a string.
    
    Args:
        text: Input string
        
    Returns:
        String with normalized whitespace
        
    Example:
        >>> remove_extra_whitespace("Hello   world  !")
        'Hello world !'
    """
    return re.sub(r'\s+', ' ', text.strip())


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate text to a maximum length.
    
    Args:
        text: Input string
        max_length: Maximum length of the result
        suffix: String to append when truncating (default: "...")
        
    Returns:
        Truncated string
        
    Example:
        >>> truncate_text("Hello world, this is a long sentence", 15)
        'Hello world,...'
    """
    if len(text) <= max_length:
        return text
    
    # If suffix would make it longer than max_length, adjust
    if len(suffix) >= max_length:
        return suffix[:max_length]
    
    return text[:max_length - len(suffix)] + suffix


def is_anagram(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams.
    
    Args:
        str1: First string
        str2: Second string
        
    Returns:
        True if anagrams, False otherwise
        
    Example:
        >>> is_anagram("listen", "silent")
        True
        >>> is_anagram("hello", "world")
        False
    """
    # Remove spaces and convert to lowercase
    clean_str1 = re.sub(r'\s+', '', str1.lower())
    clean_str2 = re.sub(r'\s+', '', str2.lower())
    
    return sorted(clean_str1) == sorted(clean_str2)


def generate_lorem_ipsum(words: int = 50) -> str:
    """
    Generate Lorem Ipsum placeholder text.
    
    Args:
        words: Number of words to generate (default: 50)
        
    Returns:
        Lorem Ipsum text
        
    Example:
        >>> generate_lorem_ipsum(5)
        'Lorem ipsum dolor sit amet'
    """
    lorem_words = [
        "Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing",
        "elit", "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore",
        "et", "dolore", "magna", "aliqua", "Ut", "enim", "ad", "minim", "veniam",
        "quis", "nostrud", "exercitation", "ullamco", "laboris", "nisi", "ut",
        "aliquip", "ex", "ea", "commodo", "consequat", "Duis", "aute", "irure",
        "dolor", "in", "reprehenderit", "in", "voluptate", "velit", "esse",
        "cillum", "dolore", "eu", "fugiat", "nulla", "pariatur", "Excepteur",
        "sint", "occaecat", "cupidatat", "non", "proident", "sunt", "in",
        "culpa", "qui", "officia", "deserunt", "mollit", "anim", "id", "est", "laborum"
    ]
    
    import random
    selected_words = [random.choice(lorem_words) for _ in range(words)]
    result = ' '.join(selected_words)
    # Capitalize first letter and add period
    return result.capitalize() + '.'


def main():
    """Main function to demonstrate the text utilities."""
    print("=== Text Utilities Demo ===\n")
    
    # Sample text for demonstration
    sample_text = "Hello World! This is a sample text. It contains multiple sentences. Let's test various functions."
    
    print(f"Original text: {sample_text}\n")
    
    # Demonstrate various functions
    print("1. Reverse string:")
    print(f"   {reverse_string(sample_text[:20])}\n")
    
    print("2. Capitalize words:")
    print(f"   {capitalize_words(sample_text[:30])}\n")
    
    print("3. Word count:")
    print(f"   {count_words(sample_text)} words\n")
    
    print("4. Character count (with spaces):")
    print(f"   {count_characters(sample_text)} characters\n")
    
    print("5. Character count (without spaces):")
    print(f"   {count_characters(sample_text, include_spaces=False)} characters\n")
    
    print("6. Remove punctuation:")
    print(f"   {remove_punctuation(sample_text)}\n")
    
    print("7. Palindrome check:")
    print(f"   'racecar' -> {is_palindrome('racecar')}")
    print(f"   'hello' -> {is_palindrome('hello')}\n")
    
    print("8. Extract emails:")
    email_text = "Contact us at info@example.com or support@test.org"
    print(f"   {extract_emails(email_text)}\n")
    
    print("9. Extract URLs:")
    url_text = "Visit https://example.com or http://test.org for more info"
    print(f"   {extract_urls(url_text)}\n")
    
    print("10. Word frequency:")
    freq_text = "hello world hello python world"
    print(f"   {word_frequency(freq_text)}\n")
    
    print("11. Longest word:")
    longest, length = find_longest_word(sample_text)
    print(f"   '{longest}' ({length} characters)\n")
    
    print("12. Case conversion:")
    print(f"   Lower: {convert_case(sample_text, 'lower')}")
    print(f"   Upper: {convert_case(sample_text, 'upper')}")
    print(f"   Title: {convert_case(sample_text, 'title')}")
    print(f"   Sentence: {convert_case(sample_text, 'sentence')}\n")
    
    print("13. Remove extra whitespace:")
    messy_text = "Hello   world  !   How   are   you?"
    print(f"   Original: '{messy_text}'")
    print(f"   Cleaned:  '{remove_extra_whitespace(messy_text)}'\n")
    
    print("14. Truncate text:")
    long_text = "This is a very long text that needs to be truncated for display purposes"
    print(f"   Original: {long_text}")
    print(f"   Truncated: {truncate_text(long_text, 30)}\n")
    
    print("15. Anagram check:")
    print(f"   'listen' & 'silent' -> {is_anagram('listen', 'silent')}")
    print(f"   'hello' & 'world' -> {is_anagram('hello', 'world')}\n")
    
    print("16. Generate Lorem Ipsum:")
    print(f"   {generate_lorem_ipsum(10)}\n")


if __name__ == "__main__":
    main()