"""
Date and time utility functions.
"""

from datetime import datetime, date, timedelta
from typing import Union


def format_date(dt: Union[datetime, date], format_str: str) -> str:
    """Format date/datetime object according to format string."""
    return dt.strftime(format_str)


def parse_date(date_str: str, format_str: str) -> datetime:
    """Parse date string according to format string."""
    return datetime.strptime(date_str, format_str)


def add_days(dt: Union[datetime, date], days: int) -> Union[datetime, date]:
    """Add days to date/datetime object."""
    return dt + timedelta(days=days)


def days_between(date1: Union[datetime, date], date2: Union[datetime, date]) -> int:
    """Calculate number of days between two dates (absolute value)."""
    if isinstance(date1, datetime):
        date1 = date1.date()
    if isinstance(date2, datetime):
        date2 = date2.date()
    return abs((date2 - date1).days)


def is_weekend(dt: Union[datetime, date]) -> bool:
    """Check if date is weekend (Saturday or Sunday)."""
    if isinstance(dt, datetime):
        dt = dt.date()
    return dt.weekday() >= 5  # 5=Saturday, 6=Sunday


def get_weekday_name(dt: Union[datetime, date]) -> str:
    """Get weekday name (e.g., Monday, Tuesday)."""
    if isinstance(dt, datetime):
        dt = dt.date()
    return dt.strftime("%A")