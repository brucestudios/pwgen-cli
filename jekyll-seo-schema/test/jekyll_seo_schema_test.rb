require "jekyll-seo-schema"
require "minitest/autorun"
require "jekyll"

class JekyllSeoSchemaTest < Minitest::Test
  def setup
    @site = Jekyll::Site.new(Jekyll.configuration({
      "source"      => File.expand_path("../fixtures", __dir__),
      "destination" => File.expand_path("../dest", __dir__),
      "seo_schema"  => {
        "name" => "Test Site",
        "url"  => "https://example.com",
        "site" => {
          "name" => "Test Site",
          "url"  => "https://example.com"
        },
        "organization" => {
          "name" => "Test Org",
          "url"  => "https://example.com",
          "logo" => "https://example.com/logo.png"
        }
      }
    }))
    @site.reset
    @site.read
    @site.generate
  end

  def test_adds_seo_schema_to_posts
    post = @site.posts.docs.first
    assert_includes post.data.keys, "seo_schema"
    assert post.data["seo_schema"].any? { |schema| schema["@type"] == "BlogPosting" }
  end

  def test_adds_website_schema_once
    website_schemas = @site.pages.flat_map { |p| p.data["seo_schema"] || [] }.select { |s| s["@type"] == "WebSite" }
    assert_equal 1, website_schemas.size
  end

  def test_adds_organization_schema_when_configured
    org_schemas = @site.pages.flat_map { |p| p.data["seo_schema"] || [] }.select { |s| s["@type"] == "Organization" }
    assert_equal 1, org_schemas.size
    assert_equal "Test Org", org_schemas.first["name"]
  end
end
