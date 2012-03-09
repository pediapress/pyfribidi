#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
from distutils.command import build_ext

import os

USE_SYSTEM_LIB = False

if not os.path.exists("fribidi-src"):
    USE_SYSTEM_LIB = True

if os.environ.get("USE_SYSTEM_LIB", "False").lower() in ("yes", "1", "true"):
    USE_SYSTEM_LIB = True


class my_build_ext(build_ext.build_ext):
    def build_extension(self, ext):
        configure = os.path.abspath("fribidi-src/configure")
        bdir = os.path.join(self.build_temp, "fribidi")
        if not os.path.isdir(bdir):
            os.makedirs(bdir)
        cwd = os.getcwd()
        os.chdir(bdir)
        try:
            if not os.path.exists("./config.status"):
                os.system("sh %s --with-glib=no" % configure)
        finally:
            os.chdir(cwd)

        self.include_dirs[:0] = [bdir, "%s/lib" % bdir]
        self.compiler.set_include_dirs(self.include_dirs)

        return build_ext.build_ext.build_extension(self, ext)


def _getpkgconfigvalue(value, package="fribidi"):
    """ get a value from pkg-config for package (default: fribidi)
    param value: long-option to pkg-config
    """
    f = os.popen("pkg-config --%s %s" % (value, package))
    x = f.readline().strip()
    f.close()

    l = []
    for y in x.split(" "):
        l.append(y[2:])
    return l

if USE_SYSTEM_LIB:
    lib_sources = []
    include_dirs = _getpkgconfigvalue("cflags-only-I") or ["/usr/include/fribidi"]
    libraries = _getpkgconfigvalue("libs-only-l") or ["fribidi"]
    define_macros = []
    my_build_ext = build_ext.build_ext
else:
        lib_sources = """
fribidi-src/lib/fribidi.c
fribidi-src/lib/fribidi-arabic.c
fribidi-src/lib/fribidi-bidi.c
fribidi-src/lib/fribidi-bidi-types.c
fribidi-src/lib/fribidi-deprecated.c
fribidi-src/lib/fribidi-joining.c
fribidi-src/lib/fribidi-joining-types.c
fribidi-src/lib/fribidi-mem.c
fribidi-src/lib/fribidi-mirroring.c
fribidi-src/lib/fribidi-run.c
fribidi-src/lib/fribidi-shape.c
fribidi-src/charset/fribidi-char-sets-cp1256.c
fribidi-src/charset/fribidi-char-sets-iso8859-8.c
fribidi-src/charset/fribidi-char-sets-cap-rtl.c
fribidi-src/charset/fribidi-char-sets-utf8.c
fribidi-src/charset/fribidi-char-sets.c
fribidi-src/charset/fribidi-char-sets-cp1255.c
fribidi-src/charset/fribidi-char-sets-iso8859-6.c
""".split()
        libraries = []
        include_dirs = ["fribidi-src", "fribidi-src/lib", "fribidi-src/charset"]
        define_macros = [("HAVE_CONFIG_H", 1)]


def read_long_description():
    fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.rst")
    return open(fn).read()


setup(name="pyfribidi",
      version="0.10.1",
      description="Python libfribidi interface",
      author="Yaacov Zamir, Nir Soffer",
      author_email="kzamir@walla.co.il",
      url="http://hspell-gui.sourceforge.net/pyfribidi.html",
      license="GPL",
      cmdclass={'build_ext': my_build_ext},
      long_description=read_long_description(),
      py_modules=["pyfribidi", "pyfribidi2"],
      ext_modules=[Extension(
            name='_pyfribidi',
            sources=['pyfribidi.c'] + lib_sources,
            define_macros=define_macros,
            libraries=libraries,
            include_dirs=include_dirs)])
