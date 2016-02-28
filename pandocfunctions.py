#!/usr/bin/env python
import pandocfilters as pf


def unchanged_inline(k, v, f, m):
    if k == "Space":
        return pf.Space()
    elif k == "SoftBreak":
        return pf.SoftBreak()
    elif k == "LineBreak":
        return pf.LineBreak()
    # One element
    elif k == "Str":
        return pf.Str(v)
    elif k == "Emph":
        return pf.Emph(v)
    elif k == "Strong":
        return pf.Strong(v)
    elif k == "Strikeout":
        return pf.Strikeout(v)
    elif k == "Superscript":
        return pf.Superscript(v)
    elif k == "Subscript":
        return pf.Subscript(v)
    elif k == "SmallCaps":
        return pf.SmallCaps(v)
    elif k == "Note":
        return pf.Note(v)
    # Two elements
    elif k == "Quoted":
        return pf.Quoted(v[0], v[1])
    elif k == "Cite":
        return pf.Cite(v[0], v[1])
    elif k == "Code":
        return pf.Code(v[0], v[1])
    elif k == "Math":
        return pf.Math(v[0], v[1])
    elif k == "RawInline":
        return pf.RawInline(v[0], v[1])
    elif k == "Span":
        return pf.Span(v[0], v[1])
    # Three elements
    elif k == "Link":
        return pf.Link(v[0], v[1], v[2])
    elif k == "Image":
        return pf.Image(v[0], v[1], v[2])

