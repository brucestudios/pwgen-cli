# URL Checker CLI

A simple command-line tool to check the status of one or more URLs. It reports HTTP status code, response time, and SSL certificate validity (for HTTPS).

## Features

- Check single or multiple URLs
- Shows HTTP status code
- Measures response time
- Validates SSL certificates for HTTPS URLs
- Retry mechanism for failed requests
- Verbose mode for detailed output
- Cross-platform (works on Linux, macOS, Windows)

## Installation

### From PyPI (Recommended)

```bash
pip install url-checker-cli
```

### From Source

1. Clone the repository:
```bash
git clone https://github.com/brucestudios/url-checker.git
cd url-checker
```

2. Install in development mode:
```bash
pip install -e .
```

## Usage

```bash
# Check a single URL
url-checker https://example.com

# Check multiple URLs
url-checker https://example.com https://google.com https://invalid-site.xyz

# With custom timeout
url-checker https://example.com --timeout 5

# Verbose output
url-checker https://example.com -v
```

## Output Format

```
✅ https://example.com - Status: 200 | Response Time: 0.45s | SSL: Valid
⚠️  https://httpstat.us/500 - Status: 500 | Response Time: 0.32s | SSL: Valid
❌ https://invalid-site.xyz - Error: HTTPSConnectionPool(host='invalid-site.xyz', port=443): Max retries exceeded with url: / (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x...>: Failed to resolve 'invalid-site.xyz' (Name or service not known)"))
```

## Development

### Running Tests

```bash
python -m pytest tests/
```

### Building the Package

```bash
python -m build
```

### Publishing to PyPI

```bash
twine upload dist/*
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request