# passgen

A secure password generator written in Python.

## Features

- Generate strong, random passwords
- Customizable length and character sets
- Option to exclude ambiguous characters (il1Lo0O)
- Cryptographically secure using `secrets` module
- Command-line interface with helpful defaults

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/passgen.git
cd passgen

# Make the script executable (optional)
chmod +x passgen.py
```

## Usage

```bash
# Generate a 16-character password with all character types
./passgen.py

# Generate a 20-character password
./passgen.py -l 20

# Generate a password without symbols
./passgen.py --no-symbols

# Exclude ambiguous characters (il1Lo0O)
./passgen.py --exclude-ambiguous

# Generate a 10-character password with only uppercase and digits
./passgen.py -l 10 --no-lower --no-symbols
```

## Options

- `-l, --length LENGTH`: Length of the password (default: 16)
- `--no-upper`: Exclude uppercase letters
- `--no-lower`: Exclude lowercase letters
- `--no-digits`: Exclude digits
- `--no-symbols`: Exclude symbols
- `--exclude-ambiguous`: Exclude ambiguous characters (il1Lo0O)

## Examples

```bash
$ ./passgen.py
v9*Fp2#kLm@Qw$Rs

$ ./passgen.py -l 20
Jk8#mN2$pQw*Rs!vEaZ%

$ ./passgen.py --exclude-ambiguous
G7$hK9&pLm@Qw*RsE

$ ./passgen.py -l 10 --no-lower --no-symbols
T7F2R8K1P0
```

## Security

This password generator uses Python's `secrets` module, which is designed for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

## License

MIT