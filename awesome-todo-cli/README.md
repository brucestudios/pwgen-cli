# Awesome Todo CLI

A beautiful, feature-rich command-line todo list application written in Python.

![Demo](demo.gif)

## Features

- ✨ Beautiful colored output with emojis
- 📝 Add, list, complete, and delete todos
- 🏷️ Categorize todos with tags
- 📅 Due dates and reminders
- 🔄 Priority levels (low, medium, high)
- 💾 Persistent storage (JSON-based)
- 🔍 Search and filter todos
- 📊 Statistics and progress tracking
- ⚙️ Configurable settings
- 🌈 Multiple themes (light/dark)
- 🔒 Data encryption option

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/awesome-todo-cli.git
cd awesome-todo-cli

# Install dependencies
pip install -r requirements.txt

# Or install via pip (after publishing to PyPI)
pip install awesome-todo-cli
```

## Usage

```bash
# Initialize your todo list
todo init

# Add a new todo
todo add "Learn Python" --priority high --tags learning,python --due "2026-05-15"

# List all todos
todo list

# List only high priority todos
todo list --priority high

# Complete a todo
todo complete 1

# Delete a todo
todo remove 1

# Search todos
todo search "python"

# Show statistics
todo stats

# Configure settings
todo config --theme dark
```

## Commands

```
init                    Initialize a new todo list
add                     Add a new todo
list                    List todos
complete                Mark todo as complete
remove                  Delete a todo
search                  Search todos
stats                   Show statistics
config                  Configure settings
backup                  Backup todo data
restore                 Restore from backup
```

## Configuration

Run `todo config` to adjust settings:
- Theme (light/dark)
- Default priority
- Auto-backup interval
- Notification preferences
- Data encryption

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Running Tests

```bash
# Run unit tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=todo

# Lint code
flake8 todo/

# Format code
black todo/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by various todo applications
- Built with Python's excellent ecosystem
- Thanks to all contributors!

---

Made with ❤️ by [Your Name](https://github.com/yourusername)