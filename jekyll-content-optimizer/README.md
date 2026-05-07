# Jekyll Content Optimizer

A CLI tool to optimize Jekyll site content including images, HTML, CSS, and JavaScript.

## Features

- Image compression and format conversion
- HTML minification
- CSS and JavaScript minification
- Asset fingerprinting for cache busting
- Jekyll integration via plugins or command line

## Installation

```bash
pip install jekyll-content-optimizer
```

## Usage

```bash
# Optimize entire site
jekyll-content-optimizer optimize --source ./_site --output ./_site-optimized

# Watch for changes and optimize incrementally
jekyll-content-optimizer watch --source ./_site --output ./_site-optimized
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/brucestudios/jekyll-content-optimizer.git
cd jekyll-content-optimizer

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Contact

Bruce Fang - henshao.fang@outlook.com

Project Link: https://github.com/brucestudios/jekyll-content-optimizer