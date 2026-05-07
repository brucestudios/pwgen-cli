# Jekyll SEO Schema

A Jekyll plugin to add JSON-LD structured data for SEO to your Jekyll site.

## Features

- Adds JSON-LD for WebSite, Organization, BlogPosting, and more.
- Easy to configure via `_config.yml`.
- Supports multiple schema types per page.
- Works with Jekyll 3.x and 4.x.

## Installation

Add this line to your Jekyll site's `Gemfile`:

```ruby
gem "jekyll-seo-schema"
```

And then execute:

    bundle install

Or install it yourself as:

    gem install jekyll-seo-schema

## Usage

1. Add the plugin to your Jekyll plugins in `_config.yml`:

```yaml
plugins:
  - jekyll-seo-schema
```

2. Configure the plugin (optional):

```yaml
seo_schema:
  site:
    name: "My Awesome Site"
    url: "https://example.com"
    logo: "https://example.com/logo.png"
  organization:
    name: "My Organization"
    url: "https://example.com"
    logo: "https://example.com/logo.png"
```

3. The plugin will automatically generate JSON-LD scripts and insert them into the `<head>` of your pages.

## Configuration Options

See [the documentation](https://github.com/brucestudios/jekyll-seo-schema/wiki/Configuration) for all available options.

## Development

To set up your environment to develop this gem, run:

    bundle install

To run the tests, run:

    bundle exec rake test

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/brucestudios/jekyll-seo-schema.

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

