# PassGen Pro

A modern, flexible password generator CLI written in Python.

## Features

- Generate strong, random passwords
- Customizable length and character sets
- Exclude ambiguous characters (optional)
- Generate multiple passwords at once
- Copy to clipboard (optional)
- Simple and intuitive interface

## Installation

```bash
pip install passgen-pro
```

## Usage

Generate a single password of default length (16):

```bash
passgen
```

Specify length:

```bash
passgen -l 32
```

Include/exclude character sets:

```bash
passgen -l 20 --no-digits --no-symbols
```

Exclude ambiguous characters (like `0`, `O`, `l`, `1`):

```bash
passgen -l 24 --exclude-ambiguous
```

Generate multiple passwords:

```bash
passgen -l 16 -n 5
```

Copy to clipboard (requires `pyperclip`):

```bash
passgen -l 16 --copy
```

## Character Sets

By default, PassGen Pro uses:
- Lowercase letters: `abcdefghijklmnopqrstuvwxyz`
- Uppercase letters: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
- Digits: `0123456789`
- Symbols: `!@#$%^&*()_+-=[]{}|;:,.<>?`

## Development

To install in development mode:

```bash
git clone https://github.com/brucestudios/passgen-pro.git
cd passgen-pro
pip install -e .
```

## License

MIT License - see the [LICENSE](LICENSE) file for details.
