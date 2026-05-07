import markdown

def enhance(markdown_text: str) -> str:
    """
    Convert Markdown to HTML with extra extensions.
    """
    extensions = ['extra', 'toc', 'tables']
    return markdown.markdown(markdown_text, extensions=extensions)
