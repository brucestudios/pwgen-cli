# OpenClaw Todo CLI

A simple command-line todo list manager written in Python.

## Features

- Add tasks with descriptions
- List all tasks (showing completion status)
- Mark tasks as complete
- Delete tasks
- Persistent storage using a JSON file

## Installation

```bash
pip install openclaw-todo-cli
```

Or install from source:

```bash
git clone https://github.com/brucestudios/openclaw-todo-cli.git
cd openclaw-todo-cli
pip install -e .
```

## Usage

```bash
# Add a new task
otodo add "Buy groceries"

# List all tasks
otodo list

# Mark task as complete (by ID)
otodo complete 1

# Delete a task (by ID)
otodo delete 1

# Show help
otodo --help
```

## Development

To contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## License

MIT License - see the [LICENSE](LICENSE) file for details.