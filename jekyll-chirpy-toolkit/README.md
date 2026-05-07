# Jekyll Chirpy Toolkit

A collection of utility scripts and helpers for Jekyll sites using the [Chirpy theme](https://github.com/cotes2020/jekyll-theme-chirpy).

## Features

- **New Post Generator**: Quickly create a new post with proper front matter.
- **Link Checker**: Validate internal and external links in your generated site.
- **SEO Helper**: Generate sitemap and check SEO metadata.
- **Deployment Helper**: Scripts to simplify deployment to GitHub Pages.

## Prerequisites

- [Jekyll](https://jekyllrb.com/) installed
- [Bundler](https://bundler.io/) (for managing Ruby gems)
- [htmlproofer](https://github.com/jekyll/htmlproofer) (for link checking)

## Installation

Clone this repository and add the scripts to your Jekyll project's `tools/` or `scripts/` directory.

```bash
git clone https://github.com/brucestudios/jekyll-chirpy-toolkit.git
cp -r jekyll-chirpy-toolkit/scripts /path/to/your/jekyll/site/
```

## Usage

### New Post

Run the new post script from your Jekyll site root:

```bash
./scripts/new-post.sh "My Post Title"
```

This will create a new file in `_posts/` with the current date and a slugified filename.

### Link Check

After building your site (`jekyll build`), run:

```bash
./scripts/check-links.sh ./_site
```

This will check for broken links and report any issues.

## Customization

Edit the scripts to match your site's configuration (e.g., URL, date format).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Chirpy Theme](https://github.com/cotes2020/jekyll-theme-chirpy) for the fantastic theme.
- All contributors to Jekyll and related tools.
