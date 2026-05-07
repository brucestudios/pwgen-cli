# Jekyll Link Checker

A Node.js utility to check for broken links in Jekyll sites. This tool scans your built Jekyll site (_site directory by default) and verifies that all internal and external links are working correctly.

## Features

- ✅ Checks internal links (relative paths, root-relative paths)
- ✅ Checks external links (HTTP/HTTPS URLs)
- ✅ Validates images, scripts, stylesheets, and anchor links
- ✅ Skips anchor links (`#section`) and JavaScript links (`javascript:...`)
- ✅ Configurable timeout and external link skipping
- ✅ Verbose and quiet modes
- ✅ Detailed reporting with file locations and link types
- ✅ Proper exit codes (0 for success, 1 for broken links)

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/jekyll-link-checker.git
cd jekyll-link-checker

# Install dependencies
npm install
```

## Usage

### Basic Usage

```bash
# Check links in your Jekyll site (assumes _site directory)
npx jekyll-link-checker

# Specify custom source and destination directories
npx jekyll-link-checker --source ./my-jekyll-site --destination ./my-jekyll-site/_site
```

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `-s, --source <path>` | Path to Jekyll source directory | `./` |
| `-d, --destination <path>` | Path to Jekyll build directory | `_site` |
| `-t, --timeout <ms>` | Request timeout in milliseconds | `5000` |
| `--skip-external` | Skip checking external links | `false` |
| `--verbose` | Verbose output showing each link check | `false` |

### Examples

```bash
# Check with 10 second timeout
npx jekyll-link-checker --timeout 10000

# Skip external links (faster, only checks internal)
npx jekyll-link-checker --skip-external

# Verbose mode to see each link being checked
npx jekyll-link-checker --verbose

# Custom directories
npx jekyll-link-checker -s ./blog -d ./blog/_site
```

## Integration with Jekyll Build Process

Add to your `package.json` scripts:

```json
{
  "scripts": {
    "build": "jekyll build",
    "test:links": "jekyll-link-checker",
    "build_and_test": "npm run build && npm run test:links"
  }
}
```

Then run:
```bash
npm run build_and_test
```

## How It Works

1. **Discovers HTML files** in your Jekyll destination directory (_site by default)
2. **Extracts links** from anchor tags (`<a href>`), images (`<img src>`), scripts (`<script src>`), and link tags (`<link href>`)
3. **Resolves URLs** relative to the file's location or site root
4. **Checks each link** using HTTP HEAD requests
5. **Reports results** with detailed breakdown of working vs broken links

## Link Types Checked

- **Anchor links** (`<a href="...">`) - Navigation links
- **Image links** (`<img src="...">`) - Images, logos, etc.
- **Script links** (`<script src="...">`) - JavaScript files
- **Stylesheet links** (`<link rel="stylesheet" href="...">`) - CSS files
- **Other link tags** (`<link href="...">`) - Favicons, etc.

## Error Handling

- **Timeouts**: Links that don't respond within the timeout period are marked as broken
- **HTTP Errors**: Any HTTP status code >= 400 is considered broken
- **Network Errors**: DNS failures, connection refused, etc. are marked as broken
- **File System Links**: Local file:// links are checked for actual file existence

## License

MIT © OpenClaw Assistant

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request