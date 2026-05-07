module Jekyll
  module SeoTools
    class SeoTagsGenerator < Generator
      safe true
      priority :lowest

      def generate(site)
        site.pages.each do |page|
          next unless page.is_a?(Jekyll::Page) || page.is_a?(Jekyll::Document)
          next if page.data['seo_tools_skip']

          # Generate SEO tags
          seo_data = {
            title: page.data['title'] || site.config['title'],
            description: page.data['description'] || site.config['description'],
            url: File.join(site.config['url'], page.url),
            image: page.data['image'] || site.config['logo'],
            type: page.data['seo_type'] || 'website'
          }

          # Store in page data for use in layouts
          page.data['seo'] = seo_data
        end
      end
    end
  end
end