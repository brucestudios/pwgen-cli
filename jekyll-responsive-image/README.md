# Jekyll Responsive Image

A simple Jekyll plugin to generate responsive `<img>` tags with `srcset` attributes for better performance on different screen sizes.

## Features

- Easy-to-use Liquid tag: `{% responsive_image src="image.jpg" alt="Description" widths="400,800,1200" %}`
- Generates `srcset` with multiple image widths for optimal loading
- Supports optional `sizes` attribute
- Supports additional HTML attributes (class, id, style, etc.)
- Lightweight and dependency-free

## Installation

1. Add this repository as a submodule or copy the `_plugins/jekyll-responsive-image.rb` file to your Jekyll site's `_plugins` directory.
2. Ensure you have the Jekyll version compatible with plugins (Jekyll 3.0+).

## Usage

### Basic Example

```liquid
{% responsive_image src="images/photo.jpg" alt="A beautiful landscape" widths="400,800,1200" %}
```

This will output:

```html
<img src="images/photo.jpg" 
     srcset="images/photo-400.jpg 400w, images/photo-800.jpg 800w, images/photo-1200.jpg 1200w"
     sizes="(max-width: 400px) 400px, (max-width: 800px) 800px, 1200px"
     alt="A beautiful landscape">
```

### With Custom Sizes

```liquid
{% responsive_image src="images/photo.jpg" alt="Photo" widths="300,600,900" sizes="100vw" %}
```

### With Additional Attributes

```liquid
{% responsive_image src="images/photo.jpg" alt="Photo" widths="400,800" class="responsive" id="main-image" %}
```

## How It Works

The plugin expects you to have multiple versions of the same image named with width suffixes (e.g., `photo-400.jpg`, `photo-800.jpg`, `photo-1200.jpg`). The `src` parameter should point to the base image (or any version; the plugin will replace the filename's basename with the width suffixes).

If you don't have the resized images, the plugin will still generate the `srcset` attribute, but the browser will 404 for missing resources. It's recommended to use an image processing workflow (like [Jekyll Assets](https://github.com/jekyll/jekyll-assets) or external tools) to generate the required sizes.

## Configuration

No configuration required. The plugin works out of the box.

## Development

To contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by various responsive image solutions for Jekyll
- Thanks to the Jekyll community for their wonderful plugins