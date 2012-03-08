#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
These are very basic tests, because fribidi has its own tests. It may be
better to reuse fribidi own tests, but its not clear what is the value
of base_dir for those tests.
"""

import sys
import unittest
import pyfribidi
from pyfribidi import RTL, LTR, ON


class TestSkipped(Exception):
    """ Raised when test can not run """


class InputTests(unittest.TestCase):

    def testRequireInputString(self):
        """ input: require input string or unicode """
        self.assertRaises(TypeError, pyfribidi.log2vis)
        
    def testInvalidInputString(self):
        """ input: raise TypeError for non string or unicode input """
        self.assertRaises(TypeError, pyfribidi.log2vis, 1)

    def testInvalidDirection(self):
        """ input: raise ValueError for invalid direction """
        self.assertRaises(ValueError, pyfribidi.log2vis, u"שלום",
                          base_direction=1)

    def testUnknownEncoding(self):
        """ input: raise LookupError for invalid encoding """
        self.assertRaises(LookupError, pyfribidi.log2vis, "שלום",
                          encoding='foo')

    def testInvalidEncodedString(self):
        """ input: raise UnicodeError for invalid encoded string """
        self.assertRaises(UnicodeError, pyfribidi.log2vis, "שלום",
                          encoding='iso8859-8')
        
        
class UnicodeTests(unittest.TestCase):

    def testEmpty(self):
        """ unicode: empty string """
        self.assertEqual(pyfribidi.log2vis(u''), u'')

    def testBigString(self):
        """ unicode: big string

        It does not make sense to order such big strings, this just
        checks that there are no size limits in pyfribidi.
        """
        # About 2MB string for default python build (ucs2)
        big = (u'א' * 1024) * 1024
        self.assertEqual(pyfribidi.log2vis(big), big)

    def testDefaultDirection(self):
        """ unicode: use RTL default """
        self.assertEqual(pyfribidi.log2vis(u"hello - שלום"),
                         pyfribidi.log2vis(u"hello - שלום", RTL))

    def testAsRTL(self):
        """ unicode: reorder line as RTL """
        self.assertEqual(pyfribidi.log2vis(u"hello - שלום", RTL),
                         u"םולש - hello")

    def testAsLTR(self):
        """ unicode: reorder line as LTR """
        self.assertEqual(pyfribidi.log2vis(u"hello - שלום", LTR),
                         u"hello - םולש")

    def testNaturalLTR(self):
        """ unicode: reorder LTR line by natural order """
        self.assertEqual(pyfribidi.log2vis(u"hello - שלום", ON),
                         u"hello - םולש")

    def testNaturalRTL(self):
        """ unicode: reorder RTL line by natural order """
        self.assertEqual(pyfribidi.log2vis(u"שלום - hello", ON),
                         u"hello - םולש")

    def testNoReorderNonSpacingMarks(self):
        """unicode: reorder non spacing marks"""
        self.assertEqual(pyfribidi.log2vis(u"חַיְפַא", RTL, reordernsm=False),
                         u"אַפְיַח"
                         )

    def testReorderNonSpacingMarks(self):
        """unicode: reorder non spacing marks"""
        self.assertEqual(pyfribidi.log2vis(u"חַיְפַא", RTL),
                         u"אפַיְחַ"
                         )
                             
    
class UTF8Tests(unittest.TestCase):
    """ Same tests for utf8, used mainly on linux """
    
    def testEmpty(self):
        """ utf8: empty string """
        self.assertEqual(pyfribidi.log2vis(''), '')

    def testBigString(self):
        """ utf8: big string

        It does not make sense to order such big strings, this just
        checks that there are no size limits in pyfribidi.
        """
        # About 2MB string
        big = ('א' * 1024) * 1024
        self.assertEqual(pyfribidi.log2vis(big), big)

    def testDefaultDirection(self):
        """ utf8: use RTL default """
        self.assertEqual(pyfribidi.log2vis("hello - שלום"),
                         pyfribidi.log2vis("hello - שלום", RTL))
    
    def testAsRTL(self):
        """ utf8: reorder line as RTL """
        self.assertEqual(pyfribidi.log2vis("hello - שלום", RTL),
                         "םולש - hello")

    def testAsLTR(self):
        """ utf8: reorder line as LTR """
        self.assertEqual(pyfribidi.log2vis("hello - שלום", LTR),
                         "hello - םולש")
    
    def testNaturalLTR(self):
        """ utf8: reorder LTR line by natural order """
        self.assertEqual(pyfribidi.log2vis("hello - שלום", ON),
                         "hello - םולש")
    
    def testNaturalRTL(self):
        """ utf8: reorder RTL line by natural order """
        self.assertEqual(pyfribidi.log2vis("שלום - hello", ON),
                         "hello - םולש")


    def testNoReorderNonSpacingMarks(self):
        """utf8: reorder non spacing marks"""
        self.assertEqual(pyfribidi.log2vis("חַיְפַא", RTL, reordernsm=False),
                         "אַפְיַח"
                         )

    def testReorderNonSpacingMarks(self):
        """unicode: reorder non spacing marks"""
        self.assertEqual(pyfribidi.log2vis("חַיְפַא", RTL),
                         "אפַיְחַ"
                         )


class OtherEncodingsTests(unittest.TestCase):
    """ Minimal tests for other encodings """
    
    def testIso8859_8NaturalRTL(self):
        """ other encodings: iso8859-8 """
        charset = 'iso8859-8'
        self.assertEqual(pyfribidi.log2vis(u"שלום - hello".encode(charset),
                                           encoding=charset),
                         u"hello - םולש".encode(charset))
    
    def testCp1255NaturalRTL(self):
        """ other encodings: cp1255 """
        charset = 'cp1255'
        self.assertEqual(pyfribidi.log2vis(u"שלום - hello".encode(charset),
                                           encoding=charset),
                         u"hello - םולש".encode(charset))

    def testUTF16NaturalRTL(self):
        """ other encodings: utf-16 """
        charset = 'utf-16'
        self.assertEqual(pyfribidi.log2vis(u"שלום - hello".encode(charset),
                                           encoding=charset),
                         u"hello - םולש".encode(charset))

class Crasher(unittest.TestCase):
    def test_glibc_free_invalid_next_size(self):
        # *** glibc detected *** /home/ralf/py27/bin/python2: free(): invalid next size (fast): 0x00000000011cff00 ***
        pyfribidi.log2vis('\xf0\x90\x8e\xa2\xf0\x90\x8e\xaf\xf0\x90\x8e\xb4\xf0\x90\x8e\xa1\xf0\x90\x8f\x83')

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromName(__name__)
    res = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not res.wasSuccessful())
