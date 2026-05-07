# gh-rate-limit

A command-line tool to check your GitHub API rate limit status.

## Features

- Displays remaining requests for core, search, and GraphQL APIs.
- Shows when the rate limit will reset.
- Uses your GitHub authentication token (from `gh auth token` or environment variable `GITHUB_TOKEN`).
- Simple and lightweight (uses only Python standard library).

## Installation

You can install gh-rate-limit via pip:

```bash
pip install gh-rate-limit
```

Or clone the repository and run the script directly:

```bash
git clone https://github.com/brucestudios/gh-rate-limit.git
cd gh-rate-limit
python -m ghratelimit
```

## Usage

```bash
gh-rate-limit
```

## Configuration

The tool looks for a GitHub token in the following order:
1. Environment variable `GITHUB_TOKEN`
2. The token used by the `gh` CLI (via `gh auth token`)

## Example Output

```
GitHub API Rate Limit Status
============================
Core:
   Limit: 5000
   Remaining: 4999
   Reset: 2026-05-02 07:35:00 UTC (in 59 minutes)

Search:
   Limit: 30
   Remaining: 30
   Reset: 2026-05-02 07:35:00 UTC (in 59 minutes)

GraphQL:
   Limit: 5000
   Remaining: 5000
   Reset: 2026-05-02 07:35:00 UTC (in 59 minutes)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.