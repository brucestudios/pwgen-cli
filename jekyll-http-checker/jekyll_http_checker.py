#!/usr/bin/env python3
"""
jekyll-http-checker: A script to check for broken HTTP links in Jekyll-generated HTML sites.

Usage:
    python jekyll_http_checker.py <path_to_jekyll_site> [--external]

Options:
    <path_to_jekyll_site>  Path to the built Jekyll site (typically _site directory)
    --external             Also check external links (requires internet and may be slow)

The script will parse all HTML files in the given directory and check:
    - Internal links (starting with '/' or without a scheme) for existence as files.
    - External links (http:// or https://) for HTTP 200 status (if --external is provided).

Exit codes:
    0: All links are OK
    1: Broken links found
    2: Error in usage or file not found
"""

import sys
import os
import re
from urllib.parse import urljoin, urlparse
import argparse
from pathlib import Path

try:
    import requests
except ImportError:
    print("Error: The 'requests' library is required for external link checking.")
    print("Install it with: pip install requests")
    sys.exit(2)

def find_html_files(directory):
    """Yield all HTML files in the given directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.html'):
                yield os.path.join(root, file)

def extract_links_from_html(file_path):
    """Extract all links (href and src) from an HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Fallback to latin-1 if utf-8 fails
        with open(file_path, 'r', encoding='latin-1') as f:
            content = f.read()
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
        return []

    # Regex to find href and src attributes
    # This is a simple regex and may not catch all edge cases but works for typical Jekyll sites.
    pattern = re.compile(r'''(?:href|src)\s*=\s*["']([^"']*)["']''', re.IGNORECASE)
    return pattern.findall(content)

def normalize_link(link, base_url=None):
    """Normalize a link, resolving relative URLs if base_url is provided."""
    if not link:
        return None
    # Skip empty anchors, javascript:, mailto:, etc.
    if link.startswith('#') or link.startswith('javascript:') or link.startswith('mailto:'):
        return None
    if base_url:
        return urljoin(base_url, link)
    return link

def is_external_link(link):
    """Check if the link is an external URL (has a scheme and netloc)."""
    try:
        parsed = urlparse(link)
        return bool(parsed.scheme) and bool(parsed.netloc)
    except Exception:
        return False

def check_internal_link(link, site_root):
    """Check if an internal link exists as a file in the site root."""
    # Remove query and fragment
    link = link.split('?')[0].split('#')[0]
    if not link:
        return True  # empty link is ignored

    # If the link is absolute (starting with /), treat it as relative to site root
    if link.startswith('/'):
        link = link[1:]
    # If the link doesn't start with a scheme, treat as relative to the site root
    if not (link.startswith('http://') or link.startswith('https://')):
        # Construct the file path
        file_path = os.path.join(site_root, link)
        # If it's a directory, look for index.html
        if os.path.isdir(file_path):
            file_path = os.path.join(file_path, 'index.html')
        return os.path.isfile(file_path)
    # If it has a scheme, we treat it as external (will be checked separately if --external)
    return None  # Indicates external

def check_external_link(link):
    """Check an external link by making an HTTP HEAD request."""
    try:
        # Use HEAD to save bandwidth, fallback to GET if HEAD not allowed
        response = requests.head(link, allow_redirects=True, timeout=10)
        if response.status_code >= 400:
            response = requests.get(link, allow_redirects=True, timeout=10)
        return response.status_code < 400
    except requests.exceptions.RequestException:
        return False

def main():
    parser = argparse.ArgumentParser(description='Check for broken HTTP links in Jekyll-generated HTML sites.')
    parser.add_argument('site_path', help='Path to the built Jekyll site (e.g., _site directory)')
    parser.add_argument('--external', action='store_true', help='Also check external links')
    args = parser.parse_args()

    site_path = os.path.abspath(args.site_path)
    if not os.path.isdir(site_path):
        print(f"Error: Site path '{site_path}' does not exist or is not a directory.")
        sys.exit(2)

    broken_links = []
    total_links = 0
    checked_external = 0

    for html_file in find_html_files(site_path):
        links = extract_links_from_html(html_file)
        for link in links:
            total_links += 1
            normalized = normalize_link(link)
            if not normalized:
                continue

            if is_external_link(normalized):
                if args.external:
                    checked_external += 1
                    if not check_external_link(normalized):
                        broken_links.append((html_file, normalized, 'external'))
                # If not checking external, skip
                continue

            # Internal link
            result = check_internal_link(normalized, site_path)
            if result is False:
                broken_links.append((html_file, normalized, 'internal'))
            # If result is None, it's an external link that we didn't check (because --external not set)
            # We treat it as OK for now.

    # Report
    if broken_links:
        print(f"Found {len(broken_links)} broken link(s):")
        for file, link, typ in broken_links:
            print(f"  {file}: {link} [{typ}]")
        print(f"\nTotal links checked: {total_links}")
        if args.external:
            print(f"External links checked: {checked_external}")
        sys.exit(1)
    else:
        print(f"All {total_links} links are OK.")
        if args.external:
            print(f"External links checked: {checked_external}")
        sys.exit(0)

if __name__ == '__main__':
    main()