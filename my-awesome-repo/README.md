# Awesome Text Utils

A lightweight Python library for common text processing utilities.

## Features

- Slugify strings for URLs
- Truncate text with ellipsis
- Convert to title case with smart handling
- Count words, sentences, characters
- Remove extra whitespace
- More utilities coming soon...

## Installation

```bash
pip install awesome-text-utils
```

## Usage

```python
from awesome_text_utils import slugify, truncate, title_case

slug = slugify("Hello, World!")  # hello-world
truncated = truncate("This is a very long text that needs shortening.", 20)
title = title_case("hello world of python")
```

## Development

### Setup

```bash
git clone https://github.com/<your-username>/awesome-text-utils.git
cd awesome-text-utils
python -m venv venv
source venv/bin/activate
pip install -e .[dev]
```

### Running Tests

```bash
pytest
```

### Building and Publishing

```bash
python -m build
twine upload dist/*
```

## License

MIT
