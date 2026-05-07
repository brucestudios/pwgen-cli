import markdown
from markdown_utils.extensions.footnote import FootnoteExtension

def test_footnote_basic():
    text = """
This is some text with a footnote.[^1]

[^1]: This is the footnote content.
"""
    md = markdown.Markdown(extensions=[FootnoteExtension()])
    html = md.convert(text)
    # We expect a sup tag with a link and the footnote at the end.
    assert '<sup><a href="#footnote-1" id="footnote-ref-1">[1]</a></sup>' in html
    assert '<p id="footnote-1"><sup><a href="#footnote-ref-1">[1]</a></sup> This is the footnote content.</p>' in html

if __name__ == "__main__":
    test_footnote_basic()
    print("All tests passed!")
