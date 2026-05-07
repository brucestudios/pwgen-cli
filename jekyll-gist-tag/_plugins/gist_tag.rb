module Jekyll
  require 'net/http'
  require 'json'

  class GistTagPage < Page
    def initialize(site, base, dir, username)
      @site = site
      @base = base
      @dir = dir
      @name = 'index.html'
      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'gist_tag.html')
      self.data['username'] = username
      self.data['title'] = "Gists by #{username}"
      # Fetch gists and attach to page data
      self.data['gists'] = fetch_gists(username)
    end

    def fetch_gists(username)
      uri = URI("https://api.github.com/users/#{username}/gists")
      response = Net::HTTP.get_response(uri)
      if response.is_a?(Net::HTTPSuccess)
        begin
          JSON.parse(response.body)
        rescue JSON::ParserError
          []
        end
      else
        # In case of error (e.g., user not found, rate limit), return empty array
        []
      end
    rescue
      []
    end
  end

  class GistTagGenerator < Generator
    safe true
    priority :lowest

    def generate(site)
      username = site.config['gist_tag_username']
      return unless username

      dir = File.join('gist', username)
      site.pages << GistTagPage.new(site, site.source, dir, username)
    end
  end
end