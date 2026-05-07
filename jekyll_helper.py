#!/usr/bin/env python3
import argparse
import subprocess
import sys
import os
from datetime import date

def serve():
    """Build and serve the Jekyll site."""
    subprocess.run(["jekyll", "serve"], check=True)

def new_post(title):
    """Create a new Jekyll post."""
    today = date.today()
    filename = f"{today}-{title.lower().replace(' ', '-')}.md"
    path = os.path.join("_posts", filename)
    # Ensure _posts directory exists
    os.makedirs("_posts", exist_ok=True)
    # Front matter
    front_matter = f"""---
layout: post
title:  "{title}"
date:   {today}
---
"""
    with open(path, "w") as f:
        f.write(front_matter)
    print(f"Created post: {path}")

def main():
    parser = argparse.ArgumentParser(description="Jekyll helper utility")
    subparsers = parser.add_subparsers(dest="command")

    # Serve command
    serve_parser = subparsers.add_parser("serve", help="Build and serve the Jekyll site")

    # New post command
    new_post_parser = subparsers.add_parser("new-post", help="Create a new Jekyll post")
    new_post_parser.add_argument("title", help="Title of the new post")

    args = parser.parse_args()

    if args.command == "serve":
        serve()
    elif args.command == "new-post":
        new_post(args.title)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
