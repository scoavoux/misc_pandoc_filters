#!/usr/bin/env python

import pandocfilters as pf
from pandocfunctions import unchanged_inline
"""
This filter includes a Cite immediatly after
a Quoted element in this element. It is useful
In conjunction with remove_spaces_before_cite()
to respect the French usage of having footnotes
call inside quotes rather than outside.

    "This needs proof"[@ref]

thus becomes:

    "This needs proof[@ref]"
"""

q = []
qt = False


def include_cite_in_quote(k, v, f, m):
    global q
    global qt
    if k == "Cite" and qt:
        qt = False
        q[1].append(pf.Cite(v[0], v[1]))
        return pf.Quoted(q[0], q[1])
    elif k == "Quoted":
        qt = True
        q = v
        return []
    elif qt:
        qt = False
        return [pf.Quoted(q[0], q[1]), unchanged_inline(k, v, f, m)]

if __name__ == "__main__":
    pf.toJSONFilter(include_cite_in_quote)
