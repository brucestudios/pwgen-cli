# Jekyll Chirpy Post Helper

A Python script to generate Jekyll posts with proper front matter for the [Chirpy theme](https://github.com/cotes2020/jekyll-theme-chirpy).

## Features

- Interactive prompts for title, tags, categories, and content
- Automatic date-based filename generation (YYYY-MM-DD-title.md)
- Proper Chirpy theme front matter format
- Slugify title for URL-friendly filenames
- Support for specifying post date
- Creates `_posts` directory if it doesn't exist

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/jekyll-chirpy-post-helper.git
   ```

2. Make the script executable:
   ```bash
   chmod +x jekyll_post_helper.py
   ```

3. (Optional) Add the script to your PATH for easy access:
   ```bash
   # Add to your ~/.bashrc or ~/.zshrc
   export PATH="$PATH:/path/to/jekyll-chirpy-post-helper"
   ```

## Usage

Run the script from your Jekyll site root directory:

```bash
python jekyll_post_helper.py
```

Or with arguments:

```bash
python jekyll_post_helper.py --title "My Awesome Post" --tags "jekyll,blog" --categories "updates"
```

### Arguments

- `--title`: Post title (will prompt if not provided)
- `--date`: Post date in YYYY-MM-DD format (defaults to today)
- `--tags`: Comma-separated list of tags
- `--categories`: Comma-separated list of categories
- `--content`: Post content (will prompt if not provided)
- `--site-root`: Root directory of your Jekyll site (defaults to current directory)

### Example Interaction

```
$ python jekyll_post_helper.py
Enter post title: My First Blog Post
Enter tags (comma-separated, leave empty for none): jekyll,blog,first-post
Enter categories (comma-separated, leave empty for none): updates
Enter post content (end with an empty line or Ctrl+D):
Welcome to my blog!

This is my first post using the Jekyll Chirpy theme helper.

Hope you enjoy reading it.
```

This will create a file like: `_posts/2026-05-05-my-first-blog-post.md` with the proper front matter.

## Output Example

The generated post will have front matter like:

```markdown
---
layout: post
title:  "My First Blog Post"
date:   2026-05-05 14:30:00 +0800
categories: [updates]
tags: [jekyll, blog, first-post]
---

Welcome to my blog!

This is my first post using the Jekyll Chirpy theme helper.

Hope you enjoy reading it.
```

## Requirements

- Python 3.6+

## License

MIT

## Contributing

Feel free to submit issues or pull requests to improve this tool.

## Acknowledgments

- [Chirpy Theme](https://github.com/cotes2020/jekyll-theme-chirpy) - The beautiful Jekyll theme this helper is designed for