#!/usr/bin/env python3
"""
Jekyll Post Helper - A simple script to generate new Jekyll post files.

Usage:
    python jekyll_post_helper.py "My Post Title"
"""

import sys
import os
import re
from datetime import datetime

def slugify(text):
    """Convert text to a URL-friendly slug."""
    # Convert to lowercase
    text = text.lower()
    # Replace non-alphanumeric characters (except spaces) with hyphens
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    # Replace spaces and multiple hyphens with a single hyphen
    text = re.sub(r'[\s-]+', '-', text)
    # Remove leading/trailing hyphens
    return text.strip('-')

def main():
    if len(sys.argv) < 2:
        print("Error: Please provide a post title.")
        print("Usage: python jekyll_post_helper.py \"Your Post Title\"")
        sys.exit(1)

    title = sys.argv[1]
    date = datetime.now()
    date_str = date.strftime('%Y-%m-%d')
    datetime_str = date.strftime('%Y-%m-%d %H:%M:%S')
    slug = slugify(title)
    filename = f"{date_str}-{slug}.md"

    # Front matter for Jekyll post
    front_matter = f"""---
layout: post
title:  "{title}"
date:   {datetime_str}
categories: jekyll update
---

"""

    # Create _posts directory if it doesn't exist
    posts_dir = "_posts"
    if not os.path.exists(posts_dir):
        os.makedirs(posts_dir)

    filepath = os.path.join(posts_dir, filename)

    # Write the file
    with open(filepath, 'w') as f:
        f.write(front_matter)

    print(f"Created new Jekyll post: {filepath}")

if __name__ == "__main__":
    main()
