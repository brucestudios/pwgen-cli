# Jekyll SEO Enhanced

A CLI tool to enhance SEO for Jekyll blogs by generating optimized front matter and providing SEO audits and suggestions.

## Features

- ✨ Create new Jekyll posts with SEO-optimized front matter
- 🔍 Audit existing posts for SEO issues
- 💡 Get SEO suggestions for titles and content
- 📝 Supports title, description, keywords, tags, and categories
- ⚡ Built with Node.js and Commander.js

## Installation

```bash
npm install -g jekyll-seo-enhanced
```

Or clone and link locally:

```bash
git clone https://github.com/brucestudios/jekyll-seo-enhanced.git
cd jekyll-seo-enhanced
npm link
```

## Usage

### Create a new post

```bash
jekyll-seo new-post
```

You'll be prompted for:
- Post title
- Category (default: blog)
- Date (defaults to today)
- Tags (comma-separated)
- Meta description (required for SEO)
- Keywords (comma-separated)

### Audit existing posts

```bash
jekyll-seo audit
```

Scans the `_posts` directory and checks for:
- Missing title
- Missing date
- Missing description (important for SEO)
- Missing keywords (helpful for SEO)

### Get SEO suggestions

```bash
jekyll-seo suggest
```

Provides suggestions for:
- Title length optimization
- Power words inclusion
- Numbers for list posts
- Question/how-to formatting

## Example Output

When creating a new post:
```
? Enter post title: How to Optimize Your Jekyll Blog for SEO
? Enter post category (default: blog): webdev
? Enter post date (YYYY-MM-DD, default: today): 2026-05-07
? Enter tags (comma-separated): jekyll, seo, webdev
? Enter meta description for SEO: Learn how to improve your Jekyll blog's search engine visibility with these proven techniques.
? Enter SEO keywords (comma-separated): Jekyll, SEO, blog optimization, static site
✅ Created post: _posts/2026-05-07-how-to-optimize-your-jekyll-blog-for-seo.md
📝 Edit the file to add your content
```

Generated front matter:
```yaml
---
layout: post
title: "How to Optimize Your Jekyll Blog for SEO"
date: 2026-05-07
category: webdev
tags: ["jekyll", "seo", "webdev"]
description: "Learn how to improve your Jekyll blog's search engine visibility with these proven techniques."
keywords: ["Jekyll", "SEO", "blog optimization", "static site"]
---
```

## Requirements

- Node.js >= 14.0.0
- A Jekyll blog with a `_posts` directory

## License

MIT

## Author

Bruce Fang