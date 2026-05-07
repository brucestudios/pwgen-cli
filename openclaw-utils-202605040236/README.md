# OpenClaw Utils

A collection of lightweight command-line utilities for OpenClaw and daily tasks.

## Features

- **PassGen**: Generate secure passwords with customizable options
- **Todo**: Simple command-line todo list manager
- **Weather**: Quick weather lookup for any location

## Installation

```bash
pip install openclaw-utils
```

Or install from source:

```bash
git clone https://github.com/brucestudios/openclaw-utils-202605040236.git
cd openclaw-utils-202605040236
pip install -e .
```

## Usage

### PassGen

Generate a secure password:

```bash
ocw-passgen              # 16-character password with all character sets
ocw-passgen -l 20       # 20-character password
ocw-passgen -n          # Exclude special characters
ocw-passgen -d          # Exclude digits
ocw-passgen -l 10 -c    # 10-character lowercase only
```

### Todo

Manage your todo list:

```bash
ocw-todo add "Buy groceries"
ocw-todo list
ocw-todo done 1
ocw-todo rm 2
```

### Weather

Get current weather:

```bash
ocw-weather "Shanghai"
ocw-weather "New York" --metric
```

## Development

### Requirements

- Python 3.8+

### Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -e .[dev]
```

### Running Tests

```bash
pytest
```

### Building

```bash
python -m build
```

## License

MIT License - see the [LICENSE](LICENSE) file for details.