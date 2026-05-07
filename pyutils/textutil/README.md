# TextUtil

A comprehensive Python library for text processing and manipulation.

## Features

- Convert between camelCase and snake_case
- Reverse strings
- Check for palindromes
- Count vowels and consonants
- Remove punctuation
- Capitalize words
- Truncate strings with ellipsis
- Wrap text to a specified width

## Installation

```bash
pip install textutil
```

## Usage

```python
from textutil import camel_to_snake, snake_to_camel, reverse_string, is_palindrome

# Convert camelCase to snake_case
camel_to_snake("helloWorld")  # Returns: "hello_world"

# Convert snake_case to camelCase
snake_to_camel("hello_world")  # Returns: "helloWorld"

# Reverse a string
reverse_string("hello")  # Returns: "olleh"

# Check for palindrome
is_palindrome("A man, a plan, a canal: Panama")  # Returns: True
```

## API Reference

See the [documentation](https://github.com/brucestudios/textutil#readme) for detailed API reference.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.