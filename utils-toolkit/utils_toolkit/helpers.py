"""Helper functions for the Utils Toolkit."""

import re
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Union


def slugify(text: str, separator: str = "-") -> str:
    """Convert a string to a URL-friendly slug.

    Args:
        text: The string to slugify.
        separator: The separator to use between words (default: '-').

    Returns:
        A URL-friendly slug.
    """
    # Convert to lowercase and strip leading/trailing whitespace
    text = text.lower().strip()
    # Replace non-alphanumeric characters (except spaces) with the separator
    text = re.sub(r"[^a-z0-9\s]", separator, text)
    # Replace whitespace (including multiple spaces) with the separator
    text = re.sub(r"\s+", separator, text)
    # Remove leading/trailing separators
    text = text.strip(separator)
    return text


def ensure_dir(path: Union[str, Path]) -> Path:
    """Ensure a directory exists, creating it if necessary.

    Args:
        path: The directory path to ensure.

    Returns:
        A Path object pointing to the directory.
    """
    path_obj = Path(path)
    path_obj.mkdir(parents=True, exist_ok=True)
    return path_obj


def format_timestamp(fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Return the current timestamp formatted according to `fmt`.

    Args:
        fmt: The format string for the timestamp (default: "%Y-%m-%d %H:%M:%S").

    Returns:
        The formatted timestamp string.
    """
    return datetime.now().strftime(fmt)


def read_file_lines(path: Union[str, Path]) -> List[str]:
    """Read all lines from a file, stripping newline characters.

    Args:
        path: The path to the file to read.

    Returns:
        A list of lines from the file, with newline characters stripped.
    """
    path_obj = Path(path)
    with path_obj.open("r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]
    return lines


def write_file_lines(path: Union[str, Path], lines: Iterable[str]) -> None:
    """Write lines to a file, each followed by a newline.

    Args:
        path: The path to the file to write.
        lines: An iterable of strings to write to the file.
    """
    path_obj = Path(path)
    with path_obj.open("w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")