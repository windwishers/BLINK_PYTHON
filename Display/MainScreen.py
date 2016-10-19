from tkinter import *

import DataCenter
import UTIL
from Control import Loader
from Display.Decorator import *
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
        DECO.set_key(MAIN_WIDGET)
        self.title = DECO.decorate(Label(self.root, text="BLINK !!! ", width=20))
        self.notification = DECO.decorate(Label(self.root, text="", width=20))
        self.walk = DECO.decorate(Button(self.root, text="WALK", command=self.run_walk, state=DISABLED))
        self.exit = DECO.decorate(Button(self.root, text="EXIT", command=self.on_exit, state=DISABLED))

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
