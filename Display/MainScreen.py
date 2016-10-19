from tkinter import *

import DataCenter
import UTIL
from Control import Loader
from Display.WalkScreen import WalkScreen


class MainScreen:
    # constructor
    def __init__(self):
        # Root Configuration
        self.loader = Loader.LoadingCsv(end=self.end_loading)
        self.root = Tk()
        self.root.protocol('WM_DELETE_WINDOW', self.on_close)
        self.root.wm_title("BLINK!!! v" + DataCenter.version)
        # Widget Configuration
        self.title = Label(self.root, text="BLINK !!! ", width=20)
        UTIL.decorate_and_pack(UTIL.DECO_MAIN_WIDGET, self.title)
        self.notification = Label(self.root, text="", width=20)
        UTIL.decorate_and_pack(UTIL.DECO_MAIN_WIDGET, self.notification)
        self.walk = Button(self.root, text="WALK", command=self.run_walk, state=DISABLED)
        UTIL.decorate_and_pack(UTIL.DECO_MAIN_WIDGET, self.walk)
        self.exit = Button(self.root, text="EXIT", command=self.on_exit, state=DISABLED)
        UTIL.decorate_and_pack(UTIL.DECO_MAIN_WIDGET, self.exit)
        UTIL.set_window_center(self.root)
        self.root.resizable(width=False, height=False)

    # Destructor
    def __del__(self):
        pass

    def on_close(self):
        if not self.loader.is_alive():
            self.root.destroy()


    def end_loading(self):
        UTIL.set_text(self.notification, "loading complete")
        self.walk.config(state=NORMAL)
        self.exit.config(state=NORMAL)

    def show(self):
        """
        show Main Screen
        """
        UTIL.set_text(self.notification, "loading csv")
        self.loader.start()
        self.root.mainloop()
        pass

    # close mainScreen
    def on_exit(self):
        self.root.destroy()

    # open walk.
    def run_walk(self):
        walk = WalkScreen(self.root)
        walk.show(self.root)
        pass


if __name__ == '__main__':
    main = MainScreen()

    main.show()
