# OpenClaw Weather CLI

A simple command-line interface to get weather information using [wttr.in](https://wttr.in).

## Features

- Get current weather for any location
- Support for metric and USCS units
- Colorful output (can be disabled)
- Simple and lightweight

## Installation

```bash
npm install -g openclaw-weather-cli
```

## Usage

```bash
weather
weather -l "New York"
weather -l "London" -u m
weather -l "auto" --no-formatting
```

## Options

- `-l, --location <location>`: Location to get weather for (city name, zip code, etc.). Default: `auto` (detects location via IP)
- `-u, --units [units]`: Units for temperature: `m` (metric), `u` (USCS), or empty for default
- `-F, --no-formatting`: Disable color/formatting output

## Example

```bash
$ weather -l "Paris" -u m
```

## License

MIT