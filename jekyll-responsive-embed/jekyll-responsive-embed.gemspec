Gem::Specification.new do |spec|
  spec.name          = "jekyll-responsive-embed"
  spec.version       = "0.1.0"
  spec.authors       = ["Bruce Fang"]
  spec.email         = ["henshao.fang@outlook.com"]

  spec.summary       = "A Jekyll plugin to generate responsive embed codes for iframes (like YouTube, Vimeo, etc.)"
  spec.description   = "This plugin provides a Liquid tag `responsive_embed` that generates responsive iframe embeds with a 16:9 aspect ratio by default, but customizable."
  spec.homepage      = "https://github.com/brucestudios/jekyll-responsive-embed"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0").reject do |f|
    f.match(%r{^(test|spec|features)/})
  end
  spec.bindir        = "exe"
  spec.executables   = spec.files.grep(%r{^exe/}) { |f| File.basename(f) }
  spec.require_paths = ["lib"]

  spec.add_runtime_dependency "jekyll", ">= 3.0", "< 5.0"
  spec.add_development_dependency "bundler", "~> 2.0"
  spec.add_development_dependency "rake", "~> 13.0"
end