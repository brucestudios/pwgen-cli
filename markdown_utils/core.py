def extract_headers(markdown_text):
    """
    Extract headers from Markdown text.
    Returns a list of tuples (header_marker, header_text).
    """
    import re
    pattern = r'^(#{1,6})\s+(.+)$'
    headers = []
    for line in markdown_text.split('\n'):
        match = re.match(pattern, line)
        if match:
            headers.append((match.group(1), match.group(2)))
    return headers

def markdown_to_text(markdown_text):
    """
    Convert Markdown to plain text by removing Markdown syntax.
    This is a very basic implementation.
    """
    import re
    # Remove headers
    text = re.sub(r'#{1,6}\s+', '', markdown_text)
    # Remove emphasis (bold, italic) but keep the text
    text = re.sub(r'(\*\*|__)(.*?)\1', r'\2', text)
    text = re.sub(r'(\*|_)(.*?)\1', r'\2', text)
    # Remove links but keep the text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Remove images
    text = re.sub(r'!\[[^\]]*\]\([^\)]+\)', '', text)
    # Remove inline code
    text = re.sub(r'`([^`]+)`', r'\1', text)
    # Remove horizontal rules
    text = re.sub(r'^(\*\s*\-?\s*){3,}$', '', text, flags=re.MULTILINE)
    # Remove blockquotes
    text = re.sub(r'^\s*>+', '', text, flags=re.MULTILINE)
    # Remove list markers
    text = re.sub(r'^\s*[\*\-\+]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*\d+\.\s+', '', text, flags=re.MULTILINE)
    # Remove extra whitespace
    text = '\n'.join(line.strip() for line in text.split('\n') if line.strip())
    return text
