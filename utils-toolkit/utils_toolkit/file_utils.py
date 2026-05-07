"""
File utility functions.
"""

import os
import shutil
from typing import List, Optional


def read_file_safely(filepath: str) -> Optional[str]:
    """Read file content with error handling.
    
    Returns None if file cannot be read.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except (FileNotFoundError, PermissionError, IOError):
        return None


def write_file_safely(filepath: str, content: str) -> bool:
    """Write content to file with error handling.
    
    Returns True if successful, False otherwise.
    """
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except (PermissionError, IOError, OSError):
        return False


def file_exists(filepath: str) -> bool:
    """Check if file exists."""
    return os.path.isfile(filepath)


def get_file_size(filepath: str) -> Optional[int]:
    """Get file size in bytes.
    
    Returns None if file does not exist or error occurs.
    """
    try:
        return os.path.getsize(filepath)
    except (FileNotFoundError, PermissionError, OSError):
        return None


def list_files(directory: str, extension: Optional[str] = None) -> List[str]:
    """List files in directory, optionally filtered by extension.
    
    Args:
        directory: Path to directory
        extension: File extension to filter by (e.g., '.txt'), None for all files
        
    Returns:
        List of filenames (not full paths)
    """
    try:
        files = []
        for f in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, f)):
                if extension is None or f.endswith(extension):
                    files.append(f)
        return files
    except (FileNotFoundError, PermissionError, OSError):
        return []


def copy_file(source: str, destination: str) -> bool:
    """Copy file from source to destination.
    
    Returns True if successful, False otherwise.
    """
    try:
        shutil.copy2(source, destination)
        return True
    except (FileNotFoundError, PermissionError, IOError, OSError):
        return False