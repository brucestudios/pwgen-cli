# Markdown TOC Generator

A simple command-line tool to generate a table of contents for markdown files.

## Features

- Extracts headings from markdown files
- Generates a nested table of contents based on heading levels
- Configurable depth (default: 3)
- Output to file or stdout

## Installation

```bash
npm install -g markdown-toc-generator
```

## Usage

```bash
markdown-toc <file> [options]
```

### Options

- `-d, --depth <number>`: Maximum heading depth to include (default: 3)
- `-o, --output <file>`: Output file (default: stdout)

### Example

```bash
markdown-toc README.md -d 3 -o TOC.md
```

## Example Input

```markdown
# Introduction
## Getting Started
### Installation
## Usage
# API Reference
## Core Functions
```

## Example Output

```markdown
# Table of Contents

- [Introduction](#introduction)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
  - [Usage](#usage)
- [API Reference](#api-reference)
  - [Core Functions](#core-functions)
```

## License

MIT