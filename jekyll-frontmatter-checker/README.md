# Jekyll Frontmatter Checker

A simple Python utility to validate Jekyll markdown files for proper frontmatter.

## Features

- Checks that each `.md` file contains YAML frontmatter delimited by `---`
- Validates that required fields (e.g., `title`, `date`) are present
- Reports missing or malformed frontmatter
- Easy to extend with custom rules

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the checker on a directory:

```bash
python -m jekyll_frontmatter_checker.check /path/to/jekyll/posts
```

Or use the CLI:

```bash
jekyll-check /path/to/posts
```

## Configuration

Create a `.jekyll-checker.yml` to specify required fields:

```yaml
required_fields:
  - title
  - date
  - tags
```

## License

MIT