# pwdgen

A simple, secure password generator written in Python.

## Features

- Generate strong random passwords
- Customizable length
- Option to include/exclude uppercase, lowercase, digits, and symbols
- Cryptographically secure using `secrets` module
- Command-line interface

## Installation

No installation required. Just download the `password_generator.py` file and run it with Python 3.

## Usage

```bash
python3 password_generator.py [options]
```

### Options

- `-l, --length LENGTH`   Length of the password (default: 16)
- `--no-upper`            Exclude uppercase letters
- `--no-lower`            Exclude lowercase letters
- `--no-digits`           Exclude digits
- `--no-symbols`          Exclude symbols

### Examples

Generate a 16-character password (default):
```bash
python3 password_generator.py
```

Generate a 20-character password without symbols:
```bash
python3 password_generator.py -l 20 --no-symbols
```

Generate a 12-character password with only letters and digits:
```bash
python3 password_generator.py -l 12 --no-symbols
```

## Security

This password generator uses the `secrets` module, which is designed for cryptographic security. The random numbers generated are suitable for managing data such as passwords, account authentication, and related secrets.

## License

MIT License

Copyright (c) 2026 brucestudios

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.