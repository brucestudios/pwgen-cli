# weather-cli

A simple command-line tool to get current weather information using [wttr.in](https://wttr.in).

## Features

- Get weather for any location by name, address, or IP-based location.
- Lightweight and fast, using the compact output format of wttr.in.
- No API key required.

## Installation

You can install the package via pip:

```bash
pip install weather-cli
```

Or clone the repository and install locally:

```bash
git clone https://github.com/yourusername/weather-cli.git
cd weather-cli
pip install .
```

## Usage

```bash
weather-cli [location]
```

If `location` is omitted, the tool uses your IP-based location.

### Examples

Get weather for your current location (based on IP):

```bash
weather-cli
```

Get weather for New York City:

```bash
weather-cli New York
```

Get weather for London, UK:

```bash
weather-cli London
```

## How It Works

The tool wraps the [wttr.in](https://wttr.in) service, which provides weather data in various formats. We use the compact format (option `format=3`) to get a one-line summary.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

- brucestudios

## Acknowledgments

- [wttr.in](https://wttr.in) for the wonderful weather service.