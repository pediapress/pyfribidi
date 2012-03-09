"""simple Python binding for fribidi.

pyfribidi uses libfribidi to order text visually using the unicode
algorithm. pyfribidi can also convert text from visual order to
logical order, but the conversion may be wrong in certain cases.
"""

from _pyfribidi import LTR, ON, RTL, log2vis as _log2vis

def log2vis(logical, base_direction=RTL, encoding="utf-8", clean=False, reordernsm=True):
    """
    Return string reordered visually according to base direction.
    Return the same type of input string, either unicode or string using
    encoding.

    Note that this function does not handle line breaking. You should
    call log2vis with each line.

    Arguments:
    - logical: unicode or encoded string
    - base_direction: optional logical base direction. Accepts one of
      the constants LTR, RTL or ON, defined in this module. ON calculate
      the base direction according to the BiDi algorithm.
    - encoding: optional string encoding (ignored for unicode input)
    """

    if not isinstance(logical, unicode):
        logical = unicode(logical, encoding)
    else:
        encoding = None
    res = _log2vis(logical, base_direction=base_direction, clean=clean, reordernsm=reordernsm)
    if encoding:
        return res.encode(encoding)
    return res
