#!/usr/bin/env python3
"""
cli-weather-tool: A simple command-line tool to get weather information.

Usage:
    weather.py [location]

If no location is provided, the script uses your IP address to determine location.
"""

import sys
import urllib.request
import json

def fetch_weather(location=None):
    """Fetch weather data from wttr.in using the JSON format."""
    if location:
        # URL encode the location to handle spaces and special characters
        import urllib.parse
        location_encoded = urllib.parse.quote(location)
        url = f"http://wttr.in/{location_encoded}?format=j1"
    else:
        url = "http://wttr.in?format=j1"
    
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data
    except urllib.error.URLError as e:
        return {"error": f"Failed to connect to weather service: {e.reason}"}
    except json.JSONDecodeError as e:
        return {"error": f"Failed to parse weather data: {e}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

def format_weather(data):
    """Format the weather data into a human-readable string."""
    if "error" in data:
        return data["error"]
    
    # Extract current condition
    current = data.get('current_condition', [{}])[0]
    weather_desc = current.get('weatherDesc', [{}])[0].get('value', 'N/A')
    temp_c = current.get('temp_C', 'N/A')
    feels_like_c = current.get('FeelsLikeC', 'N/A')
    wind_kmph = current.get('windspeedKmph', 'N/A')
    wind_dir = current.get('winddir16Point', 'N/A')
    humidity = current.get('humidity', 'N/A')
    
    # Extract location info
    area = data.get('request', [{}])[0].get('query', 'Unknown location')
    
    # Build the output
    lines = [
        f"Weather for: {area}",
        f"Condition: {weather_desc}",
        f"Temperature: {temp_c}°C (feels like {feels_like_c}°C)",
        f"Wind: {wind_kmph} km/h from {wind_dir}",
        f"Humidity: {humidity}%",
    ]
    
    # Add today's forecast if available
    weather = data.get('weather', [])
    if weather:
        today = weather[0]
        maxtemp_c = today.get('maxtempC', 'N/A')
        mintemp_c = today.get('mintempC', 'N/A')
        avg_temp = today.get('avgtempC', 'N/A')
        sunrise = today.get('astronomy', [{}])[0].get('sunrise', 'N/A')
        sunset = today.get('astronomy', [{}])[0].get('sunset', 'N/A')
        lines.extend([
            "",
            "Today's Forecast:",
            f"  High: {maxtemp_c}°C",
            f"  Low: {mintemp_c}°C",
            f"  Average: {avg_temp}°C",
            f"  Sunrise: {sunrise}",
            f"  Sunset: {sunset}",
        ])
    
    return "\n".join(lines)

def main():
    """Main entry point."""
    location = None
    if len(sys.argv) > 1:
        location = " ".join(sys.argv[1:])
    
    data = fetch_weather(location)
    print(format_weather(data))

if __name__ == "__main__":
    main()