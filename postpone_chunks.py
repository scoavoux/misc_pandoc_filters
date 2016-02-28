#!/usr/bin/env python

from pandocfilters import toJSONFilter, Str, Para, CodeBlock
"""
Developed as an answer to http://stackoverflow.com/questions/
35512308/r-markdown-a-concise-way-to-print-all-code-snippets-
used-in-the-document/

This is a way for rmarkdown to postpone the printing of
every code chunk to the end of the file, as an alternative
to echo=FALSE.
"""


chunks = []


def postpone_chunks(key, value, format, meta):
    if key == 'CodeBlock':
        [[ident, classes, keyvals], code] = value
        if "r" in classes:
            chunks.append(CodeBlock([ident, classes, keyvals], code))
            return Para([Str("")])
        elif code == 'lastchunk':
            return chunks

if __name__ == "__main__":
    toJSONFilter(postpone_chunks)
