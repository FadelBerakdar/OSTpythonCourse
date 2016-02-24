#!/usr/bin/env python3
#            GUI-based module to check,convert to float, then sum two numbers
#                       checkConvertSum.py
# By: Fadel Berakdar
# Date: 17/5/2015

"""

"""
from tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        # Constructor
        Frame.__init__(self, master)
        self.entry1 = Entry(self)  # instance attribute defined outside __init__
        self.entry2 = Entry(self)
        self.label = Label(self)
        self.button = Button(self)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # creating the widgets
        self.button = Button(self, command=self.handler, text="Sum")
        self.button.pack(side=BOTTOM)

        self.label = Label(self, text="Enter two numbers")
        self.label.pack()

        self.entry1 = Entry(self, width=20)
        self.entry1.pack()

        self.entry2 = Entry(self, width=20)
        self.entry2.pack()

    def handler(self):
        entry1 = self.entry1.get()
        entry2 = self.entry2.get()
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)

        # s if the entries can be converted to float, convert, display, sum.
        try:
            self.entry1.insert(0, float(entry1))
        except ValueError:
            pass
        try:
            self.entry2.insert(0, float(entry2))
        except ValueError:
            pass

        try:
            add = float(self.entry1.get()) + float(self.entry2.get())
            self.label.config(text="sum = {}".format(add))
        except ValueError:
            self.label.config(text="***ERROR***")

    def handler2(self):
        # the handler function of the click button.
        entry1 = self.entry1.get()
        entry2 = self.entry2.get()
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)

        # s if the entries can be converted to float, convert, display, sum.
        try:
            self.entry1.insert(0, float(entry1))
            self.entry2.insert(0, float(entry2))
            add = float(self.entry1.get()) + float(self.entry2.get())
            self.label.config(text="sum = {}".format(add))
        except ValueError:
            self.label.config(text="***ERROR***")

if __name__ == "__main__":
    root = Tk()
    root.title("Check Convert Sum Module")
    app = Application(master=root)
    app.mainloop()