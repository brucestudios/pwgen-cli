"""File operation utilities."""

import shutil
import os
from typing import Union


def copy_file(src: Union[str, os.PathLike], dst: Union[str, os.PathLike]) -> None:
    """Copy a file from src to dst.

    Args:
        src: Source file path.
        dst: Destination file path.
    """
    shutil.copy2(src, dst)


def move_file(src: Union[str, os.PathLike], dst: Union[str, os.PathLike]) -> None:
    """Move a file from src to dst.

    Args:
        src: Source file path.
        dst: Destination file path.
    """
    shutil.move(src, dst)


def delete_file(path: Union[str, os.PathLike]) -> None:
    """Delete a file at the given path.

    Args:
        path: Path to the file to delete.
    """
    os.remove(path)