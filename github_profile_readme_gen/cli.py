import argparse
import sys
from .core import generate_profile_readme

def main():
    parser = argparse.ArgumentParser(description="Generate a GitHub profile README")
    parser.add_argument("username", help="GitHub username")
    parser.add_argument("-b", "--bio", help="Short bio", default="")
    parser.add_argument("-l", "--location", help="Location", default="")
    parser.add_argument("-w", "--website", help="Personal website", default="")
    parser.add_argument("-t", "--twitter", help="Twitter handle (without @)", default="")
    parser.add_argument("-g", "--github-link", help="GitHub profile link", default="")
    parser.add_argument("--technologies", nargs="*", help="List of technologies", default=[])
    parser.add_argument("--projects", nargs="*", help="List of projects", default=[])
    parser.add_argument("-o", "--output", help="Output file (default: stdout)", default="")

    args = parser.parse_args()

    readme_content = generate_profile_readme(
        username=args.username,
        bio=args.bio,
        location=args.location,
        website=args.website,
        twitter=args.twitter,
        github_link=args.github_link,
        technologies=args.technologies,
        projects=args.projects
    )

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(readme_content)
        print(f"README written to {args.output}", file=sys.stderr)
    else:
        print(readme_content)

if __name__ == "__main__":
    main()