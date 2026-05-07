# Jekyll Chirpy SEO Plugin
# Generates SEO meta tags and structured data for Jekyll sites using the Chirpy theme

require 'jekyll'

module Jekyll
  module SeoTag
    class Generator < Generator
      safe true
      priority :lowest

      def initialize(config)
        super(config)
        @config = config['seo'] || {}
      end

      def generate(site)
        site.pages.each do |page|
          generate_seo(page)
        end
        site.posts.each do |post|
          generate_seo(post)
        end
      end

      def generate_seo(page)
        # Skip if the page is not HTML or if it's excluded
        return unless page.output_ext == '.html'

        # Get SEO data from page's front matter or defaults
        seo_data = page.data['seo'] || {}
        seo_data = @config.merge(seo_data)

        # Set default values
        seo_data['title'] ||= page.data['title'] || @config['site_name'] || site.config['title']
        seo_data['description'] ||= page.data['description'] || @config['site_description'] || site.config['description']
        seo_data['url'] ||= @config['site_url'] || site.config['url']
        seo_data['image'] ||= page.data['image'] || @config['default_image']
        seo_data['type'] ||= page.data.is_a?(Jekyll::Post) ? 'Article' : 'WebPage'

        # Generate meta tags
        page.data['seo_meta'] = generate_meta_tags(seo_data)
        page.data['seo_json_ld'] = generate_json_ld(seo_data, page)
      end

      def generate_meta_tags(data)
        tags = []
        tags << %(<title>#{escape(data['title'])}</title>)
        tags << %(<meta name="description" content="#{escape(data['description'])}">)
        tags << %(<meta name="keywords" content="#{escape(data['keywords'] || '')}">) if data['keywords']

        # Open Graph
        tags << %(<meta property="og:title" content="#{escape(data['title'])}">)
        tags << %(<meta property="og:description" content="#{escape(data['description'])}">)
        tags << %(<meta property="og:url" content="#{escape(data['url'])}">)
        tags << %(<meta property="og:type" content="#{escape(data['type'])}">)
        tags << %(<meta property="og:site_name" content="#{escape(data['site_name'] || data['title'])}">)
        tags << %(<meta property="og:image" content="#{escape(data['image'])}">) if data['image']

        # Twitter Card
        tags << %(<meta name="twitter:card" content="summary_large_image">)
        tags << %(<meta name="twitter:title" content="#{escape(data['title'])}">)
        tags << %(<meta name="twitter:description" content="#{escape(data['description'])}">)
        tags << %(<meta name="twitter:image" content="#{escape(data['image'])}">) if data['image']
        tags << %(<meta name="twitter:site" content="#{escape(data['twitter'] || '@' + data['site_name'].downcase.gsub(/\s+/, ''))}">) if data['twitter']

        tags.join("\n")
      end

      def generate_json_ld(data, page)
        json_ld = {
          "@context" => "https://schema.org",
          "@type" => data['type'],
          "name" => data['title'],
          "description" => data['description'],
          "url" => data['url'],
          "image" => data['image']
        }

        # Add datePublished and dateModified if available
        if data['datePublished']
          json_ld["datePublished"] = data['datePublished']
        end
        if data['dateModified']
          json_ld["dateModified"] = data['dateModified']
        end

        # Add author if available
        if data['author']
          if data['author'].is_a?(String)
            json_ld["author"] = { "@type" => "Person", "name" => data['author'] }
          elsif data['author'].is_a?(Hash)
            json_ld["author"] = data['author']
          end
        end

        # Add publisher if available
        if data['publisher']
          json_ld["publisher"] = {
            "@type" => "Organization",
            "name" => data['publisher']['name'] || data['site_name'],
            "logo" => {
              "@type" => "ImageObject",
              "url" => data['publisher']['logo']
            }
          }
        end

        %(<script type="application/ld+json">#{JSON.dump(json_ld)}</script>)
      end

      def escape(string)
        Jekyll::Utils.escape_html(string.to_s)
      end
    end
  end
end