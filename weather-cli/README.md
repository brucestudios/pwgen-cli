# Weather CLI

A simple command-line tool to get current weather for any location using wttr.in.

## Features

- Get current weather for a city or location
- Supports IP-based auto-detection (if no argument given)
- Lightweight and fast
- No API key required

## Installation

```bash
pip install weather-cli
```

## Usage

```bash
# Get weather for current location (based on IP)
weather

# Get weather for a specific city
weather London
weather "New York"
weather Tokyo,JP
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/brucestudios/weather-cli.git
cd weather-cli

# Install in development mode
pip install -e .
```

### Running Tests

```bash
pytest
```

## License

MIT License - see [LICENSE](LICENSE) file for details.
