# Jekyll Chirpy Utils

A collection of utility scripts to help with Jekyll Chirpy theme sites.

## Scripts

### `scripts/new-post.sh`
Interactive script to create a new post in the Jekyll Chirpy theme.

Usage:
```bash
./scripts/new-post.sh
```
The script will prompt for:
- Post title
- Date (optional, defaults to today)
- Categories (comma-separated, optional)
- Tags (comma-separated, optional)
- Whether the post is a draft (optional)

It will create a new markdown file in `_posts` with the appropriate front matter.

### `scripts/link-checker.sh`
Checks for broken links in the generated Jekyll site using [htmlproofer](https://github.com/gjtorikian/htmlproofer).

Usage:
```bash
./scripts/link-checker.sh
```
Note: This script assumes you have built the site (i.e., `_site` directory exists) or it will build it first.
It requires `htmlproofer` to be installed (via RubyGems: `gem install htmlproofer`).

### `scripts/sitemap-gen.sh`
Helper script to generate or verify the sitemap for your Jekyll Chirpy site.

The Jekyll Chirpy theme already includes a sitemap generator, but this script can be used to:
- Build the site (if not already built)
- Check that the sitemap.xml file exists in the `_site` directory
- Optionally, validate the sitemap (if you have a validation tool)

Usage:
```bash
./scripts/sitemap-gen.sh
```

## Prerequisites

- [Jekyll](https://jekyllrb.com/) installed (via Bundler recommended)
- For link checking: [htmlproofer](https://github.com/gjtorikian/htmlproofer) installed

## Installation

Clone this repository and place the scripts in your Jekyll Chirpy site's root directory, or add the `scripts` directory to your PATH.

## Contributing

Feel free to submit issues or pull requests to improve these utilities.

## License

MIT
