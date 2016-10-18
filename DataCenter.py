from model.Word import *


# noinspection PyAttributeOutsideInit
class DataCenter(object):
    __instance = None

    def __new__(cls, val):
        if DataCenter.__instance is None:
            DataCenter.__instance = object.__new__(cls)
        DataCenter.__instance = val
        DataCenter.__instance.init()
        return DataCenter.__instance

    def init(self):
        self.__word_list = []
        pass

    def load(self):
        self.__word_list.append(Word("WORD1", "MEAN1"))
        pass


class UTIL:

    @staticmethod
    def set_window_center(toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w / 2 - size[0] / 2
        y = h / 2 - size[1] / 2
        # toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
        toplevel.geometry("+%d+%d" % (x, y))

    DECO_MAIN_WIDGET = "DECO_MAIN_WIDGET"
    DECO_WALK_WIDGET = "DECO_MAIN_WIDGET"

    @staticmethod
    def decorate_and_pack(style, widget):
        if style == UTIL.DECO_MAIN_WIDGET:
            widget.configure(background='black', fg='white')
            widget.pack(fil="x")
        elif style == UTIL.DECO_WALK_WIDGET:
            widget.configure(background='black', fg='white')
            widget.pack(fil="x")

