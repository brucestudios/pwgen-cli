# Ultra Secure Password Generator

A simple, secure password generator written in Python that uses cryptographically strong random number generation (`secrets` module) to create passwords.

## Features

- Generate passwords of specified length
- Customizable character sets (letters, digits, punctuation)
- Option to exclude ambiguous characters (like `0`, `O`, `l`, `1`)
- Command-line interface for easy use
- No dependencies beyond Python standard library

## Usage

```bash
python main.py [options]
```

### Options

- `-l, --length LENGTH`: Length of the password (default: 16)
- `-d, --digits`: Include digits (0-9)
- `-p, --punctuation`: Include punctuation characters
- `-a, --letters`: Include letters (both uppercase and lowercase, default)
- `-e, --exclude-ambiguous`: Exclude ambiguous characters (0, O, l, 1)
- `-h, --help`: Show help message

### Examples

Generate a 16-character password with letters, digits, and punctuation:

```bash
python main.py -l 16 -d -p
```

Generate a 20-character password excluding ambiguous characters:

```bash
python main.py -l 20 -e
```

## Why Secure?

This generator uses the `secrets` module, which is designed for cryptographic purposes. It provides access to the most secure source of randomness available on your operating system.

Unlike pseudo-random number generators used in `random` module, `secrets` is suitable for generating passwords, account authentication, security tokens, and related secrets.

## Installation

No installation required. Just ensure you have Python 3.6+ installed.

```bash
git clone https://github.com/your-username/ultra-secure-password-gen.git
cd ultra-secure-password-gen
python main.py --help
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
