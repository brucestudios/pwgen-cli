#!/usr/bin/env bash
# new-post.sh - Create a new Jekyll post with proper front matter

# Exit on any error
set -e

# Check if title is provided
if [ -z "$1" ]; then
  echo "Usage: $0 \"Post Title\""
  exit 1
fi

TITLE="$1"
DATE=$(date +%Y-%m-%d)
SLUG=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | tr -s ' ' '-' | sed 's/[^a-z0-9-]//g')
FILENAME="_posts/${DATE}-${SLUG}.md"

# Check if file already exists
if [ -f "$FILENAME" ]; then
  echo "Error: $FILENAME already exists."
  exit 1
fi

# Create the file with front matter
cat > "$FILENAME" <<EOF
---
layout: post
title:  "$TITLE"
date:   $(date +%Y-%m-%d\ %H:%M:%S\ %z)
categories: jekyll update
---

# $TITLE

Write your post content here.
EOF

echo "Created new post: $FILENAME"
echo "Remember to run 'jekyll build' or 'jekyll serve' to preview your site."