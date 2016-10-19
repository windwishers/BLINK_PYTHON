from tkinter import *
from Display.Decorator import *
import DataCenter
import UTIL

NO_TEST = 0
REQUEST_WORD = 1
REQUEST_MEAN = 2
TEST_COMPLETE = 3

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

        self.word_string = DECO.decorate(Label(self.test, text="WORD : MEAN // COMMENT "))
        self.request = DECO.decorate(Label(self.test, text="repeat : TEXT"))
        self.input = DECO.decorate(Entry(self.test))
        self.input.bind("<Return>", self.process_input)
        self.close = DECO.decorate(Button(self.top, text="CLOSE", command=self.ok))
        UTIL.set_window_center(self.top)

        # 값 설정
        self.word_list = []
        self.test_index = 0

        self.state = NO_TEST

    # close screen
    def ok(self):
        self.top.destroy()

    # show test screen
    def show_test(self):
        # 테스트 세팅
        test_count = int(self.count.get())
        self.word_list = DataCenter.get_ran_list(length=test_count)
        self.test_index = 0
        self.state = REQUEST_WORD
        self.display_test(0)


        # 화면 설정.
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
        if self.state == TEST_COMPLETE:
            self.top.destroy()
            return
        input_string = self.input.get()
        word = self.word_list[self.test_index];
        if self.state == REQUEST_WORD and word.word == input_string:
            self.state = REQUEST_MEAN
            self.display_test(self.test_index)
        elif self.state == REQUEST_MEAN and word.mean == input_string:
            self.state = REQUEST_WORD
            self.test_index += 1
            self.display_test(self.test_index)

        self.input.delete(0, END)

    # set test string.
    def display_test(self, index = None):
        if index is None:
            index = self.test_index

        if index >= self.word_list.__len__():
            UTIL.set_text(self.request, " Test Complete , please enter.")
            self.state = TEST_COMPLETE
            return

        word = self.word_list[index]
        UTIL.set_text(self.word_string,word)
        if self.state == REQUEST_WORD:
            UTIL.set_text(self.request, "input : "+word.word)
        elif self.state == REQUEST_MEAN:
            UTIL.set_text(self.request, "input : " + word.mean)
        else:
            UTIL.set_text(self.request, "what;s wrong???? ")
