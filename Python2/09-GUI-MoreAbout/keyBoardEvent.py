from tkinter import *

class Application(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.frame = Frame(self, width=100, height=150)
        self.frame.bind("<KeyPress>", self.key_press)
        self.frame.bind("<Control-c>", lambda e: self.shortcut("Copy"))
        self.frame.bind("<Control-v>", lambda e: self.shortcut("Paste"))
        self.frame.pack()
        self.frame.focus()

    def key_press(self, event):
        print("type: {}".format(event.type))
        print("widget: {}".format(event.widget))
        print("char: {}".format(event.char))
        print("keysym: {}".format(event.keysym))
        print("keycode: {}".format(event.keycode))

    def shortcut(self, action):
        print(action)
if __name__ == "__main__":
    root = Tk()
    app = Application(master= root)
    app.mainloop()

