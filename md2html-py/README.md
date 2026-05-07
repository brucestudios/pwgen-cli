# md2html-py

A simple Python library to convert Markdown to HTML with optional YAML front matter parsing, inspired by Jekyll.

## Features

- Convert Markdown strings to HTML
- Parse YAML front matter (like Jekyll)
- Supports extensions (tables, fenced code, etc.)
- Simple and lightweight

## Installation

```bash
pip install md2html-py
```

## Usage

### Basic Usage

```python
from md2html import markdown_to_html

html = markdown_to_html("# Hello World\nThis is **bold** text.")
print(html)
# Output: <h1>Hello World</h1>\n<p>This is <strong>bold</strong> text.</p>
```

### With Front Matter

```python
from md2html import parse_front_matter

content = """---
title: My Blog Post
date: 2023-01-01
tags: [python, markdown]
---

# My Blog Post

This is the content of my post.
"""

metadata, html_content = parse_front_matter(content)
print(metadata)  # {'title': 'My Blog Post', 'date': '2023-01-01', 'tags': ['python', 'markdown']}
print(html_content)  # <h1>My Blog Post</h1>\n<p>This is the content of my post.</p>
```

### As a Command Line Tool

```bash
echo "# Hello" | md2html
# Outputs: <h1>Hello</h1>
```

## Development

```bash
# Install dependencies
pip install -e .[dev]

# Run tests
pytest

# Build package
python -m build
```

## License

MIT