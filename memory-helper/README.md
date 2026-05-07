# Memory Helper

A simple CLI tool to manage OpenClaw memory files.

## Features

- List daily memory files and `MEMORY.md`
- Search within memory files
- Add a new daily memory file with a template
- View a specific memory file

## Installation

1. Ensure you have Python 3.6+ installed.
2. Clone this repository.
3. (Optional) Add the script to your PATH for easy access.

## Usage

Run the script with no arguments to see the help:

```bash
python memory_helper.py --help
```

### Commands

- `list`: List all memory files.
- `search <term>`: Search for a term in memory files.
- `add`: Create a new daily memory file for today.
- `view <file>`: View a specific memory file (e.g., `2026-05-05.md` or `MEMORY.md`).

## Example

```bash
# List all memory files
python memory_helper.py list

# Search for the term "todo" in all memory files
python memory_helper.py search todo

# Create a new daily memory file for today
python memory_helper.py add

# View the memory file for yesterday (adjust the date as needed)
python memory_helper.py view 2026-05-04.md
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.