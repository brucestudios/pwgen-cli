module Jekyll
  class ResponsiveImageTag < Liquid::Tag
    def initialize(tag_name, markup, tokens)
      super
      @markup = markup
    end

    def render(context)
      # Parse parameters
      params = Liquid::Template.parse(@markup).render(context).strip.split(/\s+/).reduce({}) do |hash, pair|
        key, value = pair.split('=', 2)
        if key && value
          hash[key] = value.gsub(/^["']|["']$/, '') # Remove quotes
        end
        hash
      end

      src = params['src']
      alt = params['alt'] || ''
      widths_str = params['widths'] || '400,800,1200'
      sizes = params['sizes']
      # Collect any other attributes
      other_attrs = params.reject { |k, _| %w[src alt widths sizes].include?(k) }

      if src.nil? || src.empty?
        raise "responsive_image tag requires src parameter"
      end

      # Process widths
      widths = widths_str.split(',').map(&:strip).map(&:to_i).reject { |w| w.zero? }

      # Generate srcset
      srcset = widths.map do |w|
        # Insert width before extension, e.g., image-400.jpg
        # Handle paths with directories and various extensions
        base = File.basename(src, '.*')
        ext = File.extname(src)
        dir = File.dirname(src)
        resized = if ext.empty?
                    "#{src}-#{w}"
                  else
                    File.join(dir, "#{base}-#{w}#{ext}")
                  end
        "#{resized} #{w}w"
      end.join(', ')

      # Build img tag
      attrs = []
      attrs << "src=\"#{src}\""
      attrs << "srcset=\"#{srcset}\""
      attrs << "sizes=\"#{sizes}\"" if sizes && !sizes.empty?
      attrs << "alt=\"#{alt}\""
      other_attrs.each do |k, v|
        attrs << "#{k}=\"#{v}\""
      end

      "<img #{attrs.join(' ')}>"
    end
  end
end

Liquid::Template.register_tag('responsive_image', Jekyll::ResponsiveImageTag)