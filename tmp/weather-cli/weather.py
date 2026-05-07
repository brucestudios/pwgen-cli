#!/usr/bin/env python3
"""
weather-cli: A simple command-line tool to get current weather for a location.
Uses wttr.in as the backend.
"""

import sys
import argparse
import urllib.request
import urllib.error

def fetch_weather(location: str) -> str:
    """Fetch weather for given location from wttr.in."""
    # Format: wttr.in/<location>?format=3 gives a compact one-line output.
    url = f"http://wttr.in/{location}?format=3"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return response.read().decode('utf-8').strip()
    except urllib.error.URLError as e:
        return f"Error fetching weather: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"

def main():
    parser = argparse.ArgumentParser(
        description="Get current weather for a location using wttr.in."
    )
    parser.add_argument(
        "location",
        nargs="?",
        default="",
        help="Location (city, region, etc.). If omitted, uses IP-based location."
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version="weather-cli 1.0.0"
    )
    args = parser.parse_args()

    # If location is empty string, wttr.in will use IP detection.
    location = args.location if args.location else ""
    print(fetch_weather(location))

if __name__ == "__main__":
    main()