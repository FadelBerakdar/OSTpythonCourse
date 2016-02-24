from tkinter import *

ALL = N+S+W+E

class Application(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self,master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)

        for r in range(5):
            self.rowconfigure(r, weight=1)
            Button(self, text="Row {0}".format(r)).grid(row=r, column=0, sticky=ALL)
        self.rowconfigure(5, weight=1)

        for c in range(5):
            self.columnconfigure(c, weight=1)
            Button(self, text="Col {0}".format(c)).grid(row=5, column=c, sticky=ALL)

        f = Frame(self, bg="red")
        f.grid(row=0, column=1, rowspan = 5, columnspan=4, sticky=ALL)


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()