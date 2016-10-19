MAIN_WIDGET = "MAIN_WIDGET"
WALK_WIDGET = "WALK_WIDGET"
NO_KEY = "NO"


# decorator class.
class Decorator:
    def __init__(self):
        self.key = NO_KEY
        pass

    # widget decorated,
    def decorate(self, widget, key=None):
        if key is None:
            key = self.key
        if key == MAIN_WIDGET:
            widget.configure(background='black', fg='white')
            widget.pack(fil="x")
        elif key == WALK_WIDGET:
            widget.configure(background='black', fg='white')
            widget.pack(fil="x")
        return widget

    def set_key(self, key):
        self.key = key


DECO = Decorator()
