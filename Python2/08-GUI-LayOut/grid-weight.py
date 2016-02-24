__author__ = 'Fadel'
from tkinter import *

def colorgen():
    while True:
        yield "red"
        yield "blue"


class Application(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)  # this three lines very important
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=W+E+N+S)
        colors = colorgen()

        rcount = 0
        for r in (1, 22, 333):
            self.rowconfigure(r, weight=rcount)
            rcount += 1
            ccount = 0
            for c in (1, 22, 333):
                self.columnconfigure(c, weight=ccount)
                ccount += 1
                text = "Item {0} {1}".format(r, c)
                l = Label(self, text=text, bg=next(colors))
                l.grid(row=r, column=c, sticky=E+W+S+N)

    def create_widgets(self):
        pass


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
