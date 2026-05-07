# pwdstrength

A simple command-line tool to check the strength of a password.

## Features

- Checks password length, character variety, and common patterns.
- Provides a score and feedback on how to improve.
- Easy to use from the terminal.

## Installation

```bash
pip install pwdstrength
```

## Usage

```bash
pwdstrength check "myPassword123"
```

Or without arguments to prompt for a password:

```bash
pwdstrength check
```

## Example

```bash
$ pwdstrength check "weak"
❌ Weak password (score: 20/100)
Feedback:
- Too short (minimum 8 characters)
- Add more character variety (uppercase, lowercase, numbers, symbols)
```

## License

MIT