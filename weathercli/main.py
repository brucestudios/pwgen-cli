#!/usr/bin/env python3
"""
Weather CLI - A simple command line tool to get current weather.
"""

import sys
import json
import urllib.request
import urllib.parse

def get_weather(city="auto"):
    """Fetch weather for a given city or auto-detect location."""
    if city == "auto":
        # Use ipinfo.io to get location
        try:
            with urllib.request.urlopen("https://ipinfo.io/json") as response:
                data = json.load(response)
                city = data.get("city", "")
        except Exception:
            city = ""
    
    if not city:
        # Fallback to a default
        city = "London"
    
    # Use wttr.in API
    url = f"https://wttr.in/{urllib.parse.quote(city)}?format=j1"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
            current = data["current_condition"][0]
            temp_c = current["temp_C"]
            temp_f = current["temp_F"]
            desc = current["weatherDesc"][0]["value"]
            feels_like_c = current["FeelsLikeC"]
            feels_like_f = current["FeelsLikeF"]
            humidity = current["humidity"]
            wind_kph = current["windspeedKmph"]
            wind_dir = current["winddir16Point"]
            
            print(f"Weather in {city}:")
            print(f"  Condition: {desc}")
            print(f"  Temperature: {temp_c}°C / {temp_f}°F")
            print(f"  Feels like: {feels_like_c}°C / {feels_like_f}°F")
            print(f"  Humidity: {humidity}%")
            print(f"  Wind: {wind_kph} km/h {wind_dir}")
    except Exception as e:
        print(f"Error fetching weather: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    if len(sys.argv) > 1:
        city = " ".join(sys.argv[1:])
    else:
        city = "auto"
    get_weather(city)

if __name__ == "__main__":
    main()