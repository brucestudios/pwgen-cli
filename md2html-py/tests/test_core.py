import pytest
from md2html import markdown_to_html, parse_front_matter

def test_markdown_to_html():
    assert markdown_to_html("# Hello") == "<h1>Hello</h1>"
    assert markdown_to_html("**bold**") == "<p><strong>bold</strong></p>"
    assert markdown_to_html("- item\n- list") == "<ul>\n<li>item</li>\n<li>list</li>\n</ul>"

def test_parse_front_matter():
    # No front matter
    assert parse_front_matter("# Hello") == ({}, "# Hello")
    
    # With front matter
    content = """---
title: Test
date: 2023-01-01
---
# Hello
"""
    metadata, rest = parse_front_matter(content)
    assert metadata == {"title": "Test", "date": "2023-01-01"}
    assert rest.strip() == "# Hello"
    
    # Malformed front matter (no closing ---)
    assert parse_front_matter("---\ntest: value\n# No closing") == ({}, "---\ntest: value\n# No closing")