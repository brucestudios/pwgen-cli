"""mdlinkcheck - A tool to check links in Markdown files."""

from .checker import check_links
from .cli import main

__version__ = "0.1.0"
__author__ = "Bruce Fang"
__email__ = "henshao.fang@outlook.com"

__all__ = ["check_links", "main", "__version__"]