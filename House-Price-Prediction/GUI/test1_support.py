#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.11
# In conjunction with Tcl version 8.6
#    Mar 21, 2018 01:33:08 AM
#    Mar 21, 2018 08:55:02 AM
#    Mar 21, 2018 09:12:19 AM
#    Mar 21, 2018 09:38:42 AM


import sys
import test1

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
def set_Tk_var():
    global v
    v = StringVar()
    py3 = True


def getVals():
    print('test1_support.getVals')
    sys.stdout.flush()



def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    test1.vp_start_gui()











