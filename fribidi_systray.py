#!/usr/bin/python
# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

# Copyright (C) 2005, 2010 Yaacov Zamir

import gtk
import egg.trayicon
import pyfribidi

clip = gtk.Clipboard()
button = gtk.Button("BD")
trayIcon = egg.trayicon.TrayIcon("BiDiTrayIcon")

def on_button_clicked(obj):
	inText = clip.wait_for_text()
	outText = pyfribidi.log2vis (inText, pyfribidi.ON)
	clip.set_text(outText)

button.connect("clicked", on_button_clicked)
trayIcon.add(button)
trayIcon.show_all()

gtk.main()
