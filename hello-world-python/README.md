# Hello World Python CLI

A simple command-line interface that prints a friendly greeting.

## Features

- Print a customizable greeting
- Support for multiple languages (English, Spanish, French)
- Easy to install via pip
- Well-tested with pytest
- Continuous Integration with GitHub Actions

## Installation

```bash
pip install hello-world-cli
```

## Usage

```bash
hello-world
# Output: Hello, World!

hello-world --name Alice
# Output: Hello, Alice!

hello-world --lang es
# Output: ¡Hola, Mundo!

hello-world --name Bob --lang fr
# Output: Bonjour, Bob !
```

## Development

1. Clone the repository
2. Install development dependencies: `pip install -e .[dev]`
3. Run tests: `pytest`
4. Build package: `python -m build`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.