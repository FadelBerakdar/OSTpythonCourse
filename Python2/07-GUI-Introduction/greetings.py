from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.label = Label(self)
        self.buttonT = Button(self)
        self.buttonH = Button(self)
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self, text="Hello Tkinter")
        self.label.grid(row=0, column=0, columnspan=2)

        self.buttonT = Button(self, text="Texas", command=self.texas_hi)
        self.buttonT.grid(row=1, column=0)

        self.buttonH = Button(self, text="Hawaii", command=self.hawaii_hi)
        self.buttonH.grid(row=1, column=1)

    def texas_hi(self):
        self.label.config(text="Howdy, Tkinter!")

    def hawaii_hi(self):
        self.label.config(text="aloha, Tkinter!")

if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
