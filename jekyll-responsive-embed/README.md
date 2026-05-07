# Jekyll Responsive Embed

A Jekyll plugin to generate responsive iframe embed codes for YouTube, Vimeo, and other iframe-based content.

## Installation

Add this line to your Jekyll site's `Gemfile`:

```ruby
gem "jekyll-responsive-embed"
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install jekyll-responsive-embed

## Usage

In any of your pages or posts, use the Liquid tag:

{% raw %}
{% responsive_embed https://www.youtube.com/watch?v=dQw4w9WgXcQ %}
{% endraw %}

You can also specify width, height, and a custom class:

{% raw %}
{% responsive_embed https://www.youtube.com/watch?v=dQw4w9WgXcQ 560 315 my-custom-class %}
{% endraw %}

The plugin will generate a responsive iframe that maintains a 16:9 aspect ratio by default.

## How it works

The plugin wraps the iframe in a container with `position: relative` and a `padding-bottom` to maintain the aspect ratio. The iframe itself is set to `position: absolute` and fills the container.

## Development

To install dependencies and run tests:

    $ bundle install
    $ rake

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/brucestudios/jekyll-responsive-embed.

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).