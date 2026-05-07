#!/usr/bin/env bash
# check-links.sh - Check for broken links in Jekyll site using htmlproofer

# Exit on any error
set -e

# Default directory is _site if not provided
SITE_DIR="${1:-_site}"

# Check if directory exists
if [ ! -d "$SITE_DIR" ]; then
  echo "Error: Directory '$SITE_DIR' not found."
  echo "Please build your Jekyll site first with 'jekyll build' or provide the correct directory."
  exit 1
fi

# Check if htmlproofer is available
if ! command -v htmlproofer &> /dev/null; then
  echo "Error: htmlproofer not found."
  echo "Please install it with: gem install htmlproofer"
  exit 1
fi

# Run htmlproofer with recommended options for Jekyll sites
echo "Checking links in '$SITE_DIR'..."
htmlproofer "$SITE_DIR" \
  --disable-external \
  --allow-hash-href \
  --url-ignore "/#",/^mailto:/ \
  --file-ignore "/node_modules/,/vendor/,/assets/js/,/assets/css/"

echo "Link check completed."