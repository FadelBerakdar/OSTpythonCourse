from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.configure(height=75, width=75)

        menu_bar = Menu(root)
        root.config(menu=menu_bar)

        file = Menu(menu_bar)
        edit = Menu(menu_bar)
        help_ = Menu(menu_bar)

        menu_bar.add_cascade(menu=file, label="File")
        menu_bar.add_cascade(menu=edit, label="Edit")
        menu_bar.add_cascade(menu=help_, label="Help")

        file.add_command(label="New", command=lambda: print("You selected 'File | New'"))
        file.entryconfig("New", accelerator="Ctrl+N")

        file.add_command(label="Open", command=lambda: print("You selected 'File | Open...'"))
        file.add_separator()
        file.add_command(label="Exit", command=lambda: print("You selected 'File | Exit'"))
        help_.add_command(label="About", command=lambda: print("You selected 'Help | About...'"))

        self.choice = IntVar()
        edit.add_radiobutton(label="Cut", variable=self.choice, value=1)
        edit.add_radiobutton(label="Copy", variable=self.choice, value=2)
        edit.add_radiobutton(label="Paste", variable=self.choice, value=3)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        pass

if __name__ == "__main__":
    root = Tk()
    #root.option_add("*tearOFF", FALSE)
    app = Application(master=root)
    app.mainloop()



