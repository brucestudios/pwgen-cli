import unittest
from markdown_utils.core import extract_headers, markdown_to_text

class TestCore(unittest.TestCase):
    def test_extract_headers(self):
        markdown = """
# Title
## Section 1
### Subsection
## Section 2
"""
        expected = [('#', 'Title'), ('##', 'Section 1'), ('###', 'Subsection'), ('##', 'Section 2')]
        self.assertEqual(extract_headers(markdown), expected)

    def test_markdown_to_text(self):
        markdown = """
# Title
## Section 1
### Subsection
## Section 2
**bold** and *italic*
[link](http://example.com)
![image](image.jpg)
`code`
> blockquote
- list item
1. ordered list
---
"""
        # We are doing a very basic conversion, so we just check that the function runs and returns a string.
        result = markdown_to_text(markdown)
        self.assertIsInstance(result, str)
        # We can check for some expected removals
        self.assertNotIn('#', result)
        self.assertNotIn('**', result)
        self.assertNotIn('*', result)
        self.assertNotIn('[link]', result)  # Actually, the link text should remain, so let's adjust.
        # The link text should remain, so we check for the text without the link.
        self.assertIn('link', result)
        self.assertNotIn('http://example.com', result)
        self.assertNotIn('![image]', result)
        self.assertNotIn('`code`', result)
        self.assertNotIn('>', result)
        self.assertNotIn('-', result)
        self.assertNotIn('1.', result)
        self.assertNotIn('---', result)

if __name__ == '__main__':
    unittest.main()
