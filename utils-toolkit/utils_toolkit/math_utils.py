"""
Mathematical utility functions.
"""

from typing import List, Union
from math import gcd as math_gcd


def factorial(n: int) -> int:
    """Calculate factorial of n (n!)."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (0-indexed: fib(0)=0, fib(1)=1)."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def is_prime(n: int) -> bool:
    """Check if integer n is a prime number."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(n ** 0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """Calculate greatest common divisor of a and b."""
    return math_gcd(a, b)


def lcm(a: int, b: int) -> int:
    """Calculate least common multiple of a and b."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def average(numbers: List[Union[int, float]]) -> float:
    """Calculate arithmetic mean of numbers."""
    if not numbers:
        raise ValueError("Cannot compute average of empty list")
    return sum(numbers) / len(numbers)


def median(numbers: List[Union[int, float]]) -> float:
    """Calculate median of numbers."""
    if not numbers:
        raise ValueError("Cannot compute median of empty list")
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]


def mode(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """Calculate mode(s) of numbers. Returns list of most frequent value(s)."""
    if not numbers:
        raise ValueError("Cannot compute mode of empty list")
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    return modes