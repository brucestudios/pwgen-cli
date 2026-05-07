# Jekyll JSON Feed

A simple Jekyll plugin to generate [JSON Feed](https://jsonfeed.org/) for your Jekyll site.

## Installation

Add this line to your Jekyll site's `Gemfile`:

```ruby
gem 'jekyll-jsonfeed'
```

And then execute:

```bash
bundle install
```

Or install it yourself as:

```bash
gem install jekyll-jsonfeed
```

## Usage

1. Add the plugin to your `_config.yml`:

```yaml
plugins:
  - jekyll-jsonfeed
```

2. The JSON Feed will be available at `/feed.json` on your site.

## Configuration

You can customize the JSON Feed in your `_config.yml`:

```yaml
json_feed:
  name: "My Jekyll Site"
  description: "A description of my site"
  feed_url: "https://example.com/feed.json"
  icon: "https://example.com/icon.png"
  favicon: "https://example.com/favicon.ico"
  author:
    name: "Your Name"
    email: "you@example.com"
    url: "https://example.com"
```

## Development

To install this gem onto your local machine, run:

```bash
bundle install
```

To test the plugin, run:

```bash
bundle exec jekyll serve
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/[your-username]/jekyll-jsonfeed.

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).