import re
import markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor


class TaskListExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(TaskListPreprocessor(md), 'tasklist', 175)


class TaskListPreprocessor(Preprocessor):
    TASK_LIST_RE = r'^(\s*)[-*]\s+\[( |x|X)\](\s+.*)$'

    def run(self, lines):
        new_lines = []
        for line in lines:
            match = re.match(self.TASK_LIST_RE, line)
            if match:
                indent = match.group(1)
                checked = match.group(2)
                content = match.group(3)
                html = f'{indent}<li><input type="checkbox" {"checked" if checked.lower() == "x" else ""} disabled>{content}</li>'
                new_lines.append(html)
            else:
                new_lines.append(line)
        return new_lines
