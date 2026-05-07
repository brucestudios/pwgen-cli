"""
String utility functions.
"""

def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word in the text.
    
    Args:
        text: The input string.
        
    Returns:
        A string with each word capitalized.
    """
    return ' '.join(word.capitalize() for word in text.split())

def snake_to_camel(text: str) -> str:
    """Convert snake_case string to camelCase.
    
    Args:
        text: The snake_case string.
        
    Returns:
        A string in camelCase.
    """
    components = text.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def camel_to_snake(text: str) -> str:
    """Convert camelCase string to snake_case.
    
    Args:
        text: The camelCase string.
        
    Returns:
        A string in snake_case.
    """
    import re
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def truncate(text: str, length: int) -> str:
    """Truncate text to the specified length, adding '...' if truncated.
    
    Args:
        text: The input string.
        length: The maximum length of the returned string.
        
    Returns:
        The truncated string.
    """
    if len(text) <= length:
        return text
    return text[:length-3] + '...'

def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug.
    
    Args:
        text: The input string.
        
    Returns:
        A slugified string.
    """
    import re
    # Convert to lowercase and replace non-alphanumeric characters with hyphens
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    # Remove leading/trailing hyphens
    text = text.strip('-')
    return text