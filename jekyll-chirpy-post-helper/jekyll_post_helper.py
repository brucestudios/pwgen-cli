#!/usr/bin/env python3
"""
Jekyll Post Helper for Chirpy Theme
A simple script to generate Jekyll posts with proper front matter for the Chirpy theme.
"""

import os
import sys
import argparse
from datetime import datetime
import re

def slugify(text):
    """Convert text to a URL-friendly slug."""
    # Convert to lowercase, replace non-alphanumeric with hyphens, remove leading/trailing hyphens
    slug = re.sub(r'[^\w\s-]', '', text.lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug.strip('-')

def get_post_filename(date, title):
    """Generate the post filename in the format: YYYY-MM-DD-title.md"""
    date_str = date.strftime('%Y-%m-%d')
    slug = slugify(title)
    return f"{date_str}-{slug}.md"

def get_front_matter(date, title, tags, categories):
    """Generate the front matter for the Jekyll post."""
    front_matter = [
        "---",
        f"layout: post",
        f"title:  \"{title}\"",
        f"date:   {date.strftime('%Y-%m-%d %H:%M:%S %z')}",
        f"categories: {categories}",
        f"tags: {tags}",
        "---"
    ]
    return "\n".join(front_matter)

def main():
    parser = argparse.ArgumentParser(description="Generate a Jekyll post for the Chirpy theme.")
    parser.add_argument("--title", help="Post title")
    parser.add_argument("--date", help="Post date (YYYY-MM-DD), defaults to today")
    parser.add_argument("--tags", help="Tags as a comma-separated list, e.g., 'jekyll,theme'")
    parser.add_argument("--categories", help="Categories as a comma-separated list, e.g., 'updates'")
    parser.add_argument("--content", help="Post content (if not provided, will open editor or prompt)")
    parser.add_argument("--site-root", default=".", help="Root directory of the Jekyll site (defaults to current directory)")
    args = parser.parse_args()

    # Determine the post date
    if args.date:
        try:
            post_date = datetime.strptime(args.date, "%Y-%m-%d")
        except ValueError:
            print("Error: Date must be in YYYY-MM-DD format.")
            sys.exit(1)
    else:
        post_date = datetime.now()

    # Get title
    title = args.title
    if not title:
        title = input("Enter post title: ").strip()
        if not title:
            print("Error: Title is required.")
            sys.exit(1)

    # Get tags
    tags = args.tags
    if tags is None:
        tags_input = input("Enter tags (comma-separated, leave empty for none): ").strip()
        tags = tags_input if tags_input else ""
    # Format tags as a YAML list: [tag1, tag2]
    if tags:
        tag_list = [t.strip() for t in tags.split(",") if t.strip()]
        tags_formatted = "[" + ", ".join(tag_list) + "]"
    else:
        tags_formatted = "[]"

    # Get categories
    categories = args.categories
    if categories is None:
        categories_input = input("Enter categories (comma-separated, leave empty for none): ").strip()
        categories = categories_input if categories_input else ""
    # Format categories as a YAML list: [category1, category2]
    if categories:
        cat_list = [c.strip() for c in categories.split(",") if c.strip()]
        categories_formatted = "[" + ", ".join(cat_list) + "]"
    else:
        categories_formatted = "[]"

    # Get content
    content = args.content
    if not content:
        print("\nEnter post content (end with an empty line or Ctrl+D):")
        lines = []
        while True:
            try:
                line = input()
                if line == "" and not lines:  # Allow empty first line? We'll break on two consecutive empties? Let's do: break on empty line after at least one line.
                    if lines:
                        break
                    else:
                        lines.append(line)  # Actually, we want to allow empty first line? Let's just read until EOF or empty line.
                else:
                    lines.append(line)
            except EOFError:
                break
        content = "\n".join(lines)
        # If the user just pressed enter immediately, we might have empty content. That's okay.

    # Generate filename and front matter
    filename = get_post_filename(post_date, title)
    front_matter = get_front_matter(post_date, title, tags_formatted, categories_formatted)

    # Determine the _posts directory
    posts_dir = os.path.join(args.site_root, "_posts")
    if not os.path.isdir(posts_dir):
        print(f"Warning: {posts_dir} does not exist. Creating it.")
        os.makedirs(posts_dir, exist_ok=True)

    post_path = os.path.join(posts_dir, filename)

    # Write the post
    try:
        with open(post_path, 'w', encoding='utf-8') as f:
            f.write(front_matter + "\n\n" + content)
        print(f"\nPost created successfully at: {post_path}")
    except Exception as e:
        print(f"Error writing post: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()