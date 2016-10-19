from tkinter import Entry, Label, StringVar


def set_window_center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w / 2 - size[0] / 2
    y = h / 2 - size[1] / 2
    # toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
    toplevel.geometry("+%d+%d" % (x, y))


# entry text clear.
def clear_entry(entry):
    from tkinter import END
    entry.delete(0, END)


# entry clear and insert in 0.
def set_text(target, text):
    if isinstance(target, Entry):
        clear_entry(target)
        target.insert(0, text)
    elif isinstance(target, Label):
        target.config(text=text)


# internal use. sv callback.
def callback(sv):
    string = sv.get();
    if string.isdigit():
        sv.set(string)
        return
    re = ""
    for c in string:
        if c.isdigit():
            re += c
    sv.set(re)


# entry limit number.
def limit_number(entry):
    if isinstance(entry, Entry):
        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
        entry.configure(textvariable=sv)
