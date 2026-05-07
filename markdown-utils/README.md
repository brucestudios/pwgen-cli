# Markdown Utils

A collection of utilities for processing Markdown files.

## Features

- Extract headers from Markdown
- Convert Markdown to plain text
- Count words, lines, and characters in Markdown
- More utilities coming soon!

## Installation

```bash
pip install markdown-utils
```

## Usage

### Extract headers

```python
from markdown_utils.core import extract_headers

markdown_text = """
# Title
## Section 1
### Subsection
## Section 2
"""

headers = extract_headers(markdown_text)
print(headers)
# Output: [('#', 'Title'), ('##', 'Section 1'), ('###', 'Subsection'), ('##', 'Section 2')]
```

### Convert to plain text

```python
from markdown_utils.core import markdown_to_text

plain_text = markdown_to_text(markdown_text)
print(plain_text)
# Output: Title\nSection 1\nSubsection\nSection 2
```

## Development

To install in development mode:

```bash
pip install -e .[dev]
```

Running tests:

```bash
python -m unittest discover tests
```

## License

MIT
