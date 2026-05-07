module Jekyll
  module TocGenerator
    def toc_generator(content)
      # Extract headers from markdown content
      headers = content.scan(/^(#{'+'*6})\s+(.+)$/).map do |level, title|
        { level: level.length, title: title.strip, id: title.downcase.gsub(/[^a-z0-9]+/, '-').gsub(/^-|-$/, '') }
      end

      # Build TOC HTML
      toc = '<ul class="toc">'
      headers.each do |header|
        toc += "<li><a href=\"##{header[:id]}\">#{header[:title]}</a></li>"
      end
      toc += '</ul>'

      toc
    end
  end
end

Liquid::Template.register_filter(Jekyll::TocGenerator)