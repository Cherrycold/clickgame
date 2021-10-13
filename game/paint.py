# -*- coding:UTF-8 -*-
from tkinter import *
from tkinter import filedialog, messagebox, scrolledtext
from tkinter.ttk import Scrollbar, Checkbutton, Label, Button
import os


def OnCreateButton(base, text, row, column, callback):
    bt = Button(base, text=text, command=callback)
    bt.grid(row=row, column=column)
    return bt


def OnCreateLabel(base, text, row, column):
    bt = Label(base, text=text)
    bt.grid(row=row, column=column)
    return bt


def DeleteControl(control):
    control.destory()