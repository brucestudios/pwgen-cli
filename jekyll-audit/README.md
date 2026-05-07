# Jekyll Audit Tool

A simple CLI tool to audit Jekyll sites for common issues.

## Features

- Checks for valid YAML front matter in Markdown posts
- Validates the `_config.yml` file
- Easy to use command-line interface

## Installation

You can install the tool via pip:

```bash
pip install jekyll-audit
```

Or clone the repository and install locally:

```bash
git clone https://github.com/brucestudios/jekyll-audit.git
cd jekyll-audit
pip install -e .
```

## Usage

Run the audit on your Jekyll site:

```bash
jekyll-audit /path/to/your/site
```

If you are already in the site directory, you can simply run:

```bash
jekyll-audit
```

## Options

- `--posts DIRECTORY`: Specify the posts directory (default: `_posts`)
- `--config FILE`: Specify the configuration file (default: `_config.yml`)

## Example

```bash
$ jekyll-audit .
Auditing Jekyll site at: /path/to/site
==================================================
Configuration: OK

Posts: OK
==================================================
No issues found!
```

## License

MIT