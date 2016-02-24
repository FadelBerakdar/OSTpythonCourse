from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.frame = Frame(self, width=100, height=100)
        self.frame.bind("<Button-1>", self.handler)
        self.frame.pack()


    def handler(self, event):
        print(event.x, event.y)


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
