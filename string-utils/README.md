# Text Utilities

A comprehensive Python library for text processing and manipulation utilities.

## Features

- String reversal and case conversion
- Word and character counting
- Punctuation removal
- Palindrome detection
- Email and URL extraction
- Word frequency analysis
- Longest word finding
- Anagram checking
- Whitespace normalization
- Text truncation
- Lorem Ipsum generation

## Installation

```bash
pip install textutils
```

Or install from source:

```bash
git clone https://github.com/brucestudios/textutils.git
cd textutils
pip install -e .
```

## Usage

```python
from textutils.text_utils import (
    reverse_string, capitalize_words, count_words, 
    is_palindrome, extract_emails, extract_urls,
    word_frequency, is_anagram, generate_lorem_ipsum
)

# Reverse a string
reversed_text = reverse_string("hello")
print(reversed_text)  # "olleh"

# Count words
word_count = count_words("Hello world, how are you?")
print(word_count)  # 5

# Check palindrome
is_pal = is_palindrome("racecar")
print(is_pal)  # True

# Extract emails
emails = extract_emails("Contact us at info@example.com")
print(emails)  # ['info@example.com']

# Generate Lorem Ipsum
lorem = generate_lorem_ipsum(10)
print(lorem)
```

## API Reference

### String Manipulation
- `reverse_string(text: str) -> str`: Reverse a string
- `capitalize_words(text: str) -> str`: Capitalize first letter of each word
- `convert_case(text: str, case_type: str = "lower") -> str`: Convert text case (lower, upper, title, sentence)
- `remove_extra_whitespace(text: str) -> str`: Normalize whitespace
- `truncate_text(text: str, max_length: int, suffix: str = "...") -> str`: Truncate text to max length

### Analysis Functions
- `count_words(text: str) -> int`: Count words in text
- `count_characters(text: str, include_spaces: bool = True) -> int`: Count characters
- `remove_punctuation(text: str) -> str`: Remove punctuation from text
- `is_palindrome(text: str) -> bool`: Check if text is palindrome
- `word_frequency(text: str) -> Dict[str, int]`: Get word frequency dictionary
- `find_longest_word(text: str) -> Tuple[str, int]`: Find longest word and its length
- `is_anagram(str1: str, str2: str) -> bool`: Check if two strings are anagrams

### Extraction Functions
- `extract_emails(text: str) -> List[str]`: Extract email addresses
- `extract_urls(text: str) -> List[str]`: Extract URLs

### Generation Functions
- `generate_lorem_ipsum(words: int = 50) -> str`: Generate Lorem Ipsum text

## Development

To run tests:

```bash
python -m pytest tests/
```

To build the package:

```bash
python -m build
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request