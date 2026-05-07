# Jekyll Post Helper

A simple Python script to generate new Jekyll post files with proper front matter.

## Usage

```bash
python jekyll_post_helper.py "My Post Title"
```

This will create a new file in the `_posts` directory with the current date and a slugified version of the title.

Example output:
```
Created new Jekyll post: _posts/2026-05-05-my-post-title.md
```

## Requirements

- Python 3.x

## Installation

1. Clone or download this repository.
2. (Optional) Make the script executable: `chmod +x jekyll_post_helper.py`
3. Run the script as shown above.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.