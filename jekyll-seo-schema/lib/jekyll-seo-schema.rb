require "jekyll"

module JekyllSeoSchema
  class Generator < Jekyll::Generator
    safe true
    priority :lowest

    def generate(site)
      @config = site.config["seo_schema"] || {}
      site.pages.each do |page|
        generate_schema_for(page)
      end
      site.posts.each do |post|
        generate_schema_for(post)
      end
    end

    def generate_schema_for(item)
      # Only generate for HTML output
      return unless item.output_ext == ".html"

      # Collect schema data
      schema_data = []

      # WebSite schema (once per site)
      schema_data << website_schema unless @website_schema_added
      @website_schema_added = true

      # Organization schema (if configured)
      schema_data << organization_schema if @config["organization"]

      # BlogPosting schema for posts
      if item.is_a?(Jekyll::Post) || (item.data["layout"] == "post")
        schema_data << blog_posting_schema(item)
      end

      # Add the schema data to the item's data for use in templates
      item.data["seo_schema"] = schema_data.reject { |s| s.nil? }
    end

    def website_schema
      {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": @config.dig("site", "name") || @config["name"] || "My Site",
        "url": @config.dig("site", "url") || @config["url"] || "",
        "potentialAction": [{
          "@type": "SearchAction",
          "target": "#{@config.dig('site', 'url') || @config['url'] || ''}/search?q={search_term_string}",
          "query-input": "required name=search_term_string"
        }]
      }.compact
    end

    def organization_schema
      org_config = @config["organization"]
      {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": org_config["name"] || "",
        "url": org_config["url"] || "",
        "logo": org_config["logo"] || ""
      }.compact
    end

    def blog_posting_schema(post)
      {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": post.data["title"] || "",
        "description": post.data["description"] || post.data["excerpt"] || "",
        "image": post.data["image"] || "",
        "author": [{
          "@type": "Person",
          "name": post.data["author"] || @config.dig("site", "author") || ""
        }],
        "publisher": [{
          "@type": "Organization",
          "name": @config.dig("site", "name") || @config["name"] || "",
          "logo": {
            "@type": "ImageObject",
            "url": @config.dig("site", "logo") || @config["logo"] || ""
          }
        }],
        "datePublished": post.date.to_time.iso8601,
        "dateModified": post.date.to_time.iso8601,
        "mainEntityOfPage": {
          "@type": "WebPage",
          "@id": post.url
        }
      }.compact
    end
  end
end
