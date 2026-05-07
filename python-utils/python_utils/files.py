import os
import json
import csv
from typing import List, Dict, Any

def ensure_dir(filepath: str) -> None:
    """Ensure the directory for the given filepath exists."""
    directory = os.path.dirname(filepath)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

def read_json(filepath: str) -> Any:
    """Read and parse a JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(data: Any, filepath: str) -> None:
    """Write data as JSON to a file."""
    ensure_dir(filepath)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def read_csv(filepath: str) -> List[Dict[str, str]]:
    """Read a CSV file and return a list of dictionaries."""
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

def write_csv(data: List[Dict[str, str]], filepath: str) -> None:
    """Write a list of dictionaries to a CSV file."""
    ensure_dir(filepath)
    if not data:
        return
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def list_files(directory: str, extension: str = None) -> List[str]:
    """List files in a directory, optionally filtered by extension."""
    if not os.path.isdir(directory):
        return []
    files = []
    for f in os.listdir(directory):
        if extension is None or f.endswith(extension):
            files.append(os.path.join(directory, f))
    return files