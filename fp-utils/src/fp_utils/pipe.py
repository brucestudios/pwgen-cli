"""Pipe utilities."""

from typing import Callable, TypeVar

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')


def pipe(*funcs: Callable) -> Callable:
    """
    Pipe functions from left to right.
    
    Args:
        *funcs: Functions to pipe
        
    Returns:
        A new function that applies the piped functions in order
        
    Example:
        >>> def add_one(x): return x + 1
        >>> def multiply_by_two(x): return x * 2
        >>> operation = pipe(add_one, multiply_by_two)
        >>> operation(3)  # Returns 8
    """
    if not funcs:
        raise ValueError("At least one function must be provided")
    
    def piped(*args, **kwargs):
        result = funcs[0](*args, **kwargs)
        for func in funcs[1:]:
            result = func(result)
        return result
    
    return piped