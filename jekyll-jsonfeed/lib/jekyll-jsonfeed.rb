require "jekyll"

module Jekyll
  class JsonFeedGenerator < Generator
    safe true
    priority :lowest

    def generate(site)
      config = site.config["json_feed"] || {}
      feed = {
        "version" => "https://jsonfeed.org/version/1",
        "title" => config["name"] || site.config["name"] || site.title || "Untitled",
        "home_page_url" => site.config["url"],
        "feed_url" => "#{site.config["url"]}/feed.json",
        "description" => config["description"] || site.config["description"] || "",
        "user_comment" => "This feed allows you to read the posts from this site in any feed reader that supports the JSON Feed format.",
        "icon" => config["icon"] || "",
        "favicon" => config["favicon"] || "",
        "author" => {
          "name" => config.dig("author", "name") || site.config["author"] || "",
          "email" => config.dig("author", "email") || "",
          "url" => config.dig("author", "url") || site.config["url"] || ""
        },
        "items" => []
      }

      site.posts.docs.each do |post|
        url = "#{site.config["url"]}#{post.url}"
        feed["items"] << {
          "id" => url,
          "url" => url,
          "title" => post.data["title"] || "",
          "content_html" => post.output,
          "summary" => post.data["description"] || post.data["excerpt"] || "",
          "date_published" => post.date.xmlschema,
          "date_modified" => post.date.xmlschema,
          "author" => {
            "name" => post.data["author"] || (site.config["author"] if site.config["author"].is_a?(String)) || ""
          }
        }
      end

      # Write the feed to the site's destination
      feed_file = File.new(File.join(site.dest, "feed.json"), "w")
      feed_file.write(JSON.pretty_generate(feed))
      feed_file.close
    end
  end
end