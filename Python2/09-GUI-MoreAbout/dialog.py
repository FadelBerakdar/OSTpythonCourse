from tkinter import *
from tkinter.simpledialog import Dialog


class MyDialog(Dialog):
    def body(self, master):
        self.result = NONE
        for r in range(5):
            for c in range(5):
                button = Button(self)
                button.grid(row=r, column=c)
            print("Dialog created")

    def apply(self):
        self.result = "OK"


class Application(Frame):
    def create_dialog(self):
        dialog = MyDialog(self)
        print(dialog.result)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.d_button = Button(self, text="Dialog...", command=self.create_dialog)
        self.d_button.pack({"side": "left"})

        self.QUIT = Button(self, text="Quit", fg="red", command=self.quit)
        self.QUIT.pack({"side": "left"})




if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
