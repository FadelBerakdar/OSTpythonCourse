from tkinter import *

class Application(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.pack(expand=True, fill=BOTH) # this is the most important
        self.create_widgets()

    def create_widgets(self):
        self.top_frame = Frame(self)
        # never use .pack in the same line when u assigned to a variable
        Label(self.top_frame, text="Hello There !!!", background="yellow").pack(expand=True, fill=X)
        Label(self.top_frame, text="Welcome !!!", background="Red").pack( fill=BOTH, expand=True)
        Label(self.top_frame, text="Good Bye !!!", background="green").pack(expand=True, fill=Y)
        self.top_frame.pack(fill=BOTH, expand=True)

        self.middle_frame = LabelFrame(self, text="Frame")

        for widget in self.middle_frame.pack_slaves():
            widget.pack_configure(Fill=BOTH, expand=True)

        self.bottom_frame = Frame(self)
        Button(self.bottom_frame, text="ClickMe", width=20).pack(anchor="nw")
        Button(self.bottom_frame, text="PressMe", width=20).pack(anchor="e")
        Button(self.bottom_frame, text="PushMe", width=20).pack(ipadx=10)
        self.bottom_frame.pack(fill=BOTH, expand=True)





if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
