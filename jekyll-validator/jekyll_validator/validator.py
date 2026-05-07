import os
import yaml
from typing import List, Tuple

class JekyllValidator:
    def __init__(self, site_path: str):
        self.site_path = site_path
        self.issues = []

    def validate(self) -> List[str]:
        self.issues = []
        self._check_config()
        self._check_posts_dir()
        self._check_chirpy_specific()
        return self.issues

    def _check_config(self):
        config_path = os.path.join(self.site_path, '_config.yml')
        if not os.path.exists(config_path):
            self.issues.append("Missing _config.yml")
            return

        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
        except Exception as e:
            self.issues.append(f"Error parsing _config.yml: {e}")
            return

        # Basic check for theme
        if config.get('theme') != 'chirpy':
            self.issues.append("Theme is not set to 'chirpy' (optional but recommended)")

    def _check_posts_dir(self):
        posts_path = os.path.join(self.site_path, '_posts')
        if not os.path.isdir(posts_path):
            self.issues.append("Missing _posts directory")

    def _check_chirpy_specific(self):
        # Check for assets directory (Chirpy uses assets)
        assets_path = os.path.join(self.site_path, 'assets')
        if not os.path.isdir(assets_path):
            self.issues.append("Missing assets directory (Chirpy theme)")

        # Check for _data directory (Chirpy uses _data for navigation, etc.)
        data_path = os.path.join(self.site_path, '_data')
        if not os.path.isdir(data_path):
            self.issues.append("Missing _data directory (Chirpy theme)")

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: jekyll-validate <path-to-jekyll-site>")
        sys.exit(1)

    site_path = sys.argv[1]
    if not os.path.isdir(site_path):
        print(f"Error: {site_path} is not a directory")
        sys.exit(1)

    validator = JekyllValidator(site_path)
    issues = validator.validate()

    if issues:
        print("Issues found:")
        for issue in issues:
            print(f" - {issue}")
        sys.exit(1)
    else:
        print("No issues found. Your Jekyll site looks good!")
        sys.exit(0)

if __name__ == '__main__':
    main()