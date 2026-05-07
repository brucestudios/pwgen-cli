# weather-cli

A simple command-line tool to get the current weather for a location using [wttr.in](https://wttr.in).

## Installation

You can run the script directly from the source:

```bash
python3 weather.py [location]
```

Or make it executable and place it in your PATH:

```bash
chmod +x weather.py
sudo mv weather.py /usr/local/bin/weather
```

Then use it as:

```bash
weather [location]
```

## Usage

```bash
weather [location]
```

If `location` is omitted, the script will use your IP address to determine your location.

## Examples

```bash
# Get weather for New York
weather New York

# Get weather for London
weather London

# Get weather based on your IP (current location)
weather
```

## Requirements

- Python 3.x
- Internet access (to fetch data from wttr.in)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.