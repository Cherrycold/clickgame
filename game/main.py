from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Scrollbar, Checkbutton, Label, Button
import os

_version = "0.0.1"


class MainInterface(object):
    def __init__(self):
        self.app = self.createMain()
        self.app.mainloop()

    def createMain(self):
        app = Tk()
        sw = app.winfo_screenwidth()
        sh = app.winfo_screenheight()
        ww = 500
        wh = 500
        x = (sw - ww) / 2
        y = (sh - wh) / 2

        app.title("修仙模拟器 v." + _version)
        app.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        return app


main = MainInterface()