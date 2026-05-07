# Jekyll Manager

A command-line tool to manage Jekyll sites.

## Features

- Create new Jekyll sites
- Build Jekyll sites
- Serve Jekyll sites locally
- Deploy Jekyll sites to GitHub Pages

## Installation

You can install the package using pip:

```bash
pip install jekyll-manager
```

Or install from source:

```bash
git clone https://github.com/brucestudios/jekyll-manager.git
cd jekyll-manager
pip install .
```

## Usage

After installation, you can use the `jekyll-manager` command.

### Create a new Jekyll site

```bash
jekyll-manager new mysite
```

This will create a new Jekyll site in a directory named `mysite`.

### Build the Jekyll site

```bash
jekyll-manager build
```

This will build the Jekyll site in the current directory (or specify a path with `--path`).

### Serve the Jekyll site locally

```bash
jekyll-manager serve
```

This will start a local server at `http://localhost:4000` (you can change the host and port with `--host` and `--port`).

### Deploy the Jekyll site to GitHub Pages

```bash
jekyll-manager deploy
```

This will build the site and deploy it to the `gh-pages` branch of the current Git repository.

## Requirements

- Python 3.7 or higher
- Jekyll and Bundler (for building and serving the site)
- Git (for deployment)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Bruce Fang (henshao.fang@outlook.com)