Gem::Specification.new do |spec|
  spec.name          = "jekyll-jsonfeed"
  spec.version       = "0.1.0"
  spec.authors       = ["Bruce Fang"]
  spec.email         = ["henshao.fang@outlook.com"]

  spec.summary       = "A Jekyll plugin to generate JSON Feed"
  spec.description   = "Generate JSON Feed for your Jekyll site, compatible with https://jsonfeed.org/"
  spec.homepage      = "https://github.com/brucestudios/jekyll-jsonfeed"
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