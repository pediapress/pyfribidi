
/*
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
 */

/* Copyright (C) 2005,2006,2010 Yaacov Zamir, Nir Soffer */

/* 	FriBidi python binding:
    
    Install:
	python setup.py install
    
 */

#ifndef __PYFRIBIDI_H__
#define __PYFRIBIDI_H__

static PyObject *_pyfribidi_log2vis (PyObject * self, PyObject * args,
				     PyObject * kw);

static PyObject *log2vis_unicode (PyObject * unicode,
				  FriBidiParType base_direction, int clean, int reordernsm);

static PyObject *log2vis_encoded_string (PyObject * string,
					 const char *encoding,
					 FriBidiParType base_direction, int clean, int reordernsm);

static PyObject *log2vis_utf8 (PyObject * string, int unicode_length,
			       FriBidiParType base_direction, int clean, int reordernsm);

PyMODINIT_FUNC initpyfribidi (void);

PyDoc_STRVAR (_pyfribidi__doc__,
	      "simple Python binding for fribidi.\n\n"
	      "pyfribidi uses libfribidi to order text visually using the unicode\n"
	      "algorithm. pyfribidi can also convert text from visual order to\n"
	      "logical order, but the conversion may be wrong in certain cases.\n");

/* Based on fribidi-0.10.7 README */
PyDoc_STRVAR (_pyfribidi_log2vis__doc__,
	      "log2vis(logical, base_direction=RTL , encoding='utf-8') -> visual\n\n"
	      "Return string reordered visually according to base direction.\n"
	      "Return the same type of input string, either unicode or string using\n"
	      "encoding.\n\n"
	      "Note that this function does not handle line breaking. You should\n"
	      "call log2vis with each line.\n\n"
	      "Arguments:\n\n"
	      "- logical: unicode or encoded string\n"
	      "- base_direction: optional logical base direction. Accepts one of\n"
	      "  the constants LTR, RTL or ON, defined in this module. ON calculate\n"
	      "  the base direction according to the BiDi algorithm.\n"
	      "- encoding: optional string encoding (ignored for unicode input)\n");

#endif /* __PYFRIBIDI_H__ */
