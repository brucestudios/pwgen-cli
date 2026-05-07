"""Core functionality for the Markdown TODO app."""

import os
from typing import List, Tuple

TODO_FILE = "TODO.md"


class TodoManager:
    """Manage TODO items in a Markdown file."""

    def __init__(self, todo_file: str = TODO_FILE):
        self.todo_file = todo_file

    def _read_lines(self) -> List[str]:
        """Read all lines from the TODO file."""
        if not os.path.exists(self.todo_file):
            return []
        with open(self.todo_file, "r", encoding="utf-8") as f:
            return f.readlines()

    def _write_lines(self, lines: List[str]) -> None:
        """Write lines to the TODO file."""
        with open(self.todo_file, "w", encoding="utf-8") as f:
            f.writelines(lines)

    def init(self) -> None:
        """Initialize a new TODO file with a header if it doesn't exist."""
        if not os.path.exists(self.todo_file):
            self._write_lines(["# TODO List\n\n"])
        else:
            # Ensure the file starts with a header
            lines = self._read_lines()
            if not lines or not lines[0].startswith("#"):
                lines.insert(0, "# TODO List\n\n")
                self._write_lines(lines)

    def _parse_items(self, lines: List[str]) -> List[Tuple[bool, str, int]]:
        """Parse lines into a list of (completed, text, line_index) for checkbox items."""
        items = []
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith("- [ ]") or stripped.startswith("- [x]"):
                completed = stripped.startswith("- [x]")
                # Extract the text after the checkbox
                text = stripped[5:].strip()  # Remove "- [ ]" or "- [x]"
                items.append((completed, text, i))
        return items

    def add(self, task: str) -> None:
        """Add a new task to the TODO list."""
        self.init()  # Ensure the file exists and has a header
        lines = self._read_lines()
        # Find the end of the header (first empty line after the header) or just append after the header?
        # We'll insert after the header and any existing items, but for simplicity, we'll append at the end.
        # However, we want to keep the header at the top and then the list.
        # Let's find the line after the header (if the header is exactly one line) or after the header block.
        # We'll just append two newlines and then the item if the file doesn't end with a newline.
        # But a better approach: we want to keep the header and then the list of items.
        # We'll insert the new item before any trailing empty lines at the end of the file.
        # However, for simplicity, we'll just append to the end and then later we can format.

        # We'll add a blank line before the item if the file doesn't already end with a blank line.
        if lines and not lines[-1].endswith("\n"):
            lines.append("\n")
        if lines and lines[-1].strip() != "":
            lines.append("\n")
        lines.append(f"- [ ] {task}\n")
        self._write_lines(lines)

    def list(self) -> List[Tuple[bool, str]]:
        """List all TODO items."""
        self.init()
        lines = self._read_lines()
        items = self._parse_items(lines)
        return [(completed, text) for completed, text, _ in items]

    def complete(self, index: int) -> bool:
        """Mark a task as complete by its 1-based index in the list of tasks."""
        lines = self._read_lines()
        items = self._parse_items(lines)
        if index < 1 or index > len(items):
            return False
        # We need to replace the line at the item's line index
        _, _, line_idx = items[index - 1]
        # Replace the line with a completed checkbox
        # We want to keep the same indentation and just change the box.
        line = lines[line_idx]
        if line.strip().startswith("- [ ]"):
            lines[line_idx] = line.replace("- [ ]", "- [x]", 1)
        else:
            # Already completed? Then do nothing but return True?
            # We'll just return True as it's already completed.
            pass
        self._write_lines(lines)
        return True

    def remove(self, index: int) -> bool:
        """Remove a task by its 1-based index in the list of tasks."""
        lines = self._read_lines()
        items = self._parse_items(lines)
        if index < 1 or index > len(items):
            return False
        _, _, line_idx = items[index - 1]
        # Remove the line
        del lines[line_idx]
        self._write_lines(lines)
        return True