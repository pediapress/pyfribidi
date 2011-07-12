#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
import os

def _getpkgconfigvalue(value, package="fribidi"):
	""" get a value from pkg-config for package (default: fribidi)
	    param value: long-option to pkg-config
	"""
	f = os.popen("pkg-config --%s %s" % (value, package))
	x = f.readline().strip()
	f.close()

	# generators: 2.4+ only :(
	#return list(y[2:] for y in x.split(" "))

	l = []
	for y in x.split(" "):
		l.append(y[2:])
	return l

setup (name = "pyfribidi",
        version = "0.10.0",
        description = "Python libfribidi interface",
        author = "Yaacov Zamir, Nir Soffer",
        author_email = "kzamir@walla.co.il",
        url = "http://hspell-gui.sourceforge.net/pyfribidi.html",
        license = "GPL",

        ext_modules = [ Extension(
                name = 'pyfribidi',
                sources = ['pyfribidi.c'],
                libraries = _getpkgconfigvalue("libs-only-l"),
                include_dirs = _getpkgconfigvalue("cflags-only-I")
        )]
)
