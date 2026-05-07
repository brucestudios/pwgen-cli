# Weather CLI

A simple command-line tool to get current weather information using the Open-Meteo API.

## Features

- Get current weather for your location (based on IP address)
- Support for metric and imperial units
- Simple and easy to use
- No API key required (uses Open-Meteo's free tier)

## Installation

You can install the package via pip:

```bash
pip install weather-cli
```

Or install directly from the source:

```bash
git clone https://github.com/yourusername/weather-cli.git
cd weather-cli
pip install .
```

## Usage

```bash
weather-cli [--location LOCATION] [--units {metric,imperial}]
```

### Examples

```bash
# Get weather for your current location (based on IP)
weather-cli

# Specify units (imperial for Fahrenheit, mph, etc.)
weather-cli --units imperial
```

Note: The `--location` argument is currently ignored in this version. The tool uses your IP address to determine your location.

## Output Example

```
Weather for Current location:
  Condition: Partly cloudy
  Temperature: 22.5°C
  Wind Speed: 15.0 km/h
  Wind Direction: 180°
  Precipitation: 0.0 mm
  Time: 2026-05-02T10:30:00
```

## Requirements

- Python 3.6 or higher
- internet connection (to fetch weather data)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Weather data provided by [Open-Meteo](https://open-meteo.com/)
- Location detection via [ipapi.co](https://ipapi.co/)