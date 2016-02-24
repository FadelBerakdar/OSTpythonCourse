from tkinter import *


class Application(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.configure(width=60, height=100)
        self.pack(fill=BOTH, expand=TRUE)
        self.create_widgets()

    def create_widgets(self):
        self.frame = LabelFrame(self, relief=SOLID)
        self.frame.pack(fill=BOTH, expand=TRUE, padx=3, pady=3)
        self.entry = Entry(self.frame, width=40)
        self.entry.grid(row=0, column=0, columnspan=6, rowspan=2, padx=2, pady=2)

        numbers = {"self.num9":9, }

        self.num9 = Button(self.frame, text=9,  width=5, command=lambda: self.call_back(9))
        self.num9.grid(row=2, column=0, sticky=E+W+N+S, rowspan=2, columnspan=2, padx=3, pady=2)

        self.num8 = Button(self.frame, text=8,  width=5, command=lambda: self.call_back(8))
        self.num8.grid(row=2, column=2, sticky=E+W+N+S, rowspan=2, columnspan=2, padx=3, pady=2)

        self.num7 = Button(self.frame, text=7,  width=5, command=lambda: self.call_back(7))
        self.num7.grid(row=2, column=4, sticky=E+W+N+S, rowspan=2, columnspan=2, padx=3, pady=2)

        self.num6 = Button(self.frame, text=6,  width=5, command=lambda: self.call_back(6))
        self.num6.grid(row=4, column=0, sticky=E+W+N+S, rowspan=2, columnspan=2, padx=3, pady=2)

        self.num5 = Button(self.frame, text=5,  width=5, command=lambda: self.call_back(5))
        self.num5.grid(row=4, column=2, sticky=E+W+N+S, rowspan=2, columnspan=2, padx=3, pady=2)

        self.num4 = Button(self.frame, text=4,  width=5, command=lambda: self.call_back(4))
        self.num4.grid(row=4, column=4, sticky=E+W+N+S, rowspan=2, columnspan=2, padx=3, pady=2)

        self.num3 = Button(self.frame, text=3,  width=5, command=lambda: self.call_back(3))
        self.num3.grid(row=6, column=0, sticky=E+W+N+S, rowspan=2, columnspan=2, padx=3, pady=2)

        self.num2 = Button(self.frame, text=2,  width=5, command=lambda: self.call_back(2))
        self.num2.grid(row=6, column=2, sticky=E+W+N+S, rowspan=2, columnspan=2, padx=3, pady=2)

        self.num1 = Button(self.frame, text=1,  width=5, command=lambda: self.call_back(1))
        self.num1.grid(row=6, column=4, sticky=E+W+N+S, rowspan=2, columnspan=2, padx=3, pady=2)

    def call_back(self, num=0):
        self.entry.insert(END, num)


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
