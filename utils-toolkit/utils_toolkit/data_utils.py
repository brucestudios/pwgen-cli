"""
Data utility functions.
"""

from typing import List, Any, Callable, Dict, Tuple
import itertools


def remove_duplicates(items: List[Any]) -> List[Any]:
    """Remove duplicates from list while preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def flatten_list(nested_list: List[Any]) -> List[Any]:
    """Flatten a nested list."""
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


def chunk_list(items: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split list into chunks of specified size."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


def find_duplicates(items: List[Any]) -> List[Any]:
    """Find duplicate items in list."""
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)


def group_by(items: List[Any], key_func: Callable[[Any], Any]) -> Dict[Any, List[Any]]:
    """Group items by key function."""
    groups = {}
    for item in items:
        key = key_func(item)
        groups.setdefault(key, []).append(item)
    return groups


def sort_by_multiple_keys(items: List[Any], keys: List[Callable[[Any], Any]]) -> List[Any]:
    """Sort items by multiple keys (in order of priority)."""
    # Sort by keys in reverse order (least important first) so that the most important key is last
    for key in reversed(keys):
        items = sorted(items, key=key)
    return items