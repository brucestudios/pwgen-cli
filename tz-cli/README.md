# Timezone Converter CLI

A simple command-line tool to convert times between different timezones.

## Installation

You can run the script directly with Python 3.9+ (no external dependencies besides the standard library and `tzdata`).

```bash
git clone https://github.com/brucestudios/tz-converter-cli.git
cd tz-converter-cli
chmod +x tz_converter.py
```

## Usage

```bash
./tz_converter.py --to "America/New_York"
```

This will convert the current UTC time to New York time.

You can also specify a time and source timezone:

```bash
./tz_converter.py --time "2026-05-06T17:30:00" --from "UTC" --to "Asia/Shanghai"
```

## Requirements

- Python 3.9+ (for `zoneinfo` module)
- The `tzdata` package is installed automatically with Python 3.9+ on most platforms, but if you encounter issues, you can install it via `pip install tzdata`.

## License

MIT