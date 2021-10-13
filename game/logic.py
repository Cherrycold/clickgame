# -*- coding:UTF-8 -*-
import paint
import os


class gamelogic(object):
    def __init__(self, parent, logmgr) -> None:
        super().__init__()
        self.parent = parent
        self.logmgr = logmgr
        self.createButton()
        self.tesoutput()

    def createButton(self):
        for i in range(5):
            paint.OnCreateButton(
                self.parent,
                "我是按钮" + str(i),
                i,
                i,
                None,
            )
            paint.OnCreateLabel(self.parent, None, i + 5, i)

    def tesoutput(self):
        self.logmgr.logout("测试")