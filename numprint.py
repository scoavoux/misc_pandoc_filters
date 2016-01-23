#!/usr/bin/env python

"""
Pandoc filter to convert numprints in latex documents
Usage to convert from latex to another format (it
is very important that you compile in two steps)

pandoc $latex_input -f markdown -t latex | pandoc -o output_file
"""

from pandocfilters import toJSONFilter, Str
import locale
import re

locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')
npreg = re.compile("\\\\numprint{(\d+)}")


def numprint(key, value, format, meta):
    if key == 'RawInline':
        [t, contents] = value
        r = npreg.match(contents)
        if r:
            f = locale.format("%d", float(r.group(1)), grouping=True)
            return(Str(f))

if __name__ == "__main__":
    toJSONFilter(numprint)
