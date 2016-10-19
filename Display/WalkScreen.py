from tkinter import *
from Display.Decorator import *
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
        DECO.set_key(WALK_WIDGET)

        DECO.decorate(Label(self.init, text="please Test Count Max " + str(DataCenter.size()) + " ..."))
        self.count = DECO.decorate(Entry(self.init, ))
        UTIL.limit_number(self.count)
        UTIL.set_text(self.count, str(DataCenter.size()))
        DECO.decorate(Button(self.init, text="START", command=self.show_test))

        # 테스트화면 설정
        DECO.decorate(Label(self.test, text="주어진 텍스트를 입력 하시오."))

        DECO.decorate(Label(self.test, text="WORD : MEAN // COMMENT "))
        DECO.decorate(Label(self.test, text="repeat : TEXT"))
        self.input = DECO.decorate(Entry(self.test))
        self.input.bind("<Return>", self.process_input)
        self.close = DECO.decorate(Button(self.top, text="CLOSE", command=self.ok))
        UTIL.set_window_center(self.top)

        # 값 설정

    # close screen
    def ok(self):
        self.top.destroy()

    # show test screen
    def show_test(self):
        test_count = int(self.count.get())
        print(test_count)
        self.close.pack_forget()
        self.init.pack_forget()
        self.test.pack()
        DECO.decorate(self.close, WALK_WIDGET)
        self.input.focus_set()

    # show walk screen
    def show(self, parent):
        parent.wait_window(self.top)
        pass

    # process input
    def process_input(self, event):
        print(self.input.get())
        self.input.delete(0, END)
