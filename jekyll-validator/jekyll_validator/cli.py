import sys
import os
from .validator import JekyllValidator

def main():
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