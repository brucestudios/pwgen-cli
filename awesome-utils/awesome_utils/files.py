"""
File and directory utility functions.
"""

import os
import shutil
from pathlib import Path
from typing import List, Optional, Union

def ensure_dir(path: Union[str, Path]) -> None:
    """Create directory if it doesn't exist.
    
    Args:
        path: The directory path to create.
    """
    Path(path).mkdir(parents=True, exist_ok=True)

def copy_file(src: Union[str, Path], dst: Union[str, Path]) -> None:
    """Copy file from source to destination.
    
    Args:
        src: Source file path.
        dst: Destination file path.
    """
    shutil.copy2(src, dst)

def move_file(src: Union[str, Path], dst: Union[str, Path]) -> None:
    """Move file from source to destination.
    
    Args:
        src: Source file path.
        dst: Destination file path.
    """
    shutil.move(src, dst)

def get_file_size(path: Union[str, Path]) -> int:
    """Get file size in bytes.
    
    Args:
        path: The file path.
        
    Returns:
        File size in bytes.
    """
    return Path(path).stat().st_size

def list_files(directory: Union[str, Path], extension: Optional[str] = None) -> List[Path]:
    """List files in directory.
    
    Args:
        directory: The directory to search.
        extension: File extension to filter by (e.g., '.txt'). If None, list all files.
        
    Returns:
        List of file paths.
    """
    path = Path(directory)
    if extension:
        return list(path.glob(f'*{extension}'))
    return [f for f in path.iterdir() if f.is_file()]