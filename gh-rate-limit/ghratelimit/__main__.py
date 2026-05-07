#!/usr/bin/env python3
"""
gh-rate-limit: A command-line tool to check GitHub API rate limit status.
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone

def get_github_token():
    """
    Get GitHub token from environment variable GITHUB_TOKEN or from gh CLI.
    """
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        return token

    # Try to get token from gh CLI
    try:
        import subprocess
        result = subprocess.run(['gh', 'auth', 'token'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    return None

def fetch_rate_limit(token=None):
    """
    Fetch rate limit information from GitHub API.
    """
    url = "https://api.github.com/rate_limit"
    headers = {}
    if token:
        headers['Authorization'] = f'token {token}'

    req = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))
        return data
    except urllib.error.HTTPError as e:
        if e.code == 401:
            return {"error": "Unauthorized: Invalid or missing GitHub token."}
        elif e.code == 403:
            return {"error": "Forbidden: Possibly rate limited or invalid token."}
        else:
            return {"error": f"HTTP Error {e.code}: {e.reason}"}
    except urllib.error.URLError as e:
        return {"error": f"URL Error: {e.reason}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}

def format_timestamp(ts):
    """
    Format a Unix timestamp to a readable string.
    """
    dt = datetime.fromtimestamp(ts, tz=timezone.utc)
    return dt.strftime('%Y-%m-%d %H:%M:%S UTC')

def main():
    parser = argparse.ArgumentParser(description="Check GitHub API rate limit status.")
    parser.add_argument('--version', action='version', version='gh-rate-limit 1.0.0')
    args = parser.parse_args()

    token = get_github_token()
    data = fetch_rate_limit(token)

    if "error" in data:
        print(f"Error: {data['error']}")
        sys.exit(1)

    print("GitHub API Rate Limit Status")
    print("============================")
    for category in ['core', 'search', 'graphql']:
        if category in data['resources']:
            res = data['resources'][category]
            limit = res['limit']
            remaining = res['remaining']
            reset = format_timestamp(res['reset'])
            # Calculate minutes until reset
            now = datetime.now(timezone.utc).timestamp()
            minutes_left = max(0, (res['reset'] - now) / 60)
            print(f"{category.capitalize():<8}:")
            print(f"   Limit: {limit}")
            print(f"   Remaining: {remaining}")
            print(f"   Reset: {reset} (in {minutes_left:.0f} minutes)")
            print()

if __name__ == '__main__':
    main()