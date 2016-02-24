#!/usr/bin/env python3
#                        GUI-based module
#                            final.py
# By: Fadel Berakdar
# Date: 27/7/2015

from tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1, minsize=500)
        self.master.columnconfigure(0, weight=1, minsize=700)
        self.grid(sticky=N+S+W+E)

        # Background Buttons:
        for r in range(5):
            self.rowconfigure(r, weight=1)
            Button(self, text="Row {0}".format(r)).grid(row=r, column=0,
                                                        sticky=N+S+W+E)
        # Buttons:
        self.rowconfigure(5, weight=0)
        for c in range(5):
            self.columnconfigure(c, weight=1)
        # Red Button:
        self.red = Button(self, text=" Red ", command=self.handler_red)
        self.red.grid(row=6, column=0, sticky=E+W)
        # Blue Button:
        self.blue = Button(self, text=" Blue", command=self.handler_blue)
        self.blue.grid(row=6, column=1, sticky=E+W)
        # Green Button:
        self.green = Button(self, text="Green", command=self.handler_green)
        self.green.grid(row=6, column=2, sticky=E+W)
        # Black Button:
        self.black = Button(self, text="Black", command=self.handler_black)
        self.black.grid(row=6, column=3, sticky=E+W)
        # Open Button:
        self.open = Button(self, text=" Open", command=self.handler_open)
        self.open.grid(row=6, column=4, sticky=E+W)

        # Frame1:
        self.frame1 = LabelFrame(self, text="Frame 1", relief=SOLID)
        self.frame1.bind("<Button-1>", self.handler1)
        self.frame1.grid(row=0, column=0, rowspan=3, columnspan=2,
                         sticky=N+S+W+E, padx=1, pady=1)
        # Frame2:
        self.frame2 = LabelFrame(self, text="Frame 2", relief=SOLID)
        self.frame2.bind("<Button-1>", self.handler2)
        self.frame2.grid(row=3, column=0, rowspan=3, columnspan=2,
                         sticky=N+S+W+E, padx=1, pady=1)
        # Frame3:
        self.frame3 = LabelFrame(self, text="Frame 3", relief=SOLID)

        for i in range(5):
            self.frame3.rowconfigure(i, weight=1)
            self.frame3.columnconfigure(i, weight=1)

        # Entry:
        self.entry = Entry(self.frame3, width=5)
        self.entry.grid(row=0, column=0, padx=5, pady=5,
                        columnspan=6, sticky=N+W+E)
        # Text:
        self.text = Text(self.frame3, wrap="word", width=10, height=5)

        self.text.grid(row=1, column=0, padx=5, pady=5, sticky=E+W+N+S,
                       rowspan=5, columnspan=5)

        # ScrollBars:
        self.scroll = Scrollbar(self.frame3, orient=VERTICAL,
                                command=self.text.yview)
        self.scroll.grid(row=1, column=6, rowspan=5, sticky=N+S)
        self.text.config(yscrollcommand=self.scroll.set)
        self.text.focus()

        self.frame3.grid(row=0, column=2, rowspan=6, columnspan=3,
                         sticky=N+S+W+E, padx=4, pady=1)

    def handler1(self, event):
        print("Frame 1 clicked at", event.x, event.y)

    def handler2(self, event):
        print("Frame 2 clicked at", event.x, event.y)

    def handler_open(self):
        fn = self.entry.get()
        if fn != "":
            f = open(fn, "r")
            file = f.read()
            self.text.insert(END, file)

    def handler_red(self):
        self.text.config(fg="red")

    def handler_blue(self):
        self.text.config(fg="blue")

    def handler_green(self):
        self.text.config(fg="green")

    def handler_black(self):
        self.text.config(fg="black")


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
