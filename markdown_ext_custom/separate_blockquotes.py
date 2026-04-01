"""
Markdown extension that prevents consecutive blockquotes from being merged.

By default, Python-Markdown merges two blockquotes separated by a blank line
into a single <blockquote>. This preprocessor inserts an HTML comment between
them so they render as distinct elements.
"""

import re

from markdown import Extension
from markdown.preprocessors import Preprocessor

BLOCKQUOTE_RE = re.compile(r"^[ ]{0,3}>")


class SeparateBlockquotesPreprocessor(Preprocessor):
    def run(self, lines):
        result = []
        i = 0
        while i < len(lines):
            result.append(lines[i])
            if BLOCKQUOTE_RE.match(lines[i]):
                # Scan ahead past any blank lines
                j = i + 1
                while j < len(lines) and lines[j].strip() == "":
                    j += 1
                # If blank lines were skipped and the next content is also a
                # blockquote, insert a separator comment to break the merge.
                if j > i + 1 and j < len(lines) and BLOCKQUOTE_RE.match(lines[j]):
                    result.append("")
                    result.append("<!-- -->")
                    result.append("")
                    i = j - 1  # resume just before the next blockquote
            i += 1
        return result


class SeparateBlockquotesExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(
            SeparateBlockquotesPreprocessor(md),
            "separate_blockquotes",
            25,  # after normalize_whitespace (30), before html_block (20)
        )


def makeExtension(**kwargs):
    return SeparateBlockquotesExtension(**kwargs)
