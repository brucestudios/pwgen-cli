# wego - Weather Go

A simple command-line tool to fetch the current weather from [wttr.in](https://wttr.in).

## Features

- Minimal and fast
- Uses IP-based location by default
- Accepts a location argument (city, region, etc.)
- Clear, concise output

## Installation

### From Source

```bash
git clone https://github.com/<your-username>/weather-go.git
cd weather-go
chmod +x wego.py
# Optional: move wego.py to a directory in your PATH, e.g., /usr/local/bin
sudo mv wego.py /usr/local/bin/wego
```

### Requirements

- Python 3.x
- requests library (install with `pip install requests`)

## Usage

```bash
wego [location]
```

Examples:

```bash
wego          # Weather for your current location (based on IP)
wego London   # Weather for London
wego "New York"  # Weather for New York
```

## Output Format

The output is a single line with:

`<location>: <condition> <temperature> <wind> <humidity> <precipitation>`

Example:

`London: +Cloudy 15°C ↓15 km/h 80% 0.0 mm`

## License

MIT

## Acknowledgments

- [wttr.in](https://wttr.in) for the excellent weather service.