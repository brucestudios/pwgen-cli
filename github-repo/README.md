# Jekyll Link Checker

A Python tool to validate internal and external links in Jekyll sites. This crawler checks all links in your Jekyll site for validity, reporting broken links, redirects, and other issues.

## Features

- ✅ Checks both internal and external links
- ✅ Supports HTML `<a>` tags, Markdown links, and plain URLs
- ✅ Concurrent link checking for fast performance
- ✅ Detailed reporting with file locations and status codes
- ✅ Configurable timeout and base URL for relative link resolution
- ✅ Ignores common non-HTTP links (mailto:, tel:, javascript:, anchors)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python -m jekyll_link_checker.main /path/to/your/jekyll/site [--base-url https://example.com] [--timeout 30]
```

### Arguments

- `site_dir`: Path to your Jekyll site directory (required)
- `--base-url`: Base URL of your site (used to resolve relative links)
- `--timeout`: Request timeout in seconds (default: 30)
- `--verbose`: Enable verbose logging

## Example

```bash
python -m jekyll_link_checker.main ./my-jekyll-site --base-url https://myblog.com
```

## Output

The tool generates a detailed report showing:
- Total files checked
- Total links checked
- Valid links count
- Redirected links count (with details)
- Broken links count (with file locations and status codes)

## Exit Codes

- `0`: No broken links found
- `1`: Broken links detected
- `2`: Error occurred (invalid directory, etc.)

## Requirements

- Python 3.7+
- aiohttp
- aiofiles

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

Built with ❤️ for the Jekyll community.