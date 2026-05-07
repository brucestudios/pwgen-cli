# Textura

A versatile command-line tool for text transformation and manipulation.

## Features

- Case conversion (upper, lower, title, sentence, alternating)
- Text sorting (alphabetical, reverse, random, by length)
- Deduplication (remove duplicate lines, words)
- Filtering (grep-like, exclude lines)
- Text wrapping and unwrapping
- Column extraction and rearrangement
- Join/split operations
- And more...

## Installation

```bash
pip install textura
```

Or from source:

```bash
git clone https://github.com/brucestudios/textura.git
cd textura
pip install -e .
```

## Usage

### As a command-line tool

```bash
# Convert text to uppercase
echo "hello world" | textura upper

# Sort lines alphabetically
textura sort < file.txt

# Remove duplicate lines
textura dedup < file.txt

# Convert to title case
textura title < file.txt

# Extract first column (tab-separated)
textura column -t -c 1 < data.tsv

# Wrap text to 80 columns
textura wrap -w 80 < file.txt
```

### As a Python library

```python
from textura import transform

text = "hello world"
result = transform.upper(text)
print(result)  # HELLO WORLD
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/brucestudios/textura.git
cd textura

# Create a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -e ".[dev]"
```

### Running tests

```bash
pytest
```

### Code style

We use [Ruff](https://docs.astral.sh/ruff/) for linting and formatting.

```bash
ruff check .
ruff format .
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -am 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgements

- Inspired by various Unix text processing utilities (cut, sort, uniq, tr, etc.)