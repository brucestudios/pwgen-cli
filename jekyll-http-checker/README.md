# Jekyll HTTP Link Checker

A Python script to check for broken HTTP links in Jekyll-generated HTML sites.

## Features

- Checks internal links for existence as files in the Jekyll site
- Optionally checks external links for HTTP 200 status
- Handles both `href` and `src` attributes
- Ignores empty anchors, javascript:, and mailto: links
- Provides clear reporting of broken links with file locations

## Installation

1. Ensure you have Python 3.6+ installed
2. Install the required `requests` library for external link checking:

```bash
pip install requests
```

3. Copy `jekyll_http_checker.py` to your Jekyll project or install it globally

## Usage

### Basic Usage

Check only internal links (links within your Jekyll site):

```bash
python jekyll_http_checker.py _site
```

### With External Link Checking

Also check external HTTP/HTTPS links (requires internet connection):

```bash
python jekyll_http_checker.py _site --external
```

## How It Works

The script:

1. Walks through all HTML files in the specified directory (typically `_site`)
2. Extracts all `href` and `src` attributes from each file
3. For each link:
   - **Internal links**: Checks if the corresponding file exists in the site directory
   - **External links**: Makes an HTTP HEAD request to verify the link returns a 2xx status (if `--external` is provided)
4. Reports any broken links found

## Exit Codes

- `0`: All links are OK
- `1`: Broken links found
- `2`: Error in usage or file not found

## Examples

### Internal Links Only

```bash
$ python jekyll_http_checker.py _site
All 42 links are OK.
```

### With External Links

```bash
$ python jekyll_http_checker.py _site --external
Found 2 broken link(s):
  _site/blog/post1.html: https://example.com/broken [external]
  _site/about.html: /missing-page.html [internal]

Total links checked: 58
External links checked: 15
```

## Requirements

- Python 3.6+
- `requests` library (only for external link checking)

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Created for Bruce's Jekyll site maintenance.