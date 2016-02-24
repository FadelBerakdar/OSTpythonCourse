#!/usr/bin/env python3
#                        GUI-based module
#                            fullscreen.py
# By: Fadel Berakdar
# Date: 19/5/2015

from tkinter import *


class Application(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weigh=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=N+W+E+S)
        self.create_widgets()

    def create_widgets(self):
        # Frame 1&2:
        for r in range(5):
            self.rowconfigure(r, weight=2)
        for c in range(2):
            self.columnconfigure(c, weight=2)

        self.frame1 = LabelFrame(self,
                                 text="Frame 1",
                                 width=600,
                                 height=550,
                                 relief=SOLID
                                 )
        self.frame1.grid(row=0, column=0, rowspan=3,
                         columnspan=2, padx=5, pady=5)

        self.frame2 = LabelFrame(self,
                                 text="Frame 2",
                                 width=600,
                                 height=400,
                                 relief=SOLID
                                 )
        self.frame2.grid(row=3, column=0, rowspan=2,
                         columnspan=2, padx=5, pady=5)

        # Frame3:
        for r in range(2, 5):
            self.columnconfigure(r, weight=3)
        self.frame3 = LabelFrame(self,
                                 text="Frame 3",
                                 width=800,
                                 height=810,
                                 relief=SOLID
                                 )
        self.frame3.grid(row=0, column=2, rowspan=5,
                         columnspan=3, padx=5, pady=5)

        # Buttons:
        self.rowconfigure(6, weight=1)
        for c in range(5):
            self.columnconfigure(c, weight=1)
            self.button = Button(self, text="Button {}".format(c+1), )
            self.button.grid(row=6, column=c, sticky=W+E+N+S)


if __name__ == "__main__":
    root = Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    app = Application(master=root)
    app.mainloop()