from tkinter import *


class Application(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.pack()

        self.button = Button(self)
        self.crete_widgets()

    def crete_widgets(self):
        self.button = Button(self, text="Click me ")
        self.button.image = PhotoImage(file="python_logo.gif").subsample(5, 5)
        self.button.config(image=self.button.image, compound=LEFT)
        self.button.pack()

if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
