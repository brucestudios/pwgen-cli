"""Currying utilities."""

from typing import Callable, TypeVar, Any, Union

T = TypeVar('T')
R = TypeVar('R')


def curry(func: Callable[..., R]) -> Callable:
    """
    Curry a function to allow partial application.
    
    Args:
        func: The function to curry
        
    Returns:
        A curried version of the function
        
    Example:
        >>> @curry
        ... def add(x, y):
        ...     return x + y
        >>> add_five = add(5)
        >>> add_five(3)  # Returns 8
    """
    def curried(*args, **kwargs):
        # If we have all arguments needed, call the function
        try:
            return func(*args, **kwargs)
        except TypeError as e:
            # If we're missing arguments, return a new curried function
            if "missing" in str(e):
                return lambda *more_args, **more_kwargs: curried(
                    *args, *more_args, **{**kwargs, **more_kwargs}
                )
            else:
                raise
    
    return curried