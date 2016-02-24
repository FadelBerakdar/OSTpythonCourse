from tkinter import *
from tkinter import ttk


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()
        self.logo = PhotoImage(file="python_logo.gif")

    def create_widgets(self):
        # Labels:
        self.label = Label(self, text="Welcome to DNA-Protein Complex DataBase")
        self.label.config(wraplength=600)
        self.label.config(justify=CENTER)
        self.label.config(foreground='blue')
        #self.label.config(background='grey')
        self.label.config(font=("", 18, "italic"))
        self.label.img = PhotoImage(file="logo.gif").subsample(6, 4)
        self.label.config(image=self.label.img)
        self.label.config(compound='left')
        self.label.pack()

        # Buttons:
        self.button = Button(self, text="I'm Python :P")
        self.button.config(command=self.button.config(state="active"))
        self.button.img = PhotoImage(file="python_logo.gif").subsample(5, 5)
        self.button.config(image=self.button.img, compound=LEFT)
        self.button.pack(side=BOTTOM)

        # CheckButton:
        viral, prokaryotic, eukaryotic = StringVar(), StringVar(), StringVar()
        viral.set("Viral")
        prokaryotic.set("Prokaryotic")
        eukaryotic.set("Eukaryotic")

        self.checkButton = Checkbutton(self,
                                       text="Viral",
                                       variable=viral,
                                       onvalue="YesViral",
                                       offvalue="NoViral",
                                       state="active")
        print(self.checkButton.config())
        #self.checkButton.config(text="Hi")
        self.checkButton.pack()

        # RadioButton:
        self.radioButton = Radiobutton(self,
                                       text="Eucaryotic",
                                       variable=eukaryotic,
                                       value="Viral"
                                       ).pack()
        # Entry:
        self.entry = Entry(self,
                           width=30)
        self.entry.insert(0, "Search") # to insert data
        self.entry.get()               # to get the content of the entry
        self.entry.delete(0,END)       # to delete the content of the entry
        self.entry.pack()

        # ComboBox:
        self.combobox = ttk.Combobox(self,
                                     textvariable="Month",
                                     values=("Jan", "Feb", "Mar", "Apr",
                                              "May", "Jun", "Jul", "Aug",
                                              "Sep", "Oct", "Nove", "")
                                     ).pack()

        # SpinBox:
        year = StringVar()
        self.spinbox = Spinbox(self,
                               from_=1990,
                               to=2015,
                               textvariable=year
                               ).pack()

        # ProgressBar:
        value = DoubleVar()
        self.progressbar = ttk.Progressbar(self,
                                           orient=HORIZONTAL,
                                           length=200,
                                           mode="indeterminate",
                                           variable=value)
        self.progressbar.pack()
        self.progressbar.start()

        #ScaleBar:
        self.scalebar = Scale(self,
                              orient=HORIZONTAL,
                              length=600,
                              variable=value,
                              from_=0,
                              to=255)
        self.scalebar.pack()

    def event_handler(self):
        pass

if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()