#!/usr/bin/env python3
"""
File Sorter CLI
Organize files in a directory into subfolders by file type (extension).
"""

import argparse
import os
import shutil
import sys
from pathlib import Path

def get_file_category(filename):
    """Map file extension to a category folder name."""
    ext = Path(filename).suffix.lower()
    if not ext:
        return "no_extension"
    # Remove the dot
    ext = ext[1:]
    # Define categories
    categories = {
        # Images
        "jpg": "Images", "jpeg": "Images", "png": "Images", "gif": "Images",
        "bmp": "Images", "tiff": "Images", "webp": "Images", "svg": "Images",
        # Documents
        "pdf": "Documents", "doc": "Documents", "docx": "Documents",
        "txt": "Documents", "rtf": "Documents", "odt": "Documents",
        "md": "Documents", "markdown": "Documents",
        # Spreadsheets
        "xls": "Spreadsheets", "xlsx": "Spreadsheets", "csv": "Spreadsheets",
        # Presentations
        "ppt": "Presentations", "pptx": "Presentations", "odp": "Presentations",
        # Archives
        "zip": "Archives", "rar": "Archives", "7z": "Archives", "tar": "Archives",
        "gz": "Archives", "bz2": "Archives", "xz": "Archives",
        # Audio
        "mp3": "Audio", "wav": "Audio", "flac": "Audio", "aac": "Audio",
        "ogg": "Audio", "m4a": "Audio",
        # Video
        "mp4": "Video", "mkv": "Video", "avi": "Video", "mov": "Video",
        "wmv": "Video", "flv": "Video", "webm": "Video",
        # Code
        "py": "Code", "js": "Code", "ts": "Code", "html": "Code", "css": "Code",
        "java": "Code", "c": "Code", "cpp": "Code", "h": "Code", "cs": "Code",
        "php": "Code", "rb": "Code", "go": "Code", "rs": "Code", "sh": "Code",
        "json": "Code", "xml": "Code", "yaml": "Code", "yml": "Code",
        # Fonts
        "ttf": "Fonts", "otf": "Fonts", "woff": "Fonts", "woff2": "Fonts",
        # Executables
        "exe": "Executables", "msi": "Executables", "app": "Executables",
    }
    return categories.get(ext, "Other")

def main():
    parser = argparse.ArgumentParser(description="Organize files into folders by type.")
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Directory to sort (default: current directory)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without moving files"
    )
    parser.add_argument(
        "--no-folders",
        action="store_true",
        help="Do not create folders; just report categories"
    )
    args = parser.parse_args()

    target_dir = Path(args.directory).resolve()
    if not target_dir.is_dir():
        print(f"Error: {target_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    moved = 0
    skipped = 0
    for item in target_dir.iterdir():
        if item.is_file():
            category = get_file_category(item.name)
            if args.no_folders:
                print(f"{item.name} -> {category}")
                continue
            dest_dir = target_dir / category
            if not args.dry_run:
                dest_dir.mkdir(exist_ok=True)
            dest = dest_dir / item.name
            if dest.exists():
                # Avoid overwriting: add a counter
                stem = item.stem
                suffix = item.suffix
                counter = 1
                while dest.exists():
                    dest = dest_dir / f"{stem}_{counter}{suffix}"
                    counter += 1
            if args.dry_run:
                print(f"Would move: {item.name} -> {dest}")
            else:
                try:
                    shutil.move(str(item), str(dest))
                    print(f"Moved: {item.name} -> {dest}")
                    moved += 1
                except Exception as e:
                    print(f"Error moving {item.name}: {e}", file=sys.stderr)
                    skipped += 1
        else:
            skipped += 1  # skip directories

    if not args.no_folders:
        if args.dry_run:
            print(f"\nDry run complete. Would move {moved} files.")
        else:
            print(f"\nDone. Moved {moved} files, skipped {skipped} items.")

if __name__ == "__main__":
    main()