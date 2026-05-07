Gem::Specification.new do |spec|
  spec.name          = "jekyll-seo-tools"
  spec.version       = "0.1.0"
  spec.authors       = ["Bruce Fang"]
  spec.email         = ["henshao.fang@outlook.com"]

  spec.summary       = "A Jekyll plugin to enhance SEO with automatic meta tags, structured data, and social media integration."
  spec.description   = "Jekyll SEO Tools provides a comprehensive set of features to improve search engine optimization for Jekyll sites, including automatic generation of meta tags, JSON-LD structured data, Open Graph tags, and Twitter cards."
  spec.homepage      = "https://github.com/brucestudios/jekyll-seo-tools"
  spec.license       = "MIT"

  spec.files         = Dir.chdir(File.expand_path('..', __dir__)) do
    `git ls-files -z`.split("\x0").reject { |f| f.match(%r{^(test|spec|features)/}) }
  end
  spec.bindir        = "exe"
  spec.executables   = spec.files.grep(%r{^exe/}) { |f| File.basename(f) }
  spec.require_paths = ["lib"]

  spec.add_runtime_dependency "jekyll", ">= 3.0", "< 5.0"
  spec.add_development_dependency "bundler", "~> 2.0"
  spec.add_development_dependency "rake", "~> 13.0"
  spec.add_development_dependency "rspec", "~> 3.0"
end