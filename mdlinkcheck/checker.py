"""Link checking functionality for mdlinkcheck."""

from __future__ import annotations

import os
import re
from typing import List, Tuple, Optional
from urllib.parse import urlparse, urljoin

import requests
import mistune


def extract_links_from_markdown(text: str) -> List[str]:
    """Extract all links from Markdown text.
    
    Returns a list of URLs found in the Markdown.
    """
    # Create a markdown renderer
    markdown = mistune.create_markdown(renderer=mistune.AstRenderer())
    tokens = markdown(text)
    
    links = []
    
    def extract_from_tokens(tokens):
        for token in tokens:
            if token['type'] == 'link':
                links.append(token['attrs']['href'])
            if token['type'] == 'image':
                links.append(token['attrs']['src'])
            if 'children' in token:
                extract_from_tokens(token['children'])
    
    extract_from_tokens(tokens)
    return links


def is_http_url(url: str) -> bool:
    """Check if URL is http or https."""
    return url.lower().startswith(('http://', 'https://'))


def is_local_path(url: str) -> bool:
    """Check if URL is a local file path."""
    # Not a URL scheme and not empty
    return not url.startswith(('http://', 'https://', 'mailto:', '#')) and url.strip()


def normalize_path(path: str, base_dir: str) -> str:
    """Normalize a potentially relative path relative to base_dir."""
    if os.path.isabs(path):
        return path
    return os.path.normpath(os.path.join(base_dir, path))


def check_link(
    url: str, 
    base_dir: str, 
    timeout: int = 10, 
    user_agent: str = 'mdlinkcheck/0.1.0',
    ignore_local: bool = False,
    ignore_remote: bool = False
) -> Tuple[bool, Optional[str]]:
    """Check a single link.
    
    Returns (is_valid, error_message)
    """
    # Skip empty links
    if not url or url.strip() == '':
        return True, None
        
    # Skip anchor links
    if url.startswith('#'):
        return True, None
        
    # Skip mailto links
    if url.startswith('mailto:'):
        return True, None
        
    if ignore_remote and is_http_url(url):
        return True, None
        
    if ignore_local and is_local_path(url):
        return True, None
        
    if is_http_url(url):
        try:
            headers = {'User-Agent': user_agent}
            response = requests.head(url, headers=headers, timeout=timeout, allow_redirects=True)
            # Consider 2xx and 3xx as valid (redirects are okay)
            if 200 <= response.status_code < 400:
                return True, None
            else:
                return False, f"HTTP {response.status_code}"
        except requests.exceptions.RequestException as e:
            return False, str(e)
    elif is_local_path(url):
        # Resolve relative to the directory containing the Markdown file
        abs_path = normalize_path(url, base_dir)
        if os.path.exists(abs_path):
            return True, None
        else:
            return False, f"File not found: {abs_path}"
    else:
        # Unknown scheme, treat as valid for now (e.g., maybe it's a custom scheme)
        return True, None


def check_links_in_file(
    file_path: str, 
    timeout: int = 10, 
    user_agent: str = 'mdlinkcheck/0.1.0',
    ignore_local: bool = False,
    ignore_remote: bool = False
) -> Tuple[bool, List[Tuple[str, str]]]:
    """Check all links in a Markdown file.
    
    Returns (all_valid, list_of_broken_links) where each broken link is (link, error)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except OSError as e:
        return False, [(file_path, f"Cannot read file: {e}")]
    
    links = extract_links_from_markdown(content)
    if not links:
        return True, []
    
    base_dir = os.path.dirname(os.path.abspath(file_path))
    broken = []
    
    for link in links:
        valid, error = check_link(
            link, 
            base_dir, 
            timeout=timeout, 
            user_agent=user_agent,
            ignore_local=ignore_local,
            ignore_remote=ignore_remote
        )
        if not valid:
            broken.append((link, error))
    
    return len(broken) == 0, broken


def check_links_in_path(
    path: str, 
    timeout: int = 10, 
    user_agent: str = 'mdlinkcheck/0.1.0',
    ignore_local: bool = False,
    ignore_remote: bool = False
) -> Tuple[bool, List[Tuple[str, str, str]]]:
    """Check all Markdown files in a path (file or directory).
    
    Returns (all_valid, list_of_broken) where each broken is (file_path, link, error)
    """
    if os.path.isfile(path):
        if not path.endswith('.md'):
            return True, []  # Not a Markdown file, skip
        valid, broken = check_links_in_file(
            path, 
            timeout=timeout, 
            user_agent=user_agent,
            ignore_local=ignore_local,
            ignore_remote=ignore_remote
        )
        file_broken = [(path, link, error) for link, error in broken]
        return valid, file_broken
    
    elif os.path.isdir(path):
        all_valid = True
        all_broken = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    valid, broken = check_links_in_file(
                        file_path, 
                        timeout=timeout, 
                        user_agent=user_agent,
                        ignore_local=ignore_local,
                        ignore_remote=ignore_remote
                    )
                    if not valid:
                        all_valid = False
                    for link, error in broken:
                        all_broken.append((file_path, link, error))
        return all_valid, all_broken
    
    else:
        return False, [(path, "", "Path does not exist")]