#!/usr/bin/env python3
"""
Jekyll Manager - A command-line tool to manage Jekyll sites.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

def run_command(command, cwd=None):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(
            command, shell=True, check=True, capture_output=True, text=True, cwd=cwd
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Error: {e.stderr}")
        sys.exit(1)

def new_site(args):
    """Create a new Jekyll site."""
    site_name = args.name
    if not site_name:
        print("Error: Site name is required.")
        sys.exit(1)
    
    site_path = Path(site_name)
    if site_path.exists():
        print(f"Error: Directory '{site_name}' already exists.")
        sys.exit(1)
    
    print(f"Creating new Jekyll site: {site_name}")
    run_command(f"jekyll new {site_name}")
    print(f"Site '{site_name}' created successfully.")
    print(f"To get started:")
    print(f"  cd {site_name}")
    print(f"  bundle exec jekyll serve")

def build_site(args):
    """Build the Jekyll site."""
    site_path = Path(args.path) if args.path else Path.cwd()
    if not (site_path / "_config.yml").exists():
        print(f"Error: No Jekyll site found in '{site_path}'.")
        print("Make sure you are in a Jekyll site directory or provide the path with --path.")
        sys.exit(1)
    
    print(f"Building Jekyll site in '{site_path}'...")
    run_command("bundle exec jekyll build", cwd=site_path)
    print("Site built successfully.")

def serve_site(args):
    """Serve the Jekyll site locally."""
    site_path = Path(args.path) if args.path else Path.cwd()
    if not (site_path / "_config.yml").exists():
        print(f"Error: No Jekyll site found in '{site_path}'.")
        print("Make sure you are in a Jekyll site directory or provide the path with --path.")
        sys.exit(1)
    
    print(f"Serving Jekyll site from '{site_path}'...")
    print("Press Ctrl+C to stop the server.")
    try:
        run_command(f"bundle exec jekyll serve --host {args.host} --port {args.port}", cwd=site_path)
    except KeyboardInterrupt:
        print("\nServer stopped.")

def deploy_site(args):
    """Deploy the Jekyll site to GitHub Pages."""
    site_path = Path(args.path) if args.path else Path.cwd()
    if not (site_path / "_config.yml").exists():
        print(f"Error: No Jekyll site found in '{site_path}'.")
        print("Make sure you are in a Jekyll site directory or provide the path with --path.")
        sys.exit(1)
    
    # Check if we are in a git repository
    if not (site_path / ".git").exists():
        print(f"Error: '{site_path}' is not a git repository.")
        print("Please initialize a git repository and set up a remote for GitHub Pages.")
        sys.exit(1)
    
    print(f"Deploying Jekyll site from '{site_path}' to GitHub Pages...")
    # Build the site first
    build_site_arg = type('Args', (object,), {'path': str(site_path)})()
    build_site(build_site_arg)
    
    # Push to the gh-pages branch (or main if using the new GitHub Pages flow)
    # We'll use the standard approach: push the _site directory to gh-pages
    # Alternatively, we can use the jekyll-gh-pages gem, but we'll keep it simple.
    
    # Check if gh-pages branch exists, if not create it
    try:
        run_command("git rev-parse --verify gh-pages", cwd=site_path)
        run_command("git checkout gh-pages", cwd=site_path)
    except:
        run_command("git checkout --orphan gh-pages", cwd=site_path)
        run_command("git rm -rf .", cwd=site_path)
    
    # Copy the built site to the gh-pages branch
    run_command("cp -r _site/* .", cwd=site_path)
    run_command("touch .nojekyll", cwd=site_path)  # To avoid Jekyll processing on GitHub Pages
    
    # Add and commit
    run_command("git add .", cwd=site_path)
    run_command('git commit -m "Deploy site to GitHub Pages"', cwd=site_path)
    
    # Push to remote
    run_command("git push origin gh-pages --force", cwd=site_path)
    
    # Go back to the original branch
    run_command("git checkout -", cwd=site_path)
    
    print("Site deployed successfully to GitHub Pages.")

def main():
    """Main entry point for the Jekyll Manager CLI."""
    parser = argparse.ArgumentParser(
        description="Jekyll Manager - A tool to manage Jekyll sites.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  jekyll-manager new mysite          # Create a new Jekyll site named 'mysite'
  jekyll-manager build               # Build the Jekyll site in the current directory
  jekyll-manager serve               # Serve the Jekyll site locally
  jekyll-manager deploy              # Deploy the Jekyll site to GitHub Pages
        """
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # New command
    parser_new = subparsers.add_parser("new", help="Create a new Jekyll site")
    parser_new.add_argument("name", help="Name of the new Jekyll site")
    parser_new.set_defaults(func=new_site)
    
    # Build command
    parser_build = subparsers.add_parser("build", help="Build the Jekyll site")
    parser_build.add_argument("--path", help="Path to the Jekyll site (default: current directory)")
    parser_build.set_defaults(func=build_site)
    
    # Serve command
    parser_serve = subparsers.add_parser("serve", help="Serve the Jekyll site locally")
    parser_serve.add_argument("--path", help="Path to the Jekyll site (default: current directory)")
    parser_serve.add_argument("--host", default="localhost", help="Host to bind to (default: localhost)")
    parser_serve.add_argument("--port", type=int, default=4000, help="Port to listen on (default: 4000)")
    parser_serve.set_defaults(func=serve_site)
    
    # Deploy command
    parser_deploy = subparsers.add_parser("deploy", help="Deploy the Jekyll site to GitHub Pages")
    parser_deploy.add_argument("--path", help="Path to the Jekyll site (default: current directory)")
    parser_deploy.set_defaults(func=deploy_site)
    
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
        sys.exit(1)
    
    args.func(args)

if __name__ == "__main__":
    main()