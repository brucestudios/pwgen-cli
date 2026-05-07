# Markdown TODO App

A simple command-line TODO manager that stores tasks in a Markdown file.

## Features

- Add, list, complete, and remove TODO items
- Stores data in human-readable Markdown format
- Cross-platform (works on Windows, macOS, Linux)
- Zero dependencies (uses only Python standard library)

## Installation

```bash
pip install markdown-todo-app
```

Or clone and install locally:

```bash
git clone https://github.com/brucestudios/markdown-todo-app.git
cd markdown-todo-app
pip install -e .
```

## Usage

Initialize a TODO file (creates `TODO.md` if not exists):

```bash
mdtodo init
```

Add a new task:

```bash
mdtodo add "Buy groceries"
```

List all tasks:

```bash
mdtodo list
```

Mark task as complete:

```bash
mdtodo complete 1
```

Remove a task:

```bash
mdtodo remove 1
```

## Development

To run tests:

```bash
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
