# Jekyll Reading Time

A simple Jekyll plugin to calculate and display the reading time for posts.

## Installation

Add this line to your Jekyll site's `Gemfile`:

```ruby
gem 'jekyll-reading-time'
```

And then execute:

```bash
bundle install
```

Or install it yourself as:

```bash
gem install jekyll-reading-time
```

## Usage

In your templates, use the `reading_time` filter on the post content:

```liquid
{{ post.content | reading_time }}
```

This will output something like "5 min read" (based on 200 words per minute).

## How it works

The plugin counts the number of words in the input text and divides by 200 (the average words per minute reading speed). It rounds up to the nearest whole minute.

## Configuration

You can change the words per minute by setting the `words_per_minute` in your `_config.yml`:

```yaml
reading_time:
  words_per_minute: 250
```

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).