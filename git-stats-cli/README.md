# Git Stats CLI

A powerful command-line tool for analyzing Git repository statistics and generating insightful reports about code contributions, commit patterns, and developer activity.

## Features

- 📊 Comprehensive commit analysis
- 👥 Contributor statistics and activity heatmaps
- 📈 Time-based commit patterns and trends
- 🔍 File change statistics and code churn metrics
- 🎯 Customizable date ranges and filtering options
- 📋 Multiple output formats (JSON, CSV, Markdown, Text)
- 🖥️ Cross-platform compatibility (Linux, macOS, Windows)

## Installation

```bash
# Install via pip
pip install git-stats-cli

# Or install from source
git clone https://github.com/brucestudios/git-stats-cli.git
cd git-stats-cli
pip install -e .
```

## Usage

### Basic Repository Statistics
```bash
git-stats-cli summary
```

### Contributor Analysis
```bash
git-stats-cli contributors --top 10
```

### Commit Timeline
```bash
git-stats-cli timeline --since "3 months ago"
```

### File Change Statistics
```bash
git-stats-cli churn --file-types ".py,.js,.ts"
```

### Generate Report
```bash
git-stats-cli report --format markdown --output REPORT.md
```

## Configuration

Create a `.gitstats` config file in your repository:

```ini
[general]
exclude_authors = dependabot[bot], github-actions[bot]
date_format = %Y-%m-%d

[output]
default_format = markdown
color_output = true

[filters]
min_commits = 5
file_extensions = .py,.js,.ts,.java,.cpp
```

## Examples

```bash
# Show top contributors from last 6 months
git-stats-cli contributors --since "6 months ago" --limit 5

# Analyze code churn for Python files
git-stats-cli churn --file-types ".py" --since "2026-01-01"

# Generate comprehensive JSON report
git-stats-cli report --format json --output stats.json --since "1 year ago"

# Compare two time periods
git-stats-cli compare --period1 "2026-Q1" --period2 "2026-Q2"
```

## Output Formats

- `text` - Human-readable console output (default)
- `json` - Structured data for programmatic consumption
- `csv` - Spreadsheet-friendly format
- `markdown` - Documentation-ready reports

## Development

### Setup
```bash
# Clone and install development dependencies
git clone https://github.com/brucestudios/git-stats-cli.git
cd git-stats-cli
pip install -e ".[dev]"
```

### Running Tests
```bash
pytest tests/
```

### Building Distribution
```bash
python -m build
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by various Git analytics tools
- Built with ❤️ using Python and GitPython
- Thanks to the open-source community for Git and related tools