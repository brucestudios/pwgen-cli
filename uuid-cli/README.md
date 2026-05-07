# UUID CLI

A simple command-line tool to generate UUIDs (version 4).

## Features

- Generate a single UUID
- Generate multiple UUIDs
- Option to output without hyphens
- Option to output in uppercase

## Installation

You can install via pip:

```bash
pip install uuid-cli
```

Or clone the repository and run the script directly.

## Usage

```bash
# Generate a single UUID
uuid

# Generate 5 UUIDs
uuid -n 5

# Generate UUIDs without hyphens
uuid --no-hyphens

# Generate UUIDs in uppercase
uuid --uppercase
```

## Options

- `-n, --count <number>`: Number of UUIDs to generate (default: 1)
- `--no-hyphens`: Output UUIDs without hyphens
- `--uppercase`: Output UUIDs in uppercase letters

## Examples

```bash
$ uuid
a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8

$ uuid -n 3
a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8
b2c3d4e5-f6g7-8901-h2i3-j4k5l6m7n8o9
c3d4e5f6-g7h8-9012-i3j4-k5l6m7n8o9p0

$ uuid --no-hyphens --uppercase
A1B2C3D4E5F67890G1H2I3J4K5L6M7N8
```

## License

MIT License

Copyright (c) 2026 Bruce Studios

Permission is hereby granted, free of charge, to any person obtaining a copy...