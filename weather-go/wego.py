#!/usr/bin/env python3
"""
wego - Weather Go: a simple CLI to fetch weather from wttr.in
"""
import sys
import argparse
import requests

def get_weather(location: str = ""):
    """Fetch weather for location from wttr.in."""
    base_url = "https://wttr.in"
    params = {
        "format": "%l:+%C+%t+%w+%h+%p\n",  # Location: Condition +temp +wind +humidity +precipitation
    }
    if location:
        url = f"{base_url}/{location}"
    else:
        url = base_url
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        return resp.text.strip()
    except requests.RequestException as e:
        return f"Error fetching weather: {e}"

def main():
    parser = argparse.ArgumentParser(
        description="Fetch current weather from wttr.in",
        epilog="Example: wego London"
    )
    parser.add_argument(
        "location",
        nargs="?",
        help="Location (city, region, etc.) - if omitted, uses IP-based location"
    )
    args = parser.parse_args()
    weather = get_weather(args.location or "")
    print(weather)

if __name__ == "__main__":
    main()