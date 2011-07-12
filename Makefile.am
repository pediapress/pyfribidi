EXTRA_DIST = pyfribidi.c pyfribidi.h test_pyfribidi.py time_pyfribidi.py \
	fribidi_systray.py syspath.py \
	autogen.sh setup.py NEWS README AUTHORS ChangeLog

all-am: pyfribidi.so

clean-am:
	rm -f pyfribidi.so
 
pyfribidi.so: pyfribidi.c
	gcc -fpic -shared pyfribidi.c $(PY_CFLAGS) -o pyfribidi.so

install-data-local: pyfribidi.so
	$(mkinstalldirs) $(DESTDIR)$(PY_MODULES_PATH)
	$(INSTALL_DATA) pyfribidi.so $(DESTDIR)$(PY_MODULES_PATH)/pyfribidi.so
