import re
import markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor


class FootnoteExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(FootnotePreprocessor(md), 'footnote', 175)


class FootnotePreprocessor(Preprocessor):
    FOOTNOTE_RE = r'\[\^(\w+)\]'

    def run(self, lines):
        text = "\n".join(lines)
        footnotes = {}
        def replace(match):
            key = match.group(1)
            return f'<sup><a href="#footnote-{key}" id="footnote-ref-{key}">[{key}]</a></sup>'
        text = re.sub(self.FOOTNOTE_RE, replace, text)
        lines = text.split('\n')
        new_lines = []
        footnote_defs = {}
        for line in lines:
            match = re.match(r'\[\^(\w+)\]:(.*)', line)
            if match:
                key = match.group(1)
                content = match.group(2).strip()
                footnote_defs[key] = content
            else:
                new_lines.append(line)
        text = "\n".join(new_lines)
        if footnote_defs:
            text += '\n\n---\n\n## Footnotes\n'
            for key, content in footnote_defs.items():
                text += f'<p id="footnote-{key}"><sup><a href="#footnote-ref-{key}">[{key}]</a></sup> {content}</p>\n'
        return text.split('\n')
