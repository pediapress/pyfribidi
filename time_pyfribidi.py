#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
time pyfribidi with all hebrew encodings.
"""

import syspath
import timeit
import pyfribidi

hebrew_encodings = ['unicode', 'utf-8', 'utf-16', 'iso8859-8', 'cp1255']

def timeEncoding(encoding, tests):

    setup="""
import pyfribidi
text = 'Hello - שלום, hello - שלום, hello - שלום, hello - שלום, hello - שלום.'
text = text.decode('utf-8')
if '%(encoding)s' != 'unicode':
    text = text.encode('%(encoding)s')
""" % locals()
    
    if encoding in ['unicode', 'utf-8']:
        # utf-8 is the default encoding for strings
        code = "pyfribidi.log2vis(text)"
    else:
        # other encodings require encoding parameter
        code = "pyfribidi.log2vis(text, encoding='%s')" % encoding

    timer = timeit.Timer(code, setup)
    seconds = timer.timeit(number=tests)
    microseconds = 1000000 * seconds / tests
    print "%12s: %.8f seconds (%.2f usec/pass)" % (encoding, seconds,
                                                   microseconds)

    
# warm up caches
for i in xrange(100000):
    pyfribidi.log2vis(u'Some text to warm up the caches')

lines = 50 # typical screen of text
print
print 'time to rerorder %s lines:' % lines
print
for encoding in hebrew_encodings:
    timeEncoding(encoding, lines)

lines = 100000 
print
print 'time to rerorder %s lines:' % lines
print
for encoding in hebrew_encodings:
    timeEncoding(encoding, lines)
