import argparse
import requests
import sys

def get_weather(latitude, longitude):
    """Fetch weather data from Open-Meteo API."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": "true",
        "timezone": "auto"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Get current weather for a location.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--city", type=str, help="City name (uses Open-Meteo geocoding API)")
    group.add_argument("--lat", type=float, help="Latitude")
    parser.add_argument("--lon", type=float, help="Longitude (required if --lat is provided)")

    args = parser.parse_args()

    if args.lat is not None and args.lon is None:
        parser.error("--lon is required when --lat is provided")
    if args.lon is not None and args.lat is None:
        parser.error("--lat is required when --lon is provided")

    if args.city:
        # Use Open-Meteo geocoding API to get latitude and longitude from city name
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        geo_params = {
            "name": args.city,
            "count": 1,
            "language": "en",
            "format": "json"
        }
        try:
            geo_response = requests.get(geo_url, params=geo_params)
            geo_response.raise_for_status()
            geo_data = geo_response.json()
            if not geo_data["results"]:
                print(f"City '{args.city}' not found.", file=sys.stderr)
                sys.exit(1)
            latitude = geo_data["results"][0]["latitude"]
            longitude = geo_data["results"][0]["longitude"]
            location_name = geo_data["results"][0]["name"]
        except requests.RequestException as e:
            print(f"Error geocoding city: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        latitude = args.lat
        longitude = args.lon
        location_name = f"latitude {latitude}, longitude {longitude}"

    weather_data = get_weather(latitude, longitude)
    current = weather_data.get("current_weather")
    if not current:
        print("No current weather data available.", file=sys.stderr)
        sys.exit(1)

    temperature = current.get("temperature")
    windspeed = current.get("windspeed")
    weathercode = current.get("weathercode")
    time = current.get("time")

    # Simple weather code mapping (from Open-Meteo documentation)
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        56: "Light freezing drizzle",
        57: "Dense freezing drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        66: "Light freezing rain",
        67: "Heavy freezing rain",
        71: "Slight snow fall",
        73: "Moderate snow fall",
        75: "Heavy snow fall",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail"
    }
    weather_description = weather_codes.get(weathercode, f"Unknown code {weathercode}")

    print(f"Current weather in {location_name}:")
    print(f"  Temperature: {temperature}°C")
    print(f"  Weather: {weather_description}")
    print(f"  Wind Speed: {windspeed} km/h")
    print(f"  Time: {time}")

if __name__ == "__main__":
    main()