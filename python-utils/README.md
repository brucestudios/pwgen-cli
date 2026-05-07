# Python Utils

A collection of utility functions for Python to simplify common tasks.

## Features

- String manipulation utilities
- File handling helpers
- Data validation functions

## Installation

```bash
pip install python-utils
```

## Usage

### String Utilities

```python
from python_utils.string_utils import capitalize_words, remove_extra_spaces

text = "  hello   world  "
capitalized = capitalize_words(text)  # "Hello   World  "
cleaned = remove_extra_spaces(text)   # "hello world"
```

### File Utilities

```python
from python_utils.file_utils import read_lines, write_lines

lines = read_lines('example.txt')
write_lines('output.txt', lines)
```

### Validators

```python
from python_utils.validators import is_valid_email, is_strong_password

is_valid_email('test@example.com')  # True
is_strong_password('weak')          # False
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

MIT