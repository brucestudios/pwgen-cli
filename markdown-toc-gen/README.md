# Markdown TOC Generator

A simple Python tool to generate a table of contents for Markdown files.

## Features

- Generates TOC from headings (`#`, `##`, `###`, etc.)
- Supports custom indentation (spaces or tabs)
- Can insert TOC at a specific marker or append to file
- Command-line interface with helpful options
- Works with both relative and absolute file paths

## Installation

```bash
pip install markdown-toc-gen
```

Or install from source:

```bash
git clone https://github.com/yourusername/markdown-toc-gen.git
cd markdown-toc-gen
pip install -e .
```

## Usage

### Command Line

```bash
markdown-toc-gen input.md [-o output.md] [--indent 2] [--marker "<!-- toc -->"]
```

- `input.md`: The markdown file to process
- `-o, --output`: Output file (default: overwrite input)
- `--indent`: Number of spaces for indentation (default: 2)
- `--marker`: If present, TOC will replace this line; otherwise appended at top

### As a Library

```python
from markdown_toc_gen import generate_toc

toc = generate_toc("path/to/file.md", indent=2)
print(toc)
```

## Example

Given a markdown file:

```markdown
# Introduction

## Getting Started

### Installation

## Usage

## API Reference
```

Running `markdown-toc-gen file.md` produces:

```markdown
## Table of Contents

- [Introduction](#introduction)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
  - [Usage](#usage)
  - [API Reference](#api-reference)
```

## License

MIT