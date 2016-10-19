from tkinter import *

import DataCenter
import UTIL
from Display.WalkScreen import WalkScreen


class MainScreen:
    # constructor
    def __init__(self):
        # Root Configuration
        self.root = Tk()
        self.root.wm_title("BLINK!!! v" + DataCenter.version)
        # Widget Configuration
        self.title = Label(self.root, text="BLINK !!! ", width=15)
        UTIL.decorate_and_pack(UTIL.DECO_MAIN_WIDGET, self.title)
        self.walk = Button(self.root, text="WALK", command=self.run_walk)
        UTIL.decorate_and_pack(UTIL.DECO_MAIN_WIDGET, self.walk)
        self.exit = Button(self.root, text="EXIT", command=self.on_exit)
        UTIL.decorate_and_pack(UTIL.DECO_MAIN_WIDGET, self.exit)
        UTIL.set_window_center(self.root)
        self.root.resizable(width=False, height=False)

    # Destructor
    def __del__(self):
        pass

    def show(self):
        """
        show Main Screen
        """
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
