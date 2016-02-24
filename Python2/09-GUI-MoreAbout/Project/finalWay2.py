from tkinter import *
import os

ALL = N+S+W+E

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        # Set up cell in top frame to hold widgets
        self.master.rowconfigure(0, weight = 1, minsize=500)
        self.master.columnconfigure(0, weight = 1, minsize=500)
        self.grid(sticky = ALL)  

        
        # Add visible widgets
        frame1 = Frame(self)
        frame1.grid(row=0, column=0, sticky = ALL, columnspan=2)
        self.label1 = Label(frame1, text='Frame 1', bg='light grey', name='frame1')
        self.label1.grid(row=0, column = 0, sticky=ALL)
        #label1.pack()
        frame1.rowconfigure(0, weight=1)
        frame1.columnconfigure(0, weight=1)
        self.label1.bind('', self.print_coord)
        
        frame2 = Frame(self, borderwidth=3) 
        frame2.grid(row=1, column=0, sticky=ALL, columnspan=2)
        self.label2 = Label(frame2, text='Frame 2', bg='dark green', fg='white', name='frame2')
        self.label2.grid(row=0, column = 0, sticky=ALL)
        frame2.rowconfigure(0, weight=1)
        frame2.columnconfigure(0, weight=1)
        self.label2.bind('', self.print_coord)
                
        frame3 = Frame(self, bg='dark red', borderwidth=10)
        frame3.grid(row=0, column=2, sticky=ALL, rowspan=2, columnspan=3)
        self.label3 = Label(frame3, text = 'Frame 3', bg='dark red', fg='white', name='frame3')
        self.label3.grid(row=0, column = 0, sticky=N)
        frame3.rowconfigure(0, weight=1)
        frame3.columnconfigure(0, weight=1)
        self.fileName_entry=Entry(frame3)
        self.fileName_entry.grid(row=1, column=0, sticky=E+W+N)
        frame3.rowconfigure(1, weight=1)
        
        self.fileText_text = Text(frame3, height=1, width=1)
        self.fileText_text.grid(row=2, column=0, sticky=ALL)
        frame3.rowconfigure(2, weight=5)
           
        # Buttons
        b=Button(self, text='Red', command = lambda: self.change_color('red'))
        b.grid(row=2, column=0, sticky=E+W)  
              
        b=Button(self, text='Blue', command = lambda: self.change_color('blue'))
        b.grid(row=2, column=1, sticky=E+W)
        
        b=Button(self, text='Green', command = lambda: self.change_color('green'))
        b.grid(row=2, column=2, sticky=E+W)
        
        b=Button(self, text='Black', command = lambda: self.change_color('black'))
        b.grid(row=2, column=3, sticky=E+W)
        
        b=Button(self, text='Open', command = self.open_file)
        b.grid(row=2, column=4, sticky=E+W)
        
        for colnum in range(5):
            self.columnconfigure(colnum, weight=1)
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1) 
        self.fileName_entry.focus()

    def print_coord(self, event):
        print('You clicked in {0} at {1}, {2}'.format(event.widget.winfo_name(), event.x, event.y))  
    
    def change_color(self, color):
        self.fileText_text.config(fg=color)
    
    def open_file(self):
        fn = self.fileName_entry.get()
        txt_file=open(fn)
        txt = txt_file.read()
        self.fileText_text.delete(1.0,END)
        self.fileText_text.insert(END,txt)
        
                
if __name__ == '__main__':
        
    root=Tk()
    app = Application(master=root)
    app.mainloop()
