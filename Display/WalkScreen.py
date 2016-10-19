from tkinter import *

import DataCenter
import UTIL


class WalkScreen:
    def __init__(self, parent):
        """ """
        self.top = Toplevel(parent)
        self.top.grab_set()  # make modal


        # 화면 생성.
        self.init = Frame(self.top)
        self.test = Frame(self.top)

        # 첫화면 설정.
        self.init.pack(fill="x")
        UTIL.decorate_and_pack(UTIL.DECO_WALK_WIDGET, Label(self.init, text="please enter ..."))
        UTIL.decorate_and_pack(UTIL.DECO_WALK_WIDGET, Button(self.init, text="START", command=self.show_test))

        # 테스트화면 설정
        UTIL.decorate_and_pack(UTIL.DECO_WALK_WIDGET, Label(self.test, text="주어진 텍스트를 입력 하시오."))
        UTIL.decorate_and_pack(UTIL.DECO_WALK_WIDGET, Label(self.test, text="WORD : MEAN // COMMENT "))
        UTIL.decorate_and_pack(UTIL.DECO_WALK_WIDGET, Label(self.test, text="repeat : TEXT"))
        self.input = Entry(self.test)
        self.input.bind("<Return>", self.process_input)
        UTIL.decorate_and_pack(UTIL.DECO_WALK_WIDGET,self.input)
        self.close = Button(self.top, text="CLOSE", command=self.ok)
        UTIL.set_window_center(self.top)

        #값 설정

    # close screen
    def ok(self):
        self.top.destroy()

    # show test screen
    def show_test(self):
        self.close.pack_forget()
        self.init.pack_forget()
        self.test.pack()
        UTIL.decorate_and_pack(UTIL.DECO_WALK_WIDGET, self.close)
        self.input.focus_set()

    # show walk screen
    def show(self, parent):
        parent.wait_window(self.top)
        pass

    # process input
    def process_input(self, event):
        print(self.input.get())
        self.input.delete(0, END)
