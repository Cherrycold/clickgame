# -*- coding:UTF-8 -*-
import time
from tkinter import messagebox


class logmgr(object):
    def __init__(self, text):
        # rootpath = os.path.abspath(os.path.dirname(os.getcwd()))
        # folder = os.path.exists(rootpath + "/log")
        # if not folder:
        #     os.makedirs(rootpath + "/log")
        # filename = rootpath + "/log/" + time.strftime("%m_%d_%H",
        #                                               time.localtime())
        # self.file = open(filename, 'w')
        self.text = text

    def logout(self, outstr):
        log = "[ " + time.strftime("%Y-%m-%d %H:%M:%S",
                                   time.localtime()) + " ] : " + outstr + "\n"
        # self.file.write(log)
        # self.file.flush()
        self.text.insert('end', log)
        self.text.update()
        return log

    def loginfo(self, msg):
        messagebox.showinfo("info !", msg)

    def logwarn(self, msg):
        messagebox.showwarn("warn !", msg)

    def logerror(self, msg):
        messagebox.showerror("error !", msg)


# return logmgr