# Jekyll Toolbox

A collection of useful scripts for maintaining Jekyll sites.

## Features

- **Link Checker**: Verify internal and external links in your generated Jekyll site.
- **Sitemap Generator**: Create a sitemap.xml file for your Jekyll site.
- **More to come**...

## Installation

Clone this repository and make the scripts executable:

```bash
git clone https://github.com/brucestudios/jekyll-toolbox.git
cd jekyll-toolbox
chmod +x jekyll-toolbox.sh
```

## Usage

Run the main script with a command:

```bash
./jekyll-toolbox.sh <command> [options]
```

### Available Commands

- `check-links`: Check for broken links in the generated site.
- `generate-sitemap`: Generate a sitemap for the site.

### Examples

Check links in the default `_site` directory:

```bash
./jekyll-toolbox.sh check-links
```

Check links in a custom directory:

```bash
./jekyll-toolbox.sh check-links --dir ./my-site/_site
```

Generate a sitemap:

```bash
./jekyll-toolbox.sh generate-sitemap --url https://example.com --dir ./_site
```

## Script Details

### jekyll-toolbox.sh

The main entry point for the toolbox. It delegates to subcommands.

#### check-links

Scans HTML files in the Jekyll site output (default: `_site`) for:
- Internal links (relative paths) that point to non-existent files.
- External links (http/https) that return non-200 status codes (optional, requires curl).

#### generate-sitemap

Generates a sitemap.xml file from HTML files in the site directory, using the last modification time of each file.

## Contributing

Feel free to submit issues and pull requests!

## License

MIT © 2026 Bruce Fang