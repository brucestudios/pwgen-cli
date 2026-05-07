# UUID Tool

A simple command-line tool to generate UUIDs (version 4) written in Python.

## Features

- Generate one or more UUIDs with a single command.
- Simple and easy to use.
- No dependencies beyond Python's standard library.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/uuid-tool.git
   ```
2. Navigate to the directory:
   ```bash
   cd uuid-tool
   ```
3. Make sure you have Python 3.x installed.

## Usage

Run the script with Python:

```bash
python uuid.py
```

To generate multiple UUIDs, use the `-n` or `--number` option:

```bash
python uuid.py -n 5
```

## Example Output

```bash
$ python uuid.py
f47ac10b-58cc-4372-a567-0e02b2c3d479

$ python uuid.py -n 3
6513d882-7d7c-4d2e-8e3b-8b8b8b8b8b8b
c0ffee12-3456-7890-abcd-ef1234567890
a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.