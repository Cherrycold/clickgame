# -*- coding:UTF-8 -*-
from tkinter import *
from tkinter import filedialog, messagebox, scrolledtext
from tkinter.ttk import Scrollbar, Checkbutton, Label, Button
import os

import logmgr
import paint
import logic

_version = "0.0.1"


class MainInterface(object):
    def __init__(self):
        self.app = self.createMain()
        self.display = self.createDisplay()
        self.logmgr = logmgr.logmgr(self.display)
        self.logic = logic.gamelogic(self.app, self.logmgr)
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

    def createDisplay(self):
        display = scrolledtext.ScrolledText(
            self.app, width=70, height=13)  #滚动文本框（宽，高（这里的高应该是以行数为单位），字体样式）
        display.grid(row=20, column=0, columnspan=10)
        return display


main = MainInterface()