import sys
import requests
import argparse

def get_weather(location=""):
    """
    Fetch weather from wttr.in for the given location.
    If location is empty, it uses the IP-based location.
    """
    # wttr.in format: http://wttr.in/<location>?format=3
    # We use format=3 to get a one-line output: "+Weather report: location\n+Condition: temp\n..."
    # But we can also use format=2 for just the weather and temperature.
    # Let's use format=2: "%l:+%c+%t" (location: condition+temp)
    url = f"http://wttr.in/{location}?format=2" if location else "http://wttr.in?format=2"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        return f"Error fetching weather: {e}"

def main():
    parser = argparse.ArgumentParser(description="Get current weather for a location.")
    parser.add_argument("location", nargs="?", help="Location (city, etc.) to get weather for. If omitted, uses IP-based location.")
    args = parser.parse_args()
    
    weather = get_weather(args.location or "")
    print(weather)

if __name__ == "__main__":
    main()