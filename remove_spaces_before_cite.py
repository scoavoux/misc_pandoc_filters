#!/usr/bin/env python
import pandocfilters as pf
from pandocfunctions import unchanged_inline
"""
This filter removes all spaces that precede a
cite element. It is useful for footnote cites
when one wants to keep the cites separated from
the rest of the text in markdown.

    This needs proof [@ref]

thus becomes:

    This needs proof[@ref]
"""

qt = False


def remove_spaces_before_cite(k, v, f, m):
    global qt
    if k == "Cite" and qt:
        qt = False
    elif k == "Space":
        qt = True
        return []
    elif qt:
        qt = False
        return [pf.Space(), unchanged_inline(k, v, f, m)]

if __name__ == "__main__":
    pf.toJSONFilter(remove_spaces_before_cite)
