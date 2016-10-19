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


def decorate_and_pack(style, widget):
    if style == DECO_MAIN_WIDGET:
        widget.configure(background='black', fg='white')
        widget.pack(fil="x")
    elif style == DECO_WALK_WIDGET:
        widget.configure(background='black', fg='white')
        widget.pack(fil="x")