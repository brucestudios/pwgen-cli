import markdown
import yaml
from typing import Tuple, Dict, Any

def markdown_to_html(text: str) -> str:
    """
    Convert Markdown string to HTML.
    
    Args:
        text: Markdown text
        
    Returns:
        HTML string
    """
    return markdown.markdown(
        text,
        extensions=['extra', 'codehilite', 'tables', 'toc']
    )

def parse_front_matter(text: str) -> Tuple[Dict[str, Any], str]:
    """
    Parse YAML front matter from Markdown text.
    
    Expected format:
    ---
    key: value
    ---
    # Content
    
    Returns:
        Tuple of (metadata_dict, content_without_front_matter)
    """
    if not text.startswith('---'):
        return {}, text
    
    # Find the end of front matter
    parts = text.split('---', 2)
    if len(parts) < 3:
        return {}, text
    
    # parts[0] is empty (before first ---)
    # parts[1] is the front matter
    # parts[2] is the rest
    try:
        metadata = yaml.safe_load(parts[1]) or {}
        if not isinstance(metadata, dict):
            metadata = {}
    except yaml.YAMLError:
        metadata = {}
    
    content = parts[2].lstrip('\n')
    return metadata, content