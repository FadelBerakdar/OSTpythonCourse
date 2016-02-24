from tkinter import *  # tool kit interface



class Application(Frame):
    """ define a class Application, which is a subclass of tkinter.Frame
    the tkinter.Frame class defines all the general behavior required
    of GUI program.
    but there general behaviors do not encompass the specific contents of this
    window, for the specific behaviors, we have createWidget function.
    """
    def say_hi(self):
        """the event handler for clicks"""
        print("Hi there, everyone!")

    def create_widgets(self):
        """ define the specific behaviors of the GUI program. byt initializing
            the widgets
        """
        self.Hi = Button(self, text= "hi", fg="red", command=self.say_hi)
        self.Hi.pack({"side": "left"})
        # quit with out () means return not call
        self.Quit = Button(self, text="Goodbye", fg="blue", command=self.quit)
        self.Quit.pack({"side": "left"})

    def __init__(self, master=None):
        """
        the __init__ method of the tkinter.Frame class does the following:
        1- performs all the standard tkinter.Frame initialization actions
           by calling its superclass (tkinter.Frame's__init())
        2- calls the newly frames's pack() method, which prepares it to be part
           of the windows display
        3- calls the createWidgets() method.
        """
        Frame.__init__(self, master)   # master means the tk parent widget
        self.pack()
        self.create_widgets()

root = Tk()
app = Application(master=root)  # "app" is an instance of the class Application
app.mainloop()  # hands control over to window manager # event loop
