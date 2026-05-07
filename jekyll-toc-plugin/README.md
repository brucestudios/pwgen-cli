# Jekyll TOC Plugin

A simple and flexible Jekyll plugin to automatically generate table of contents for your posts and pages.

## Features

- Automatically generates TOC from markdown headers (h1-h6)
- Customizable heading levels
- Optional TOC container element
- Smooth scrolling support
- No dependencies required

## Installation

1. Copy the `_plugins` folder to your Jekyll site
2. Or install as a gem: `gem install jekyll-toc-plugin`
3. Add to your Gemfile: `gem 'jekyll-toc-plugin'`
4. Run `bundle install`

## Usage

Add the following to your layout or include where you want the TOC to appear:

```liquid
{% toc %}
```

### Configuration

In your `_config.yml`:

```yaml
toc:
  min_level: 1    # Minimum heading level to include (default: 1)
  max_level: 3    # Maximum heading level to include (default: 3)
  class: "toc"    # CSS class for the TOC container (default: "toc")
  id: "toc"       # HTML id for the TOC container (default: "toc")
```

## Development

To contribute:

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

MIT