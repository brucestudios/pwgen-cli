# Awesome Weather CLI

A simple command-line tool to get current weather information for any location using the [wttr.in](https://wttr.in) service.

## Features

- Get current weather for any location by name
- Uses your IP address to determine location when no argument is provided
- Displays temperature, conditions, wind, humidity, and daily forecast
- Simple and fast - no API keys required
- Works on any system with Python 3

## Installation

### Option 1: Download the script directly

```bash
curl -O https://raw.githubusercontent.com/yourusername/awesome-weather-cli/main/weather.py
chmod +x weather.py
./weather.py "New York"
```

### Option 2: Clone the repository

```bash
git clone https://github.com/yourusername/awesome-weather-cli.git
cd awesome-weather-cli
chmod +x weather.py
./weather.py "London"
```

## Usage

```bash
# Get weather for your current location (based on IP)
./weather.py

# Get weather for a specific city
./weather.py "San Francisco"

# Get weather for a location with state/country
./weather.py "Paris, France"

# Get weather using coordinates
./weather.py "35.6895,139.6917"  # Tokyo coordinates
```

## Output Example

```
Weather for: San Francisco, CA, USA
Condition: Partly cloudy
Temperature: 18°C (feels like 18°C)
Wind: 11 km/h from WSW
Humidity: 72%

Today's Forecast:
  High: 20°C
  Low: 14°C
  Average: 17°C
  Sunrise: 06:12 AM
  Sunset: 07:45 PM
```

## How It Works

This tool uses the excellent [wttr.in](https://wttr.in) service, which provides weather information in various formats. The script requests the JSON format (`?format=j1`) and parses it to display a clean, readable output.

## Requirements

- Python 3.x
- Internet connection (to access wttr.in)

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request