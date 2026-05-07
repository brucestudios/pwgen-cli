import pytest
from utils_toolkit.helpers import slugify, ensure_dir, format_timestamp, read_file_lines, write_file_lines
import tempfile
import os


def test_slugify():
    assert slugify("Hello World!") == "hello-world"
    assert slugify("  Leading and trailing spaces  ") == "leading-and-trailing-spaces"
    assert slugify("Multiple---separators") == "multiple-separators"
    assert slugify("Special_chars: @#$%^&*()") == "special-chars-----"


def test_ensure_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        new_dir = os.path.join(tmpdir, "new", "nested")
        result = ensure_dir(new_dir)
        assert os.path.isdir(new_dir)
        assert str(result) == new_dir


def test_format_timestamp():
    # Just check that it returns a string in the expected format
    ts = format_timestamp("%Y-%m-%d")
    assert len(ts) == 10  # YYYY-MM-DD
    assert ts[4] == '-' and ts[7] == '-'


def test_read_write_file_lines():
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "test.txt")
        lines_to_write = ["line one", "line two", "line three"]
        write_file_lines(filepath, lines_to_write)
        lines_read = read_file_lines(filepath)
        assert lines_read == lines_to_write