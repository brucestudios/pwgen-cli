# Jekyll Front Matter Generator

A simple Python script to generate Jekyll front matter for markdown files.

## Usage

```bash
python generate_frontmatter.py --title "My Post" --date "2026-05-06" --tags "jekyll,blog"
```

Outputs:

```yaml
---
layout: post
title: "My Post"
date: 2026-05-06
tags: [jekyll, blog]
---
```

## License

MIT