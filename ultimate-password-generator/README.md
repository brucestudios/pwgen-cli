# Ultimate Password Generator

A powerful and flexible command-line tool for generating secure, random passwords with various options.

## Features

- Generate passwords of any length
- Include/exclude uppercase, lowercase, numbers, symbols
- Exclude ambiguous characters (like `0`, `O`, `l`, `1`)
- Generate multiple passwords at once
- Option to generate pronounceable passwords
- Copy to clipboard (optional)
- Export to file
- Simple and intuitive interface

## Installation

```bash
pip install ultimate-password-generator
```

Or clone and install locally:

```bash
git clone https://github.com/brucestudios/ultimate-password-generator.git
cd ultimate-password-generator
pip install -e .
```

## Usage

```bash
# Generate a single 16-character password
upg

# Generate a 20-character password with numbers and symbols
upg -l 20 -n -s

# Generate 5 passwords, each 12 characters, excluding ambiguous characters
upg -c 5 -l 12 --no-ambiguous

# Generate a pronounceable password
upg --pronounceable

# Save passwords to a file
upg -c 10 -l 16 -o passwords.txt
```

## Options

```
usage: upg [-h] [-l LENGTH] [-c COUNT] [-u] [-l] [-n] [-s] [--no-ambiguous]
           [--pronounceable] [-o OUTPUT] [--clipboard]

Generate secure passwords.

optional arguments:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        Length of each password (default: 16)
  -c COUNT, --count COUNT
                        Number of passwords to generate (default: 1)
  -u, --uppercase       Include uppercase letters (A-Z)
  -l, --lowercase       Include lowercase letters (a-z)
  -n, --numbers         Include numbers (0-9)
  -s, --symbols         Include symbols (!@#$%^&* etc.)
  --no-ambiguous        Exclude ambiguous characters (0Oql1)
  --pronounceable       Generate pronounceable passwords
  -o OUTPUT, --output OUTPUT
                        Output file to save passwords
  --clipboard           Copy result to clipboard (requires pyperclip)
```

## Character Sets

By default, the generator uses:
- lowercase letters: `abcdefghijkmnpqrstuvwxyz` (if `--no-ambiguous` excludes 'l')
- uppercase letters: `ABCDEFGHJKLMNPQRSTUVWXYZ` (if `--no-ambiguous` excludes 'O', 'I')
- numbers: `23456789` (if `--no-ambiguous` excludes '0', '1')
- symbols: `!@#$%^&*()_+-=[]{}|;:,.<>?`

## Pronounceable Mode

When `--pronounceable` is enabled, passwords are generated using a consonant-vowel pattern, making them easier to remember while still secure.

## Examples

Generate a strong 24-character password with all character types:

```bash
upg -l 24 -u -l -n -s
```

Generate 3 passwords for Wi-Fi networks (no ambiguous characters):

```bash
upg -c 3 -l 16 --no-ambiguous
```

Generate a list of 50 pronounceable passwords for temporary accounts:

```bash
upg -c 50 --pronounceable -l 10
```

## Requirements

- Python 3.7+
- Optional: `pyperclip` for clipboard functionality

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Contact

Bruce Fang - henshao.fang@outlook.com

Project Link: https://github.com/brucestudios/ultimate-password-generator