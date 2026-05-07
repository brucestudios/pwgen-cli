from typing import List, T, Callable, Any, Dict

def flatten(list_of_lists: List[List[T]]) -> List[T]:
    """Flatten a list of lists into a single list."""
    return [item for sublist in list_of_lists for item in sublist]

def unique(items: List[T]) -> List[T]:
    """Return a list of unique items preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def chunk(items: List[T], size: int) -> List[List[T]]:
    """Split a list into chunks of given size."""
    if size <= 0:
        raise ValueError("Size must be positive")
    return [items[i:i+size] for i in range(0, len(items), size)]

def group_by(items: List[T], key_func: Callable[[T], Any]) -> Dict[Any, List[T]]:
    """Group items by the result of key_func."""
    groups = {}
    for item in items:
        key = key_func(item)
        groups.setdefault(key, []).append(item)
    return groups