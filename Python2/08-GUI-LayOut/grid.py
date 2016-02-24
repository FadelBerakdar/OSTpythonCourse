from tkinter import *
all="NSWE"

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.grid(sticky=N+W+S+E)
        self.create_widgets()

    def create_widgets(self):

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=6)

        Label(self, text="Yellow", background="Yellow").grid(row=0, column=2, rowspan=2,sticky=N+W+S+E)
        Label(self, text="Blue", background="blue").grid(row=1, column=0, columnspan=2,sticky=N+W+S+E)
        Label(self, text="Green", background="green").grid(row=0, column=0,sticky=N+W+S+E)
        Label(self, text="Orange", background="Orange").grid(row=0, column=1,sticky=N+W+S+E)

        self.grid(sticky=all)
if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
