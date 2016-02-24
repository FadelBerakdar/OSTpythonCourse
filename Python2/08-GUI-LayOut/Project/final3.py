from tkinter import *

ALL = N+S+E+W

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        # Set up cell in top frame to hold widgets
        self.master.rowconfigure(0, weight = 1, minsize=500)
        self.master.columnconfigure(0, weight = 1, minsize=750)
        self.grid(sticky = ALL)

        for r in range(9):
            for c in range(6):
                self.rowconfigure(r, weight=1)
                self.columnconfigure(c, weight=1)
        self.frame1 = LabelFrame(self, text="Frame1")
        self.label1 = Label(self.frame1)
        self.label1.pack(fill=BOTH, expand=TRUE)
        self.frame1.grid(sticky = ALL, row=0, column=0, rowspan=5, columnspan=6)

        self.frame2 = LabelFrame(self, text="Frame2")
        self.label2 = Label(self.frame2)
        self.label2.pack(fill=BOTH, expand=TRUE)
        self.frame2.grid(sticky = ALL,  row=5, column=0, rowspan=4, columnspan=6)

        for r in range(9):
            for c in range(6,15):
                self.rowconfigure(r, weight=1)
                self.columnconfigure(c, weight=2)

        self.frame3 = LabelFrame(self, text="Frame3")
        self.label3 = Label(self.frame3)
        self.label3.pack(fill=BOTH, expand=TRUE)
        self.frame3.grid(sticky = ALL,  row=0, column=6, rowspan=9, columnspan=9)

        self.button1 = Button(self, text= "Button1")
        self.button1.grid(row= 10, column=0, columnspan=2, sticky = E+W)

        self.button2 = Button(self, text= "Button1")
        self.button2.grid(row= 10, column=2, columnspan=2, sticky = E+W)

if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.mainloop()