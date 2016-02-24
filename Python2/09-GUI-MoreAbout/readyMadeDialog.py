

from tkinter import *
from tkinter.filedialog import LoadFileDialog, SaveFileDialog, Directory
from tkinter.colorchooser import askcolor
from tkinter.messagebox import (showinfo, showwarning, showerror, askquestion,
                                askokcancel, askyesno, askyesnocancel,
                                askretrycancel)


class Application(Frame):
    def askdir(self):
        d = Directory(self)
        print(d.show())

    def messages(self):
        print("info", showinfo("Spam", "Egg Information"))
        print("warning", showwarning("Spam", "Egg Warning"))
        print("error", showerror("Spam", "Egg Alert"))
        print("question", askquestion("Spam", "Question?"))
        print("proceed", askokcancel("Spam", "Proceed?"))
        print("yes/no", askyesno("Spam", "Got it?"))
        print("yes/no/cancel", askyesnocancel("Spam", "Want it?"))
        print("s again", askretrycancel("Spam", "Try again?"))

    def file_open(self):
        d = LoadFileDialog(self)
        fname = d.go("nosuch.txt", "*bunch_class")
        if fname is None:
            print("Canceled...")
        else:
            print("Open file", fname)

    def file_save(self):
        d = SaveFileDialog(self)
        fname = d.go("example", "*bunch_class")
        if fname is None:
            print("Canceled...")
        else:
            print("Saving file", fname)

    def color(self):
        d = askcolor()
        print(d)

    def createWidgets(self):
        d_button = Button(self)
        d_button.config(width=12, text="Directory Test", command=self.askdir)
        d_button.pack(side=TOP)
        m_button = Button(self)
        m_button.config(width=12, text="Messages Test", command=self.messages)
        m_button.pack()
        c_button = Button(self)
        c_button.config(width=12, text="Color Choice", command=self.color)
        c_button.pack()
        l_button = Button(self)
        l_button.config(width=12, text="Open File", command=self.file_open)
        l_button.pack()
        s_button = Button(self)
        s_button.config(width=12, text="Save File", command=self.file_save)
        s_button.pack()
        self.QUIT = Button(self)
        self.QUIT.config(width=12, text="Quit", fg="red", command=self.quit)
        self.QUIT.pack(side=TOP)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()