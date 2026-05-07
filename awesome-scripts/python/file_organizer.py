#!/usr/bin/env python3
"""
File Organizer Script
Automatically organizes files in a directory by their file extensions.

Usage:
    python file_organizer.py [directory_path]
    
If no directory is provided, organizes the current directory.
"""

import os
import shutil
import sys
from pathlib import Path

def get_file_category(file_extension):
    """Map file extensions to categories."""
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.pages', '.md'],
        'Spreadsheets': ['.xls', '.xlsx', '.csv', '.ods', '.numbers'],
        'Presentations': ['.ppt', '.pptx', '.odp', '.key'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
        'Video': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h', '.cs', '.php', '.rb', '.go', '.rs', '.swift', '.kt', '.ts'],
        'Executables': ['.exe', '.msi', '.deb', '.rpm', '.dmg', '.app'],
    }
    
    for category, extensions in categories.items():
        if file_extension.lower() in extensions:
            return category
    return 'Others'

def organize_directory(directory_path):
    """Organize files in the specified directory."""
    directory = Path(directory_path)
    
    if not directory.exists():
        print(f"Error: Directory '{directory_path}' does not exist.")
        return False
    
    if not directory.is_dir():
        print(f"Error: '{directory_path}' is not a directory.")
        return False
    
    print(f"Organizing files in: {directory.absolute()}")
    
    # Create category directories
    categories = set()
    for item in directory.iterdir():
        if item.is_file():
            file_extension = item.suffix
            category = get_file_category(file_extension)
            categories.add(category)
    
    # Create directories for each category
    for category in categories:
        category_dir = directory / category
        category_dir.mkdir(exist_ok=True)
    
    # Move files to appropriate directories
    moved_count = 0
    for item in directory.iterdir():
        if item.is_file():
            file_extension = item.suffix
            category = get_file_category(file_extension)
            destination = directory / category / item.name
            
            # Handle duplicate filenames
            counter = 1
            original_destination = destination
            while destination.exists():
                stem = item.stem
                suffix = item.suffix
                destination = directory / category / f"{stem}_{counter}{suffix}"
                counter += 1
            
            try:
                shutil.move(str(item), str(destination))
                print(f"Moved: {item.name} -> {category}/")
                moved_count += 1
            except Exception as e:
                print(f"Error moving {item.name}: {e}")
    
    print(f"\nOrganization complete! Moved {moved_count} files.")
    return True

def main():
    """Main function."""
    if len(sys.argv) > 2:
        print("Usage: python file_organizer.py [directory_path]")
        sys.exit(1)
    
    directory_path = sys.argv[1] if len(sys.argv) == 2 else "."
    success = organize_directory(directory_path)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()