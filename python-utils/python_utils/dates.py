from datetime import datetime, timedelta
import re

def _parse_date(date_str: str) -> datetime:
    """Parse a date string in YYYY-MM-DD format."""
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
        raise ValueError("Date must be in YYYY-MM-DD format")
    return datetime.strptime(date_str, '%Y-%m-%d')

def add_days(date_str: str, days: int) -> str:
    """Add days to a date and return the new date in YYYY-MM-DD format."""
    dt = _parse_date(date_str)
    new_dt = dt + timedelta(days=days)
    return new_dt.strftime('%Y-%m-%d')

def subtract_days(date_str: str, days: int) -> str:
    """Subtract days from a date and return the new date in YYYY-MM-DD format."""
    dt = _parse_date(date_str)
    new_dt = dt - timedelta(days=days)
    return new_dt.strftime('%Y-%m-%d')

def days_between(date1: str, date2: str) -> int:
    """Return the number of days between two dates (absolute value)."""
    dt1 = _parse_date(date1)
    dt2 = _parse_date(date2)
    delta = dt2 - dt1
    return abs(delta.days)

def is_leap_year(year: int) -> bool:
    """Return True if the year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)