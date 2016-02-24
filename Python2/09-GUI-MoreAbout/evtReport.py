from tkinter import *


class Application(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.pack()
        self.focus()
        self.create_widgets()

    def create_widgets(self):
        self.frame = Frame(self, width=100, height=100)
        self.frame.bind("o", self.handler1)
        self.frame.bind("k", self.handler1)
        self.frame.bind("<Button-1>", self.handler3)

        self.master.bind("<Key>", self.handler2)
        self.master.bind("<Button-1>", self.handler4)

        self.frame.pack()
        self.frame.focus()

    def handler1(self, event):
        print("Keystroke '{0}' ({1}) {2} ".format(event.char,
                                                  len(event.char),
                                                  event.keycode))
        return "Break"

    def handler2(self, event):
        print("RootKeystroke '{0}' ({1}) {2} ".format(event.char,
                                                      len(event.char),
                                                      event.keycode))

    def handler3(self, event):
        print("Frame clicked at", event.x, event.y)
        if event.x > 50 and event.y > 50:
            return "Break"

    def handler4(self, event):
        print("Root clicked at", event.x, event.y)

if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
