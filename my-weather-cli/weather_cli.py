#!/usr/bin/env python3
"""
weather-cli: A simple command-line tool to get weather information using wttr.in.

Usage:
    weather-cli [location]

If location is omitted, uses the user's IP-based location.
"""

import sys
import argparse
import requests
from textwrap import dedent

def get_weather(location: str = '') -> str:
    """Fetch weather from wttr.in for the given location."""
    base_url = "https://wttr.in"
    params = {
        'format': 3,  # Compact one-line output
    }
    if location:
        params['q'] = location  # Not actually used; we append to path
        # wttr.in uses path: /location
        url = f"{base_url}/{location}"
    else:
        url = base_url
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        return resp.text.strip()
    except requests.RequestException as e:
        return f"Error fetching weather: {e}"

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Get current weather from wttr.in",
        usage="weather-cli [location]"
    )
    parser.add_argument(
        'location',
        nargs='?',
        default='',
        help='Location (city, address, etc.). If omitted, uses IP-based location.'
    )
    args = parser.parse_args()

    output = get_weather(args.location)
    print(output)

if __name__ == '__main__':
    main()