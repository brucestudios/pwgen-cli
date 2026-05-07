# Changelog Generator

A Python tool to generate changelogs from git commits.

## Installation

```bash
pip install changelog-generator
```

## Usage

### As a command-line tool

```bash
changelog
```

### As a library

```python
from changelog_generator.core import generate_changelog

changelog = generate_changelog(since="2026-01-01", until="2026-05-01")
print(changelog)
```

## Features

- Generates changelogs from git commit history.
- Supports conventional commit types (feat, fix, docs, etc.).
- Allows filtering by date and commit subject pattern.
- Outputs in Markdown format with links to commits.

## License

MIT