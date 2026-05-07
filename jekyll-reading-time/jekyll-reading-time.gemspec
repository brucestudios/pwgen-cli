Gem::Specification.new do |spec|
  spec.name          = "jekyll-reading-time"
  spec.version       = "0.1.0"
  spec.authors       = ["Bruce Fang"]
  spec.email         = ["henshao.fang@outlook.com"]

  spec.summary       = "A Jekyll plugin to calculate and display reading time for posts"
  spec.description   = "A simple Jekyll plugin that provides a Liquid filter to calculate the reading time of a post or any text content."
  spec.homepage      = "https://github.com/brucestudios/jekyll-reading-time"
  spec.license       = "MIT"

  spec.files         = Dir["_plugins/**/*", "README.md", "LICENSE.txt", "jekyll-reading-time.gemspec"]
  spec.require_paths = ["_plugins"]

  spec.add_runtime_dependency "jekyll", ">= 3.0", "< 5.0"
end