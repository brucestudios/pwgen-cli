#!/bin/bash
# Interactive script to create a new Jekyll Chirpy post

set -e

# Default values
DATE=$(date +%Y-%m-%d)
TITLE=""
CATEGORIES=""
TAGS=""
DRAFT=false

# Prompt for input
read -rp "Enter post title: " TITLE
if [[ -z "$TITLE" ]]; then
  echo "Title is required."
  exit 1
fi

read -rp "Enter date (YYYY-MM-DD) [$DATE]: " INPUT_DATE
if [[ -n "$INPUT_DATE" ]]; then
  DATE=$INPUT_DATE
fi

read -rp "Enter categories (comma-separated, optional): " CATEGORIES
read -rp "Enter tags (comma-separated, optional): " TAGS
read -rp "Is this a draft? (y/N): " DRAFT_INPUT
if [[ "$DRAFT_INPUT" =~ ^[Yy]$ ]]; then
  DRAFT=true
fi

# Format filename: YYYY-MM-DD-title.md (slugified)
SLUG=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | tr -s ' ' '-' | sed 's/[^a-z0-9-]//g')
FILENAME="${DATE}-${SLUG}.md"
POST_DIR="_posts"

# Ensure _posts directory exists
mkdir -p "$POST_DIR"

# Front matter
cat > "${POST_DIR}/${FILENAME}" <<FOO
---
layout: post
title: "$TITLE"
date: ${DATE}
categories: ${CATEGORIES}
tags: ${TAGS}
---
FOO

if $DRAFT; then
  mv "${POST_DIR}/${FILENAME}" "${POST_DIR}/${FILENAME}.draft"
  echo "Draft created: ${POST_DIR}/${FILENAME}.draft"
else
  echo "Post created: ${POST_DIR}/${FILENAME}"
fi
