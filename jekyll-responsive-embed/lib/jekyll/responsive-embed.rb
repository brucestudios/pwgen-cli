module Jekyll
  module ResponsiveEmbed
    # Generates responsive iframe embed code
    class ResponsiveEmbedTag < Liquid::Tag
      def initialize(tag_name, markup, tokens)
        super
        @markup = markup.strip
      end

      def render(context)
        # Parse the markup: URL [width] [height] [class]
        # Example: https://www.youtube.com/watch?v=abc123 560 315 my-class
        parts = @markup.split(/\s+/)
        url = parts[0]
        width = parts[1] || "100%"
        height = parts[2] || "auto"
        klass = parts[3] || "responsive-embed"

        # If height is "auto", we'll set it via CSS to maintain aspect ratio
        # We'll generate a container div with the iframe inside
        # The container will have a class for styling and the iframe will be responsive

        # Default aspect ratio is 16:9, but we can make it configurable if needed
        # For simplicity, we'll use a fixed aspect ratio container and let the iframe fill it

        <<~HTML
          <div class="#{klass}" style="position: relative; width: #{width}; height: 0; padding-bottom: 56.25%;">
            <iframe src="#{url}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;" allowfullscreen></iframe>
          </div>
        HTML
      end
    end
  end
end

Liquid::Template.register_tag('responsive_embed', Jekyll::ResponsiveEmbed::ResponsiveEmbedTag)