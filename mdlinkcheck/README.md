# mdlinkcheck

A simple command-line tool to check for broken links in Markdown files.

## Features

- Checks HTTP(S) links for availability (HEAD request)
- Validates local file links exist
- Ignores anchor links and mailto: links
- Configurable timeout and user-agent
- Exit code indicates success/failure for CI integration

## Installation

```bash
pip install mdlinkcheck
```

## Usage

```bash
mdlinkcheck path/to/file.md
mdlinkcheck path/to/dir/  # recursively checks all .md files
```

## Options

- `--timeout SECONDS`: HTTP request timeout (default: 10)
- `--user-agent STRING`: Custom User-Agent header
- `--ignore-LOCAL`: Skip local file checks
- `--ignore-REMOTE`: Skip HTTP(S) checks
- `-v, --verbose`: Verbose output

## Example

```bash
$ mdlinkcheck README.md
Checking README.md...
✓ All links are valid.
```

## Development

### Setup

```bash
git clone https://github.com/brucestudios/mdlinkcheck.git
cd mdlinkcheck
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Linting

```bash
ruff check .
```

## License

MIT
