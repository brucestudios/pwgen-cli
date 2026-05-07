#!/usr/bin/env python3
"""
Jekyll Audit Tool
A simple CLI tool to audit Jekyll sites for common issues.
"""

import os
import sys
import argparse
import yaml
from pathlib import Path

def check_front_matter(file_path):
    """Check if a Markdown file has valid YAML front matter."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            return False, "Missing front matter delimiter"
        
        # Find the end of front matter
        parts = content.split('---', 2)
        if len(parts) < 3:
            return False, "Incomplete front matter"
        
        front_matter = parts[1]
        # Try to parse YAML
        yaml.safe_load(front_matter)
        return True, "OK"
    except yaml.YAMLError as e:
        return False, f"Invalid YAML in front matter: {e}"
    except Exception as e:
        return False, f"Error reading file: {e}"

def check_post_directories(posts_dir):
    """Check all posts in the _posts directory."""
    issues = []
    if not os.path.isdir(posts_dir):
        issues.append(f"_posts directory not found: {posts_dir}")
        return issues
    
    for post_file in Path(posts_dir).glob('*.md'):
        valid, message = check_front_matter(post_file)
        if not valid:
            issues.append(f"{post_file.name}: {message}")
    
    return issues

def check_config(config_file='_config.yml'):
    """Check if _config.yml exists and is valid YAML."""
    if not os.path.isfile(config_file):
        return [f"Configuration file not found: {config_file}"]
    
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            yaml.safe_load(f)
        return []
    except yaml.YAMLError as e:
        return [f"Invalid YAML in {config_file}: {e}"]
    except Exception as e:
        return [f"Error reading {config_file}: {e}"]

def main():
    parser = argparse.ArgumentParser(description='Audit a Jekyll site for common issues.')
    parser.add_argument('site_path', nargs='?', default='.', help='Path to the Jekyll site (default: current directory)')
    parser.add_argument('--posts', default='_posts', help='Posts directory relative to site path (default: _posts)')
    parser.add_argument('--config', default='_config.yml', help='Configuration file (default: _config.yml)')
    
    args = parser.parse_args()
    
    site_path = os.path.abspath(args.site_path)
    posts_dir = os.path.join(site_path, args.posts)
    config_file = os.path.join(site_path, args.config)
    
    print(f"Auditing Jekyll site at: {site_path}")
    print("=" * 50)
    
    all_issues = []
    
    # Check config
    config_issues = check_config(config_file)
    if config_issues:
        print("Configuration Issues:")
        for issue in config_issues:
            print(f"  - {issue}")
        all_issues.extend(config_issues)
    else:
        print("Configuration: OK")
    
    # Check posts
    post_issues = check_post_directories(posts_dir)
    if post_issues:
        print("\nPost Issues:")
        for issue in post_issues:
            print(f"  - {issue}")
        all_issues.extend(post_issues)
    else:
        print("\nPosts: OK")
    
    print("=" * 50)
    if all_issues:
        print(f"Found {len(all_issues)} issue(s).")
        sys.exit(1)
    else:
        print("No issues found!")
        sys.exit(0)

if __name__ == '__main__':
    main()