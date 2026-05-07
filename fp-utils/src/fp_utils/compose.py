"""Function composition utilities."""

from typing import Callable, TypeVar

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')


def compose(*funcs: Callable) -> Callable:
    """
    Compose functions from right to left.
    
    Args:
        *funcs: Functions to compose
        
    Returns:
        A new function that applies the composed functions
        
    Example:
        >>> def add_one(x): return x + 1
        >>> def multiply_by_two(x): return x * 2
        >>> operation = compose(multiply_by_two, add_one)
        >>> operation(3)  # Returns 8
    """
    if not funcs:
        raise ValueError("At least one function must be provided")
    
    def composed(*args, **kwargs):
        result = funcs[-1](*args, **kwargs)
        for func in reversed(funcs[:-1]):
            result = func(result)
        return result
    
    return composed