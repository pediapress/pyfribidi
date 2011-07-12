import os, sys

if sys.platform == 'darwin':
    # Setup sys.path so we can build and test a built version without
    # installing in the system site-packages, which reqire root access.
    builddir = [os.path.join('build', name) for name in os.listdir('build')
                if name.startswith('lib.%s' % sys.platform)]
    sys.path = builddir + sys.path

