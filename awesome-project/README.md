# Temperature Converter

A simple command-line utility to convert temperatures between Celsius and Fahrenheit.

## Features

- Convert Celsius to Fahrenheit
- Convert Fahrenheit to Celsius
- Interactive mode
- Batch conversion from file
- Comprehensive test suite
- MIT Licensed

## Installation

Clone the repository and ensure you have Python 3.8+ installed.

```bash
git clone https://github.com/<your-username>/temperature-converter.git
cd temperature-converter
```

## Usage

### Command Line

```bash
python -m src.tempconv convert 25 CtoF
```

```
25°C = 77.0°F
```

```bash
python -m src.tempconv convert 77 FtoC
```

```
77°F = 25.0°C
```

### Interactive Mode

```bash
python -m src.tempconv interactive
```

Follow the prompts.

### Batch Conversion

Create a text file with lines like `25 C` or `77 F` (value and unit), then run:

```bash
python -m src.tempconv batch temperatures.txt
```

Output will be printed to stdout.

## Running Tests

```bash
python -m pytest tests/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
