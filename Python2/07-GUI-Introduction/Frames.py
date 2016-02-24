__author__ = 'Fadel'

from tkinter import *
from tkinter import ttk

class Application(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self,master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.searchFrame = LabelFrame(self,
                                      text="Search",
                                      #Rwidth=1200,
                                      height= 400,
                                      relief=SOLID
                                      )
        self.searchFrame.pack(fill=X)


        self.treeView = ttk.Treeview(self.searchFrame,
                                     height=12
                                     )
        self.treeView.insert("", "0", "group1", text="Helix-turn-helix")
        self.treeView.insert("group1", "0", "group1homed", text="Homeodomain family")
        self.treeView.insert("group1", "1", "group1cro", text="Cro and Repressor family")
        self.treeView.insert("group1", "2", "group1lacI", text="LacI repressor family")
        self.treeView.insert("group1", "3", "group1hEndo", text="Endonuclease FokI family")

        self.treeView.insert("", "0", "group1", text="Helix-turn-helix")
        self.treeView.insert("", "1", "group2", text="Zinc-coordinating")
        self.treeView.insert("", "2", "group3", text="Zipper-type")
        self.treeView.insert("", "3", "group4", text="Other α-helix")
        self.treeView.insert("", "4", "group5", text="β-sheet")
        self.treeView.insert("", "5", "group6", text="β-hairpin/ribbon")
        self.treeView.insert("", "6", "group7", text="Enzyme")
        self.treeView.insert("", "7", "group8", text="Other")
        self.treeView.grid(row=0,column=0, padx=10, pady=10)



        self.checkButton = Checkbutton(self.searchFrame, text="Check")

        self.checkButton.grid(row=0,column=2, padx=10, pady=10)

        #self.searchFrame.rowconfigure(0,weight=1)
        #self.searchFrame.columnconfigure(0,weight=0)
        #self.searchFrame.columnconfigure(1,weight=1)
        #self.searchFrame.columnconfigure(2,weight=2)



        self.resultFrame = LabelFrame(self,
                                      text="Result:",
                                      #width=1200,
                                      height=600,
                                      relief=RIDGE
                                      )
        self.resultFrame.pack(fill=X)

        '''
        self.canvas = Canvas(self.resultFrame,
                             #width=1100,
                             height=550
                             )
        #self.canvas.config(yscrollcommand=self.scrollBar.set)
        self.canvas.grid(row=0,column=0)

        self.scrollBar = Scrollbar(self.resultFrame,
                                   orient=VERTICAL,
                                   command=self.canvas.yview
                                   )

        self.scrollBar.grid(row=0, column=1, sticky="ns" )
        '''


    def handler(self):
        pass

if __name__ == "__main__":
    root = Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.title("DNA-Protein Complex Database ")
    app = Application(master=root)
    app.mainloop()