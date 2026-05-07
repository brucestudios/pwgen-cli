# Weather CLI

A simple command-line tool to get the current weather for a given location or auto-detect your location.

## Features

- Get weather by city name
- Auto-detect location based on IP
- Displays temperature in both Celsius and Fahrenheit
- Shows weather condition, feels like temperature, humidity, and wind

## Usage

```bash
# Auto-detect location
python3 main.py

# Specify a city
python3 main.py "New York"
python3 main.py "London"
```

## Requirements

- Python 3.6+
- Internet connection (to fetch weather data)

## How it Works

The script uses the [wttr.in](https://wttr.in/) service to fetch weather data in JSON format.
For auto-detection, it uses [ipinfo.io](https://ipinfo.io/) to get the city based on your IP address.

## License

MIT